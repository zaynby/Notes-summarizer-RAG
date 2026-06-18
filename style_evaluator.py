from pathlib import Path
from datetime import datetime
import config
from style_memory import load_style_memory, get_module_style, record_attempt, STYLE_FAMILIES
from llm import call_llm

EVALUATION_PROMPT = """You are a student evaluating your own study notes. Read these {count} recent summaries for the module "{module}" and assess their quality.

Rate each summary on a scale of 1-10 for:
1. **Clarity** — Is it easy to understand?
2. **Completeness** — Does it capture key concepts?
3. **Usefulness** — Would it help you study for exams?

Then answer:
- What style are these summaries using? (e.g., "term-definition-example", "code breakdown", "bullets", "narrative")
- Is this style effective for this module's content?
- What would you change to improve future summaries?

Be honest and critical. A score of 7-8 is average; 9-10 is excellent; below 6 needs improvement.

Return ONLY this JSON format (no other text):
{{
    "avg_score": 7.5,
    "style_detected": "term_definition_example",
    "style_family": "structured_academic",
    "effective": true,
    "notes": "Brief feedback..."
}}
"""

SUMMARY_COUNT_EVAL = 5  # how many recent summaries to evaluate

def count_summaries_for_module(module: str) -> int:
    prefix = module.lower().replace(" ", "_")
    count = 0
    for f in config.SUMMARIZATION_DIR.glob(f"{prefix}_*.md"):
        count += 1
    return count

def load_recent_summaries(module: str, n: int = SUMMARY_COUNT_EVAL) -> str:
    prefix = module.lower().replace(" ", "_")
    files = sorted(config.SUMMARIZATION_DIR.glob(f"{prefix}_*.md"))
    if not files:
        return ""

    recent = files[-n:]
    excerpts = []
    for f in recent:
        try:
            content = f.read_text(encoding="utf-8")
            lines = content.strip().split("\n")
            # Take first 20 lines as excerpt
            excerpt = "\n".join(lines[:20])
            excerpts.append(f"=== {f.name} ===\n{excerpt}")
        except Exception:
            continue

    return "\n\n".join(excerpts)

def evaluate_module_style(module: str) -> dict:
    """Evaluate recent summaries for a module and determine if style should change."""
    summaries_text = load_recent_summaries(module, SUMMARY_COUNT_EVAL)
    if not summaries_text:
        return {"result": "no_summaries"}

    style_memory = load_style_memory()
    style_info = get_module_style(module, style_memory)

    prompt = EVALUATION_PROMPT.format(
        count=min(count_summaries_for_module(module), SUMMARY_COUNT_EVAL),
        module=module
    ) + f"\n\n### Recent Summaries:\n{summaries_text[:12000]}"

    result = call_llm(prompt, system="You are a student evaluating notes. Return only JSON.")

    import json
    import re

    json_match = re.search(r'\{[^{}]*\}', result.strip(), re.DOTALL)
    if json_match:
        try:
            evaluation = json.loads(json_match.group())
            score = evaluation.get("avg_score", 0)
            effective = evaluation.get("effective", False)
            style_family = evaluation.get("style_family", style_info.get("style_family"))
            notes = evaluation.get("notes", "")

            record_attempt(module, style_memory, score)

            return {
                "result": "evaluated",
                "score": score,
                "effective": effective,
                "style_family": style_family,
                "notes": notes,
                "locked": style_info.get("locked", False)
            }
        except (json.JSONDecodeError, KeyError):
            return {"result": "parse_error", "raw": result[:500]}

    return {"result": "parse_error", "raw": result[:500]}

def evaluate_all_modules():
    """Check all modules that have sufficient summaries and evaluate them."""
    style_memory = load_style_memory()
    modules = style_memory.get("modules", {}).copy()
    results = []

    for module in list(modules.keys()):
        count = count_summaries_for_module(module)
        if count >= config.EVAL_INTERVAL and not modules[module].get("locked"):
            result = evaluate_module_style(module)
            results.append({"module": module, **result})

    return results
