import enum

from lib import Tape, chunks


def get_input():
    with open("inputs/day13.txt") as f:
        values = list(map(int, f.read().strip().split(",")))

    return Game(Tape(values))


class TileType(int, enum.Enum):
    Empty = 0
    Wall = 1
    Block = 2
    Paddle = 3
    Ball = 4


class Game:
    def __init__(self, tape):
        self.tape = tape
        self.world = Game.build_world(tape)

    @staticmethod
    def build_world(tape):
        world = dict()

        tape.run()

        for x, y, tile_id in chunks(tape.output, 3):
            world[(x, y)] = TileType(tile_id)

        return world


def part1():
    game = get_input()
    return len([tile for tile in game.world.values() if tile == TileType.Block])


if __name__ == "__main__":
    print(part1())
