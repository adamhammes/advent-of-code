import collections
from fractions import Fraction
import math


def safely_reduce(dx, dy):
    if dx == 0:
        return 0, dy / abs(dy)
    elif dy == 0:
        return dx / abs(dx), dy

    gcd = math.gcd(dx, dy)
    return dx / gcd, dy / gcd


def get_input():
    with open("inputs/day10.txt") as f:
        return f.read().strip()


class Point(collections.namedtuple("Point", ["x", "y"])):
    def reduced_rise_run(self, p_other):
        dx, dy = p_other.x - self.x, p_other.y - self.y
        return safely_reduce(dx, dy)


def parse_input(coordinate_grid):
    points = set()

    for x, row in enumerate(coordinate_grid.splitlines()):
        for y, character in enumerate(row):
            if character == "#":
                points.add(Point(x, y))

    return points


def part1(points):
    vector_map = collections.defaultdict(set)

    for point in points:
        for other_point in points:
            if point != other_point:
                vector_map[point].add(point.reduced_rise_run(other_point))

    return max(len(point_set) for point_set in vector_map.values())


if __name__ == "__main__":
    points = parse_input(get_input())
    print(part1(points))
