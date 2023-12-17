import enum
import math
import queue
import typing

import lib
from lib import Point, Grid


class Direction(enum.Enum):
    Up = Point(0, 1)
    Right = Point(1, 0)
    Down = Point(0, -1)
    Left = Point(-1, 0)

    def opposite(self) -> "Direction":
        return {
            None: None,
            Direction.Up: Direction.Down,
            Direction.Right: Direction.Left,
            Direction.Down: Direction.Up,
            Direction.Left: Direction.Right,
        }[self]


class TravelState(typing.NamedTuple):
    location: Point
    direction: Direction | None

    def displace(self, direction: Direction, times: int) -> "TravelState":
        p = self.location.displace(*direction.value.times(times))
        return TravelState(p, direction)

    def possible_moves(self, lengths: range) -> typing.Iterable["TravelState"]:
        if self.direction is None:
            possible_directions = list(Direction)
        else:
            forbidden = [self.direction, self.direction.opposite()]
            possible_directions = [d for d in Direction if d not in forbidden]

        for direction in possible_directions:
            for length in lengths:
                yield self.displace(direction, length)


class QueueItem(typing.NamedTuple):
    cost: int
    state: TravelState

    def __lt__(self, o: "QueueItem") -> bool:
        return self.cost < o.cost


def dumb_line(p1: Point, p2: Point) -> list[Point]:
    if p1.x == p2.x:
        dy = int(math.copysign(1, p2.y - p1.y))
        return [Point(p1.x, y) for y in range(p1.y + dy, p2.y + dy, dy)]
    else:
        dx = int(math.copysign(1, p2.x - p1.x))
        return [Point(x, p1.y) for x in range(p1.x + dx, p2.x + dx, dx)]


def explore(grid: Grid, move_lengths: range, goal: Point) -> int:
    start = TravelState(Point(0, 0), direction=None)
    seen: dict[TravelState, int] = {}
    prioq = queue.PriorityQueue()
    prioq.put(QueueItem(0, start))

    while prioq:
        current: QueueItem = prioq.get()

        if current.state in seen:
            continue

        if current.state.location == goal:
            return current.cost

        seen[current.state] = current.cost

        possible_moves = [
            move
            for move in current.state.possible_moves(move_lengths)
            if move.location in grid
        ]

        for move in possible_moves:
            dumb_moves = dumb_line(current.state.location, move.location)
            move_cost = current.cost + sum(int(grid[p]) for p in dumb_moves)
            prioq.put(QueueItem(move_cost, move))


def part_1(raw: str) -> int:
    grid = lib.parse_grid(raw)
    destination = Point(max(p.x for p in grid), max(p.y for p in grid))
    return explore(grid, range(1, 4), destination)


def part_2(raw: str) -> int:
    grid = lib.parse_grid(raw)
    destination = Point(max(p.x for p in grid), max(p.y for p in grid))
    return explore(grid, range(4, 10 + 1), destination)


if __name__ == "__main__":
    print(part_1(lib.get_input(17)))
    print(part_2(lib.get_input(17)))
