from day17 import *

EXAMPLE_1 = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""


def test_explore():
    # assert part_1(EXAMPLE_1) == 102
    grid = lib.parse_grid(EXAMPLE_1)
    r = range(1, 4)
    assert explore(grid, r, Point(2, 1)) == 6
    assert explore(grid, r, Point(5, 1)) == 20
    assert explore(grid, r, Point(5, 0)) == 23
    assert explore(grid, r, Point(6, 0)) == 25
    assert explore(grid, r, Point(8, 0)) == 29


def test_dumb_line():
    assert dumb_line(Point(5, 0), Point(2, 0)) == [
        Point(4, 0),
        Point(3, 0),
        Point(2, 0),
    ]

    assert dumb_line(Point(0, 1), Point(0, 4)) == [
        Point(0, 2),
        Point(0, 3),
        Point(0, 4),
    ]


def test_part_1():
    assert part_1(EXAMPLE_1) == 102


def test_part_2():
    assert part_2(EXAMPLE_1) == 94
