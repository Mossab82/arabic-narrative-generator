from camel_tools.utils.dediac import dediac_ar
from camel_tools.tokenizers.word import simple_word_tokenize

class TextPreprocessor:
    def __init__(self):
        """
        Initializes the text preprocessor for Arabic text.
        """
        pass

    def preprocess_text(self, text):
        """
        Preprocess Arabic text by normalizing, removing diacritics, and tokenizing.

        Args:
            text (str): Input Arabic text.

        Returns:
            str: Preprocessed and tokenized text.
        """
        cleaned_text = self.clean_text(text)
        normalized_text = self.normalize_arabic(cleaned_text)
        tokenized_text = self.tokenize(normalized_text)
        return tokenized_text

    def clean_text(self, text):
        """
        Removes diacritics and excessive whitespace.

        Args:
            text (str): Input Arabic text.

        Returns:
            str: Cleaned text.
        """
        text = dediac_ar(text)  # Removes diacritics
        return " ".join(text.split())  # Removes extra spaces

    def normalize_arabic(self, text):
        """
        Normalizes Arabic characters (e.g., converts ي to ى).

        Args:
            text (str): Input Arabic text.

        Returns:
            str: Normalized text.
        """
        replacements = {
            "إ": "ا",
            "أ": "ا",
            "آ": "ا",
            "ة": "ه",
            "ى": "ي"
        }
        for key, value in replacements.items():
            text = text.replace(key, value)
        return text

    def tokenize(self, text):
        """
        Tokenizes Arabic text into words.

        Args:
            text (str): Input Arabic text.

        Returns:
            list: List of tokens.
        """
        return simple_word_tokenize(text)
