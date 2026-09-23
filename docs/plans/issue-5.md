# Plan: add clamp(x, lo, hi) helper (issue #5)

Spec: `docs/specs/issue-5.md`

## Overview
Implement a minimal `clamp` helper limiting a value to the closed interval
`[lo, hi]`, plus pytest coverage. Standard library only; no new files beyond
the two deliverables.

## Tasks

### 1. Implement `clamp.py` (repo root)
- Define `def clamp(x: float, lo: float, hi: float) -> float`.
- Raise `ValueError` if `lo > hi` (check first).
- Return `lo` if `x < lo`, `hi` if `x > hi`, else `x`.
- Idiomatic form: `return max(lo, min(x, hi))` after the `lo > hi` guard.
- No imports, no `__main__`, no extra helpers.

### 2. Implement `test_clamp.py` (repo root)
- `import pytest` and `from clamp import clamp`.
- Test below: `clamp(-1, 0, 10) == 0`.
- Test inside: `clamp(5, 0, 10) == 5` (also boundary values `0` and `10`).
- Test above: `clamp(11, 0, 10) == 10`.
- Test invalid range: `with pytest.raises(ValueError): clamp(1, 10, 0)`.

## Verification
- Run `pytest test_clamp.py` (or `pytest`) from repo root; all tests pass.

## Constraints
- Only `clamp.py` and `test_clamp.py` added. No third-party dependencies.
