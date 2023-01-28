from day18 import *

EXAMPLE = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


def test_part_1():
    assert part_1(EXAMPLE) == 64


def test_part_2():
    assert part_2(EXAMPLE) == 58
