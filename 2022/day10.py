import typing

import lib


Instruction = typing.Tuple[str, int]


def parse_input(raw: str) -> list[Instruction]:
    instructions = []
    for line in raw.strip().splitlines():
        i_type = "addx" if "a" in line else "noop"
        val = int(line.split(" ")[1]) if i_type == "addx" else 0
        instructions.append((i_type, val))

    return instructions


def get_cycle_values(instructions: list[Instruction]) -> list[int]:
    cycle_values = []
    cycle = 0
    value = 1

    for instruction_type, instruction_value in instructions:
        if instruction_type == "noop":
            cycle_values.append(value)
            cycle += 1
        else:
            cycle_values += [value] * 2
            value += instruction_value

    return cycle_values


def part_1(raw: str) -> int:
    instructions = parse_input(raw)
    cycle_values = get_cycle_values(instructions)

    val = 0
    for index in range(20, len(cycle_values), 40):
        val += cycle_values[index - 1] * index

    return val


def part_2(raw: str):
    instructions = parse_input(raw)
    cycle_values = get_cycle_values(instructions)

    for y in range(6):
        for x in range(40):
            index = y * 40 + x

            if cycle_values[index] in [x - 1, x, x + 1]:
                print("█", end="")
            else:
                print(" ", end="")

        print()


if __name__ == "__main__":
    print(part_1(lib.get_input(10)))
    part_2(lib.get_input(10))
