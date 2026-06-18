from pathlib import Path
import config

def detect_module(file_path: str) -> str:
    """Detect module by walking up from file path until we find a direct child of the watch folder."""
    watch_path = Path(config.WATCH_FOLDER).resolve()
    file_path = Path(file_path).resolve()

    # Walk up from parent directory
    current = file_path.parent
    while current != watch_path and current != current.parent:
        parent = current.parent
        if parent == watch_path:
            # Current directory is a direct child of watch folder = module name
            return current.name.lower().replace(" ", "_")
        current = parent

    # If file is directly in watch folder, use parent name
    if file_path.parent == watch_path:
        return "_unknown"

    # Fallback to immediate parent
    return file_path.parent.name.lower().replace(" ", "_")
