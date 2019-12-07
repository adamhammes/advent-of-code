class Tape:
    def __init__(self, values, params=None, input_value=1):
        self.values = values
        self.cursor = 0
        self.finished = False
        self.output = []
        self.input_value = input_value

        if params is not None:
            self.values[1], self.values[2] = params

        self.instructions = {
            1: (self._add, 3),
            2: (self._multiply, 3),
            3: (self._input, 1),
            4: (self._output, 1),
            5: (self._jump_if_true, 2),
            6: (self._jump_if_false, 2),
            7: (self._less_than, 3),
            8: (self._equal, 3),
            99: (self._halt, 0),
        }

    def _get_values(self, full_opcode, instruction_count):
        parameter_string = str(full_opcode // 100).rjust(instruction_count, "0")
        uses_immediate = list(reversed(list(map(lambda x: x == "1", parameter_string))))

        if full_opcode % 100 in [1, 2, 7, 8]:
            uses_immediate[-1] = True

        for i, immediate_mode in enumerate(uses_immediate):
            op_value = self.values[self.cursor + i]
            value_to_use = op_value if immediate_mode else self.values[op_value]
            yield value_to_use

    def _exec(self):
        full_opcode = self.values[self.cursor]
        instruction = full_opcode % 100
        method, instruction_count = self.instructions[instruction]
        self.cursor += 1

        if instruction in [3, 4, 99]:
            args = self.values[self.cursor : self.cursor + instruction_count]
        else:
            args = self._get_values(full_opcode, instruction_count)

        if method(*args) is None:
            self.cursor += instruction_count

    def run(self):
        while not self.finished:
            self._exec()

        return self.values

    def _add(self, x, y, outputPos):
        self.values[outputPos] = x + y

    def _multiply(self, x, y, outputPos):
        self.values[outputPos] = x * y

    def _halt(self):
        self.finished = True

    def _input(self, address):
        self.values[address] = self.input_value

    def _output(self, address):
        self.output.append(self.values[address])

    def _jump_if_true(self, test, address):
        if test:
            self.cursor = address
            return True

    def _jump_if_false(self, test, address):
        if not test:
            self.cursor = address
            return True

    def _less_than(self, x, y, address):
        self.values[address] = 1 if x < y else 0

    def _equal(self, x, y, address):
        self.values[address] = 1 if x == y else 0


def get_input():
    with open("inputs/day05.txt") as f:
        return list(map(int, f.read().split(",")))


def part1():
    tape = Tape(get_input())
    tape.run()
    return tape.output[-1]


def part2():
    tape = Tape(get_input(), input_value=5)
    tape.run()
    return tape.output[-1]


if __name__ == "__main__":
    print(part1())
    print(part2())
