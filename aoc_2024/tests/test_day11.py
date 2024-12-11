from day11 import *


def test_change():
    assert change(0) == [1]
    assert change(1) == [2024]
    assert change(10) == [1, 0]
    assert change(99) == [9, 9]
    assert change(999) == [2021976]

