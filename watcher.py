import time
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import config
from summarizer import process_file
from style_evaluator import evaluate_module_style, count_summaries_for_module
from style_memory import load_style_memory, get_module_style
from module_detector import detect_module

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler(config.LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("watcher")

# Debounce: track recently processed files by path
_recently_processed = set()
_DEBOUNCE_SECONDS = 10  # Skip same file within this window

# Track per-module count for evaluation triggers
module_file_count = {}
style_data = load_style_memory()


def _should_skip(file_path: str) -> bool:
    """Check if file should be skipped (unsupported, temp, or recently processed)."""
    ext = Path(file_path).suffix.lower()
    if ext not in config.SUPPORTED_EXTENSIONS:
        return True

    name = Path(file_path).name
    if name.startswith("~$") or name.startswith("."):
        return True

    return False


class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        self._process(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        self._process(event.src_path)

    def _process(self, file_path: str):
        if _should_skip(file_path):
            return

        # Debounce: skip if processed recently
        if file_path in _recently_processed:
            return
        _recently_processed.add(file_path)

        log.info(f"New file detected: {file_path}")

        # Wait for file to finish writing
        time.sleep(2)

        result = process_file(file_path, style_data)
        log.info(result)

        # Schedule debounce cleanup after _DEBOUNCE_SECONDS
        def _cleanup():
            time.sleep(_DEBOUNCE_SECONDS)
            _recently_processed.discard(file_path)

        import threading
        threading.Thread(target=_cleanup, daemon=True).start()

        # Track per-module count and trigger evaluation
        module = detect_module(file_path)
        module_file_count[module] = module_file_count.get(module, 0) + 1

        if module_file_count[module] >= config.EVAL_INTERVAL:
            log.info(f"Evaluating style for module '{module}' "
                     f"({module_file_count[module]} files processed)")
            module_file_count[module] = 0

            eval_result = evaluate_module_style(module)
            log.info(f"Evaluation result for '{module}': {eval_result}")


def _auto_select_provider():
    """Auto-select provider based on what's available."""
    if config.LLM_PROVIDER == "nvidia" and not config.NVIDIA_API_KEY:
        log.warning("NVIDIA_API_KEY not set. Falling back to Ollama.")
        log.info("Tip: Set your key in the .env file: NVIDIA_API_KEY=nvapi-...")
        config.LLM_PROVIDER = "ollama"

    if config.LLM_PROVIDER == "ollama":
        log.info(f"Using Ollama model: {config.OLLAMA_MODEL}")
        log.info("Make sure Ollama is running (ollama serve) and the model is pulled.")
    elif config.LLM_PROVIDER == "nvidia":
        log.info(f"Using NVIDIA NIM model: {config.NVIDIA_MODEL}")


def watch_folder():
    folder = Path(config.WATCH_FOLDER)
    if not folder.exists():
        log.error(f"Watch folder does not exist: {folder}")
        return

    _auto_select_provider()

    log.info(f"Starting watcher on: {folder}")
    log.info(f"Watching for: {', '.join(config.SUPPORTED_EXTENSIONS)}")

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(folder), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log.info("Watcher stopped by user")

    observer.join()


if __name__ == "__main__":
    watch_folder()
