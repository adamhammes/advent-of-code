import itertools
import unittest

tests1 = [
    ([1, -2, 3, 1], 3),
    ([1, 1, 1], 3),
    ([1, 1, -2], 0),
    ([-1, -2, -3], -6),
]

tests2 = [([1, -1, 2], 2)]


def get_input():
    with open("inputs/day1.txt") as f:
        return map(int, f.readlines())


def compute_frequency_drift(numbers):
    return sum(numbers, 0)


def repeated_frequency_drift(numbers):
    seen_frequencies = set()
    current_sum = 0

    for frequency in itertools.cycle(numbers):
        current_sum += frequency

        if current_sum in seen_frequencies:
            return current_sum

        seen_frequencies.add(current_sum)


class TestDay1(unittest.TestCase):
    def test1(self):
        for test_input, result in tests1:
            self.assertEqual(result, compute_frequency_drift(test_input))

    def test2(self):
        for test_input, result in tests2:
            self.assertEqual(result, repeated_frequency_drift(test_input))


if __name__ == "__main__":
    print(compute_frequency_drift(get_input()))
    print(repeated_frequency_drift(get_input()))
