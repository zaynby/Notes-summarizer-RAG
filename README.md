# Study Knowledge Base RAG

A local RAG (Retrieval-Augmented Generation) pipeline that indexes your lecture materials — slides, PDFs, and Jupyter notebooks — into a searchable vector database. Designed for agents to query.

## Quick Start

```bash
pip install -r requirements.txt
# Copy and edit .env.example → .env with your study folder path
python main.py index
python main.py query "your question"
```

## Commands

| Command | Description |
|---------|-------------|
| `python main.py index` | Index all study materials |
| `python main.py index --force` | Re-index everything |
| `python main.py watch` | Index + watch for new/modified files |
| `python main.py query "question"` | Search the knowledge base |
| `python main.py query "question" --module deep_learning` | Search one module |
| `python main.py stats` | Show per-module chunk counts |
| `python main.py serve` | Start REST API for agent access |
| `python main.py serve --port 9000` | Custom port |

## Requirements

- Python 3.11+
- [Ollama](https://ollama.ai) running locally with `nomic-embed-text` model pulled
- Windows (paths use backslash convention; adjustable for other OS)

### Pull the embedding model

```bash
ollama pull nomic-embed-text
```

## REST API

Start the server for agent access:

```bash
python main.py serve
```

```python
import requests
r = requests.post("http://localhost:8000/query", json={
    "question": "explain backpropagation",
    "module": "deep_learning",
    "top_k": 5
})
print(r.json())
```

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/query` | POST | Search the knowledge base |
| `/stats` | GET | Per-module chunk counts |

## Architecture

```
main.py                CLI: index, watch, query, stats, serve
config.py              Paths and settings
module_detector.py     Extracts module name from file path
extractors/            Text extraction per file type (pptx, pdf, ipynb)
processing/
  chunker.py           Structural chunking (no overlap)
  filter.py            Skip exercises, solutions, certificates
rag/
  scanner.py           Walk source folder with filtering
  indexer.py           Extract → chunk → embed → store
  embedder.py          nomic-embed-text via Ollama
  vector_store.py      ChromaDB operations
  retriever.py         Query interface
  watcher.py           File system watcher
  api.py               FastAPI REST server
```

## Configuration

Copy `.env.example` to `.env` and set:

```env
WATCH_FOLDER=C:\Path\To\Your\Study\Materials
```

## What gets indexed

Only `.pptx`, `.pdf`, and `.ipynb` files. Filtered out automatically:
- Exercises, tutorials, assignments, quizzes
- OALs and in-class activities
- Solutions and answer keys
- Certificates and badges
- Modules: `calculus`, `ehe`

## Tech Stack

| Component | Choice |
|-----------|--------|
| Vector DB | ChromaDB |
| Embeddings | nomic-embed-text (via Ollama) |
| Chunking | Structural (by slide/page/cell) |
| File parsing | python-pptx, PyMuPDF, nbformat |
| File watching | watchdog |
| REST API | FastAPI + uvicorn |
