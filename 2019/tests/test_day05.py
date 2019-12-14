import unittest

from day05 import part1, part2


class TestDay05(unittest.TestCase):
    def test_regressions(self):
        self.assertEqual(5182797, part1())
        self.assertEqual(12077198, part2())
