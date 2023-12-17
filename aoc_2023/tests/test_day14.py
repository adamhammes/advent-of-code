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


def test_print():
    grid = parse_input(EXAMPLE_1)
    print_grid(grid)


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

EXAMPLE_1_1_CYCLE = """
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
"""

EXAMPLE_1_2_CYCLE = """
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
"""

SIMPLE = """
.xx
...
x.x
"""


def test_parse_input():
    grid = parse_input(EXAMPLE_1)
    assert grid[Point(0, 0)] == "#"
    assert grid[Point(0, 9)] == "O"
    assert grid[Point(9, 0)] == "."


def test_tilt():
    grid = parse_input(EXAMPLE_1)
    grid = tilt(grid)
    assert grid == parse_input(EXAMPLE_1_TILTED_NORTH)


def test_score():
    assert score(parse_input(EXAMPLE_1_TILTED_NORTH)) == 136


def test_part_1():
    assert part_1(EXAMPLE_1) == 136


def test_part_2():
    assert part_2(EXAMPLE_1) == 64


def test_cycle():
    start = parse_input(EXAMPLE_1)
    cycled = cycle(start)

    assert cycled == parse_input(EXAMPLE_1_1_CYCLE)
    assert cycle(cycled) == parse_input(EXAMPLE_1_2_CYCLE)
