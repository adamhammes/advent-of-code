import collections
import itertools
import typing
from typing import Iterator

import lib
from lib import Point as P

EXAMPLE = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

actual = lib.get_input(17)

shapes = {
    "horizontal_line": (P(2, 0), P(3, 0), P(4, 0), P(5, 0)),
    "plus": (P(2, 1), P(3, 2), P(3, 1), P(3, 0), P(4, 1)),
    "flipped_l": (P(2, 0), P(3, 0), P(4, 0), P(4, 1), P(4, 2)),
    "vertical_line": (P(2, 0), P(2, 1), P(2, 2), P(2, 3)),
    "block": (P(2, 0), P(2, 1), P(3, 0), P(3, 1)),
}


class CacheKey(typing.NamedTuple):
    points: frozenset[P]
    shape: tuple[P, ...]
    jet: str


def print_shape(shape: list[P]):
    for y in range(3, -1, -1):
        for x in range(8):
            is_rock = P(x, y) in shape
            print(lib.PRINTABLE_SQUARE if is_rock else " ", end="")
        print()


def print_rocks(rocks: set[P]):
    y_max = max(p.y for p in rocks)

    for y in range(y_max + 1, -1, -1):
        for x in range(8):
            is_rock = P(x, y) in rocks
            print(lib.PRINTABLE_SQUARE if is_rock else " ", end="")

        print()


def calc_rock_movement(rocks: set[P], shape: list[P], jets: Iterator[str]) -> list[P]:
    while True:
        movement = {"<": P(-1, 0), ">": P(1, 0)}[next(jets)]
        jetted_shape = [p.displace(*movement) for p in shape]

        new_shape = (
            jetted_shape
            if all(p.x in range(7) and p not in rocks for p in jetted_shape)
            else shape
        )

        dropped_shape = [p.displace(0, -1) for p in new_shape]
        if any(p in rocks for p in dropped_shape):
            return new_shape

        shape = dropped_shape


def simulate_rocks(rocks: set[P], jets: Iterator[str], num_iterations: int) -> set[P]:
    ordered_shapes = list(shapes.values())
    y_max = max(p.y for p in rocks)

    for i in range(num_iterations):
        current_shape = ordered_shapes[i % len(ordered_shapes)]
        current_shape = [p.displace(0, y_max + 4) for p in current_shape]

        dropped_shape = calc_rock_movement(rocks, current_shape, jets)
        shape_y_max = max(p.y for p in dropped_shape)
        y_max = max(y_max, shape_y_max)

        rocks.update(dropped_shape)

    return rocks


def part_2(raw: str, n=2022) -> int:
    rocks = set(P(x, 0) for x in range(8))
    raw = raw.strip()
    jets = itertools.cycle(raw)

    safety_factor = 10
    cycle_length = safety_factor * len(raw) * len(shapes)
    print(cycle_length)

    cycled_rocks = simulate_rocks(rocks, jets, cycle_length)
    max_y = max(r.y for r in cycled_rocks)

    cut_off_rocks = {r for r in rocks if r.y > max_y - 100}

    divided, modulo = n // cycle_length, n % cycle_length
    height_adjustment = max_y * (divided - 1)

    final_rocks = simulate_rocks(cut_off_rocks, jets, modulo)
    return height_adjustment + max(r.y for r in final_rocks)


def part_1(raw: str, n=2022) -> int:
    rocks = set(P(x, 0) for x in range(8))
    jets = itertools.cycle(raw.strip())
    final_rocks = simulate_rocks(rocks, jets, n)
    return max(r.y for r in final_rocks)


def find_seen_states(raw: str) -> int:
    max_size = len(raw) * len(shapes)
    states: dict[frozenset[P], list[int]] = collections.defaultdict(list)

    state_cache: dict[CacheKey, ]

    rocks = set(P(x, 0) for x in range(8))
    jets = itertools.cycle(raw.strip())


    simulate_rocks(rocks, jets, 20_000)
    rocks_by_altitude = collections.defaultdict(list)
    for rock in rocks:
        rocks_by_altitude[rock.y].append(rock)

    for y in range(20_000):

        points = list()
        for y_min in range(y - max_size, y):
            points += rocks_by_altitude[y_min]

        finger_print = frozenset(p.displace(0, -y) for p in points)
        states[finger_print].append(y)

    repeats = [occ for occ in states.values() if len(occ) > 1][0]
    print(repeats)
    for a, b in lib.window(repeats[1:], 2):
        a_val = part_1(raw, a)
        b_val = part_1(raw, b)
        print(b_val - a_val)


if __name__ == "__main__":
    # print(part_1(lib.get_input(17)))
    find_seen_states(EXAMPLE)
