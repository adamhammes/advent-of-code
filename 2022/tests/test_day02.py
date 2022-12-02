from day02 import *

EXAMPLE_1 = """
A Y
B X
C Z
"""


def test_part_1():
    assert part_1(EXAMPLE_1) == 15
    assert part_1(lib.get_input(2)) == 11386


def test_part_2():
    assert part_2(EXAMPLE_1) == 12
    assert part_2(lib.get_input(2)) == 13600
