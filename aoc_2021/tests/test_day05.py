from lib import Point
from day05 import *

EXAMPLE_1 = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_points_on_line():
    assert points_on_line(Point(1, 1), Point(1, 3)) == [
        Point(1, 1),
        Point(1, 2),
        Point(1, 3),
    ]


def test_parse_input():
    lines = parse_input(EXAMPLE_1)

    assert len(lines) == 10
    assert lines[0] == (Point(0, 9), Point(5, 9))


def test_overlapping_points():
    lines = parse_input(EXAMPLE_1)
    assert find_overlapping_points(lines) == 12


def test_part_1():
    assert part_1(EXAMPLE_1) == 5


def test_part_2():
    assert part_2(EXAMPLE_1) == 12
