import logging
from pathlib import Path
from extractors import extract_pptx, extract_pdf, extract_ipynb
from processing.chunker import chunk_text
from rag.embedder import embed_text
from rag.vector_store import index_chunks, file_exists
from rag.scanner import scan
import config

log = logging.getLogger("indexer")

def _get_extractor(ext):
    if ext == ".pptx":
        return extract_pptx
    elif ext == ".pdf":
        return extract_pdf
    elif ext == ".ipynb":
        return extract_ipynb
    return None

def index_file(file_path, module):
    ext = Path(file_path).suffix.lower()
    extractor = _get_extractor(ext)
    if not extractor:
        return "No extractor"

    raw = extractor(file_path)
    if not raw:
        return "No content"

    source_type = ext.lstrip(".")
    chunks = chunk_text(raw, source_type)

    for chunk in chunks:
        vec = embed_text(chunk["text"])
        if vec:
            chunk["embedding"] = vec

    index_chunks(chunks, module, Path(file_path).name, file_path)
    return f"{len(chunks)} chunks"

def index_all(force=False):
    files = scan()
    total = len(files)
    processed = 0
    skipped = 0
    errors = 0

    for i, (file_path, module, filename) in enumerate(files, 1):
        if not force and file_exists(file_path):
            print(f"[{i:>4}/{total}] SKIP {filename} (already indexed)")
            skipped += 1
            continue

        print(f"[{i:>4}/{total}] {module:20} {filename}")
        try:
            result = index_file(file_path, module)
            print(f"  -> {result}")
            processed += 1
        except Exception as e:
            print(f"  -> ERROR: {e}")
            errors += 1

    print(f"\nDone. {processed} indexed, {skipped} skipped, {errors} errors.")
    return processed, skipped, errors
