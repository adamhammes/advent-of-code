import collections
import enum
import re
import typing as t

import lib
from lib import Point


class Directions(enum.Enum):
    North = Point(0, -1)
    East = Point(1, 0)
    South = Point(0, 1)
    West = Point(-1, 0)


class Contents(enum.Enum):
    Empty = " "
    Air = "."
    Wall = "#"


Grid = [[Contents]]
Instruction = int | t.Literal["R"] | t.Literal["L"]


def parse_input(raw: str) -> (Grid, [Instruction]):
    raw_points: str
    raw_instructions: str
    raw_points, raw_instructions = raw.split("\n\n")

    point_lines = raw_points.strip("\n").splitlines()

    # Pad out lines with spaces to remove jagged edges
    max_width = max(map(len, point_lines))
    point_lines = [line.ljust(max_width, " ") for line in point_lines]

    grid: Grid = []
    for line in point_lines:
        grid.append([Contents(c) for c in line])

    instructions = re.split("([RL])", raw_instructions.strip())
    instructions = [
        int(string) if string.isdecimal() else string for string in instructions
    ]

    return grid, instructions


def move(grid: Grid, current_position: Point, direction: Point, distance: int) -> Point:
    height, width = len(grid), len(grid[0])
    num_steps_taken = 0
    last_viable_position = current_position

    while num_steps_taken < distance:
        current_position = current_position.displace(*direction)
        x, y = current_position.x % width, current_position.y % height
        current_position = Point(x, y)

        cell: Contents = grid[current_position.y][current_position.x]

        match cell:
            case Contents.Air:
                last_viable_position = current_position
                num_steps_taken += 1
            case Contents.Wall:
                return last_viable_position
            case Contents.Empty:
                pass

    return last_viable_position


def part_1(raw: str):
    grid, instructions = parse_input(raw)

    start_x = grid[0].index(Contents.Air)
    current_position = Point(start_x, 0)

    directions = collections.deque(
        [
            Directions.East,
            Directions.South,
            Directions.West,
            Directions.North,
        ]
    )

    for instruction in instructions:
        match instruction:
            case int():
                current_position = move(
                    grid, current_position, directions[0].value, instruction
                )
            case "R":
                directions.rotate(-1)
            case "L":
                directions.rotate(1)

    facing_points = {
        Directions.East: 0,
        Directions.South: 1,
        Directions.West: 2,
        Directions.North: 3,
    }[directions[0]]

    return (
        (current_position.y + 1) * 1_000 + (current_position.x + 1) * 4 + facing_points
    )


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
