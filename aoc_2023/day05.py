import re
import typing

import lib


class MapRange(typing.NamedTuple):
    destination_start: int
    source_start: int
    range_length: int


class SeedRange(typing.NamedTuple):
    start: int
    stop: int

    def is_empty(self):
        return self.stop < self.start

    def translate(self, by: int) -> "SeedRange":
        return SeedRange(self.start + by, self.stop + by)

    def map_range(self, map_ranges: typing.Iterable[MapRange]) -> list["SeedRange"]:
        to_check = [self]
        new_ranges = []
        for r in map_ranges:
            r_stop = r.source_start + r.range_length - 1
            r_delta = r.destination_start - r.source_start

            for seed_range in to_check.copy():
                overlapping = SeedRange(
                    max(seed_range.start, r.source_start), min(seed_range.stop, r_stop)
                ).translate(r_delta)

                if overlapping.is_empty():
                    continue

                before = SeedRange(
                    seed_range.start, min(seed_range.stop, r.source_start - 1)
                )
                after = SeedRange(
                    max(seed_range.start, r.source_start + r.range_length),
                    seed_range.stop,
                )

                to_check.remove(seed_range)
                to_check += [sr2 for sr2 in [before, after] if not sr2.is_empty()]
                new_ranges.append(overlapping)

        return [sr for sr in new_ranges + to_check if not sr.is_empty()]


class Map(typing.NamedTuple):
    source: str
    destination: str
    ranges: tuple[MapRange, ...]


class Almanac(typing.NamedTuple):
    seeds: list[int]
    mapping: dict[str, Map]

    def solve(self, seed_ranges: list[SeedRange]):
        cur_source = "seed"
        while cur_source in self.mapping:
            cur_mapping = self.mapping[cur_source]
            cur_source = cur_mapping.destination

            new_ranges = set()
            for sr in seed_ranges:
                new_ranges.update(sr.map_range(cur_mapping.ranges))

            seed_ranges = new_ranges

        return min(seed_ranges).start


def parse_map(raw_map: str) -> Map:
    """humidity-to-location map:"""
    name_match = re.match("([a-z]+)-[a-z]+-([a-z]+) .*", raw_map)

    ranges = tuple(
        MapRange(*lib.extract_ints(line)) for line in raw_map.strip().splitlines()[1:]
    )

    return Map(*name_match.group(1, 2), ranges=ranges)


def parse_input(raw: str) -> Almanac:
    newline_blocks = raw.strip().split("\n\n")
    raw_seeds, raw_maps = newline_blocks[0], newline_blocks[1:]

    seeds = lib.extract_ints(raw_seeds)
    maps = tuple(map(parse_map, raw_maps))
    mapping = {_map.source: _map for _map in maps}

    return Almanac(seeds=seeds, mapping=mapping)


def part_1(raw: str) -> int:
    almanac = parse_input(raw)
    seed_ranges = [SeedRange(seed, seed) for seed in almanac.seeds]
    return almanac.solve(seed_ranges)


def part_2(raw: str) -> int:
    almanac = parse_input(raw)

    seed_ranges: list[SeedRange] = [
        SeedRange(start, start + length - 1)
        for start, length in lib.chunks(almanac.seeds, 2)
    ]

    return almanac.solve(seed_ranges)


if __name__ == "__main__":
    print(part_1(lib.get_input(5)))
    print(part_2(lib.get_input(5)))
