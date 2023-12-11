from day10 import *

EXAMPLE_1 = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""


def test_parse_input():
    field = parse_input(EXAMPLE_1)

    bottom_left = Point(1, 1)
    assert field.grid[bottom_left] == "L"
    assert field.edges[bottom_left] == {Point(2, 1), Point(1, 2)}

    top_left = Point(1, 3)
    assert field.grid[top_left] == "S"
    assert field.edges[top_left] == {Point(1, 2), Point(2, 3)}


def test_part_1():
    assert part_1(EXAMPLE_1) == 4


EXAMPLE_2 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""


def test_part_2():
    assert part_2(EXAMPLE_2) == 4
