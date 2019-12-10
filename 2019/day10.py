import collections
from fractions import Fraction
import math
import unittest

MY_EXAMPLE = """
..#..
..#..
#####
..#..
..#..
"""

MY_EXAMPLE_2 = """
######
"""

EXAMPLE_1 = """
.#..#
.....
#####
....#
...##
""".strip()

EXAMPLE_2 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""


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
    def slope(self, p_other):
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
    visible_points = collections.defaultdict(set)

    for point in points:
        for other_point in points:
            if point != other_point:
                visible_points[point].add(point.slope(other_point))

    return max(len(point_set) for point_set in visible_points.values())


class TestDay10(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(6, part1(parse_input(MY_EXAMPLE)))
        self.assertEqual(2, part1(parse_input(MY_EXAMPLE_2)))
        self.assertEqual(8, part1(parse_input(EXAMPLE_1)))
        self.assertEqual(33, part1(parse_input(EXAMPLE_2)))

    def test_regressions(self):
        self.assertEqual(269, part1(parse_input(get_input())))


if __name__ == "__main__":
    points = parse_input(get_input())
    print(part1(points))
