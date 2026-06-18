import logging
from pathlib import Path
from datetime import datetime

import config
from llm import call_llm
from extractors import extract_pptx, extract_pdf, extract_ipynb
from module_detector import detect_module
from style_memory import load_style_memory, get_module_style
from journal import append_to_journal

log = logging.getLogger("summarizer")

SYSTEM_PROMPT_CLASSIFY = """You are an academic note-taking assistant. Given the content of a file, classify it as either THEORY or PRACTICAL/CODE, then format the notes accordingly.

### If THEORY material:
Structure notes like a student's study guide:
- **Term/Concept** — Definition — Expansion/Explanation
  - Key details, examples, or context that help understand it
- List all important terms in the order they appear
- Add any formulas, rules, or principles with brief explanations
- Use markdown formatting (bold for terms, italics for emphasis)

### If PRACTICAL/CODE material:
Break the code into logical chunks. For each chunk:
- **Chunk:** [what this section does in 1 sentence]
- **Explanation:** Step-by-step breakdown of how it works
- **Key Variables:**
  - `variable_name` — what it holds — what values you can change it to and what effect that has
  - (repeat for all variables in the chunk)
- **How to modify:** Specific guidance on what you can customize

Strict rules:
- Start with a header: `## THEORY NOTES` or `## PRACTICAL NOTES`
- If content is mixed, prioritize the dominant type but note the other briefly
- If no meaningful content found, say "No meaningful content found"
- Link each key term as a [[Wikilink]] so it becomes its own note later
- Do NOT include any preamble before the header
"""

SYSTEM_PROMPT_SUMMARIZE = """You are an academic note-taking assistant specializing in summarizing educational materials for polytechnic students.

{style_prompt}

Generate a comprehensive summary of the provided content according to the classification above.
Make it concise but thorough. Use proper markdown formatting.
Link each key term as a [[Wikilink]] so that related concepts are connected across all your notes.
"""

STYLE_DESCRIPTIONS = {
    "structured_academic": "Use a structured academic format: term -> definition -> formula -> example",
    "bullet_synthesis": "Use concise bullet points synthesizing key ideas",
    "narrative_flow": "Use a narrative paragraph-style flow with concept connections",
    "code_breakdown": "Use code chunks -> explanation -> variables table -> modifications guide",
    "question_answer": "Use a Question & Answer format for self-testing",
    "mind_map": "Use a hierarchical mind-map style with nested concepts",
}


def get_extractor(file_path: str):
    ext = Path(file_path).suffix.lower()
    if ext == ".pptx":
        return extract_pptx
    elif ext == ".pdf":
        return extract_pdf
    elif ext == ".ipynb":
        return extract_ipynb
    return None


def load_few_shot_rag(module: str, content: str) -> str:
    """Load few-shot examples using RAG retrieval, with flat file fallback."""
    try:
        from rag.vector_store import search_similar_by_module, search_similar
        results = search_similar_by_module(content, module, config.TOP_K_RETRIEVAL)
        if not results:
            results = search_similar(content, config.TOP_K_RETRIEVAL)
        if results:
            parts = []
            for r in results:
                parts.append(
                    f"### Example from {r['filename']} ({r['module']}):\n{r['text'][:1000]}"
                )
            return "\n\n" + "\n\n".join(parts)
    except Exception as e:
        log.warning(f"RAG retrieval failed, falling back to flat file: {e}")

    # Fallback: flat file read
    prefix = module.lower().replace(" ", "_")
    examples = []
    for f_path in config.SUMMARIZATION_DIR.glob(f"{prefix}_*.md"):
        try:
            txt = f_path.read_text(encoding="utf-8").strip()
            if len(txt) > 50:
                examples.append(txt)
        except Exception:
            continue
    if not examples:
        return ""
    examples.sort()
    return "\n\n" + "\n\n".join(
        f"### Example {i+1}:\n{ex}" for i, ex in enumerate(examples[-config.TOP_K_RETRIEVAL:])
    )


def ingest_to_rag(content: str, module: str, filename: str, file_path: str, ext: str):
    """Ingest extracted content into the RAG vector store."""
    try:
        from rag import ingest_text
        source_type = ext.lstrip(".")
        ingest_text(content, module, filename, file_path, source_type)
        log.info(f"Ingested {filename} into RAG store")
    except Exception as e:
        log.warning(f"RAG ingestion skipped: {e}")


def process_file(file_path: str, style_data: dict = None):
    file_path_obj = Path(file_path)
    ext = file_path_obj.suffix.lower()

    if ext not in config.SUPPORTED_EXTENSIONS:
        return f"Skipped: unsupported file type {ext}"

    extractor = get_extractor(file_path)
    if not extractor:
        return f"No extractor for {file_path}"

    content = extractor(file_path)
    if not content or len(content.strip()) < 50:
        return "Skipped: no meaningful content"

    module = detect_module(file_path)
    style_info = style_data or get_module_style(module, load_style_memory())
    style_family = style_info.get("style_family", "structured_academic")
    locked = style_info.get("locked", False)
    style_desc = STYLE_DESCRIPTIONS.get(style_family, "")

    # Classification
    log.info("Classifying content (the first LLM call)")
    classification = call_llm(
        f"### File Content:\n{content[:15000]}",
        system=SYSTEM_PROMPT_CLASSIFY
    )
    is_theory = "## THEORY NOTES" in classification
    is_practical = "## PRACTICAL NOTES" in classification
    log.info(f"Classification done: {'THEORY' if is_theory else 'PRACTICAL' if is_practical else 'unknown'}")

    # RAG retrieval for few-shot
    examples = load_few_shot_rag(module, content)

    # Summarization
    summarize_system = SYSTEM_PROMPT_SUMMARIZE.format(style_prompt=style_desc)
    if examples:
        summarize_system += examples

    log.info(f"Generating summary (~{len(content)//1000}K chars content)")
    summary = call_llm(
        f"### File Content:\n{content[:20000]}",
        system=summarize_system
    )

    # Save to local journal
    append_to_journal(module, file_path_obj.name, summary, style_family, locked)

    # Save raw copy
    safe_name = module.lower().replace(" ", "_")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    summary_file = config.SUMMARIZATION_DIR / f"{safe_name}_{timestamp}_{file_path_obj.name}.md"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(f"# {file_path_obj.name}\n")
        f.write(f"**Module:** {module}\n")
        f.write(f"**Style:** {style_family} ({'locked' if locked else 'experimenting'})\n\n")
        f.write(summary)

    # RAG ingestion
    ingest_to_rag(content, module, file_path_obj.name, file_path, ext)

    return f"Processed {file_path_obj.name} → {module}. Style: {style_family}"
