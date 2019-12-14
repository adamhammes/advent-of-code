import collections
from fractions import Fraction
import itertools
import math


def safely_reduce(dx, dy):
    if dx == 0:
        return 0, dy / abs(dy)
    elif dy == 0:
        return dx / abs(dx), dy

    gcd = math.gcd(dx, dy)
    return dx // gcd, dy // gcd


def get_input():
    with open("inputs/day10.txt") as f:
        return f.read().strip()


class Point(collections.namedtuple("Point", ["x", "y"])):
    def reduced_rise_run(self, p_other):
        dx, dy = p_other.x - self.x, p_other.y - self.y
        return safely_reduce(dx, dy)

    def angle(self, p_other):
        from math import atan2, pi

        ox, oy = p_other
        dx, dy = ox - self.x, self.y - oy

        offset = math.pi
        angle = atan2(dx, dy) * 180 / pi

        return (angle + 360) % 360

    def distance_to(self, p_other):
        from math import sqrt

        ox, oy = p_other
        dx, dy = ox - self.x, oy - self.y

        return sqrt(dx ** 2 + dy ** 2)


def parse_input(coordinate_grid):
    points = set()

    for y, row in enumerate(coordinate_grid.splitlines()):
        for x, character in enumerate(row):
            if character == "#":
                points.add(Point(x, y))

    return points


def make_vector_map(points):
    vector_map = collections.defaultdict(set)

    for point in points:
        for other_point in points:
            if point != other_point:
                vector_map[point].add(point.reduced_rise_run(other_point))

    return vector_map


def get_station(vector_map):
    return max(vector_map.keys(), key=lambda p: len(vector_map[p]))


def part1(points):
    vector_map = make_vector_map(points)
    station = get_station(vector_map)
    return len(vector_map[station])


def kill_asteroids(points):
    vector_map = make_vector_map(points)
    center = get_station(vector_map)

    other_points = set(points) - {center}
    angle_map = collections.defaultdict(list)
    [angle_map[center.angle(point)].append(point) for point in other_points]

    for p_list in angle_map.values():
        p_list.sort(key=center.distance_to)

    angle_map = {
        angle: collections.deque(points) for angle, points in angle_map.items()
    }

    sorted_angles = list(sorted(angle_map.keys()))

    for angle in itertools.chain(sorted_angles):
        if not any(angle_map.values()):
            return

        points = angle_map[angle]
        if not points:
            continue

        yield points.popleft()


def part2(points):
    asteroids = [asteroid for _, asteroid in zip(range(200), kill_asteroids(points))]

    x, y = asteroids[-1]
    return x * 100 + y


if __name__ == "__main__":
    points = parse_input(get_input())
    print(part1(points))
    print(part2(points))
