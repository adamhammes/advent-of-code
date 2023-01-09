import collections
import typing

import lib
from lib import extract_ints


class P(typing.NamedTuple):
    x: int
    y: int
    z: int

    # fmt: off
    adjacent = [
        ( 1,  0,  0),
        (-1,  0,  0),
        ( 0,  1,  0),
        ( 0, -1,  0),
        ( 0,  0,  1),
        ( 0,  0, -1),
    ]
    # fmt: off

    def neighbors(self) -> typing.Iterable["P"]:
        return (self.displace(P(*d)) for d in P.adjacent)

    def displace(self, vector: "P") -> "P":
        return P(self.x + vector.x, self.y + vector.y, self.z + vector.z)


def parse_input(raw: str) -> set[P]:
    lines = raw.strip().splitlines()
    return {P(*ints) for ints in map(extract_ints, lines)}


def find_open_faces(points: set[P]) -> list[P]:
    faces = []
    for p in points:
        faces += [n for n in p.neighbors() if n not in points]

    return faces


def part_1(raw: str) -> int:
    points = parse_input(raw)
    return len(find_open_faces(points))


def is_reachable(points: set[P], start_point: P, end_point: P) -> (bool, set[P]):
    queue = collections.deque([start_point])
    visited = {start_point}

    while queue:
        cur_point = queue.popleft()
        if cur_point == end_point:
            return True

        neighbors = [
            n for n in cur_point.neighbors() if n not in points and n not in visited
        ]

        visited.update(neighbors)
        queue += neighbors

    return False


def part_2(raw: str) -> int:
    points = parse_input(raw)

    # pick a point guaranteed to be outside the droplet
    topmost = max(points, key=lambda p: p.z)
    outside_point = topmost.displace(P(0, 0, 1))

    faces = find_open_faces(points)
    faces_set = set(faces)

    interior_points = set()
    for i, p in enumerate(faces_set):
        if not is_reachable(points, p, outside_point):
            interior_points.add(p)

    return sum(p not in interior_points for p in faces)


if __name__ == "__main__":
    # print(part_1(lib.get_input(18)))
    print(part_2(lib.get_input(18)))
