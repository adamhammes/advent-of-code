import unittest

from day02 import Tape, part1, part2


class TestDay1(unittest.TestCase):
    def test1(self):
        test_cases = [
            (
                [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
                [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
            ),
            ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
            ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
            ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
        ]

        for _input, expected in test_cases:
            result = Tape(_input).run()
            self.assertEqual(expected, result)

    def test_regressions(self):
        self.assertEqual(3058646, part1())
        self.assertEqual(8976, part2())
