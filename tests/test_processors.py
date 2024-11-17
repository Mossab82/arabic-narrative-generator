```python
import pytest
from src.processors.text_processor import TextProcessor

@pytest.fixture
def processor():
    return TextProcessor()

def test_text_normalization(processor):
    test_text = "قَالَ شَهْرَيَارُ"
    normalized = processor.normalize_text(test_text)
    assert isinstance(normalized, str)
    assert normalized != test_text
    assert "قال شهريار" in normalized

def test_text_tokenization(processor):
    test_text = "قال شهريار لشهرزاد"
    tokens = processor.tokenize_text(test_text)
    assert isinstance(tokens, list)
    assert len(tokens) == 3
    assert "قال" in tokens
    assert "شهريار" in tokens
