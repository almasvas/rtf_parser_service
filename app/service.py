from app.parser import extract_text_from_rtf

def parse_rtf_file(file_bytes: bytes) -> str:
    return extract_text_from_rtf(file_bytes)
