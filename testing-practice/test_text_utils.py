from text_utils import clean_text

def test_clean_text_removes_extra_spaces():
    assert clean_text("  Hello   World  ") == "hello there"

def test_clean_text_empty():
    assert clean_text("") == ""