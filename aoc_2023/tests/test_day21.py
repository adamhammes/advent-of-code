from day21 import *

EXAMPLE_1 = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def test_find_spots():
    graph, start = parse_input(EXAMPLE_1)
    assert find_spots(graph, start, 1) == 2
    assert find_spots(graph, start, 6) == 16
