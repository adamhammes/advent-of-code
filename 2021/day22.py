import itertools
import re
import typing
from typing import Tuple

import lib


def bounds(r: range) -> Tuple[int, int]:
    return min(r), max(r)


def range_intersection(r1: range, r2: range) -> range:
    lower = max(min(r1), min(r2))
    upper = min(max(r1), max(r2))
    return range(lower, upper + 1)


def split_range(outer: range, inner: range) -> Tuple[range, range, range]:
    empty = range(0, 0)
    if outer.stop <= inner.start:
        return outer, empty, empty
    elif outer.start >= inner.stop:
        return empty, empty, outer

    center = range(max(outer.start, inner.start), min(outer.stop, inner.stop))
    left = range(outer.start, center.start)
    right = range(center.stop, outer.stop)
    return left, center, right


class Cuboid(typing.NamedTuple):
    x_range: range
    y_range: range
    z_range: range

    def is_big(self) -> bool:
        return (
            min(self.x_range) < -50
            or max(self.x_range) > 50
            or min(self.y_range) < -50
            or max(self.y_range) > 50
            or min(self.z_range) < -50
            or max(self.z_range) > 50
        )

    def size(self) -> int:
        return len(self.x_range) * len(self.y_range) * len(self.z_range)

    def intersects_with(self, other: "Cuboid") -> bool:
        return all(
            [
                range_intersection(self.x_range, other.x_range),
                range_intersection(self.y_range, other.y_range),
                range_intersection(self.z_range, other.z_range),
            ]
        )

    def points(self) -> set[Tuple[int, int, int]]:
        return set(
            (x, y, z) for x in self.x_range for y in self.y_range for z in self.z_range
        )

    def is_empty(self) -> bool:
        return any(
            r.start >= r.stop for r in [self.x_range, self.y_range, self.z_range]
        )

    def split(self, other: "Cuboid") -> list["Cuboid"]:
        if not self.intersects_with(other):
            return [self]

        bottom, z_overlap, top = split_range(self.z_range, other.z_range)
        left, x_overlap, right = split_range(self.x_range, other.x_range)
        front, y_overlap, back = split_range(self.y_range, other.y_range)

        split = [
            # bottom
            Cuboid(x_range=self.x_range, y_range=self.y_range, z_range=bottom),
            # top
            Cuboid(x_range=self.x_range, y_range=self.y_range, z_range=top),
            # left
            Cuboid(x_range=left, y_range=self.y_range, z_range=z_overlap),
            # right
            Cuboid(x_range=right, y_range=self.y_range, z_range=z_overlap),
            # front
            Cuboid(x_range=x_overlap, y_range=front, z_range=z_overlap),
            # back
            Cuboid(x_range=x_overlap, y_range=back, z_range=z_overlap),
        ]

        return [c for c in split if not c.is_empty()]


def parse_input(raw: str) -> list[Tuple[Cuboid, bool]]:
    to_return = []
    for line in raw.strip().split("\n"):
        on_or_off = line.startswith("on")

        x1, x2, y1, y2, z1, z2 = list(map(int, re.findall(r"-?\d+", line)))
        cube = Cuboid(
            x_range=range(x1, x2 + 1),
            y_range=range(y1, y2 + 1),
            z_range=range(z1, z2 + 1),
        )

        to_return.append((cube, on_or_off))

    return to_return


def part_1(raw: str, allow_big: bool) -> int:
    cubes: dict[Cuboid, list[Cuboid]] = {}

    for cuboid, on_or_off in parse_input(raw):
        if cuboid.is_big() and not allow_big:
            continue

        new_cubes = {}
        for top_level_cuboid in cubes:
            if top_level_cuboid.intersects_with(cuboid):
                new_cubes[top_level_cuboid] = []
                for sub_cube in cubes[top_level_cuboid]:
                    new_cubes[top_level_cuboid] += sub_cube.split(cuboid)
            else:
                new_cubes[top_level_cuboid] = cubes[top_level_cuboid]

        if on_or_off:
            new_cubes[cuboid] = [cuboid]

        cubes = new_cubes

    count = 0
    for cube_group in cubes.values():
        for sub_cube in cube_group:
            count += sub_cube.size()

    return count


if __name__ == "__main__":
    print(part_1(lib.get_input(22), False))
    print(part_1(lib.get_input(22), True))
