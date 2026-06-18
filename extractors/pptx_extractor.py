from pptx import Presentation
from pathlib import Path

def extract_pptx(file_path: str) -> str:
    "Extract text from a PowerPoint file."
    try:
        prs = Presentation(file_path)
        text_parts = []
        for slide_num, slide in enumerate(prs.slides, 1):
            text_parts.append(f"# Slide {slide_num}")
            for shape in slide.shapes:
                if shape.has_text_frame:
                    for paragraph in shape.text_frame.paragraphs:
                        text = paragraph.text.strip()
                        if text:
                            text_parts.append(text)
        return "\n\n".join(text_parts)
    except Exception as e:
        return f"Error extracting PPTX: {str(e)}"
