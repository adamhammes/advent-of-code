import re

import lib

written_out_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

_WORDS = "|".join(written_out_digits.keys())
DIGIT = re.compile(r"\d|" + _WORDS)
BACKWARDS_DIGIT = re.compile(r"\d|" + _WORDS[::-1])


def part_1(raw: str) -> int:
    total = 0
    for line in raw.strip().splitlines():
        digits = list(filter(str.isdigit, line))
        total += int(digits[0] + digits[-1])

    return total


def part_2(raw: str) -> int:
    total = 0
    for line in raw.strip().splitlines():
        first_digit = DIGIT.search(line).group()
        second_digit = BACKWARDS_DIGIT.search(line[::-1]).group()[::-1]

        first_digit = written_out_digits.get(first_digit, first_digit)
        second_digit = written_out_digits.get(second_digit, second_digit)
        calibration_number = int(str(first_digit) + str(second_digit))
        total += calibration_number

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(1)))
    # print(part_1(EXAMPLE_INPUT))
    # print(part_1("3two3eightjszbfourkxbh5twonepr"))
