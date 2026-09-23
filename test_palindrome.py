from palindrome import is_palindrome


def test_sentence_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_non_palindrome():
    assert is_palindrome("hello") is False


def test_empty_string():
    assert is_palindrome("") is True
