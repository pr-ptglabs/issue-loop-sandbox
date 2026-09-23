# Spec: add clamp(x, lo, hi) helper (issue #5)

## Goal
Provide a minimal `clamp` helper that limits a value to a closed interval `[lo, hi]`.

## Deliverables
- `clamp.py` at the repo root.
- `test_clamp.py` at the repo root with pytest tests.

No other files, no third-party dependencies.

## API
```python
def clamp(x: float, lo: float, hi: float) -> float
```

### Behavior
- Returns `x` limited to the closed interval `[lo, hi]`:
  - `x < lo` → returns `lo` (below).
  - `lo <= x <= hi` → returns `x` (inside).
  - `x > hi` → returns `hi` (above).
- Raises `ValueError` if `lo > hi`.

## Tests (`test_clamp.py`)
Cover the four cases:
1. Below: `x < lo` returns `lo`.
2. Inside: `lo <= x <= hi` returns `x`.
3. Above: `x > hi` returns `hi`.
4. Invalid range: `lo > hi` raises `ValueError` (assert via `pytest.raises`).

## Constraints
- Keep it minimal — standard library only, no extra files or dependencies.
