from day20 import *

EXAMPLE_1 = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


def test_calc_distances():
    grid, start, end = parse_input(EXAMPLE_1)
    distances = calc_distances(grid, start, end)
    assert distances[start] == Distance(0, 84)
    assert distances[end] == Distance(84, 0)
    for d in distances.values():
        assert d.from_end + d.from_start == 84


def test_part_1():
    assert part_1(EXAMPLE_1, 64) == 1
    assert part_1(EXAMPLE_1, 20) == 5
    assert part_1(EXAMPLE_1, 12) == 8


def test_part_2():
    assert part_2(EXAMPLE_1, 76) == 3
    assert part_2(EXAMPLE_1, 74) == 7
    assert part_2(EXAMPLE_1, 72) == 29
