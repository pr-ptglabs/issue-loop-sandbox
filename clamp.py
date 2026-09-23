def clamp(x: float, lo: float, hi: float) -> float:
    """Return x limited to the closed interval [lo, hi]."""
    if lo > hi:
        raise ValueError("lo must not be greater than hi")
    return max(lo, min(x, hi))
