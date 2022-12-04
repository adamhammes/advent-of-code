from day04 import *

EXAMPLE_1 = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_part_1():
    assert part_1(EXAMPLE_1) == 2
    assert part_1(lib.get_input(4)) == 651


def test_part_2():
    assert part_2(EXAMPLE_1) == 4
    assert part_2(lib.get_input(4)) == 956
