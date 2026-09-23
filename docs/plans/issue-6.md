# Plan: issue-6 — add `is_palindrome(text)` helper

Derived from `docs/specs/issue-6.md`. No gaps found; spec is complete.

## Tasks

### 1. Create `palindrome.py` (repo root)
- Define `is_palindrome(text: str) -> bool`.
- Normalize: lowercase the text and keep only alphanumeric characters
  (use `str.isalnum()` / `str.casefold()`; standard library only).
- Return whether the normalized sequence equals its reverse.
- Empty/normalized-to-empty input returns `True`.

### 2. Create `test_palindrome.py` (repo root)
- pytest tests covering exactly the three spec cases:
  - `"A man, a plan, a canal: Panama"` → `True`
  - `"hello"` → `False`
  - `""` → `True`

## Verification
- Run `pytest test_palindrome.py` from the repo root; all tests pass.

## Constraints
- Minimal: only the two files above, standard library only, no third-party
  dependencies beyond pytest as the test runner.
