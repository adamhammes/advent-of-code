import collections
import enum
import typing
from typing import Literal

import lib
from lib import Point, Grid


class Direction(enum.Enum):
    Up = Point(0, 1)
    Right = Point(1, 0)
    Down = Point(0, -1)
    Left = Point(-1, 0)


class PhotonState(typing.NamedTuple):
    location: Point
    direction: Direction

    def step(self):
        new_position = self.location.displace(*self.direction.value)
        return PhotonState(location=new_position, direction=self.direction)


Mirror = Literal["-"] | Literal["|"] | Literal["/"] | Literal["\\"]


def reflect(direction: Direction, mirror: Mirror) -> list[Direction]:
    return {
        (Direction.Up, "|"): [Direction.Up],
        (Direction.Up, "-"): [Direction.Left, Direction.Right],
        (Direction.Up, "/"): [Direction.Right],
        (Direction.Up, "\\"): [Direction.Left],
        #
        (Direction.Down, "|"): [Direction.Down],
        (Direction.Down, "-"): [Direction.Left, Direction.Right],
        (Direction.Down, "/"): [Direction.Left],
        (Direction.Down, "\\"): [Direction.Right],
        #
        (Direction.Right, "|"): [Direction.Down, Direction.Up],
        (Direction.Right, "-"): [Direction.Right],
        (Direction.Right, "/"): [Direction.Up],
        (Direction.Right, "\\"): [Direction.Down],
        #
        (Direction.Left, "|"): [Direction.Down, Direction.Up],
        (Direction.Left, "-"): [Direction.Left],
        (Direction.Left, "/"): [Direction.Down],
        (Direction.Left, "\\"): [Direction.Up],
    }[(direction, mirror)]


def explore(grid: Grid, start: PhotonState) -> set[PhotonState]:
    seen = set()
    queue = collections.deque([start])

    while queue:
        current = queue.popleft()
        current = current.step()

        if current in seen or current.location not in grid:
            continue

        seen.add(current)
        if grid[current.location] == ".":
            queue.append(current)
        else:
            directions = reflect(current.direction, grid[current.location])
            for direction in directions:
                queue.append(PhotonState(current.location, direction))

    return seen


def count_energized(grid: Grid, start: PhotonState) -> int:
    seen = explore(grid, start)
    return len(set(state.location for state in seen))


def part_1(raw: str) -> int:
    grid = lib.parse_grid(raw, rev_y=True)
    y_max = max(p.y for p in grid)
    return count_energized(grid, PhotonState(Point(-1, y_max), Direction.Right))


def part_2(raw: str) -> int:
    grid = lib.parse_grid(raw, rev_y=True)

    max_x, max_y = max(p.x for p in grid), max(p.y for p in grid)

    start_locations = []
    for x in range(0, max_x):
        start_locations.append(PhotonState(Point(x, -1), direction=Direction.Up))
        start_locations.append(
            PhotonState(Point(x, max_y + 1), direction=Direction.Down)
        )

    for y in range(0, max_y):
        start_locations.append(PhotonState(Point(-1, y), direction=Direction.Right))
        start_locations.append(
            PhotonState(Point(max_x + 1, y), direction=Direction.Left)
        )

    return max(count_energized(grid, start) for start in start_locations)


if __name__ == "__main__":
    print(part_1(lib.get_input(16)))
    print(part_2(lib.get_input(16)))
