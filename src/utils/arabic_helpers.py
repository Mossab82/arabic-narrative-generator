from camel_tools.utils.normalize import normalize_unicode

def normalize_text(text):
    """
    Normalizes Arabic text to ensure consistent encoding.

    Args:
        text (str): Input Arabic text.

    Returns:
        str: Normalized Arabic text.
    """
    return normalize_unicode(text)
