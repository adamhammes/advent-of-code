import typing

import math

import lib
from lib import Point

Grid = dict[Point, str]


def parse_input(raw: str) -> Grid:
    grid = {}
    for y, line in enumerate(raw.strip().splitlines()):
        for x, c in enumerate(line):
            grid[Point(x, y)] = c

    return grid


def find_numbers(grid: Grid) -> dict[frozenset[Point, ...], int]:
    y_max = max(p.y for p in grid)

    to_return = {}
    for y in range(y_max + 1):
        line = [p for p in grid if p.y == y]
        line = list(sorted(line, key=lambda p: p.x))

        num_groups = []
        current_group = []
        for point in line:
            if grid[point].isdigit():
                current_group.append(point)
            else:
                if current_group:
                    num_groups.append(current_group)
                    current_group = []

        if current_group:
            num_groups.append(current_group)

        for grouped_digits in num_groups:
            if grouped_digits:
                num = int("".join(map(grid.get, grouped_digits)))
                to_return[frozenset(grouped_digits)] = num

    return to_return


def is_part_number(coords: typing.Iterable[Point], grid: Grid) -> bool:
    neighbors = {n for p in coords for n in p.neighbors8()}.intersection(grid.keys())
    neighbor_vals = set(map(grid.get, neighbors))
    return any(val != "." and not val.isdigit() for val in neighbor_vals)


def part_1(raw: str) -> int:
    grid = parse_input(raw)
    number_coords = find_numbers(grid)

    total = 0
    for coords, number in number_coords.items():
        if is_part_number(coords, grid):
            total += number

    return total


def part_2(raw: str) -> int:
    grid = parse_input(raw)
    number_coords = find_numbers(grid)

    gears = [p for p, val in grid.items() if val == "*"]

    total = 0
    for gear in gears:
        adjacent_numbers = []
        for coords, number in number_coords.items():
            if coords.intersection(gear.neighbors8()):
                adjacent_numbers.append(number)

        if len(adjacent_numbers) == 2:
            total += math.prod(adjacent_numbers)

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(3)))
    print(part_2(lib.get_input(3)))
