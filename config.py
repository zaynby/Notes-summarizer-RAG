import os
from pathlib import Path

# Load .env file if present
from dotenv import load_dotenv
_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    load_dotenv(_env_file)

# Paths
WATCH_FOLDER = r"C:\Users\Lenovo\Desktop\Poly life\Raw Sources folder\Poly Year 2 Sem 1"
BASE_DIR = Path(__file__).parent.resolve()
JOURNALS_DIR = BASE_DIR / "journals"
SUMMARIZATION_DIR = BASE_DIR / "summarization"
STYLE_MEMORY_PATH = BASE_DIR / "style_memory.json"
STYLE_LOG_PATH = BASE_DIR / "style_log.md"

# Ensure directories exist
JOURNALS_DIR.mkdir(exist_ok=True)
SUMMARIZATION_DIR.mkdir(exist_ok=True)

# LLM Provider Settings
LLM_PROVIDER = "nvidia"  # "nvidia", "ollama", or "openrouter"

# NVIDIA NIM Settings
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
NVIDIA_MODEL = "moonshotai/kimi-k2.6"

# Ollama Settings
OLLAMA_MODEL = "qwen2.5:7b"
OLLAMA_BASE_URL = "http://localhost:11434"

# OpenRouter Settings (optional fallback)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "meta-llama/llama-3.1-70b-instruct"

# Self-improvement
EVAL_INTERVAL = 5  # Evaluate style every N summaries per module
MIN_SCORE_TO_LOCK = 8  # Out of 10
MAX_STYLE_ATTEMPTS = 3  # Before switching style family
MAX_STYLE_EXAMPLES = None  # None = all past summaries as examples

# Supported file extensions
SUPPORTED_EXTENSIONS = {".pptx", ".pdf", ".ipynb"}

# Logging
LOG_FILE = BASE_DIR / "watcher.log"

# ChromaDB / Vector Store
CHROMADB_PATH = BASE_DIR / "chromadb_data"

# Embedding
EMBEDDING_MODEL = "nomic-embed-text"

# RAG chunking
CHUNK_SIZE = 500  # tokens per chunk
TOP_K_RETRIEVAL = 5  # chunks to retrieve for few-shot
