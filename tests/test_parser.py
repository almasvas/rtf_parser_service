from app.parser import extract_text_from_rtf

def test_extract_text():
    rtf = b"{\\rtf1\\ansi\\deff0 {\\fonttbl {\\f0 Courier;}}\\f0\\fs20 Hello, world!}"
    assert "Hello, world!" in extract_text_from_rtf(rtf)
