import re

import lib


def part_1(raw: str):
    groups = re.findall(r"mul\(\d+,\d+\)", raw)
    ints = map(lib.extract_ints, groups)

    return sum(a * b for a, b in ints)


def part_2(raw: str):
    pattern = r"(?:mul\(\d+,\d+\))|(?:don't\(\))|(?:do\(\))"
    groups = re.findall(pattern, raw)

    enabled = True
    total = 0
    for group in groups:
        match group:
            case "don't()":
                enabled = False
            case "do()":
                enabled = True
            case _:
                if enabled:
                    a, b = lib.extract_ints(group)
                    total += a * b

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(3)))
    print(part_2(lib.get_input(3)))
