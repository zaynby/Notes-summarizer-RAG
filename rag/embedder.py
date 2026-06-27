import logging
from typing import Optional, List
import config

log = logging.getLogger("embedder")
_client = None

def _get_client():
    global _client
    if _client is None:
        import ollama
        _client = ollama.Client(host=config.OLLAMA_BASE_URL)
    return _client

def embed_text(text: str) -> Optional[List[float]]:
    try:
        client = _get_client()
        resp = client.embeddings(model=config.EMBEDDING_MODEL, prompt=text[:8192])
        return resp["embedding"]
    except Exception as e:
        log.error(f"Embedding failed: {e}")
        return None
