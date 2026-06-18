import logging
from pathlib import Path
from typing import Optional

import config
from llm import call_llm
from rag.vector_store import search_similar

log = logging.getLogger("query")

QUERY_PROMPT = """You are a student assistant. Answer the question based ONLY on the provided notes below.

If the notes don't contain enough information, say "I couldn't find enough information in your notes about this."

Notes:
{notes}

Question: {question}

Answer concisely. At the end, list the source files used as wikilinks: [[SourceFile]].
"""


def answer_question(question: str, module: Optional[str] = None, top_k: int = 5):
    """Answer a question using RAG over the stored notes."""
    notes = search_similar(question, top_k)
    if not notes:
        print("No relevant notes found in the vector store yet.")
        print("Make sure you've processed some files first with `python main.py watch`")
        return

    notes_text = "\n\n".join(
        f"[{n['filename']} / {n['module']}] {n['text']}"
        for n in notes
    )

    prompt = QUERY_PROMPT.format(
        notes=notes_text[:15000],
        question=question,
    )

    answer = call_llm(prompt, system="You answer questions from student notes.")

    print(f"\n{'='*60}")
    print(f"Q: {question}")
    print(f"{'='*60}\n")
    print(answer)
    print(f"\n{'='*60}")
    print("Sources retrieved from vector store:")
    for i, note in enumerate(notes, 1):
        print(f"  {i}. {note['filename']} ({note['module']})")
