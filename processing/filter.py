from pathlib import Path

SKIP_DIR_PATTERNS = [
    "exercise", "tutorial", "assignment", "homework", "quiz",
    "oal", "solution", "activity", "activities",
    "assignments", "exercises",
]

SKIP_FILE_PATTERNS = [
    "certificate", "certification", "badge", "credential",
    "rubric", "syllabus", "answer_key", "answer key",
    "suggested_solution", "suggested solution", "_solution",
    "suggestion", "_solution_", "solution_",
]

def should_skip(file_path):
    path = Path(file_path)
    name_lower = path.name.lower()
    parts_lower = [p.lower() for p in path.parts]
    ext = path.suffix.lower()

    if ext not in {".pptx", ".pdf", ".ipynb"}:
        return True, "unsupported extension"

    if any("lesson slide" in part for part in parts_lower):
        return False, ""

    if ext == ".pptx":
        return False, ""

    for part in parts_lower:
        for pattern in SKIP_DIR_PATTERNS:
            if pattern in part:
                return True, f"path contains '{pattern}'"

    for pattern in SKIP_FILE_PATTERNS:
        if pattern in name_lower:
            return True, f"filename contains '{pattern}'"

    if ext == ".ipynb" and any("practical" in part for part in parts_lower):
        return False, ""

    return False, ""
