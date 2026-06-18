import fitz  # PyMuPDF

def extract_pdf(file_path: str) -> str:
    "Extract text from a PDF file."
    try:
        doc = fitz.open(file_path)
        text_parts = []
        for page_num, page in enumerate(doc, 1):
            text = page.get_text().strip()
            if text:
                text_parts.append(f"# Page {page_num}\n{text}")
        doc.close()
        return "\n\n".join(text_parts)
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"
