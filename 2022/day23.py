import collections
import enum
import itertools

import lib
from lib import Point


class Directions(enum.Enum):
    North = [(x, 1) for x in [-1, 0, 1]]
    East = [(1, y) for y in [-1, 0, 1]]
    South = [(x, -1) for x in [-1, 0, 1]]
    West = [(-1, y) for y in [-1, 0, 1]]


def parse_input(raw: str) -> set[Point]:
    points = set()
    lines = raw.strip().splitlines()[::-1]

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                points.add(Point(x, y))

    return points


def advance_elves(elves: set[Point], directions: [Directions]) -> set[Point]:
    proposed_move_count: dict[Point, int] = collections.defaultdict(int)
    proposed_moves: dict[Point, Point] = {}

    for elf in elves:
        if all(p not in elves for p in elf.neighbors8()):
            continue

        for direction in directions:
            if all(elf.displace(*p) not in elves for p in direction.value):
                proposed_point = elf.displace(*direction.value[1])

                proposed_moves[elf] = proposed_point
                proposed_move_count[proposed_point] += 1
                break

    new_points = set()
    for elf in elves:
        if elf not in proposed_moves:
            new_points.add(elf)
            continue

        proposed_move = proposed_moves[elf]
        if proposed_move_count[proposed_move] > 1:
            new_points.add(elf)
        else:
            new_points.add(proposed_move)

    return new_points


def part_1(raw: str, num_iterations=10):
    elves = parse_input(raw)
    directions = collections.deque(
        [Directions.North, Directions.South, Directions.West, Directions.East]
    )

    for _ in range(num_iterations):
        elves = advance_elves(elves, directions)
        directions.rotate(-1)

    xs = [p.x for p in elves]
    ys = [p.y for p in elves]

    count = 0
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            count += Point(x, y) not in elves

    return count


def part_2(raw: str) -> int:
    elves = parse_input(raw)
    directions = collections.deque(
        [Directions.North, Directions.South, Directions.West, Directions.East]
    )

    for iteration in itertools.count(1):
        new_elves = advance_elves(elves, directions)
        if new_elves == elves:
            return iteration

        elves = new_elves
        directions.rotate(-1)


if __name__ == "__main__":
    print(part_1(lib.get_input(23)))
    print(part_2(lib.get_input(23)))
