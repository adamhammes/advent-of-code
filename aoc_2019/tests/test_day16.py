import unittest

from day16 import *

TEST_SIGNAL = [1, 2, 3, 4, 5, 6, 7, 8]

LARGE_INPUT_1 = list(map(int, "80871224585914546619083218645595"))
LARGE_INPUT_2 = list(map(int, "19617804207202209144916044189917"))
LARGE_INPUT_3 = list(map(int, "69317163492948606335995924319873"))


class TestDay16(unittest.TestCase):
    def test_generate_pattern(self):
        expected = [1, 0, -1, 0, 1, 0, -1, 0]
        self.assertEqual(expected, generate_pattern(0, len(TEST_SIGNAL)))

    def test_apply_pattern(self):
        nums = apply_pattern(TEST_SIGNAL)

        expected = [4, 8, 2, 2, 6, 1, 5, 8]
        self.assertEqual(expected, nums)

    def test_iterate_pattern(self):
        expected = [0, 1, 0, 2, 9, 4, 9, 8]
        self.assertEqual(expected, iterate_pattern(TEST_SIGNAL, 4))

    def test_part1(self):
        self.assertEqual("24176176", part1(LARGE_INPUT_1))
