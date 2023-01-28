import enum

from lib import Tape, Point


class Codes(enum.Enum):
    Newline = 10
    Scaffold = ord("#")
    Space = ord(".")
    Up = ord("^")
    Right = ord(">")
    Down = ord("v")
    Left = ord("<")


class World:
    def __init__(self, tape):
        self.tape = tape
        self.points = set()
        self.populate()

    def populate(self):
        self.tape.run()

        x, y = 0, 0
        for code in map(Codes, self.tape.output):
            if code == Codes.Newline:
                x *= 0
                y += 1
                continue

            if code in [Codes.Scaffold, Codes.Up, Codes.Right, Codes.Down, Codes.Left]:
                self.points.add(Point(x, y))

            x += 1

    def neighbors(self, point):
        return self.points & set(point.neighbors())

    def scaffold_points(self):
        return [p for p in self.points if len(self.neighbors(p)) == 4]


def part1():
    world: World = Tape.tape_from_challenge(17, World)

    return sum(p.x * p.y for p in world.scaffold_points())


if __name__ == "__main__":
    print(part1())
