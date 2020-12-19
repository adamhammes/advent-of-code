import typing as t

import lib


def apply(operators: t.List[str], values: t.List[int]):
    values.append(eval(f"{values.pop()} {operators.pop()} {values.pop()}"))


def greater_precedence(op1: str, op2: str):
    return op1 == "+" and op2 == "*"


def shunting_yard(raw: str, *, ignore_precedence=False) -> int:
    values = []
    operators = []

    for c in raw.replace(" ", ""):
        if c.isnumeric():
            values.append(int(c))
        elif c == "(":
            operators.append(c)
        elif c == ")":
            while operators and operators[-1] != "(":
                apply(operators, values)
            operators.pop()
        else:
            while (
                operators
                and operators[-1] not in "()"
                and (greater_precedence(operators[-1], c) or ignore_precedence)
            ):
                apply(operators, values)
            operators.append(c)

    while operators:
        apply(operators, values)

    return values[0]


def part_1(raw: str) -> int:
    return sum(shunting_yard(line, ignore_precedence=True) for line in raw.splitlines())


def part_2(raw: str) -> int:
    return sum(map(shunting_yard, raw.splitlines()))


if __name__ == "__main__":
    print(part_1(lib.get_input(18)))
    print(part_2(lib.get_input(18)))
