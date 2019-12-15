import collections
import enum
from lib import Tape


def get_input(origin_color=0):
    with open("inputs/day11.txt") as f:
        vals = list(map(int, f.read().strip().split(",")))

    return Robot(Tape(vals), origin_color=origin_color)


class Direction(tuple, enum.Enum):
    Up = (0, 1)
    Right = (1, 0)
    Down = (0, -1)
    Left = (-1, 0)

    def turn_left(self, point):
        new_direction = {
            Direction.Up: Direction.Left,
            Direction.Left: Direction.Down,
            Direction.Down: Direction.Right,
            Direction.Right: Direction.Up,
        }[self]

        new_location = point[0] + new_direction[0], point[1] + new_direction[1]

        return new_direction, new_location

    def turn_right(self, point):
        new_direction = {
            Direction.Up: Direction.Right,
            Direction.Left: Direction.Up,
            Direction.Down: Direction.Left,
            Direction.Right: Direction.Down,
        }[self]

        new_location = point[0] + new_direction[0], point[1] + new_direction[1]

        return new_direction, new_location


class Robot:
    def __init__(self, tape, origin_color=0):
        self.tape = tape
        self.direction = Direction.Up
        self.painted_points = set()
        self.world = collections.defaultdict(int)
        self.position = (0, 0)

        self.world[self.position] = origin_color

    def run(self):
        while True:
            current_color = self.world[self.position]
            self.tape.set_input([current_color])
            self.tape.run(halt_on_output=True)
            self.tape.run(halt_on_output=True)

            if self.tape.finished:
                return

            paint_color, direction = self.tape.output[-2:]
            self.world[self.position] = paint_color
            self.painted_points.add(self.position)

            if direction == 1:
                self.direction, self.position = self.direction.turn_right(self.position)
            else:
                self.direction, self.position = self.direction.turn_left(self.position)


def part1():
    robot = get_input()
    robot.run()
    return len(robot.painted_points)


def print_world(points):
    max_x = max(points, key=lambda p: p[0])[0]
    max_y = max(points, key=lambda p: p[1])[1]
    min_y = min(points, key=lambda p: p[1])[1]

    for y in range(max_y, min_y - 1, -1):
        line = []

        for x in range(max_x + 1):
            line.append("█" if (x, y) in points else " ")
        print("".join(line))


def part2():
    robot = get_input(origin_color=1)
    robot.run()
    white_pixels = [point for point, color in robot.world.items() if color == 1]
    print(print_world(white_pixels))


if __name__ == "__main__":
    print(part1())
    part2()
