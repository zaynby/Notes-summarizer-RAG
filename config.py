import os
from pathlib import Path
from dotenv import load_dotenv

_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    load_dotenv(_env_file)

BASE_DIR = Path(__file__).parent.resolve()

WATCH_FOLDER = os.getenv("WATCH_FOLDER")
if not WATCH_FOLDER:
    raise RuntimeError("WATCH_FOLDER not set in .env")

SUPPORTED_EXTENSIONS = {".pptx", ".pdf", ".ipynb"}
SKIP_MODULES = {"calculus", "ehe"}
CHROMADB_PATH = BASE_DIR / "chromadb_data"
EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_BASE_URL = "http://localhost:11434"
