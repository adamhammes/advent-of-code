import collections
import typing

import lib
from lib import Point as P

EXAMPLE = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

shapes = {
    "horizontal_line": (P(2, 0), P(3, 0), P(4, 0), P(5, 0)),
    "plus": (P(2, 1), P(3, 2), P(3, 1), P(3, 0), P(4, 1)),
    "flipped_l": (P(2, 0), P(3, 0), P(4, 0), P(4, 1), P(4, 2)),
    "vertical_line": (P(2, 0), P(2, 1), P(2, 2), P(2, 3)),
    "block": (P(2, 0), P(2, 1), P(3, 0), P(3, 1)),
}

ordered_shapes = list(shapes.values())
Shape = tuple[P, ...]


class CacheKey(typing.NamedTuple):
    rocks: frozenset[P]
    jet_index: int
    shape_index: int


class CacheState(typing.NamedTuple):
    num_shapes_dropped: int
    y_max: int


class Tunnel:
    def __init__(self, jet_pattern: str, cache_height=40):
        self.jet_pattern = jet_pattern.strip()
        self.rocks = set(P(x, 0) for x in range(8))

        self.jet_index = 0
        self.num_shapes_dropped = 0

        self.y_max = 0

        self.cache: dict[CacheKey, list[CacheState]] = collections.defaultdict(list)
        self.cache_height = cache_height
        self.last_cache_key = CacheKey(rocks=frozenset(), jet_index=0, shape_index=0)

    def get_next_shape(self) -> Shape:
        shape = ordered_shapes[self.num_shapes_dropped % len(ordered_shapes)]
        self.num_shapes_dropped += 1
        return tuple(p.displace(0, self.y_max + 4) for p in shape)

    def get_next_jet(self) -> P:
        jet = self.jet_pattern[self.jet_index]
        self.jet_index += 1
        self.jet_index %= len(self.jet_pattern)
        return {"<": P(-1, 0), ">": P(1, 0)}[jet]

    def shape_in_bounds(self, shape: Shape) -> bool:
        return all(p.x in range(7) and p not in self.rocks for p in shape)

    def drop_rock(self) -> Shape:
        shape = self.get_next_shape()

        while True:
            jet_movement = self.get_next_jet()
            windswept_rock = tuple(p.displace(*jet_movement) for p in shape)

            shape = windswept_rock if self.shape_in_bounds(windswept_rock) else shape

            dropped_shape = tuple(p.displace(0, -1) for p in shape)

            if not self.shape_in_bounds(dropped_shape):
                return shape

            shape = dropped_shape

    def add_to_collection(self, shape: Shape) -> list[CacheState]:
        self.rocks.update(shape)
        shape_y_max = max(p.y for p in shape)
        self.y_max = max(shape_y_max, self.y_max)

        y_min = max(1, self.y_max - self.cache_height)

        previous_cache_rocks = self.last_cache_key.rocks
        new_cache_rocks = set(shape).union(previous_cache_rocks)
        new_cache_rocks = {
            P(p.x, p.y - y_min)
            for p in new_cache_rocks
            if p.y in range(y_min, self.y_max + 1)
        }

        cache_key = CacheKey(
            rocks=frozenset(new_cache_rocks),
            jet_index=self.jet_index,
            shape_index=self.num_shapes_dropped % len(ordered_shapes),
        )

        cache_state = CacheState(
            num_shapes_dropped=self.num_shapes_dropped, y_max=self.y_max
        )

        self.cache[cache_key].append(cache_state)
        self.last_cache_key = cache_key
        return self.cache[cache_key]

    def simulate(self, num_iterations: int, allow_skip=True):
        iterations = 0
        time_has_skipped = not allow_skip
        while iterations < num_iterations:
            iterations += 1
            dropped_shape = self.drop_rock()
            cache_state = self.add_to_collection(dropped_shape)

            if len(cache_state) < 3 or time_has_skipped:
                continue

            time_has_skipped = True
            s2 = cache_state[1]
            s3 = cache_state[2]

            iteration_gap = s3.num_shapes_dropped - s2.num_shapes_dropped
            y_max_gap = s3.y_max - s2.y_max

            cycles_to_skip = (num_iterations - iterations) // iteration_gap
            iterations += cycles_to_skip * iteration_gap
            simulated_y_max = self.y_max + y_max_gap * cycles_to_skip

            y_max_diff = simulated_y_max - self.y_max
            self.rocks = set(P(p.x, p.y + y_max_diff) for p in self.rocks)
            self.y_max = simulated_y_max


def part_1(raw: str) -> int:
    tunnel = Tunnel(raw)
    tunnel.simulate(2022, allow_skip=True)
    return tunnel.y_max


def part_2(raw: str) -> int:
    tunnel = Tunnel(raw)
    tunnel.simulate(1_000_000_000_000, allow_skip=True)
    return tunnel.y_max


if __name__ == "__main__":
    print(part_2(lib.get_input(17)))
