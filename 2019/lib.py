import collections
import enum
import itertools
import math
import typing as t


class Point(collections.namedtuple("Point", ["x", "y"])):
    def displace(self, x: float, y: float) -> "Point":
        return Point(self.x + x, self.y + y)

    def move_by_direction(self, direction: "CardinalDirection") -> "Point":
        return self.displace(*direction.value)

    def neighbors(self) -> t.Iterable["Point"]:
        for direction in CardinalDirection:
            yield self.displace(*direction.value)

    def is_neighbors_with(self, other_point: "Point") -> bool:
        return other_point in list(self.neighbors())

    def difference(self, other_point: "Point") -> "Point":
        return Point(other_point.x - self.x, other_point.y - self.y)

    def direction_to(self, other_point: "Point") -> "CardinalDirection":
        return CardinalDirection(self.difference(other_point))


class CardinalDirection(enum.Enum):
    Up = Point(0, 1)
    Right = Point(1, 0)
    Down = Point(0, -1)
    Left = Point(-1, 0)

    def inverse_direction(self) -> "CardinalDirection":
        return {
            CardinalDirection.Up: CardinalDirection.Down,
            CardinalDirection.Right: CardinalDirection.Left,
            CardinalDirection.Down: CardinalDirection.Up,
            CardinalDirection.Left: CardinalDirection.Right,
        }[self]


def chunks(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def first(iterable, condition):
    return next(item for item in iterable if condition(item))


def lcm(*args: int):

    lcm = args[0]
    for i in args[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm


class ParamType(enum.Enum):
    Address = enum.auto()
    Value = enum.auto()


def _read_param_modes(instruction, instruction_count):
    parameter_string = str(instruction // 100).rjust(instruction_count, "0")
    return reversed(list(map(int, parameter_string)))


class Tape:
    @staticmethod
    def tape_from_challenge(challenge, f_after=None, **kwargs):
        file_name = f"inputs/day{str(challenge).rjust(2, '0')}.txt"
        with open(file_name) as f:
            instructions = list(map(int, f.read().strip().split(",")))
            tape = Tape(instructions, **kwargs)

            if not f_after:
                return tape

            return f_after(tape)

    def __init__(
        self,
        values: t.List[int],
        params: t.Optional[t.Tuple[int, int]] = None,
        input_values=None,
    ):
        self.values = values
        self.cursor = 0
        self.finished = False
        self.output = []
        self.extra_values = collections.defaultdict(int)
        self.relative_offset = 0
        self.set_input(input_values)

        if params is not None:
            self.values[1], self.values[2] = params

        self.instructions = {
            1: (self._add, [ParamType.Value, ParamType.Value, ParamType.Address]),
            2: (self._multiply, [ParamType.Value, ParamType.Value, ParamType.Address]),
            3: (self._input, [ParamType.Address]),
            4: (self._output, [ParamType.Value]),
            5: (self._jump_if_true, [ParamType.Value, ParamType.Value]),
            6: (self._jump_if_false, [ParamType.Value, ParamType.Value]),
            7: (self._less_than, [ParamType.Value, ParamType.Value, ParamType.Address]),
            8: (self._equal, [ParamType.Value, ParamType.Value, ParamType.Address]),
            9: (self._adjust_relative_offset, [ParamType.Value]),
            99: (self._halt, []),
        }

    def set_input(self, input_values):
        listified = input_values
        if input_values is None:
            listified = []
        elif not isinstance(input_values, list):
            listified = [input_values]

        self.input_values = collections.deque(listified)

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

    def _get_values(self, full_opcode, param_types):
        parameter_modes = _read_param_modes(full_opcode, len(param_types))

        for i, parameter_mode, param_type in zip(
            itertools.count(), parameter_modes, param_types
        ):
            op_value = self._read(self.cursor + i)

            yield {
                (0, ParamType.Address): lambda: op_value,
                (0, ParamType.Value): lambda: self._read(op_value),
                (1, ParamType.Address): lambda: op_value,  # technically shouldn't exist
                (1, ParamType.Value): lambda: op_value,
                (2, ParamType.Address): lambda: op_value + self.relative_offset,
                (2, ParamType.Value): lambda: self._read(
                    op_value + self.relative_offset
                ),
            }[parameter_mode, param_type]()

    def _exec(self):
        full_opcode = self.values[self.cursor]
        instruction = full_opcode % 100
        method, param_types = self.instructions[instruction]
        instruction_count = len(param_types)
        self.cursor += 1

        if instruction == 99:
            args = self.values[self.cursor : self.cursor + instruction_count]
        else:
            args = self._get_values(full_opcode, param_types)

        result = method(*args)
        if result is None:
            self.cursor += instruction_count

        return instruction != 4

    def step(self):
        return self._exec()

    def run(self, halt_on_output=False):
        while not self.finished:
            was_output_instruction = not self._exec()

            if halt_on_output and was_output_instruction:
                break

        return self.values

    def run_until_output(self, num_output_values=1, provide_input=None):
        previous_num_output_values = len(self.output)
        if provide_input is not None:
            self.set_input(provide_input)

        [self.run(halt_on_output=True) for _ in range(num_output_values)]

        assert len(self.output) == num_output_values + previous_num_output_values

        return self.output[-num_output_values:]

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
        self._write(address, 1 if x == y else 0)

    def _adjust_relative_offset(self, value):
        self.relative_offset += value
