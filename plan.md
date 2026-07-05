# Plan: Add a greet(name) function

Derived from [spec.md](spec.md). Minimal implementation, no extra files or dependencies.

## Tasks

1. **Create `greet.py`** (repo root)
   - Define `def greet(name: str) -> str:` returning `f"Hello, {name}!"`.
   - No imports, no side effects, no `__main__` block.

2. **Create `test_greet.py`** (repo root)
   - Import `greet` from `greet`.
   - Add `def test_greet():` asserting `greet("World") == "Hello, World!"`.

3. **Verify**
   - Run `pytest` and confirm it passes.

## Acceptance Criteria
- `pytest` passes.
- `greet("World") == "Hello, World!"`.

## Notes / Constraints
- Keep it minimal: only `greet.py` and `test_greet.py` are added.
- No changes to existing files.
- pytest is the only (dev/test-only) dependency.
