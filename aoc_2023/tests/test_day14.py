from day14 import *

EXAMPLE_1 = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

EXAMPLE_1_TILTED_NORTH = """
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
"""


def test_parse_input():
    grid = parse_input(EXAMPLE_1)
    assert grid[Point(0, 0)] == "#"
    assert grid[Point(0, 9)] == "O"
    assert grid[Point(9, 0)] == "."


def test_tilt():
    grid = parse_input(EXAMPLE_1)
    tilt(grid)

    assert grid == parse_input(EXAMPLE_1_TILTED_NORTH)


def test_score():
    assert score(parse_input(EXAMPLE_1_TILTED_NORTH)) == 136


def test_part_1():
    assert part_1(EXAMPLE_1) == 136
