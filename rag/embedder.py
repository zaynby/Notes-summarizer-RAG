import logging
from typing import Optional, List
import httpx
import config

log = logging.getLogger("embedder")

# ── Ollama ──────────────────────────────────────────────────

_ollama_client = None

def _get_ollama_client():
    global _ollama_client
    if _ollama_client is None:
        import ollama
        _ollama_client = ollama.Client(host=config.OLLAMA_BASE_URL)
    return _ollama_client

def _embed_ollama(text: str) -> Optional[List[float]]:
    client = _get_ollama_client()
    resp = client.embeddings(model=config.EMBEDDING_MODEL, prompt=text[:8192])
    return resp["embedding"]

# ── Hugging Face Inference API ─────────────────────────────

def _embed_hf(text: str) -> Optional[List[float]]:
    headers = {"Authorization": f"Bearer {config.HF_API_TOKEN}"}
    url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{config.HF_EMBEDDING_MODEL}"
    resp = httpx.post(
        url, headers=headers,
        json={"inputs": text, "options": {"wait_for_model": True}},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if isinstance(data, list) and data and isinstance(data[0], list):
        return data[0]
    return data if isinstance(data, list) else None

# ── Public interface ───────────────────────────────────────

def embed_text(text: str) -> Optional[List[float]]:
    try:
        if config.EMBEDDING_PROVIDER == "huggingface":
            return _embed_hf(text)
        return _embed_ollama(text)
    except Exception as e:
        log.error(f"Embedding failed ({config.EMBEDDING_PROVIDER}): {e}")
        return None
