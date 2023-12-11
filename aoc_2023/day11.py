import dataclasses
import itertools

import lib
from lib import Point


@dataclasses.dataclass
class System:
    galaxies: list[Point]
    empty_rows: list[int]
    empty_columns: list[int]


def parse_input(raw: str) -> System:
    lines = raw.strip().splitlines()

    empty_rows = [i for i, line in enumerate(lines) if all(c == "." for c in line)]
    empty_columns = [
        i for i in range(len(lines)) if all(line[i] == "." for line in lines)
    ]

    galaxies = list(
        sorted(
            [p for p, val in lib.parse_grid(raw).items() if val == "#"],
            key=lambda p2: (p2.y, p2.x),
        )
    )

    return System(galaxies=galaxies, empty_rows=empty_rows, empty_columns=empty_columns)


def calc_distance(system: System, g1: Point, g2: Point, expansion_factor=2) -> int:
    x_range = range(*sorted([g1.x, g2.x]))
    empty_x_collisions = [i for i in system.empty_columns if i in x_range]
    row_distance = len(x_range) + len(empty_x_collisions) * (expansion_factor - 1)

    y_range = range(*sorted([g1.y, g2.y]))
    empty_y_collisions = [i for i in system.empty_rows if i in y_range]
    column_distance = len(y_range) + len(empty_y_collisions) * (expansion_factor - 1)
    return row_distance + column_distance


def sum_distances(system: System, expansion_factor: int) -> int:
    distances: dict[(Point, Point), int] = {}
    for g1, g2 in itertools.product(
        system.galaxies, system.galaxies
    ):  # type: (Point, Point)
        g1, g2 = list(sorted([g1, g2]))
        if g1 == g2 or (g1, g2) in distances:
            continue

        distances[(g1, g2)] = calc_distance(system, g1, g2, expansion_factor)

    return sum(distances.values())


def part_1(raw: str) -> int:
    system = parse_input(raw)
    return sum_distances(system, 2)


def part_2(raw: str) -> int:
    system = parse_input(raw)
    return sum_distances(system, 1_000_000)


if __name__ == "__main__":
    print(part_1(lib.get_input(11)))
    print(part_2(lib.get_input(11)))
