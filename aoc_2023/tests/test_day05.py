from day05 import *


def test_parse_input():
    almanac = parse_input(EXAMPLE_1)
    assert almanac.seeds == [79, 14, 55, 13]

    assert len(almanac.mapping) == 7

    _map = almanac.mapping["seed"]
    assert _map.source == "seed"
    assert _map.destination == "soil"

    assert _map.ranges[0] == MapRange(50, 98, 2)


def test_convert_source():
    seed_soil = parse_input(EXAMPLE_1).mapping["seed"]

    assert seed_soil.convert_source(0) == 0
    assert seed_soil.convert_source(50) == 52
    assert seed_soil.convert_source(98) == 50
    assert seed_soil.convert_source(99) == 51


def test_part_1():
    assert part_1(EXAMPLE_1) == 35


def test_part_2():
    assert part_2(EXAMPLE_1) == 46


def test_seed_range():
    seed_range = SeedRange(79, 92)
    mapping = MapRange(source_start=50, destination_start=52, range_length=48)
    assert seed_range.map_range([mapping]) == [SeedRange(81, 94)]

    assert set(
        SeedRange(1, 6).map_range(
            [MapRange(source_start=3, destination_start=13, range_length=2)]
        )
    ) == {SeedRange(1, 2), SeedRange(13, 14), SeedRange(5, 6)}


"""
sr = 79, 92
mapping = 52..99 +2


sr = 55..67
mapping = 


81, 94
"""

EXAMPLE_1 = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
