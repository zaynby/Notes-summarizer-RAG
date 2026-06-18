# Notes-summarizer

> AI-powered study agent that watches your school folders, classifies theory vs code, summarizes everything into a searchable RAG second brain. Query your notes in plain English.

![Python](https://img.shields.io/badge/python-3.11+-blue?logo=python)
![Ollama](https://img.shields.io/badge/LLM-Ollama%20%7C%20NVIDIA%20NIM%20%7C%20OpenRouter-green)
![ChromaDB](https://img.shields.io/badge/vector-ChromaDB-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Features

- **Auto-watch** — Watches folders for new `.pptx`, `.pdf`, `.ipynb` files and processes them instantly
- **Smart classification** — Detects whether content is theory or practical code, routes to the right summary style
- **RAG-powered Q&A** — Ask questions in natural language; retrieves semantically relevant chunks from your entire note corpus
- **LLM-agnostic** — Works with Ollama (local), NVIDIA NIM (free tier), or OpenRouter — auto-detects and falls back
- **Self-improving** — Evaluates summary quality every 5 files per module, adapts style family to what works best
- **Idempotent sync** — Scan existing folders without reprocessing already-indexed files
- **Per-module journals** — Tracks progress and style evolution for each subject

## Architecture

```
Study Folder (.pptx/.pdf/.ipynb)
        |
    [Watcher] —──→ [Extractor] —──→ [Classifier] —──→ [Summarizer] ──→ Summary (.md)
                           \                                    /
                            └── [Chunker] ──→ [Embedder] ──→ [ChromaDB]
                                                                |
                                                           [Query Engine]
                                                                |
                                                          Your question
```

## Usage

| Command | Description |
|---|---|
| `python main.py watch` | Start folder watcher (processes new files in real-time) |
| `python main.py sync [--force]` | Scan folder and index all unprocessed files |
| `python main.py query "..."` | Ask a question over your vector store |
| `python main.py status` | Show style memory, modules, and vector store stats |
| `python main.py rag-count` | Count chunks in the vector store |
| `python main.py eval [module]` | Evaluate & improve summary quality per module |
| `python main.py process <file>` | Process a single file manually |

## Configuration

All settings in `config.py` and `.env`:

| Variable | Default | Description |
|---|---|---|
| `WATCH_FOLDER` | *(required)* | Path to your study notes folder |
| `NVIDIA_API_KEY` | — | NVIDIA NIM API key (free at build.nvidia.com) |
| `OPENROUTER_API_KEY` | — | OpenRouter API key (optional fallback) |
| `OLLAMA_MODEL` | `qwen2.5:7b` | Local LLM model name |
| `EMBED_MODEL` | `nomic-embed-text` | Embedding model (must be in Ollama) |

## Project Structure

```
Notes-summarizer/
├── main.py              # CLI entry point
├── config.py            # Paths, models, chunk settings
├── watcher.py           # Real-time folder monitor
├── summarizer.py        # Classification → summarization pipeline
├── llm.py               # Multi-provider LLM client
├── query.py             # RAG question-answering
├── module_detector.py   # Extract module name from file path
├── journal.py           # Per-module progress journaling
├── style_evaluator.py   # Self-improvement evaluation loop
├── style_memory.py      # Per-module style state (JSON)
├── extractors/          # Text extraction per file type
│   ├── pptx_extractor.py
│   ├── pdf_extractor.py
│   └── ipynb_extractor.py
├── rag/                 # Vector RAG pipeline
│   ├── chunker.py       # Slide/cell/page-aware chunking
│   ├── embedder.py      # nomic-embed-text wrapper
│   ├── vector_store.py  # ChromaDB persistence layer
│   └── __init__.py      # Ingest & retrieve helpers
├── requirements.txt
└── .env.example
```

## Tech Stack

| Component | Choice | Why |
|---|---|---|
| **LLMs** | Ollama (local) / NVIDIA NIM / OpenRouter | Free, private, no API keys required for local |
| **Embeddings** | `nomic-embed-text` via Ollama | 768-dim, local, zero cost |
| **Vector store** | ChromaDB | Pure Python, persistent, no server needed |
| **File parsing** | python-pptx, PyMuPDF, nbformat | Full coverage of school file formats |
| **File watching** | watchdog | Cross-platform, event-driven |

## How It Works

1. **Detection** — A new file lands in your watch folder. The watcher picks it up.
2. **Extraction** — Text is pulled out: slides for PPTX, pages for PDF, cells for IPYNB.
3. **Classification** — The LLM decides: is this *theory* (lecture slides, notes) or *practical code* (exercises, notebooks)?
4. **Summarization** — Content is summarized in a style family chosen per-module (structured academic, code breakdown, etc.), adapting over time.
5. **Indexing** — The summary is chunked, embedded, and stored in ChromaDB.
6. **Querying** — Ask a question → embed it → search top-5 similar chunks → LLM generates a grounded answer.

## License

MIT
