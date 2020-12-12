import enum
import itertools
import typing

from lib import Point

# 26

SAMPLE = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()


class SeatStatus(enum.Enum):
    Occupied = 0
    Empty = 1
    Floor = 2


SeatMap = typing.Dict[Point, SeatStatus]


def get_input():
    with open("inputs/day11.txt") as f:
        return f.read()


def parse_input(raw: str) -> SeatMap:
    seat_map = {}

    for y, line in enumerate(raw.splitlines()):
        for x, char in enumerate(line):
            p = Point(x, y)
            status = {".": SeatStatus.Floor, "L": SeatStatus.Empty}[char]

            seat_map[p] = status

    return seat_map


def visible_neighbors(seats: SeatMap, origin: Point) -> typing.List[SeatStatus]:
    directions = Point.directions8
    statuses = []

    for x, y in directions:
        for magnitude in itertools.count(1):
            dx, dy = x * magnitude, y * magnitude
            p = origin.displace(dx, dy)

            if p not in seats:
                break

            if seats[p] != SeatStatus.Floor:
                statuses.append(seats[p])
                break

    return statuses


def iterate(seat_map: SeatMap) -> SeatMap:
    new_map = {}

    for point, status in seat_map.items():
        neighbors = [p for p in point.neighbors8() if p in seat_map]
        neighbor_statuses = [seat_map[p] for p in neighbors]

        if status == SeatStatus.Empty and SeatStatus.Occupied not in neighbor_statuses:
            new_map[point] = SeatStatus.Occupied
        elif (
            status == SeatStatus.Occupied
            and neighbor_statuses.count(SeatStatus.Occupied) >= 4
        ):
            new_map[point] = SeatStatus.Empty
        else:
            new_map[point] = status

    return new_map


def iterate2(seat_map: SeatMap) -> SeatMap:
    new_map = {}

    for point, status in seat_map.items():
        neighbor_statuses = visible_neighbors(seat_map, point)

        if status == SeatStatus.Empty and SeatStatus.Occupied not in neighbor_statuses:
            new_map[point] = SeatStatus.Occupied
        elif (
            status == SeatStatus.Occupied
            and neighbor_statuses.count(SeatStatus.Occupied) >= 5
        ):
            new_map[point] = SeatStatus.Empty
        else:
            new_map[point] = status

    return new_map


def part_1(raw: str):
    seat_map = parse_input(raw)

    while True:
        new_map = iterate(seat_map)

        if new_map == seat_map:
            return list(new_map.values()).count(SeatStatus.Occupied)

        seat_map = new_map


def part_2(raw: str):
    seat_map = parse_input(raw)

    while True:
        new_seat_map = iterate2(seat_map)

        if new_seat_map == seat_map:
            return len(
                [
                    status
                    for status in seat_map.values()
                    if status == SeatStatus.Occupied
                ]
            )

        seat_map = new_seat_map


if __name__ == "__main__":
    print(part_1(get_input()))
    print(part_2(get_input()))
