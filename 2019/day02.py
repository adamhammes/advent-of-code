import unittest


class Tape:
    def __init__(self, values, params=None):
        self.values = values
        self.cursor = 0
        self.finished = False

        if params is not None:
            self.values[1], self.values[2] = params

    def step(self):
        opcode = self.values[self.cursor]

        if opcode == 99:
            self.cursor += 1
            self.finished = True
        elif opcode == 1:
            self._add()
        elif opcode == 2:
            self._multiply()

    def _add(self):
        pos1, pos2, outputPos = self.values[self.cursor + 1 : self.cursor + 4]
        self.values[outputPos] = self.values[pos1] + self.values[pos2]
        self.cursor += 4

    def _multiply(self):
        pos1, pos2, outputPos = self.values[self.cursor + 1 : self.cursor + 4]
        self.values[outputPos] = self.values[pos1] * self.values[pos2]
        self.cursor += 4

    def run(self):
        while not self.finished:
            self.step()

        return self.values


def get_input():
    with open("inputs/day02.txt") as f:
        return list(map(int, f.read().split(",")))


def brute_force_2():
    for i in range(100):
        for j in range(100):
            output = Tape(get_input(), params=(i, j)).run()[0]
            if output == 19690720:
                return 100 * i + j

    return None


class TestDay1(unittest.TestCase):
    def test1(self):
        test_cases = [
            (
                [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
                [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
            ),
            ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
            ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
            ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
        ]

        for _input, expected in test_cases:
            result = Tape(_input).run()
            self.assertEqual(expected, result)

    def test_regressions(self):
        self.assertEqual(3058646, Tape(get_input(), params=(12, 2)).run()[0])
        self.assertEqual(8976, brute_force_2())


if __name__ == "__main__":
    print(Tape(get_input(), params=(12, 2)).run()[0])
    print(brute_force_2())
