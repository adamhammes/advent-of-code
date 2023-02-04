import collections
import functools
import itertools
import typing
import dataclasses

import lib
from lib import Point


class Dimensions(typing.NamedTuple):
    width: int
    height: int

    def contains_point(self, p: Point) -> bool:
        return p.x in range(self.width) and p.y in range(self.height)


Blizzards = dict[Point, list[Point]]


@dataclasses.dataclass(frozen=True)
class BlizzardSystem:
    blizzards: Blizzards
    dimensions: Dimensions

    @property
    def start_position(self) -> Point:
        return Point(0, -1)

    @property
    def end_position(self) -> Point:
        return Point(self.dimensions.width - 1, self.dimensions.height)

    def generate_possible_moves(self, current_position: Point) -> list[Point]:
        occupied_positions = set(self.next_blizzard_positions.keys())
        move_candidates = current_position.neighbors4() + [current_position]
        return [
            move
            for move in move_candidates
            if (self.dimensions.contains_point(move) and move not in occupied_positions)
            or move in [self.start_position, self.end_position]
        ]

    @functools.cached_property
    def next_blizzard_positions(self) -> Blizzards:
        new_blizzards = collections.defaultdict(list)

        for point, blizzards in self.blizzards.items():
            for direction in blizzards:
                new_position = point.displace(*direction)
                wrapped_position = Point(
                    new_position.x % self.dimensions.width,
                    new_position.y % self.dimensions.height,
                )
                new_blizzards[wrapped_position].append(direction)

        return new_blizzards

    def advance(self) -> "BlizzardSystem":
        return BlizzardSystem(
            blizzards=self.next_blizzard_positions, dimensions=self.dimensions
        )


def parse_input(raw: str) -> BlizzardSystem:
    lines = raw.strip().splitlines()
    field = [row.replace("#", "") for row in lines[1:-1]]

    dims = Dimensions(height=len(field), width=len(field[0]))

    blizzards = collections.defaultdict(list)
    for y, line in enumerate(field):
        for x, c in enumerate(line):
            if c == ".":
                continue

            blizzard_direction = {
                ">": Point(1, 0),
                "v": Point(0, 1),
                "<": Point(-1, 0),
                "^": Point(0, -1),
            }[c]

            blizzards[Point(x, y)].append(blizzard_direction)

    return BlizzardSystem(blizzards, dims)


def path_find(
    system: BlizzardSystem, start_position: Point, end_position: Point
) -> (BlizzardSystem, int):
    positions_to_visit = system.generate_possible_moves(start_position)
    for num_iterations in itertools.count(start=1):
        next_positions = set()
        for position in positions_to_visit:
            next_positions.update(system.generate_possible_moves(position))

        system = system.advance()
        if end_position in next_positions:
            return system, num_iterations

        positions_to_visit = next_positions


def part_1(raw: str) -> int:
    system = parse_input(raw)

    _, time = path_find(system, system.start_position, system.end_position)
    return time


def part_2(raw: str) -> int:
    system = parse_input(raw)

    system, trip_1 = path_find(system, system.start_position, system.end_position)
    system, trip_2 = path_find(system, system.end_position, system.start_position)
    system, trip_3 = path_find(system, system.start_position, system.end_position)

    return sum([trip_1, trip_3, trip_2])


if __name__ == "__main__":
    print(part_1(lib.get_input(24)))
    print(part_2(lib.get_input(24)))
