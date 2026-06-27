from rag.embedder import embed_text
from rag.vector_store import search

def query(query_text, top_k=5, module=None):
    vec = embed_text(query_text)
    if not vec:
        print("Failed to embed query.")
        return []
    results = search(vec, top_k=top_k, module=module)
    return results

def print_results(results):
    if not results:
        print("No results found.")
        return
    for i, r in enumerate(results, 1):
        print(f"\n{'='*60}")
        print(f"Result {i}  (score: {r['score']})")
        print(f"Module: {r['module']}  |  File: {r['filename']}  |  {r['label']}")
        print(f"{'='*60}")
        text = r["text"][:600]
        print(text)
        if len(r["text"]) > 600:
            print("...")
