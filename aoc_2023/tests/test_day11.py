from day11 import *

EXAMPLE_1 = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def test_parse_input():
    system = parse_input(EXAMPLE_1)
    assert system.empty_columns == [2, 5, 8]
    assert system.empty_rows == [3, 7]

    assert len(system.galaxies) == 9


def test_calc_distance():
    system = parse_input(EXAMPLE_1)
    g = {i + 1: g for i, g in enumerate(system.galaxies)}

    assert calc_distance(system, g[5], g[9]) == 9
    assert calc_distance(system, g[5], g[6]) == 12
    assert calc_distance(system, g[1], g[7]) == 15
    assert calc_distance(system, g[3], g[6]) == 17
    assert calc_distance(system, g[8], g[9]) == 5


def test_part_1():
    assert part_1(EXAMPLE_1) == 374


def test_part_2():
    system = parse_input(EXAMPLE_1)
    assert sum_distances(system, 10) == 1030
