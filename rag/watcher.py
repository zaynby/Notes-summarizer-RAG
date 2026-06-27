import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import config
from rag.indexer import index_file
from module_detector import detect_module
from processing.filter import should_skip


class StudyHandler(FileSystemEventHandler):
    def __init__(self):
        self._debounce = {}

    def on_created(self, event):
        if not event.is_directory:
            self._process(event.src_path, "created")

    def on_modified(self, event):
        if not event.is_directory:
            self._process(event.src_path, "modified")

    def _process(self, file_path, event_type):
        path = Path(file_path)
        ext = path.suffix.lower()

        if ext not in config.SUPPORTED_EXTENSIONS:
            return
        name = path.name
        if name.startswith("~$") or name.startswith("."):
            return
        if ".ipynb_checkpoints" in path.parts:
            return

        module = detect_module(file_path)
        if module in config.SKIP_MODULES:
            return

        skip, reason = should_skip(file_path)
        if skip:
            print(f"[watcher] Filtered: {path.relative_to(config.WATCH_FOLDER)} ({reason})")
            return

        now = time.time()
        last = self._debounce.get(file_path, 0)
        if now - last < 2:
            return
        self._debounce[file_path] = now

        rel = path.relative_to(config.WATCH_FOLDER)
        print(f"[watcher] {event_type}: {rel}")
        time.sleep(1)

        try:
            result = index_file(file_path, module)
            print(f"  -> {result}")
        except Exception as e:
            print(f"  -> ERROR: {e}")


def start_watcher():
    watch_path = Path(config.WATCH_FOLDER)
    if not watch_path.exists():
        print(f"Watch folder does not exist: {watch_path}")
        return

    event_handler = StudyHandler()
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=True)
    observer.start()

    print(f"Watching: {watch_path}")
    print("Waiting for new or modified files... (Ctrl+C to stop)\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nWatcher stopped.")
        observer.stop()
    observer.join()
