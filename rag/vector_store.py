import logging
import threading
from pathlib import Path
from typing import List, Dict, Any, Optional
import chromadb
from chromadb.config import Settings
import config

log = logging.getLogger("vector_store")
_collection = None
_lock = threading.RLock()

def _get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(
            path=str(Path(config.CHROMADB_PATH).resolve()),
            settings=Settings(anonymized_telemetry=False)
        )
        _collection = client.get_or_create_collection(
            name="study_notes",
            metadata={"hnsw:space": "cosine"}
        )
    return _collection

def index_chunks(chunks: List[Dict[str, Any]], module: str, filename: str, file_path: str):
    with _lock:
        collection = _get_collection()
        ids, embeddings, metadatas, documents = [], [], [], []
        for chunk in chunks:
            vec = chunk.get("embedding")
            if not vec:
                continue
            chunk_id = f"{file_path}:{chunk['position']}"
            ids.append(chunk_id)
            embeddings.append(vec)
            metadatas.append({
                "module": module,
                "filename": filename,
                "file_path": file_path,
                "position": str(chunk["position"]),
                "label": chunk.get("label", ""),
            })
            documents.append(chunk["text"])
        if ids:
            collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=documents)
            log.info(f"Indexed {len(ids)} chunks from {filename}")

def search(query_vec: List[float], top_k: int = 5, module: Optional[str] = None) -> List[Dict[str, Any]]:
    with _lock:
        collection = _get_collection()
        where = {"module": module} if module else None
        results = collection.query(
            query_embeddings=[query_vec],
            n_results=min(top_k, 50),
            where=where,
        )
        out = []
        for i in range(len(results["ids"][0])):
            out.append({
                "text": results["documents"][0][i],
                "module": results["metadatas"][0][i].get("module", "?"),
                "filename": results["metadatas"][0][i].get("filename", "?"),
                "position": results["metadatas"][0][i].get("position", "?"),
                "label": results["metadatas"][0][i].get("label", ""),
                "score": round(results["distances"][0][i], 4) if results.get("distances") else 0,
            })
        return out

def file_exists(file_path: str) -> bool:
    with _lock:
        collection = _get_collection()
        r = collection.get(where={"file_path": file_path}, limit=1)
        return len(r["ids"]) > 0

def delete_file(file_path: str):
    with _lock:
        _get_collection().delete(where={"file_path": file_path})

def count_chunks() -> int:
    with _lock:
        return _get_collection().count()

def module_stats() -> List[Dict[str, Any]]:
    with _lock:
        collection = _get_collection()
        all_meta = collection.get(limit=count_chunks())["metadatas"]
        counts = {}
        for m in all_meta:
            mod = m.get("module", "unknown")
            counts[mod] = counts.get(mod, 0) + 1
        return [{"module": k, "chunks": v} for k, v in sorted(counts.items())]
