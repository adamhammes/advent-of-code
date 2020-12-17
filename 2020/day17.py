import collections
import typing

import lib


def parse_input(raw: str, *, num_dimensions) -> typing.DefaultDict[lib.PointNd, bool]:
    points = {}

    for y, line in enumerate(raw.splitlines()):
        for x, char in enumerate(line):
            active = char == "#"
            points[lib.Point(x, y)] = active

    dimensional_points = collections.defaultdict(lambda: False)

    for point, active in points.items():
        n_dimensions = [*point, *[0] * (num_dimensions - 2)]
        dimensional_points[lib.PointNd(n_dimensions)] = active

    return dimensional_points


def solve(grid):
    for _ in range(6):
        new_grid = collections.defaultdict(lambda: False)
        points_to_consider = set(n for p in grid.keys() for n in p.neighbors())

        for point in points_to_consider:
            is_active = grid[point]
            neighbors = [grid[n] for n in point.neighbors() if n in grid]

            if is_active:
                new_grid[point] = sum(neighbors) in [2, 3]
            else:
                new_grid[point] = sum(neighbors) == 3

        # Prune inactive points for that sweet performance gain
        inactive_points = [p for p, active in new_grid.items() if not active]
        [new_grid.pop(p) for p in inactive_points]

        grid = new_grid

    return sum(grid.values())


def part_1(raw: str):
    return solve(parse_input(raw, num_dimensions=3))


def part_2(raw: str):
    return solve(parse_input(raw, num_dimensions=4))


if __name__ == "__main__":
    print(part_1(lib.get_input(17)))
    print(part_2(lib.get_input(17)))
