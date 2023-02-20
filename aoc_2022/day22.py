import collections
import dataclasses
import enum
import re
import typing as t

import lib
from lib import Point


class Dir(enum.Enum):
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


square_mapping = {
    # fmt: off
    Point(1, 0): 1,
    Point(2, 0): 2,
    Point(1, 1): 3,
    Point(0, 2): 4,
    Point(1, 2): 5,
    Point(0, 3): 6,
    # fmt: on
}

rev_square_mapping: dict[int, Point] = {
    _id: coord for coord, _id in square_mapping.items()
}


@dataclasses.dataclass
class Grove:
    grid: Grid
    instructions: list[Instruction]
    current_position = Point(0, 0)

    directions = collections.deque(
        [
            Dir.East,
            Dir.South,
            Dir.West,
            Dir.North,
        ]
    )

    def __post_init__(self):
        self.current_position = Point(self.grid[0].index(Contents.Air), 0)

    @property
    def edge_size(self) -> int:
        return len(self.grid[0]) // 3

    def square_id(self, p: Point) -> t.Optional[int]:
        adjusted_x = p.x // self.edge_size
        adjusted_y = p.y // self.edge_size

        return square_mapping.get(Point(adjusted_x, adjusted_y), None)

    def wrap(self, position: Point, direction: Dir) -> tuple[int, Point, Dir]:
        current_square_id = self.square_id(position)
        cur = self.relative_position(position)
        size = self.edge_size

        match current_square_id, direction:
            case 1, Dir.North:
                return 6, Point(0, cur.x), Dir.East
            case 1, Dir.West:
                return 4, Point(0, size - cur.y - 1), Dir.East
            case 2, Dir.North:
                return 6, Point(cur.x, size - 1), Dir.North
            case 2, Dir.East:
                return 5, Point(size - 1, size - cur.y - 1), Dir.West
            case 2, Dir.South:
                return 3, Point(size - 1, cur.x), Dir.West
            case 3, Dir.East:
                return 2, Point(cur.y, size - 1), Dir.North
            case 3, Dir.West:
                return 4, Point(cur.y, 0), Dir.South
            case 4, Dir.North:
                return 3, Point(0, cur.x), Dir.East
            case 4, Dir.West:
                return 1, Point(0, size - cur.y - 1), Dir.East
            case 5, Dir.East:
                return 2, Point(size - 1, size - cur.y - 1), Dir.West
            case 5, Dir.South:
                return 6, Point(size - 1, cur.x), Dir.West
            case 6, Dir.East:
                return 5, Point(cur.y, size - 1), Dir.North
            case 6, Dir.South:
                return 2, Point(cur.x, 0), Dir.South
            case 6, Dir.West:
                return 1, Point(cur.y, 0), Dir.South
            case _:
                print("oop")

    def relative_position(self, p: Point):
        square_corner = rev_square_mapping[self.square_id(p)]
        return p.displace(*square_corner.times(-self.edge_size))

    def absolute_position(self, square_id: int, position: Point) -> Point:
        square_position = rev_square_mapping[square_id].times(self.edge_size)
        return square_position.displace(*position)

    def rotate_to_direction(self, direction: Dir):
        while self.directions[0] != direction:
            self.directions.rotate(1)

    def peek_step(self, position: Point, direction: Dir) -> tuple[Point, Dir]:
        naive_position = position.displace(*direction.value)

        if self.square_id(naive_position) is not None:
            return naive_position, direction

        new_square_id, relative_position, new_direction = self.wrap(position, direction)
        absolute_position = self.absolute_position(new_square_id, relative_position)
        return absolute_position, new_direction

    def move(self, direction: Dir, distance: int) -> tuple[Point, Dir]:
        num_steps_taken = 0
        current_position = self.current_position
        last_viable_position = current_position
        last_viable_direction = direction

        while num_steps_taken < distance:
            current_position, direction = self.peek_step(current_position, direction)

            cell: Contents = self.grid[current_position.y][current_position.x]

            match cell:
                case Contents.Air:
                    last_viable_position = current_position
                    last_viable_direction = direction
                    num_steps_taken += 1
                case Contents.Wall:
                    return last_viable_position, last_viable_direction
                case Contents.Empty:
                    pass

        return last_viable_position, last_viable_direction

    def current_score(self) -> int:
        facing_points = {
            Dir.East: 0,
            Dir.South: 1,
            Dir.West: 2,
            Dir.North: 3,
        }[self.directions[0]]

        return (
            (self.current_position.y + 1) * 1_000
            + (self.current_position.x + 1) * 4
            + facing_points
        )

    def do_thing(self):
        for instruction in self.instructions:
            match instruction:
                case int():
                    new_position, new_direction = self.move(
                        self.directions[0], instruction
                    )
                    self.current_position = new_position
                    self.rotate_to_direction(new_direction)
                case "R":
                    self.directions.rotate(-1)
                case "L":
                    self.directions.rotate(1)

        return self.current_score()


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

    return Grove(grid, instructions)


def part_1(raw: str):
    return parse_input(raw).do_thing()


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
