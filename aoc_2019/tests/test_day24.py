import unittest

from day24 import *

EXAMPLE_1_0 = """
....#
#..#.
#..##
..#..
#....
"""

EXAMPLE_1_1 = """
#..#.
####.
###.#
##.##
.##..
"""

EXAMPLE_1_2 = """
#####
....#
....#
...#.
#.###
"""

EXAMPLE_1_REPEATING = """
.....
.....
.....
#....
.#...
"""


class TestDay24(unittest.TestCase):
    def test_cycle(self):
        start = parse_input(EXAMPLE_1_0)

        grid_iterator = grid_generator(start)

        self.assertEqual(parse_input(EXAMPLE_1_1), next(grid_iterator))
        self.assertEqual(parse_input(EXAMPLE_1_2), next(grid_iterator))

    def test_calculate_biodiversity(self):
        self.assertEqual(
            2129920, calculate_biodiversity(parse_input(EXAMPLE_1_REPEATING))
        )
