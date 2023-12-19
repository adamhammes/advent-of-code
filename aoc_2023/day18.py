import dataclasses
import enum
import re
import typing

import lib
from lib import Point


class Direction(enum.Enum):
    Up = Point(0, 1)
    Right = Point(1, 0)
    Down = Point(0, -1)
    Left = Point(-1, 0)


class Dig(typing.NamedTuple):
    direction: Direction
    length: int
    color: str

    def as_hex(self) -> "Dig":
        color_digit = self.color[-1]
        direction = {
            "0": Direction.Right,
            "1": Direction.Down,
            "2": Direction.Left,
            "3": Direction.Up,
        }[color_digit]

        length = int(self.color[:5], 16)
        return Dig(direction, length, self.color)


def parse_dig(line: str) -> Dig:
    direction = {
        "U": Direction.Up,
        "R": Direction.Right,
        "D": Direction.Down,
        "L": Direction.Left,
    }[line[0]]

    length = lib.extract_ints(line)[0]

    color = re.search("#([a-z0-9]{6})", line).group(1)
    return Dig(direction, length, color)


def parse_input(raw: str) -> list[Dig]:
    return list(map(parse_dig, raw.strip().splitlines()))


DigPoints = list[tuple[Point, Point]]


def count_perimeter(digs: list[Dig]) -> int:
    return sum(dig.length for dig in digs)


def find_dig_points(digs: list[Dig]) -> DigPoints:
    corner_list = []
    current = Point(0, 0)
    for dig in digs:
        p1 = current
        current = current.displace(*dig.direction.value.times(dig.length))
        corner_list.append((p1, current))

    return corner_list


def calc_area(digs: list[Dig]) -> int:
    points = find_dig_points(digs)

    interior_area = 0
    for p1, p2 in points:
        interior_area += p1.x * p2.y - p2.x * p1.y

    interior_area = abs(interior_area) // 2

    return interior_area + count_perimeter(digs) // 2 + 1


def part_1(raw: str) -> int:
    digs = parse_input(raw)
    return calc_area(digs)


def part_2(raw: str) -> int:
    digs = parse_input(raw)
    digs = [dig.as_hex() for dig in digs]
    return calc_area(digs)


if __name__ == "__main__":
    print(part_1(lib.get_input(18)))
    print(part_2(lib.get_input(18)))
