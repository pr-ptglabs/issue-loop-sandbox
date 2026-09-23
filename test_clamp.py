import pytest

from clamp import clamp


def test_below():
    assert clamp(-1, 0, 10) == 0


def test_inside():
    assert clamp(5, 0, 10) == 5
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_above():
    assert clamp(11, 0, 10) == 10


def test_invalid_range():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)
