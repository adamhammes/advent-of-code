import re
import typing

import math

import lib


class BoatRace(typing.NamedTuple):
    time: int
    distance: int


def parse_input(raw: str) -> list[BoatRace]:
    raw_times, raw_distances = raw.strip().splitlines()
    times = lib.extract_ints(raw_times)
    distances = lib.extract_ints(raw_distances)

    return [
        BoatRace(distance=distance, time=time)
        for distance, time in zip(distances, times)
    ]


def parse_bad_kerning(raw: str) -> BoatRace:
    raw_times, raw_distances = raw.strip().splitlines()
    time_digits = re.findall(r"\d", raw_times)
    distance_digits = re.findall(r"\d", raw_distances)

    return BoatRace(
        time=int("".join(time_digits)), distance=int("".join(distance_digits))
    )


def calc_distance_in_time(time: int, wait_time: int) -> int:
    time -= wait_time
    return time * wait_time


def count_winning_times(race: BoatRace) -> int:
    return sum(
        calc_distance_in_time(race.time, wait_time) > race.distance
        for wait_time in range(1, race.time)
    )


def part_1(raw: str):
    races = parse_input(raw)
    return math.prod(count_winning_times(race) for race in races)


def part_2(raw: str):
    race = parse_bad_kerning(raw)
    return count_winning_times(race)


if __name__ == "__main__":
    print(part_1(lib.get_input(6)))
    print(part_2(lib.get_input(6)))
