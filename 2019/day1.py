import math
import unittest


def get_input():
    with open("inputs/day1.txt") as f:
        return map(int, f.readlines())


def fuel_needed(mass):
    return math.floor(mass / 3) - 2


def recursive_fuel_needed(mass):
    total_fuel = 0
    current_mass = fuel_needed(mass)

    while current_mass > 0:
        total_fuel += current_mass
        current_mass = fuel_needed(current_mass)

    return total_fuel


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


if __name__ == "__main__":
    print(sum(map(fuel_needed, get_input())))
    print(sum(map(recursive_fuel_needed, get_input())))
