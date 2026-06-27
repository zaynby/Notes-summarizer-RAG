def chunk_pptx(pages):
    chunks = []
    for num, text in pages:
        chunks.append({
            "position": num,
            "label": f"Slide {num}",
            "text": text
        })
    return chunks

def chunk_pdf(pages):
    chunks = []
    for num, text in pages:
        chunks.append({
            "position": num,
            "label": f"Page {num}",
            "text": text
        })
    return chunks

def chunk_ipynb(cells):
    chunks = []
    for num, cell_type, source in cells:
        prefix = "Code" if cell_type == "code" else "Markdown"
        chunks.append({
            "position": num,
            "label": f"Cell {num} ({prefix})",
            "text": source
        })
    return chunks

def chunk_text(raw, source_type):
    if source_type == "pptx":
        return chunk_pptx(raw)
    elif source_type == "pdf":
        return chunk_pdf(raw)
    elif source_type == "ipynb":
        return chunk_ipynb(raw)
    return [{"position": 0, "label": "", "text": raw}]
