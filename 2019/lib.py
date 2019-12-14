import collections
import itertools
import math


def chunks(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def first(iterable, condition):
    return next(item for item in iterable if condition(item))


def lcm(*args):

    lcm = args[0]
    for i in args[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm


class Tape:
    def __init__(self, values, params=None, input_values=None):
        self.values = values
        self.cursor = 0
        self.finished = False
        self.output = []
        self.input_values = collections.deque(input_values or [])
        self.extra_values = collections.defaultdict(int)

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

    def _read(self, address):
        if address >= len(self.values):
            return self.extra_values[address]

        return self.values[address]

    def _write(self, address, value):
        if address >= len(self.values):
            self.extra_values[address] = value
        else:
            self.values[address] = value

    def add_input(self, _in):
        self.input_values.append(_in)

    def _get_values(self, full_opcode, instruction_count):
        parameter_string = str(full_opcode // 100).rjust(instruction_count, "0")
        parameter_modes = list(reversed(list(map(int, parameter_string))))

        if full_opcode % 100 in [1, 2, 7, 8]:
            parameter_modes[-1] = True

        for i, parameter_mode in enumerate(parameter_modes):
            op_value = self.values[self.cursor + i]
            if parameter_mode == 0:
                yield self.values[op_value]
            elif parameter_mode == 1:
                yield op_value

    def _exec(self):
        full_opcode = self.values[self.cursor]
        instruction = full_opcode % 100
        method, instruction_count = self.instructions[instruction]
        self.cursor += 1

        if instruction in [3, 99]:
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
        self._write(outputPos, x + y)

    def _multiply(self, x, y, outputPos):
        self._write(outputPos, x * y)

    def _halt(self):
        self.finished = True

    def _input(self, address):
        _in = self.input_values.popleft()
        self._write(address, _in)

    def _output(self, value):
        self.output.append(value)

    def _jump_if_true(self, test, address):
        if test:
            self.cursor = address
            return True

    def _jump_if_false(self, test, address):
        if not test:
            self.cursor = address
            return True

    def _less_than(self, x, y, address):
        self._write(address, 1 if x < y else 0)

    def _equal(self, x, y, address):
        self.values(address, 1 if x == y else 0)
