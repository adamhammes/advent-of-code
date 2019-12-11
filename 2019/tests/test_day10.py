import unittest

from day10 import parse_input, get_input, part1


MY_EXAMPLE = """
..#..
..#..
#####
..#..
..#..
"""

MY_EXAMPLE_2 = """
######
"""

EXAMPLE_1 = """
.#..#
.....
#####
....#
...##
""".strip()

EXAMPLE_2 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""


class TestDay10(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(6, part1(parse_input(MY_EXAMPLE)))
        self.assertEqual(2, part1(parse_input(MY_EXAMPLE_2)))
        self.assertEqual(8, part1(parse_input(EXAMPLE_1)))
        self.assertEqual(33, part1(parse_input(EXAMPLE_2)))

    def test_regressions(self):
        self.assertEqual(269, part1(parse_input(get_input())))
