from pathlib import Path
from datetime import datetime
import config

def ensure_journal(module: str) -> Path:
    """Ensure journal file exists for a module and return its path."""
    safe_name = module.lower().replace(" ", "_")
    journal_path = config.JOURNALS_DIR / f"{safe_name}.md"
    if not journal_path.exists():
        journal_path.write_text(f"# {safe_name.upper()} Journal\n\n", encoding="utf-8")
    return journal_path

def append_to_journal(module: str, filename: str, summary: str, style_family: str, locked: bool):
    """Append a summary to the module's journal."""
    journal_path = ensure_journal(module)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    entry = f"""---

## {now} — {filename}
**Style:** {style_family} ({'locked' if locked else 'experimenting'})

{summary}

---

"""
    with open(journal_path, "a", encoding="utf-8") as f:
        f.write(entry)

def get_journal_path(module: str) -> Path:
    safe_name = module.lower().replace(" ", "_")
    return config.JOURNALS_DIR / f"{safe_name}.md"
