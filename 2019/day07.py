import collections
import itertools


class Tape:
    def __init__(self, values, params=None, input_values=None):
        self.values = values
        self.cursor = 0
        self.finished = False
        self.output = []
        self.input_values = collections.deque(input_values)

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

    def add_input(self, _in):
        self.input_values.append(_in)

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

        result = method(*args)
        if result is None:
            self.cursor += instruction_count

        return instruction != 4

    def step(self):
        return self._exec()

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
        _in = self.input_values.popleft()
        self.values[address] = _in

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
    with open("inputs/day07.txt") as f:
        return list(map(int, f.read().split(",")))


def calculate_amplitude(settings):
    previous_signal = 0

    for setting in settings:
        input_values = (i for i in [setting, previous_signal])
        tape = Tape(get_input(), input_values=input_values)
        tape.run()
        previous_signal = tape.output[-1]

    return previous_signal


def calculate_amplitude_2(settings):
    tapes = []

    for setting in settings:
        tapes.append(Tape(get_input(), input_values=[setting]))

    tapes[0].add_input(0)

    while all(not tape.finished for tape in tapes):
        for tape_index, tape in enumerate(tapes):
            should_continue = tape.step()
            while should_continue and not tape.finished:
                should_continue = tape.step()

            output = tape.output[-1]
            tapes[(tape_index + 1) % 5].add_input(output)

    return tapes[-1].output[-1]


def part1():
    phase_settings = itertools.permutations(range(5))

    return max(map(calculate_amplitude, phase_settings))


def part2():
    phase_settings = list(itertools.permutations(range(5, 10)))

    return max(map(calculate_amplitude_2, phase_settings))


if __name__ == "__main__":
    print(part1())
    print(part2())
