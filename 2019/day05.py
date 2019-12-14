from lib import Tape


def get_input():
    with open("inputs/day05.txt") as f:
        return list(map(int, f.read().split(",")))


def part1():
    tape = Tape(get_input(), input_values=[1])
    tape.run()
    return tape.output[-1]


def part2():
    tape = Tape(get_input(), input_values=[5])
    tape.run()
    return tape.output[-1]


if __name__ == "__main__":
    print(part1())
    print(part2())
