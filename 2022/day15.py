import collections
import typing

import lib
from lib import Point

Input = list[tuple[Point, Point]]

class BoundingBox(typing.NamedTuple):
    top: int
    right: int
    bottom: int
    left: int


def parse_input(raw: str) -> list[tuple[Point, Point]]:
    pairs = []
    for line in raw.strip().splitlines():
        a, b, c, d = lib.extract_ints(line)
        pairs.append((Point(a, b), Point(c, d)))

    return pairs


def calc_bb(carts: dict[Point, int]) -> BoundingBox:
    min_x, max_x = min(carts, key=lambda p: p.x), max(carts, key=lambda p: p.x)
    min_y, max_y = min(carts, key=lambda p: p.y), max(carts, key=lambda p: p.y)

    return BoundingBox(
        top=max_y.y + carts[max_y],
        right=max_x.x + carts[max_x],
        bottom=min_y.y - carts[min_y],
        left=min_x.x - carts[min_x],
    )


def is_seen(carts: dict[Point, int], p: Point) -> bool:
    for sensor, sensor_range in carts.items():
        if sensor.manhattan_distance_to(p) <= sensor_range:
            return True

    return False


def part_1(raw: str) -> int:
    pairs = parse_input(raw)
    sensors_and_beacons = set(p for pair in pairs for p in pair)

    carts = {p1: p1.manhattan_distance_to(p2) for p1, p2 in pairs}
    bb = calc_bb(carts)

    points_to_check = (Point(x, 2000000) for x in range(bb.left, bb.right + 1))
    return sum(
        p not in sensors_and_beacons and is_seen(carts, p) for p in points_to_check
    )


def get_range_at_altitude(p: Point, sensor_range: int, y: int) -> range:
    y_dist = abs(p.y - y)
    spread = sensor_range - y_dist

    return range(p.x - spread, p.x + spread + 1)


def find_gaps_in_ranges(ranges: list[range]) -> list[int]:
    ranges = collections.deque(sorted(ranges, key=lambda r: (r.start, r.stop)))

    cur_range = ranges.popleft()
    gaps = []

    while ranges:
        next_range = ranges.popleft()

        if cur_range.stop > 4_000_000:
            return gaps

        if cur_range.stop < 0:
            cur_range = next_range
            continue

        if next_range.stop < cur_range.stop:
            continue

        if cur_range.stop < next_range.start:
            gaps += list(range(max(cur_range) + 1, min(next_range)))

        cur_range = next_range

    return gaps


def part_2(raw: str) -> int:
    size = 4000000
    pairs = parse_input(raw)
    carts = {p1: p1.manhattan_distance_to(p2) for p1, p2 in pairs}

    for y in range(size + 1):
        ranges = [
            get_range_at_altitude(sensor, sensor_range, y)
            for sensor, sensor_range in carts.items()
        ]

        non_empty_ranges = [r for r in ranges if r.start < r.stop]
        missing_points = [
            x for x in find_gaps_in_ranges(non_empty_ranges) if x in range(0, size + 1)
        ]

        if len(missing_points) > 1:
            print(missing_points)
            raise Exception()
        elif len(missing_points) == 1:
            return missing_points[0] * 4000000 + y


if __name__ == "__main__":
    print(part_1(lib.get_input(15)))
    print(part_2(lib.get_input(15)))
