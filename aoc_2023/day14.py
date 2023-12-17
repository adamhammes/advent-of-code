import itertools

from lib import Point, Grid
import lib


def parse_input(raw: str) -> lib.Grid:
    return lib.parse_grid(raw, rev_y=True)


def scootch_point(grid: Grid, p: Point) -> Point:
    while True:
        next_point = p.north()
        if next_point not in grid or grid[next_point] != ".":
            return p

        p = next_point


def tilt(grid: lib.Grid):
    grid_prime = grid.copy()
    height = max(p.y for p in grid_prime)

    y_range = list(reversed(range(0, height)))
    for y in y_range:
        points_to_move = [p for p, val in grid_prime.items() if p.y == y and val == "O"]
        for p in points_to_move:
            scooched = scootch_point(grid_prime, p)
            grid_prime[p] = "."
            grid_prime[scooched] = "O"

    return grid_prime


def rotate(grid: lib.Grid) -> lib.Grid:
    x_max, y_max = max(p.x for p in grid), max(p.y for p in grid)
    grid_prime = {}
    for p, val in grid.items():
        # yp = p.x
        # xp = y_max - p.y

        xp = p.y
        yp = x_max - p.x
        grid_prime[Point(xp, yp)] = val

    return grid_prime


def cycle(grid: Grid) -> Grid:
    for _ in range(4):
        grid = tilt(grid)
        grid = rotate(grid)

    return grid


def score(grid: Grid) -> int:
    return sum(p.y + 1 for p, val in grid.items() if val == "O")


def print_grid(grid: Grid):
    x_max, y_max = max(p.x for p in grid), max(p.y for p in grid)

    lines = []
    for y in range(y_max + 1):
        line = "".join(grid[Point(x, y)] for x in range(x_max + 1))
        lines.append(line)

    print()
    for line in reversed(lines):
        print(line)


def part_1(raw: str) -> int:
    grid = parse_input(raw)
    grid = tilt(grid)
    return score(grid)


def part_2(raw: str) -> int:
    desired_cycles = 1_000_000_000
    grid = parse_input(raw)

    seen_at: dict[frozenset[Point], int] = {}
    for i in itertools.count(1):
        grid = cycle(grid)
        fingerprint = frozenset(p for p, val in grid.items() if val == "O")

        if fingerprint not in seen_at:
            seen_at[fingerprint] = i
            continue

        cycle_length = i - seen_at[fingerprint]
        i += (desired_cycles - seen_at[fingerprint]) // cycle_length * cycle_length
        i -= cycle_length

        while i < desired_cycles:
            grid = cycle(grid)
            i += 1

        return score(grid)


if __name__ == "__main__":
    print(part_1(lib.get_input(14)))
    print(part_2(lib.get_input(14)))
