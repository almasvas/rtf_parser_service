from striprtf.striprtf import rtf_to_text

def extract_text_from_rtf(content: bytes) -> str:
    try:
        text = rtf_to_text(content.decode("cp1251"))
        return text.strip()
    except Exception as e:
        raise ValueError(f"Ошибка парсинга: {e}")
