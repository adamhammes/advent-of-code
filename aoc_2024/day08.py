import collections
import itertools
import typing
from typing import Tuple

import lib
from lib import Point


class Size(typing.NamedTuple):
    x: int
    y: int

    def in_bounds(self, p: lib.Point) -> bool:
        return 0 <= p.x <= self.x and 0 <= p.y <= self.y


def parse_input(raw: str) -> Tuple[Size, dict[str, list[Point]]]:
    grid = lib.parse_grid(raw, rev_y=True)

    antenna = collections.defaultdict(list)
    for p, value in grid.items():
        if value != ".":
            antenna[value].append(p)

    x_max, y_max = max(p.x for p in grid), max(p.y for p in grid)

    return Size(x_max, y_max), antenna


def find_antinodes(ps: list[Point]) -> set[Point]:
    nodes = set()

    for p1, p2 in itertools.combinations(ps, 2):
        delta = p1.delta_to(p2)
        close = p1.displace(*delta.times(-1))
        far = p1.displace(*delta.times(2))
        nodes |= {close, far}

    return nodes


def find_antinodes_2(size: Size, ps: list[Point]) -> set[Point]:
    nodes = set()

    for p1, p2 in itertools.permutations(ps, 2):
        delta = p1.delta_to(p2)

        for delta_range in itertools.count(0):
            p1_prime = p1.displace(*delta.times(delta_range))
            if not size.in_bounds(p1_prime):
                break

            nodes.add(p1_prime)

    return nodes


def part_1(raw: str) -> int:
    size, grid = parse_input(raw)

    antinodes = set()
    for _, points in grid.items():
        antinodes |= {p for p in find_antinodes(points) if size.in_bounds(p)}

    return len(antinodes)


def part_2(raw: str) -> int:
    size, grid = parse_input(raw)

    antinodes = set()
    for _, points in grid.items():
        antinodes |= {p for p in find_antinodes_2(size, points)}

    return len(antinodes)


if __name__ == "__main__":
    print(part_1(lib.get_input(8)))
    print(part_2(lib.get_input(8)))
