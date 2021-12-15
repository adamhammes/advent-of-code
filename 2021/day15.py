import heapq

import lib
from lib import Point, parse_grid, product

Cave = dict[Point, int]


def parse_input(raw: str) -> dict[Point, int]:
    raw_grid = parse_grid(raw)
    return {point: int(s) for point, s in raw_grid.items()}


def copy_grid(grid: Cave, dx: int, dy: int) -> Cave:
    return {
        point.displace(dx, dy): score + 1 if score < 9 else 1
        for point, score in grid.items()
    }


def expand_grid(original_grid: Cave) -> Cave:
    all_grids = {Point(0, 0): original_grid}
    grid_size = int(len(original_grid) ** 0.5)

    for x in range(0, 5):
        if x > 0:
            grid_to_left = all_grids[Point(x - 1, 0)]
            all_grids[Point(x, 0)] = copy_grid(grid_to_left, grid_size, 0)

        for y in range(1, 5):
            grid_above = all_grids[Point(x, y - 1)]
            all_grids[Point(x, y)] = copy_grid(grid_above, 0, grid_size)

    all_points = {}
    for grid in all_grids.values():
        all_points.update(grid)

    return all_points


def find_path(cave: Cave) -> int:
    start = Point(0, 0)
    end = max(cave, key=product)
    found_lowest_cost = set()

    heap = [(0, start)]

    while heap:
        current_cost, current_position = heapq.heappop(heap)
        if current_position in found_lowest_cost:
            continue

        if current_position == end:
            return current_cost

        found_lowest_cost.add(current_position)

        unexplored_neighbors = [
            neighbor for neighbor in current_position.neighbors4() if neighbor in cave
        ]

        for neighbor in unexplored_neighbors:
            heapq.heappush(heap, (current_cost + cave[neighbor], neighbor))


def part_1(raw: str) -> int:
    grid = parse_input(raw)
    return find_path(grid)


def part_2(raw: str) -> int:
    grid = expand_grid(parse_input(raw))
    return find_path(grid)


if __name__ == "__main__":
    print(part_1(lib.get_input(15)))
    print(part_2(lib.get_input(15)))
