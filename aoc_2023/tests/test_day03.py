from day03 import *

EXAMPLE_1 = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_parse_input():
    grid = parse_input(EXAMPLE_1)

    assert grid[Point(0, 0)] == "4"
    assert grid[Point(1, 0)] == "6"
    assert grid[Point(3, 1)] == "*"


def test_find_numbers():
    grid = parse_input(EXAMPLE_1)
    num_group = find_numbers(grid)

    key = frozenset([Point(0, 0), Point(1, 0), Point(2, 0)])
    assert num_group[key] == 467


def test_part_1():
    assert part_1(EXAMPLE_1) == 4361


def test_part_2():
    assert part_2(EXAMPLE_1) == 467835
