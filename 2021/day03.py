import lib
from typing import Callable


def most_common_bit(lines: [str], col: int) -> str:
    zeroes, ones = 0, 0

    for line in lines:
        if line[col] == "0":
            zeroes += 1
        else:
            ones += 1

    return "0" if zeroes > ones else "1"


def least_common_bit(lines: [str], col: int) -> str:
    return "0" if most_common_bit(lines, col) == "1" else "1"


def part_1(raw: str) -> int:
    lines = raw.splitlines()

    high_bits = []
    low_bits = []
    for col in range(len(lines[0])):
        high_bits.append(most_common_bit(lines, col))
        low_bits.append(least_common_bit(lines, col))

    high = int("".join(high_bits), 2)
    low = int("".join(low_bits), 2)

    return high * low


def find_rating(lines: [str], classifier: Callable[[[str], int], str]) -> int:
    for col in range(len(lines[0])):
        bit_key = classifier(lines, col)
        lines = [l for l in lines if l[col] == bit_key]

        if len(lines) == 1:
            return int(lines[0], 2)


def part_2(raw: str):
    lines = raw.splitlines()

    oxygen = find_rating(lines, most_common_bit)
    co2 = find_rating(lines, least_common_bit)

    return oxygen * co2


if __name__ == "__main__":
    print(part_1(lib.get_input(3)))
    print(part_2(lib.get_input(3)))
