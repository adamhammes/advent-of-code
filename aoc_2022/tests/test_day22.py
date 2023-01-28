from day22 import *

EXAMPLE = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""


def test_parse_grid():
    grid, _ = parse_input(EXAMPLE)
    fifth_row = grid[4]
    assert fifth_row[:4] == [Contents.Air, Contents.Air, Contents.Air, Contents.Wall]


def test_move():
    grid, _ = parse_input(EXAMPLE)

    point_a = Point(11, 6)
    assert move(grid, point_a, Directions.East.value, 1) == Point(0, 6)
    assert move(grid, point_a, Directions.East.value, 10) == Point(1, 6)

    assert move(grid, point_a, Directions.North.value, 1) == Point(11, 5)
    assert move(grid, point_a, Directions.South.value, 5) == Point(11, 7)
