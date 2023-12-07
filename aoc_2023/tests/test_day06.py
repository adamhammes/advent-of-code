from day06 import *

EXAMPLE_1 = """
Time:      7  15   30
Distance:  9  40  200
"""


def test_parse_input():
    assert parse_input(EXAMPLE_1) == [
        BoatRace(9, 7),
        BoatRace(40, 15),
        BoatRace(200, 30),
    ]


def test_calc_distance_in_time():
    assert calc_distance_in_time(7, 1) == 6
    assert calc_distance_in_time(7, 2) == 10


def test_count_winning_times():
    assert count_winning_times(BoatRace(time=7, distance=9)) == 4


def test_part_1():
    assert part_1(EXAMPLE_1) == 288


def test_bad_kerning():
    assert parse_bad_kerning(EXAMPLE_1) == BoatRace(time=71530, distance=940200)


def test_part_2():
    assert part_2(EXAMPLE_1) == 71503
