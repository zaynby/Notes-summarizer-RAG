import fitz

def extract_pdf(file_path):
    doc = fitz.open(file_path)
    pages = []
    for page_num, page in enumerate(doc, 1):
        text = page.get_text().strip()
        if text:
            pages.append((page_num, text))
    doc.close()
    return pages
