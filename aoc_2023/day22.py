import dataclasses
import functools
import itertools

import lib
from lib import P3D


@dataclasses.dataclass(eq=True, frozen=True)
class Cube:
    points: frozenset[P3D]

    def min_z(self) -> int:
        return min(p.z for p in self.points)

    def down(self) -> "Cube":
        return Cube(frozenset(P3D(p.x, p.y, p.z - 1) for p in self.points))

    @functools.cached_property
    def above(self) -> set[P3D]:
        max_z = max(p.z for p in self.points)
        top_layer = (p for p in self.points if p.z == max_z)
        return set(P3D(p.x, p.y, p.z + 1) for p in top_layer)

    def supports(self, other: "Cube") -> bool:
        return any(p in other.points for p in self.above)


def _parse_cube(line: str) -> Cube:
    c1, c2, c3, f1, f2, f3 = lib.extract_ints(line)

    points = []
    for x in range(c1, f1 + 1):
        for y in range(c2, f2 + 1):
            for z in range(c3, f3 + 1):
                points.append(P3D(x, y, z))

    return Cube(frozenset(points))


def parse_input(raw: str) -> list[Cube]:
    return list(map(_parse_cube, raw.strip().splitlines()))


def settle(cubes: list[Cube]) -> list[Cube]:
    cubes.sort(key=Cube.min_z)

    settled_points = set()
    settled_cubes = []
    for cube in cubes:
        while cube.min_z() > 1 and all(
            p not in settled_points for p in cube.down().points
        ):
            cube = cube.down()

        settled_points.update(cube.points)
        settled_cubes.append(cube)

    return settled_cubes


def do_the_thing(cubes: list[Cube]) -> list[Cube]:
    supports = {c: set() for c in cubes}
    supported_by = {c: set() for c in cubes}

    for c1, c2 in itertools.permutations(cubes, 2):
        if c1.supports(c2):
            supports[c1].add(c2)
            supported_by[c2].add(c1)

    interesting = []
    for cube in cubes:
        supported_cubes = supports[cube]

        if not supported_cubes or all(
            len(supported_by[c]) > 1 for c in supported_cubes
        ):
            interesting.append(cube)

    return interesting


def part_1(raw: str) -> int:
    cubes = parse_input(raw)
    cubes = settle(cubes)
    return len(do_the_thing(cubes))


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
