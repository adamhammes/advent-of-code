from collections import Counter
from lib import Point
import lib
from typing import Tuple
import re


def points_on_line(p1: Point, p2: Point) -> list[Point]:
    def convert_to_step(diff: int) -> int:
        return 0 if not diff else diff / abs(diff)

    dx, dy = p2.x - p1.x, p2.y - p1.y

    step_x, step_y = convert_to_step(dx), convert_to_step(dy)

    points = []
    cur_point = p1

    while True:
        points.append(cur_point)
        if cur_point == p2:
            return points

        cur_point = cur_point.displace(step_x, step_y)


def parse_input(raw: str) -> list[Tuple[Point, Point]]:
    def points_from_line(line: str) -> Tuple[Point, Point]:
        x1, y1, x2, y2 = list(map(int, re.findall(r"\d+", line)))
        return Point(x1, y1), Point(x2, y2)

    return list(map(points_from_line, raw.strip().splitlines()))


def find_overlapping_points(lines: list[Tuple[Point, Point]]):
    line_points = [point for p1, p2 in lines for point in points_on_line(p1, p2)]
    counter = Counter(line_points)
    return sum(count > 1 for count in counter.values())


def part_1(raw: str) -> int:
    lines = parse_input(raw)
    non_diagonal_lines = [(p1, p2) for p1, p2 in lines if p1.x == p2.x or p1.y == p2.y]
    return find_overlapping_points(non_diagonal_lines)


def part_2(raw: str) -> int:
    return find_overlapping_points(parse_input(raw))


if __name__ == "__main__":
    print(part_1(lib.get_input(5)))
    print(part_2(lib.get_input(5)))
