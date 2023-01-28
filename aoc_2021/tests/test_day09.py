from day09 import *

EXAMPLE_1 = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_parse_input():
    parsed = parse_input(EXAMPLE_1)

    assert len(parsed) == 50
    assert parsed[Point(0, 0)] == 2
    assert parsed[Point(9, 4)] == 8


def test_part_1():
    assert part_1(EXAMPLE_1) == 15


def test_flood_fill():
    point_map = parse_input(EXAMPLE_1)
    flood_area = flood_fill(point_map, Point(9, 0))
    assert len(flood_area) == 9

    assert Point(6, 1) not in flood_area


def test_part_2():
    assert part_2(EXAMPLE_1) == 1134
