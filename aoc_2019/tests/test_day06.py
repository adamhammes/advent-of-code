import unittest

from day06 import *

TEST_INPUT = parse_input(
    ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
)

TEST_INPUT_2 = parse_input(
    [
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L",
        "K)YOU",
        "I)SAN",
    ]
)


class TestDay06(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(42, part1(TEST_INPUT))
        self.assertEqual(4, part2(TEST_INPUT_2))

    def test_regressions(self):
        self.assertEqual(140608, part1(get_input()))
        self.assertEqual(337, part2(get_input()))
