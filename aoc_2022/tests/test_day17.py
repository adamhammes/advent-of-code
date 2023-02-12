from day17 import *

EXAMPLE = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""


def test_part_1():
    assert part_1(EXAMPLE) == 3068


def test_part_2():
    assert part_2(EXAMPLE) == 1514285714288
