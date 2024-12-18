import collections
import typing

import lib
from lib import Point


class Bounds(typing.NamedTuple):
    x: int
    y: int

    def in_range(self, p: Point) -> bool:
        return 0 <= p.x <= self.x and 0 <= p.y <= self.y


def parse_input(raw: str) -> list[Point]:
    return [Point(*lib.extract_ints(line)) for line in raw.strip().splitlines()]


def explore(rocks: list[Point], bounds: Bounds) -> int | None:
    start = Point(0, 0)
    goal = Point(*bounds)
    visited = {start} | set(rocks)

    queue = collections.deque([(0, start)])
    while queue:
        distance, current_position = queue.popleft()

        if current_position == goal:
            return distance

        neighbors = [
            n
            for n in current_position.neighbors4()
            if n not in visited and bounds.in_range(n)
        ]

        for n in neighbors:
            visited.add(n)
            queue.append((distance + 1, n))

    return None


def part_1(raw: str, bounds=Bounds(70, 70)):
    rocks = parse_input(raw)[:1024]
    return explore(rocks, bounds)


def part_2(raw: str, bounds=Bounds(70, 70)):
    rocks = parse_input(raw)
    for rock_index in range(1024, len(rocks) + 1):
        rocks_subset = rocks[:rock_index]
        if explore(rocks[:rock_index], bounds) is None:
            rock = rocks_subset[-1]
            return f"{rock.x},{rock.y}"


if __name__ == "__main__":
    print(part_1(lib.get_input(18)))
    print(part_2(lib.get_input(18)))
