import itertools

from lib import Point
import lib


OctopiGrid = dict[Point, int]


def parse_input(raw: str) -> OctopiGrid:
    point_map = {}
    for y, line in enumerate(raw.strip().splitlines()):
        for x, c in enumerate(line.strip()):
            point_map[Point(x, y)] = int(c)

    return point_map


def simulate_cycle(grid: OctopiGrid) -> OctopiGrid:
    for octopus in grid:
        grid[octopus] += 1

    flashed_octopi = set()
    while any(
        octopus not in flashed_octopi and energy > 9 for octopus, energy in grid.items()
    ):
        octopi_to_flash = [o for o in grid if grid[o] > 9 and o not in flashed_octopi]

        flashed_octopi.update(octopi_to_flash)

        for octopus in octopi_to_flash:
            neighbors = [n for n in octopus.neighbors8() if n in grid]
            for n in neighbors:
                grid[n] += 1

    for octopus in flashed_octopi:
        grid[octopus] = 0

    return grid


def part_1(raw: str) -> int:
    grid = parse_input(raw)

    flashed = 0
    for _ in range(100):
        grid = simulate_cycle(grid)
        flashed += sum(energy == 0 for energy in grid.values())

    return flashed


def part_2(raw: str) -> int:
    grid = parse_input(raw)

    for iteration in itertools.count(start=1):
        grid = simulate_cycle(grid)
        if sum(grid.values()) == 0:
            return iteration


if __name__ == "__main__":
    print(part_1(lib.get_input(11)))
    print(part_2(lib.get_input(11)))
