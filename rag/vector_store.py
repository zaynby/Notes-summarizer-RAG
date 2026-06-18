import logging
from typing import List, Dict, Any, Optional
import chromadb
from chromadb.config import Settings
from pathlib import Path

import config

log = logging.getLogger("vector_store")

_collection = None


def _get_collection():
    global _collection
    if _collection is None:
        db_path = str(Path(config.CHROMADB_PATH).resolve())
        client = chromadb.PersistentClient(
            path=db_path,
            settings=Settings(anonymized_telemetry=False)
        )
        _collection = client.get_or_create_collection(
            name="study_notes",
            metadata={"hnsw:space": "cosine"}
        )
    return _collection


def add_chunks(
    chunks: List[Dict[str, Any]],
    module: str,
    filename: str,
    file_path: str
):
    """Add chunked content to vector store."""
    collection = _get_collection()
    existing_ids = set()
    batch_ids = []
    batch_embeddings = []
    batch_metadatas = []
    batch_documents = []

    for i, chunk in enumerate(chunks):
        if chunk.get("embedding_status") != "ok":
            continue

        chunk_id = f"{file_path}:{i}"
        if chunk_id in existing_ids:
            continue
        existing_ids.add(chunk_id)

        batch_ids.append(chunk_id)
        batch_embeddings.append(chunk["embedding"])
        batch_metadatas.append({
            "module": module,
            "filename": filename,
            "file_path": file_path,
            "chunk_index": str(i),
        })
        batch_documents.append(chunk["text"])

    if batch_ids:
        # Upsert to handle re-processing same file
        collection.upsert(
            ids=batch_ids,
            embeddings=batch_embeddings,
            metadatas=batch_metadatas,
            documents=batch_documents,
        )
        log.info(f"Stored {len(batch_ids)} chunks for {filename}")
    else:
        log.warning(f"No chunks with valid embeddings for {filename}")


def search_similar(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """Search vector store for chunks similar to query text."""
    from rag.embedder import embed_text

    vec = embed_text(query)
    if not vec:
        log.warning("Could not embed query, returning empty results")
        return []

    collection = _get_collection()
    results = collection.query(
        query_embeddings=[vec],
        n_results=min(top_k, 20),
    )

    retrieved = []
    for i in range(len(results["ids"][0])):
        retrieved.append({
            "text": results["documents"][0][i],
            "module": results["metadatas"][0][i].get("module", "?"),
            "filename": results["metadatas"][0][i].get("filename", "?"),
            "score": results["distances"][0][i] if results.get("distances") else 0,
        })
    return retrieved


def search_similar_by_module(
    query: str, module: str, top_k: int = 5
) -> List[Dict[str, Any]]:
    """Search similar chunks, filtered by module."""
    results = search_similar(query, top_k)
    return [r for r in results if r.get("module") == module]


def file_exists(file_path: str) -> bool:
    """Check if any chunks exist for a given file path."""
    collection = _get_collection()
    count = collection.count()
    if count == 0:
        return False
    results = collection.get(where={"file_path": file_path}, limit=1)
    return len(results["ids"]) > 0


def delete_file(file_path: str):
    """Delete all chunks for a given file path."""
    collection = _get_collection()
    collection.delete(where={"file_path": file_path})
    log.info(f"Deleted chunks for {file_path}")


def count_chunks() -> int:
    collection = _get_collection()
    return collection.count()
