import collections
from typing import Iterable, Optional

import lib
from lib import Point


def build_line(p1: Point, p2: Point) -> Iterable[Point]:
    start_x, end_x = sorted([p1.x, p2.x])
    start_y, end_y = sorted([p1.y, p2.y])
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            yield Point(x, y)


def parse_line(line: str) -> list[Point]:
    nums = lib.extract_ints(line)
    return [Point(x, y) for x, y in lib.chunks(nums, 2)]


def parse_input(raw: str) -> set[Point]:
    points = set()
    for line_points in map(parse_line, raw.splitlines()):
        for p1, p2 in lib.window(line_points, 2):
            points.update(build_line(p1, p2))

    return points


def simulate_sand(rocks: set[Point], sand: set[Point]) -> Point | None:
    taken_points = rocks | sand
    floor = max(p.y for p in taken_points)

    cur = Point(500, 0)

    possible_movements = [Point(0, 1), Point(-1, 1), Point(1, 1)]
    while cur.y < floor:
        possible_results = [cur.displace(*m) for m in possible_movements]
        reachable_results = [p for p in possible_results if p not in taken_points]

        if not reachable_results:
            return cur

        cur = reachable_results[0]

    return None


def part_1(raw: str) -> int:
    rocks = parse_input(raw)
    sand = set()

    while (sand_pos := simulate_sand(rocks, sand)) is not None:
        sand.add(sand_pos)

    return len(sand)


def part_2(raw: str) -> int:
    seen_points = set(Point(500, 0))
    points_to_visit = collections.deque([Point(500, 0)])

    rocks = parse_input(raw)
    floor = max(r.y for r in rocks) + 2

    while points_to_visit:
        cur_point = points_to_visit.popleft()

        connecting_points = set(
            cur_point.displace(*m) for m in [Point(0, 1), Point(-1, 1), Point(1, 1)]
        )

        reachable_points = [
            p
            for p in connecting_points
            if p not in seen_points and p not in rocks and p.y < floor
        ]

        points_to_visit += reachable_points
        seen_points.update(reachable_points)

    return len(seen_points) - 1


if __name__ == "__main__":
    print(part_1(lib.get_input(14)))
    print(part_2(lib.get_input(14)))
