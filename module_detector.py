from pathlib import Path
import config

def detect_module(file_path):
    watch = Path(config.WATCH_FOLDER).resolve()
    fp = Path(file_path).resolve()
    current = fp.parent
    while current != watch and current != current.parent:
        if current.parent == watch:
            return current.name.lower().replace(" ", "_")
        current = current.parent
    return fp.parent.name.lower().replace(" ", "_")
