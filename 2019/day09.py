import unittest

from lib import Tape


def get_input():
    with open("inputs/day09.txt") as f:
        return list(map(int, f.read().split(",")))


def part1():
    tape = Tape(get_input(), input_values=[1])
    tape.run()
    return tape.output


def part2():
    tape = Tape(get_input(), input_values=[2])
    tape.run()
    return tape.output


class TestDay09(unittest.TestCase):
    def simple_test(self, _in, expected):
        tape = Tape(_in, input_values=[expected])
        tape.run()
        self.assertEqual(expected, tape.output[-1])

    def test_examples(self):
        self.simple_test([109, -1, 4, 1, 99], -1)
        self.simple_test([109, -1, 104, 1, 99], 1)
        self.simple_test([109, 1, 9, 2, 204, -6, 99], 204)
        self.simple_test([109, 1, 109, 9, 204, -6, 99], 204)
        self.simple_test([109, 1, 209, -1, 204, -106, 99], 204)
        self.simple_test([109, 1, 3, 3, 204, 2, 99], 424242)
        self.simple_test([109, 1, 203, 2, 204, 2, 99], 424242)

        test = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        tape = Tape(test)
        tape.run()
        self.assertEqual(16, len(str(tape.output[-1])))

        test = [104, 1125899906842624, 99]

        tape = Tape(test)
        tape.run()
        self.assertEqual(1125899906842624, tape.output[-1])


if __name__ == "__main__":
    print(part1())
    print(part2())
