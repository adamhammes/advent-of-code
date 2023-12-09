from day09 import *

EXAMPLE_1 = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def test_diff():
    assert diff([0, 3, 6, 9, 12, 15]) == (False, [3, 3, 3, 3, 3])

    assert calc_next([0, 3, 6, 9, 12, 15]) == 18


def test_part_1():
    assert part_1(EXAMPLE_1) == 114


def test_part_2():
    assert part_2(EXAMPLE_1) == 2
