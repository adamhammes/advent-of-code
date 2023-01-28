import math
import typing

from lib import Point
import lib


class Instruction(typing.NamedTuple):
    direction: str
    distance: int

    def as_point(self) -> Point:
        return {
            "U": Point(0, 1),
            "R": Point(1, 0),
            "D": Point(0, -1),
            "L": Point(-1, 0),
        }[self.direction]


def parse_input(raw: str) -> [Instruction]:
    instructions = []
    for line in raw.strip().splitlines():
        direction, raw_distance = line.split(" ")
        instructions.append(Instruction(direction, int(raw_distance)))

    return instructions


def calculate_tail_movement(tail_pos: Point, head_pos: Point) -> Point:
    dx, dy = head_pos.x - tail_pos.x, head_pos.y - tail_pos.y

    if abs(dx) <= 1 and abs(dy) <= 1:  # cardinal direction or overlapping
        return tail_pos
    else:  # diagonal move
        move_y = int(math.copysign(1, dy)) if dy else 0
        move_x = int(math.copysign(1, dx)) if dx else 0
        return tail_pos.displace(move_x, move_y)


def calculate_seen_points(instructions: list[Instruction], rope_length: int) -> int:
    rope = [Point(0, 0)] * rope_length

    seen = {rope[-1]}
    for instruction in instructions:
        for _ in range(instruction.distance):
            rope[0] = rope[0].displace(*instruction.as_point())

            for i in range(len(rope) - 1):
                rope[i + 1] = calculate_tail_movement(rope[i + 1], rope[i])

            seen.add(rope[-1])

    return len(seen)


def part_1(raw: str) -> int:
    return calculate_seen_points(parse_input(raw), 2)


def part_2(raw: str) -> int:
    return calculate_seen_points(parse_input(raw), 10)


if __name__ == "__main__":
    print(part_1(lib.get_input(9)))
    print(part_2(lib.get_input(9)))
