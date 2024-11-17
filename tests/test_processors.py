import pytest
from src.processors.text_preprocessor import TextPreprocessor

@pytest.fixture
def preprocessor():
    return TextPreprocessor()

def test_clean_text(preprocessor):
    text = "تَجْرِبَةٌ  "
    result = preprocessor.clean_text(text)
    assert result == "تجربة"

def test_normalize_arabic(preprocessor):
    text = "إختبار"
    result = preprocessor.normalize_arabic(text)
    assert result == "اختبار"

def test_tokenize(preprocessor):
    text = "هذا اختبار"
    result = preprocessor.tokenize(text)
    assert result == ["هذا", "اختبار"]

