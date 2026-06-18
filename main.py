"""
Personal Agent — Self-Improving Note Summarizer + RAG Second Brain

Usage:
    python main.py watch               Start watching folder for new files
    python main.py eval [module]       Run evaluation on modules
    python main.py process <file>      Process a specific file
    python main.py status              Show style memory status
    python main.py query <question>    Ask a question over your notes
    python main.py rag-count           Show number of chunks in vector store
"""

import sys
import json
from pathlib import Path

import config
from watcher import watch_folder
from summarizer import process_file
from style_evaluator import evaluate_module_style, count_summaries_for_module
from style_memory import load_style_memory


def cmd_watch():
    watch_folder()


def cmd_eval():
    style_memory = load_style_memory()
    modules = style_memory.get("modules", {})
    if not modules:
        print("No modules found in style memory yet.")
        return

    # If specific module provided, only evaluate that one
    target = sys.argv[2] if len(sys.argv) > 2 else None

    for module in modules:
        if target and module != target:
            continue
        count = count_summaries_for_module(module)
        print(f"Module: {module} — Summaries: {count} — "
              f"Style: {modules[module].get('style_family')} — "
              f"Locked: {modules[module].get('locked', False)}")
        result = input(f"  Evaluate '{module}'? (y/n): ").strip().lower()
        if result == "y":
            eval_result = evaluate_module_style(module)
            print(f"  Result: {json.dumps(eval_result, indent=2)}")


def cmd_process():
    if len(sys.argv) < 3:
        print("Usage: python main.py process <file_path>")
        return
    file_path = sys.argv[2]
    if not Path(file_path).exists():
        print(f"File not found: {file_path}")
        return
    result = process_file(file_path)
    print(result)


def cmd_sync():
    from rag.vector_store import file_exists
    force = "--force" in sys.argv
    dry_run = "--dry-run" in sys.argv

    watch = Path(config.WATCH_FOLDER)
    if not watch.exists():
        print(f"Folder not found: {watch}")
        return

    # Collect all supported files
    all_files = []
    for ext in config.SUPPORTED_EXTENSIONS:
        all_files.extend(watch.rglob(f"*{ext}"))

    # Filter temp and checkpoint files
    all_files = [
        f for f in all_files
        if not f.name.startswith("~$")
        and ".ipynb_checkpoints" not in f.parts
        and not f.name.startswith(".")
    ]

    if not all_files:
        print("No supported files found.")
        return

    total = len(all_files)
    print(f"Found {total} files in {watch}")

    if dry_run:
        print("\nWould process:")
        for f in all_files:
            rel = f.relative_to(watch)
            already = " [already indexed]" if not force and file_exists(str(f)) else ""
            print(f"  {rel}{already}")
        return

    # Process each file
    force_flag = " (forced)" if force else ""
    print(f"Processing{force_flag}...\n")

    processed = 0
    skipped = 0
    errors = 0

    for i, file_path in enumerate(all_files, 1):
        rel = file_path.relative_to(watch)

        if not force and file_exists(str(file_path)):
            print(f"[{i:>4}/{total}] SKIP {rel} (already indexed)")
            skipped += 1
            continue

        print(f"[{i:>4}/{total}] {rel}")
        try:
            result = process_file(str(file_path))
            print(f"  -> {result}")
            processed += 1
        except Exception as e:
            print(f"  -> ERROR: {e}")
            errors += 1

    print(f"\nDone. {processed} processed, {skipped} skipped, {errors} errors.")


def cmd_status():
    style_memory = load_style_memory()
    print(f"Last updated: {style_memory.get('last_updated', 'N/A')}")
    print()

    modules = style_memory.get("modules", {})
    if not modules:
        print("No modules processed yet.")
        return

    print(f"{'Module':30} {'Style':30} {'Attempts':10} {'Score':10} {'Locked':10}")
    print("-" * 90)
    for module, info in modules.items():
        count = count_summaries_for_module(module)
        print(f"{module:30} {info.get('style_family', '?'):30} "
              f"{info.get('attempts', 0):<10} "
              f"{str(info.get('score', 'N/A')):10} "
              f"{'Yes' if info.get('locked') else 'No':10} "
              f"(summaries: {count})")

    # Vector store count
    try:
        from rag.vector_store import count_chunks
        c = count_chunks()
        print(f"\nVector store: {c} chunks stored")
    except Exception:
        pass


def cmd_query():
    if len(sys.argv) < 3:
        print("Usage: python main.py query \"your question here\"")
        return
    question = " ".join(sys.argv[2:])
    from query import answer_question
    answer_question(question)


def cmd_rag_count():
    try:
        from rag.vector_store import count_chunks
        c = count_chunks()
        print(f"Vector store contains {c} chunks across all modules.")
    except Exception as e:
        print(f"Could not query vector store: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py watch                Start the folder watcher")
        print("  python main.py sync [--force]       Sync all existing files into RAG")
        print("  python main.py eval [module]        Evaluate styles")
        print("  python main.py process <file>       Process a single file")
        print("  python main.py status               Show style memory status")
        print("  python main.py query \"...\"          Ask a question over your notes")
        print("  python main.py rag-count            Show vector store statistics")
        return

    command = sys.argv[1]
    commands = {
        "watch": cmd_watch,
        "sync": cmd_sync,
        "eval": cmd_eval,
        "process": cmd_process,
        "status": cmd_status,
        "query": cmd_query,
        "rag-count": cmd_rag_count,
    }

    cmd = commands.get(command)
    if cmd:
        cmd()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
