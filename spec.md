# Spec: Add a greet(name) function

## Goal
Provide a minimal `greet` function with a corresponding test.

## Deliverables
1. `greet.py` (repo root)
   - Function: `greet(name: str) -> str`
   - Behavior: returns the string `Hello, {name}!` (the `name` value interpolated).
   - Example: `greet("World")` returns `"Hello, World!"`.

2. `test_greet.py` (repo root)
   - A pytest test asserting `greet("World") == "Hello, World!"`.

## Constraints
- Keep it minimal: no extra files, no external dependencies beyond pytest (dev/test only).
- No changes to existing files.

## Acceptance Criteria
- `pytest` passes.
- `greet("World") == "Hello, World!"`.
