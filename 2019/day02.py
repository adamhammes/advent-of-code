def get_input():
    with open("inputs/day02.txt") as f:
        return list(map(int, f.read().split(",")))


class Tape:
    def __init__(self, values, params=None):
        self.values = values
        self.cursor = 0
        self.finished = False

        if params is not None:
            self.values[1], self.values[2] = params

        self.instructions = {
            1: (self._add, 3),
            2: (self._multiply, 3),
            99: (self._halt, 0),
        }

    def _exec(self, method, instruction_count):
        self.cursor += 1
        args = self.values[self.cursor : self.cursor + instruction_count]
        method(*args)
        self.cursor += instruction_count

    def step(self):
        opcode = self.values[self.cursor]
        self._exec(*self.instructions[opcode])

    def run(self):
        while not self.finished:
            self.step()

        return self.values

    def _add(self, pos1, pos2, outputPos):
        self.values[outputPos] = self.values[pos1] + self.values[pos2]

    def _multiply(self, pos1, pos2, outputPos):
        self.values[outputPos] = self.values[pos1] * self.values[pos2]

    def _halt(self):
        self.finished = True


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
