# Spec: issue-6 — add `is_palindrome(text)` helper

## Goal
Provide a minimal palindrome-checking helper with tests.

## Deliverables
- `palindrome.py` (repo root) exposing `is_palindrome(text: str) -> bool`.
- `test_palindrome.py` (repo root) with pytest tests.

## Behavior
`is_palindrome(text)` returns `True` if `text` reads the same forwards and
backwards after:
- lowercasing (case-insensitive comparison), and
- removing all non-alphanumeric characters.

Examples:
- `"A man, a plan, a canal: Panama"` → `True`
- `"hello"` → `False`
- `""` → `True` (empty string is a palindrome)

## Tests (`test_palindrome.py`)
Cover exactly the three cases above:
- `"A man, a plan, a canal: Panama"` → `True`
- `"hello"` → `False`
- `""` → `True`

## Constraints
- Keep it minimal: no extra files, no third-party dependencies (standard
  library only; pytest is the only test runner).
