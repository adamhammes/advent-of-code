import string

import lib


def score_letter(letter: str) -> int:
    return string.ascii_letters.find(letter) + 1


def part_1(raw: str) -> int:
    lines = raw.strip().splitlines()

    total = 0
    for line in lines:
        length = len(line)
        first, second = line[: length // 2], line[length // 2 :]

        intersect = next(iter(set(first) & set(second)))
        total += score_letter(intersect)

    return total


def part_2(raw: str) -> int:
    lines = raw.strip().splitlines()

    total = 0

    for group_of_three in lib.chunks(lines, 3):
        a, b, c = list(group_of_three)
        intersect = next(iter(set(a) & set(b) & set(c)))
        total += score_letter(intersect)

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(3)))
    print(part_2(lib.get_input(3)))
