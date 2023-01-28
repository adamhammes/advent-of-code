import unittest

from day07 import part1, part2


class TestDay07(unittest.TestCase):
    def test_regressions(self):
        self.assertEqual(17790, part1())
        self.assertEqual(19384820, part2())
