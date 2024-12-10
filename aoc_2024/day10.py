import lib
from lib import Point


def parse_input(raw: str) -> dict[Point, int]:
    grid = lib.parse_grid(raw)
    return {key: int(val) for key, val in grid.items()}


def trailhead_score(grid: dict[Point, int], trailhead: Point) -> set[Point]:
    current_elevation = grid[trailhead]
    if current_elevation == 9:
        return {trailhead}

    next_positions = [
        p for p in trailhead.neighbors4() if grid.get(p) == current_elevation + 1
    ]

    return set().union(*(trailhead_score(grid, p) for p in next_positions))


def trailhead_rating(grid: dict[Point, int], trailhead: Point) -> int:
    current_elevation = grid[trailhead]
    if current_elevation == 9:
        return 1

    return sum(
        trailhead_rating(grid, p)
        for p in trailhead.neighbors4()
        if grid.get(p) == current_elevation + 1
    )


def part_1(raw: str) -> int:
    grid = parse_input(raw)
    trailheads = [p for p, elevation in grid.items() if elevation == 0]

    return sum(len(trailhead_score(grid, p)) for p in trailheads)


def part_2(raw: str) -> int:
    grid = parse_input(raw)
    trailheads = [p for p, elevation in grid.items() if elevation == 0]
    return sum(trailhead_rating(grid, p) for p in trailheads)


if __name__ == "__main__":
    print(part_1(lib.get_input(10)))
    print(part_2(lib.get_input(10)))
