import itertools
import typing

from lib import Point

Grid = typing.FrozenSet[Point]


def get_input():
    with open("inputs/day24.txt") as f:
        return f.read()


def parse_input(string: str) -> Grid:
    points = set()
    for y, row in enumerate(string.strip().splitlines()):
        for x, character in enumerate(row):
            if character == "#":
                points.add(Point(x, y))

    return frozenset(points)


def grid_generator(start: Grid) -> typing.Iterable[Grid]:
    current_grid = start
    while True:
        next_grid = set()
        for x, y in itertools.product(range(5), range(5)):

            point = Point(x, y)
            num_adjacent_bugs = len(current_grid.intersection(point.neighbors()))

            if point not in current_grid and num_adjacent_bugs in [1, 2]:
                next_grid.add(point)

            if point in current_grid and num_adjacent_bugs == 1:
                next_grid.add(point)

        yield frozenset(next_grid)
        current_grid = next_grid


def calculate_biodiversity(grid: Grid) -> int:
    total = 0
    for i, xy in enumerate(itertools.product(range(5), range(5))):
        if Point(*reversed(xy)) in grid:
            total += 2 ** i

    return total


def part1(_in=None):
    _in = _in if _in else get_input()

    start_grid = parse_input(_in)
    seen_grids = {start_grid}

    for grid in grid_generator(start_grid):
        if grid in seen_grids:
            return calculate_biodiversity(grid)

        seen_grids.add(grid)


if __name__ == "__main__":
    print(part1())
