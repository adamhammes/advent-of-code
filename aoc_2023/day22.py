import dataclasses
import functools

import lib
from lib import P3D


@dataclasses.dataclass(eq=True, frozen=True)
class Cube:
    points: frozenset[P3D]

    def min_z(self) -> int:
        return min(p.z for p in self.points)

    @functools.cached_property
    def down(self) -> "Cube":
        return Cube(frozenset(P3D(p.x, p.y, p.z - 1) for p in self.points))


def _parse_cube(line: str) -> Cube:
    c1, c2, c3, f1, f2, f3 = lib.extract_ints(line)

    points = []
    for x in range(c1, f1 + 1):
        for y in range(c2, f2 + 1):
            for z in range(c3, f3 + 1):
                points.append(P3D(x, y, z))

    return Cube(frozenset(points))


def settle(cubes: list[Cube]) -> tuple[list[Cube], int]:
    cubes.sort(key=Cube.min_z)

    settled_points = set()
    settled_cubes = []
    num_changed = 0
    for cube in cubes:
        was_moved = False
        while cube.min_z() > 1 and not cube.down.points.intersection(settled_points):
            cube = cube.down
            was_moved = True

        num_changed += was_moved
        settled_points.update(cube.points)
        settled_cubes.append(cube)

    return settled_cubes, num_changed


def calc_num_dependencies(cubes: list[Cube]) -> dict[Cube, int]:
    cubes, _ = settle(cubes)

    dependencies = {}
    for cube in cubes:
        other_cubes = set(cubes) - {cube}
        _, num_changed = settle(list(other_cubes))
        dependencies[cube] = num_changed

    return dependencies


def parse_input(raw: str) -> list[Cube]:
    return list(map(_parse_cube, raw.strip().splitlines()))


def part_1(raw: str) -> int:
    cubes = parse_input(raw)
    dependencies = calc_num_dependencies(cubes)
    return sum(not num_dependent for num_dependent in dependencies.values())


def part_2(raw: str) -> int:
    cubes = parse_input(raw)
    dependencies = calc_num_dependencies(cubes)
    return sum(dependencies.values())


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
    print(part_2(lib.get_input(22)))
