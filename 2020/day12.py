import dataclasses
import enum

from lib import Point


def get_input():
    with open("inputs/day12.txt") as f:
        return f.read().strip()


class TurnDirection(enum.Enum):
    Clockwise = enum.auto()
    CounterClockwise = enum.auto()


class Orientation(enum.IntEnum):
    North = 0
    East = 1
    South = 2
    West = 3

    def as_coords(self) -> Point:
        # fmt: off
        return Point(*{
            Orientation.North: ( 0,  1),
            Orientation.East:  ( 1,  0),
            Orientation.South: ( 0, -1),
            Orientation.West:  (-1,  0),
        }[self])

    @staticmethod
    def from_char(c: str) -> 'Orientation':
        return {
            'N': Orientation.North,
            'E': Orientation.East,
            'S': Orientation.South,
            'W': Orientation.West,
        }[c]


@dataclasses.dataclass
class ShipState:
    position: Point = Point(0, 0)
    orientation: Orientation = Orientation.East
    waypoint: Point = Point(10, 1)

    def displace_in_direction(self, direction: Orientation, steps: int):
        dx, dy = direction.as_coords()
        self.position = self.position.displace(dx * steps, dy * steps)

    def displace_front(self, steps: int):
        self.displace_in_direction(self.orientation, steps)

    def turn(self, direction: TurnDirection, steps: int):
        if direction == TurnDirection.Clockwise:
            self.orientation = Orientation((self.orientation + steps) % 4)
        else:
            self.orientation = Orientation((self.orientation - steps) % 4)

    def move(self, line: str) -> 'ShipState':
        instruction, steps = line[0], int(line[1:])

        if instruction in "NESW":
            direction = Orientation.from_char(instruction)
            self.displace_in_direction(direction, steps)
        elif instruction == "L":
            num_turns = steps // 90
            self.turn(TurnDirection.CounterClockwise, num_turns)
        elif instruction == "R":
            num_turns = steps // 90
            self.turn(TurnDirection.Clockwise, num_turns)
        elif instruction == "F":
            self.displace_front(steps)

        return self

    def move_waypoint(self, line: str) -> 'ShipState':
        instruction, steps = line[0], int(line[1:])

        if instruction in "NESW":
            displacement = Orientation.from_char(instruction).as_coords().times(steps)
            self.waypoint = self.waypoint.displace(*displacement)
        elif instruction in "LR":
            degrees = -1 * steps if instruction == "R" else steps
            self.waypoint = self.waypoint.rotate(degrees)
        elif instruction == "F":
            displacement = self.waypoint.times(steps)
            self.position = self.position.displace(*displacement)

        return self


def part_1(raw: str):
    ship = ShipState()
    [ship.move(line) for line in raw.splitlines()]
    return Point(0, 0).manhattan_distance_to(ship.position)


def part_2(raw: str):
    ship = ShipState()
    [ship.move_waypoint(line) for line in raw.splitlines()]
    return Point(0, 0).manhattan_distance_to(ship.position)


if __name__ == "__main__":
    print(part_1(get_input()))
    print(part_2(get_input()))
