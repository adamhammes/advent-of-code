import collections
from typing import Tuple

import lib
from lib import Point


def parse_input(raw: str) -> Tuple[lib.Grid, Point]:
    grid = lib.parse_grid(raw, rev_y=True)
    guard_position = lib.first(grid, lambda p: grid[p] == "^")
    return grid, guard_position


def traverse(grid: lib.Grid, guard_position: Point) -> int | None:
    directions = collections.deque([(0, 1), (1, 0), (0, -1), (-1, 0)])

    visited_states = set()
    while True:
        current_facing = directions[0]
        current_state = guard_position, current_facing
        if current_state in visited_states:
            return None

        visited_states.add((guard_position, current_facing))
        next_position = guard_position.displace(*directions[0])

        if next_position not in grid:
            break
        elif grid[next_position] == "#":
            directions.rotate(-1)
        else:
            guard_position = next_position

    return len(set(p for p, _ in visited_states))


def part_1(raw: str) -> int:
    grid, guard_position = parse_input(raw)
    return traverse(grid, guard_position)


def part_2(raw: str) -> int:
    grid, guard_position = parse_input(raw)

    loop_count = 0
    for p, value in grid.items():
        if value in "^#":
            continue

        grid_with_new_obstacle = grid.copy()
        grid_with_new_obstacle[p] = "#"
        loop_count += traverse(grid_with_new_obstacle, guard_position) is None

    return loop_count


if __name__ == "__main__":
    print(part_1(lib.get_input(6)))
    print(part_2(lib.get_input(6)))
