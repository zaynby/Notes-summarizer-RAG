import re
import logging
from typing import List, Dict, Any

log = logging.getLogger("chunker")

# Rough estimate: 1 token ≈ 4 chars
CHUNK_CHARS = 2000  # ~500 tokens
OVERLAP_CHARS = 200


def chunk_by_slides(text: str) -> List[str]:
    """Split PPTX text by slide markers."""
    slides = re.split(r'# Slide \d+', text)
    return [s.strip() for s in slides if len(s.strip()) > 50]


def chunk_by_pages(text: str) -> List[str]:
    """Split PDF text by page markers."""
    pages = re.split(r'# Page \d+', text)
    return [p.strip() for p in pages if len(p.strip()) > 50]


def chunk_by_cells(text: str) -> List[str]:
    """Split IPYNB text by cell markers."""
    cells = re.split(r'# (Markdown|Code|Raw) Cell \d+', text)
    # re.split with capture group produces interlaced results
    chunks = []
    current = ""
    for part in cells:
        if part in ("Markdown", "Code", "Raw"):
            if current.strip():
                chunks.append(current.strip())
            current = ""
        else:
            current += part
    if current.strip():
        chunks.append(current.strip())
    return [c for c in chunks if len(c) > 50]


def chunk_generic(text: str) -> List[str]:
    """Fallback: split by fixed character size with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + CHUNK_CHARS, len(text))
        chunks.append(text[start:end].strip())
        start += CHUNK_CHARS - OVERLAP_CHARS
    return [c for c in chunks if len(c) > 50]


def chunk_text(text: str, source_type: str = "generic") -> List[Dict[str, Any]]:
    """Split extracted text into chunks. Returns list of {text: str}."""
    if source_type == "pptx":
        chunks = chunk_by_slides(text)
    elif source_type == "pdf":
        chunks = chunk_by_pages(text)
    elif source_type == "ipynb":
        chunks = chunk_by_cells(text)
    else:
        chunks = chunk_generic(text)

    if not chunks:
        chunks = chunk_generic(text)

    return [{"text": c} for c in chunks]
