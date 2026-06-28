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

# Embedding
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "ollama")
EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_BASE_URL = "http://localhost:11434"
HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")
HF_EMBEDDING_MODEL = os.getenv("HF_EMBEDDING_MODEL", "BAAI/bge-base-en-v1.5")

# LLM (NVIDIA NIM)
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "meta/llama-3.1-8b-instruct")

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# API
API_PORT = int(os.getenv("API_PORT", "8000"))
