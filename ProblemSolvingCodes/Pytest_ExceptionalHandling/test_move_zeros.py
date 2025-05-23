import pytest
from empty7 import move_zeros_to_end


def test_move_zeros_all():
    assert move_zeros_to_end([0, 1, 0, 3, 12, 0]) == [1, 3, 12, 0, 0, 0]
    assert move_zeros_to_end([0, 0, 1]) == [1, 0, 0]
    assert move_zeros_to_end([1, 0, 0]) == [1, 0, 0]
    assert move_zeros_to_end([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert move_zeros_to_end([1, 2, 3]) == [1, 2, 3]
    assert move_zeros_to_end([0]) == [0]


def test_move_zeros_invalid():
    # assert move_zeros_to_end(["a", "b"]) == "invalid input"
    assert move_zeros_to_end([0]) == [0]
