import math


def get_input():
    with open("inputs/day01.txt") as f:
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


def part1():
    return sum(map(fuel_needed, get_input()))


def part2():
    return sum(map(recursive_fuel_needed, get_input()))


if __name__ == "__main__":
    print(part1())
    print(part2())
