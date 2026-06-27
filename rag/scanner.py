from pathlib import Path
import config
from module_detector import detect_module
from processing.filter import should_skip

def scan():
    watch = Path(config.WATCH_FOLDER)
    if not watch.exists():
        print(f"Watch folder not found: {watch}")
        return []

    files = []
    seen = set()

    for ext in config.SUPPORTED_EXTENSIONS:
        for f in watch.rglob(f"*{ext}"):
            name = f.name
            if name.startswith("~$") or name.startswith("."):
                continue
            if ".ipynb_checkpoints" in f.parts:
                continue

            module = detect_module(str(f))
            if module in config.SKIP_MODULES:
                continue

            skip, reason = should_skip(str(f))
            if skip:
                continue

            dedup_key = f"{module}/{name}"
            if dedup_key in seen:
                continue
            seen.add(dedup_key)

            files.append((str(f), module, name))

    files.sort(key=lambda x: (x[1], x[2]))
    return files
