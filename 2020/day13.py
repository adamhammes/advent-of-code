import itertools
import math
import typing

import lib


def parse_input(raw: str) -> typing.Tuple[int, typing.List[int]]:
    lines = raw.splitlines()
    first, second = lines[0], lines[1]
    bus_ids = [int(val) for val in second.split(",") if val.isnumeric()]
    return int(first), bus_ids


def first_departure_after(timestamp: int, bus_id: int) -> int:
    return math.ceil(timestamp / bus_id) * bus_id


def part_1(raw: str):
    arrival, bus_ids = parse_input(raw)
    departure, bus_id = min(
        (first_departure_after(arrival, bid), bid) for bid in bus_ids
    )
    return (departure - arrival) * bus_id


def parse_part_2(raw: str) -> typing.List[typing.Tuple[int, int]]:
    raw_buses = raw.splitlines()[1].split(",")
    return [
        (int(bus_id), index)
        for index, bus_id in enumerate(raw_buses)
        if bus_id.isnumeric()
    ]


def find_min(m, prod, y, y_offset):
    possibilities = itertools.count(m, prod)
    return lib.first(possibilities, lambda num: (num + y_offset) % y == 0)


def part_2(raw: str):
    constraints = parse_part_2(raw)

    m = find_min(
        constraints[0][0], constraints[0][0], constraints[1][0], constraints[1][1]
    )
    prod = constraints[0][0]
    for val, offset in constraints[1:]:
        m = find_min(m, prod, val, offset)
        prod *= val

    return m


if __name__ == "__main__":
    print(part_1(lib.get_input(13)))
    print(part_2(lib.get_input(13)))
