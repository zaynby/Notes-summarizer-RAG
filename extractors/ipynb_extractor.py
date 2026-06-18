import json
from pathlib import Path

def extract_ipynb(file_path: str) -> str:
    "Extract text and code from a Jupyter Notebook file."
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        text_parts = []
        for i, cell in enumerate(notebook.get('cells', [])):
            cell_type = cell.get('cell_type', 'unknown')
            source = ''.join(cell.get('source', []))

            if not source.strip():
                continue

            if cell_type == 'markdown':
                text_parts.append(f"# Markdown Cell {i+1}\n{source}")
            elif cell_type == 'code':
                text_parts.append(f"# Code Cell {i+1}\n```python\n{source}\n```")
            else:
                text_parts.append(f"# Raw Cell {i+1}\n{source}")

        return "\n\n".join(text_parts)
    except Exception as e:
        return f"Error extracting IPYNB: {str(e)}"
