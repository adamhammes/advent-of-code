from lib import Tape


def get_input():
    with open("inputs/day02.txt") as f:
        return list(map(int, f.read().split(",")))


def part1():
    return Tape(get_input(), params=(12, 2)).run()[0]


def part2():
    for i in range(100):
        for j in range(100):
            output = Tape(get_input(), params=(i, j)).run()[0]
            if output == 19690720:
                return 100 * i + j

    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
