import unittest

from day01 import *


class TestDay1(unittest.TestCase):
    def test1(self):
        test_cases = [
            (12, 2),
            (14, 2),
            (1969, 654),
            (100756, 33583),
        ]

        for mass, fuel in test_cases:
            self.assertEqual(fuel_needed(mass), fuel)

    def test2(self):
        test_cases = [
            (14, 2),
            (1969, 966),
            (100756, 50346),
        ]

        for mass, fuel in test_cases:
            self.assertEqual(recursive_fuel_needed(mass), fuel)

    def test_regressions(self):
        self.assertEqual(3178783, part1())
        self.assertEqual(4765294, part2())
