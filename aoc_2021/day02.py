from lib import get_input
from lib import Point
from typing import NamedTuple


class Movement(NamedTuple):
    direction: str
    magnitude: int

    def as_point(self) -> Point:
        return {"forward": Point(1, 0), "down": Point(0, 1), "up": Point(0, -1)}[
            self.direction
        ].times(self.magnitude)


def parse_input(raw_input: str) -> [Movement]:
    return [
        Movement(line.split()[0], int(line.split()[1]))
        for line in raw_input.splitlines()
    ]


def part_1(movements: [Movement]) -> int:
    position = Point(0, 0)

    for movement in movements:
        position = position.displace(*movement.as_point())

    return position.x * position.y


def part_2(movements: [Movement]) -> int:
    x, depth, aim = 0, 0, 0

    for movement in movements:
        if movement.direction == "down":
            aim += movement.magnitude
        elif movement.direction == "up":
            aim -= movement.magnitude
        elif movement.direction == "forward":
            x += movement.magnitude
            depth += movement.magnitude * aim

    return x * depth


if __name__ == "__main__":
    inputs = parse_input(get_input(2))

    print(part_1(inputs))
    print(part_2(inputs))
