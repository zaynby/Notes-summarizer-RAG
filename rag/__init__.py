from rag.chunker import chunk_text
from rag.embedder import embed_chunks
from rag.vector_store import add_chunks, search_similar, count_chunks


def ingest_text(
    text: str,
    module: str,
    filename: str,
    file_path: str,
    source_type: str = "generic"
):
    """Full ingestion pipeline: chunk → embed → store."""
    chunks = chunk_text(text, source_type)
    chunks = embed_chunks(chunks)
    add_chunks(chunks, module, filename, file_path)


def retrieve_few_shot(text: str, module: str = None, top_k: int = 5) -> str:
    """Retrieve similar chunks as few-shot examples for summarization."""
    results = search_similar(text, top_k)
    if not results:
        return ""

    parts = []
    for r in results:
        parts.append(
            f"### Example from {r['filename']} ({r['module']}):\n{r['text']}"
        )
    return "\n\n".join(parts)


__all__ = ["ingest_text", "retrieve_few_shot", "count_chunks"]
