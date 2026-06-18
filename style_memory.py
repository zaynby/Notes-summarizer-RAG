import json
import time
from pathlib import Path
from config import STYLE_MEMORY_PATH, MAX_STYLE_ATTEMPTS, MIN_SCORE_TO_LOCK

# Default style families
STYLE_FAMILIES = [
    "structured_academic",  # term -> definition -> formula -> example
    "bullet_synthesis",     # condensed bullets with key points
    "narrative_flow",       # paragraph-style with connections
    "code_breakdown",       # chunks -> variables -> modifications
    "question_answer",      # Q&A format for self-testing
    "mind_map"              # hierarchical concept map
]

def _init_memory():
    return {
        "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "modules": {}
    }

def load_style_memory() -> dict:
    if not STYLE_MEMORY_PATH.exists():
        data = _init_memory()
        save_style_memory(data)
        return data
    with open(STYLE_MEMORY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_style_memory(data: dict):
    data["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(STYLE_MEMORY_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_module_style(module: str, data: dict) -> dict:
    modules = data.setdefault("modules", {})
    if module not in modules:
        modules[module] = {
            "best_style": None,
            "style_family": "structured_academic",  # Default start
            "style_index": 0,
            "attempts": 0,
            "locked": False,
            "score": None
        }
        save_style_memory(data)
    return modules[module]

def lock_style(module: str, data: dict, score: float):
    style = get_module_style(module, data)
    style["locked"] = True
    style["score"] = score
    save_style_memory(data)

def next_style_family(module: str, data: dict):
    "Switch to next style family if current one isn't working."
    style = get_module_style(module, data)
    current_family = style.get("style_family", "structured_academic")
    current_index = STYLE_FAMILIES.index(current_family) if current_family in STYLE_FAMILIES else 0

    next_index = (current_index + 1) % len(STYLE_FAMILIES)
    style["style_family"] = STYLE_FAMILIES[next_index]
    style["style_index"] = next_index
    style["attempts"] = 0
    style["locked"] = False
    style["score"] = None
    save_style_memory(data)

def record_attempt(module: str, data: dict, score: float):
    style = get_module_style(module, data)
    style["attempts"] += 1
    style["score"] = score

    if score >= MIN_SCORE_TO_LOCK:
        lock_style(module, data, score)
    elif style["attempts"] >= MAX_STYLE_ATTEMPTS:
        next_style_family(module, data)

    save_style_memory(data)
