import dataclasses
import math

import lib
from lib import Point


@dataclasses.dataclass(frozen=True)
class Bounds:
    x: int
    y: int


PROBLEM_BOUNDS = Bounds(101, 103)


@dataclasses.dataclass
class Robot:
    position: Point
    velocity: Point

    def move(self, bounds: Bounds):
        pos = self.position.displace(*self.velocity)
        self.position = Point(pos.x % bounds.x, pos.y % bounds.y)


def parse_input(raw: str) -> list[Robot]:
    num_lines = map(lib.extract_ints, raw.strip().splitlines())
    return [Robot(Point(l[0], l[1]), Point(l[2], l[3])) for l in num_lines]


def part_1(raw: str, bounds=PROBLEM_BOUNDS):
    robots = parse_input(raw)

    for _ in range(100):
        for r in robots:
            r.move(bounds)

    quadrant_counts = [0, 0, 0, 0]
    x_avg, y_avg = bounds.x // 2, bounds.y // 2
    for r in robots:
        if r.position.x == x_avg or r.position.y == y_avg:
            continue

        left = r.position.x < math.floor(x_avg)
        top = r.position.y < y_avg
        quadrant = left + 2 * top
        quadrant_counts[quadrant] += 1

    return lib.product(quadrant_counts)


def count_connections(robots: list[Robot]) -> int:
    positions = {r.position for r in robots}

    count = 0
    for r in robots:
        for n in r.position.neighbors4():
            if n in positions:
                count += 1

    return count


def part_2(raw: str, bounds=PROBLEM_BOUNDS):
    robots = parse_input(raw)

    connected_count = []
    for i in range(1, 10_000):
        [r.move(bounds) for r in robots]
        connected_count.append((count_connections(robots), -i))

    return -max(connected_count)[1]


if __name__ == "__main__":
    print(part_1(lib.get_input(14)))
    print(part_2(lib.get_input(14)))
