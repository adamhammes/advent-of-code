import typing

import lib


class Equation(typing.NamedTuple):
    result: int
    operands: list[int]


def parse_equation(line: str) -> Equation:
    nums = lib.extract_ints(line)
    return Equation(nums[0], nums[1:])


def parse_input(raw: str) -> list[Equation]:
    return list(map(parse_equation, raw.strip().splitlines()))


def is_valid(eq: Equation, allow_concatenation=False) -> bool:
    if len(eq.operands) == 1:
        return eq.result == eq.operands[0]

    a, b = eq.operands[0], eq.operands[1]

    mul = a * b
    add = a + b
    concat = int(str(a) + str(b))

    remaining_operands = eq.operands[2:]
    equations = [
        Equation(eq.result, [mul] + remaining_operands),
        Equation(eq.result, [add] + remaining_operands),
    ]

    if allow_concatenation:
        concat_eq = Equation(eq.result, [concat] + remaining_operands)
        equations.append(concat_eq)

    return any(is_valid(eq, allow_concatenation) for eq in equations)


def part_1(raw: str) -> int:
    equations = parse_input(raw)
    return sum(eq.result for eq in equations if is_valid(eq))


def part_2(raw: str) -> int:
    equations = parse_input(raw)
    return sum(eq.result for eq in equations if is_valid(eq, allow_concatenation=True))


if __name__ == "__main__":
    print(part_1(lib.get_input(7)))
    print(part_2(lib.get_input(7)))
