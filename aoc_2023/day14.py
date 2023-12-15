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
    height = max(p.y for p in grid)

    y_range = list(reversed(range(0, height)))
    for y in y_range:
        points_to_move = [p for p, val in grid.items() if p.y == y and val == "O"]
        for p in points_to_move:
            scooched = scootch_point(grid, p)
            grid[p] = "."
            grid[scooched] = "O"


def score(grid: Grid) -> int:
    return sum(p.y + 1 for p, val in grid.items() if val == "O")


def part_1(raw: str) -> int:
    grid = parse_input(raw)
    tilt(grid)
    return score(grid)


if __name__ == "__main__":
    print(part_1(lib.get_input(14)))
