from day11 import *

EXAMPLE_1 = """
11111
19991
19191
19991
11111
"""

EXAMPLE_2 = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def test_simulate():
    start_grid = parse_input(EXAMPLE_1)

    assert simulate_cycle(start_grid) == parse_input(
        """
        34543
        40004
        50005
        40004
        34543 
        """
    )


def test_part_1():
    assert part_1(EXAMPLE_2) == 1656


def test_part_2():
    assert part_2(EXAMPLE_2) == 195
