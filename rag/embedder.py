import logging
from typing import List, Optional

log = logging.getLogger("embedder")

# Global client for reuse
_ollama_client = None


def _get_client():
    global _ollama_client
    if _ollama_client is None:
        import ollama
        # Reuse config directly at call time
        import config as cfg
        _ollama_client = ollama.Client(host=cfg.OLLAMA_BASE_URL)
    return _ollama_client


def embed_text(text: str) -> Optional[List[float]]:
    """Embed a single text string using nomic-embed-text."""
    try:
        client = _get_client()
        import config as cfg
        response = client.embeddings(
            model=cfg.EMBEDDING_MODEL,
            prompt=text[:8192]  # cap at model's context limit
        )
        return response["embedding"]
    except Exception as e:
        log.error(f"Embedding failed: {e}")
        return None


def embed_chunks(chunks: List[dict]) -> List[dict]:
    """Embed a list of chunks (mutates in place)."""
    for chunk in chunks:
        vec = embed_text(chunk["text"])
        if vec:
            chunk["embedding"] = vec
            chunk["embedding_status"] = "ok"
        else:
            chunk["embedding_status"] = "failed"
    return chunks
