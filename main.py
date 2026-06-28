"""
RAG Knowledge Base — Index your study materials and query them.

Usage:
    python main.py index [--force]     Index all files in watch folder
    python main.py watch               Watch for new/modified files and index automatically
    python main.py query <question>    Search the knowledge base
    python main.py stats               Show indexing stats
    python main.py serve [--port N]    Start REST API server
    python main.py telegram            Start Telegram bot (starts API server too)
"""

import sys
import logging

import config
from rag.indexer import index_all
from rag.retriever import query, print_results
from rag.vector_store import count_chunks, module_stats

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s %(name)s: %(message)s",
)


def cmd_index():
    force = "--force" in sys.argv
    index_all(force=force)


def cmd_query():
    if len(sys.argv) < 3:
        print("Usage: python main.py query \"your question\" [--module MODULE] [--top-k N]")
        return
    question = sys.argv[2]
    module = None
    top_k = 5
    args = sys.argv[3:]
    for i, a in enumerate(args):
        if a == "--module" and i + 1 < len(args):
            module = args[i + 1]
        if a == "--top-k" and i + 1 < len(args):
            try:
                top_k = int(args[i + 1])
            except ValueError:
                pass

    results = query(question, top_k=top_k, module=module)
    print_results(results)


def cmd_stats():
    c = count_chunks()
    print(f"Total chunks: {c}")
    print()
    for m in module_stats():
        print(f"  {m['module']:25} {m['chunks']} chunks")


def cmd_watch():
    print("=== Initial sync (indexing unprocessed files) ===")
    index_all(force=False)
    print("\n=== Starting file watcher ===")
    from rag.watcher import start_watcher
    start_watcher()


def cmd_serve():
    import uvicorn
    port = int(config.API_PORT)
    args = sys.argv[2:]
    for i, a in enumerate(args):
        if a == "--port" and i + 1 < len(args):
            try:
                port = int(args[i + 1])
            except ValueError:
                pass
    print(f"Starting API server on http://localhost:{port}")
    uvicorn.run("rag.api:app", host="0.0.0.0", port=port, log_level="info")

def cmd_telegram():
    import threading, uvicorn, time
    port = int(config.API_PORT)
    t = threading.Thread(
        target=uvicorn.run,
        args=("rag.api:app",),
        kwargs={"host": "0.0.0.0", "port": port, "log_level": "error"},
        daemon=True,
    )
    t.start()
    time.sleep(2)

    from bot.telegram import run_bot
    run_bot()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1]
    commands = {
        "index": cmd_index,
        "query": cmd_query,
        "stats": cmd_stats,
        "watch": cmd_watch,
        "serve": cmd_serve,
        "telegram": cmd_telegram,
    }

    cmd = commands.get(command)
    if cmd:
        cmd()
    else:
        print(f"Unknown command: {command}")
        print("Available: index, query, stats, watch, serve, telegram")
        sys.exit(1)


if __name__ == "__main__":
    main()
