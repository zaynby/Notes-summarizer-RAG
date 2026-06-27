import json

def extract_ipynb(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    cells = []
    for i, cell in enumerate(nb.get("cells", []), 1):
        source = "".join(cell.get("source", []))
        if not source.strip():
            continue
        cell_type = cell.get("cell_type", "raw")
        cells.append((i, cell_type, source.strip()))
    return cells
