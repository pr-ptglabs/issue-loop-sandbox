def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards.

    Case is ignored and non-alphanumeric characters are skipped.
    """
    normalized = [ch.casefold() for ch in text if ch.isalnum()]
    return normalized == normalized[::-1]
