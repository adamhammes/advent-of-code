import lib
from day12 import *

EXAMPLE_1 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

SHORT_EXAMPLE = """
AAAA
BBCD
BBCC
EEEC
"""


def test_find_area():
    grid = lib.parse_grid(SHORT_EXAMPLE)
    assert find_area(grid, Point(0, 0)) == {
        Point(0, 0),
        Point(1, 0),
        Point(2, 0),
        Point(3, 0),
    }


def test_get_perimeter():
    grid = lib.parse_grid(EXAMPLE_1)
    assert get_perimeter(grid, "R") == 18
    assert get_perimeter(grid, "I") == 30


def test_part_1():
    assert part_1(EXAMPLE_1) == 1930
