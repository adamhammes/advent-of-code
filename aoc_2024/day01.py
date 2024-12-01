import collections

import lib


def part_1(raw: str):
    int_lines = list(map(lib.extract_ints, raw.strip().splitlines()))
    left = sorted(line[0] for line in int_lines)
    right = sorted(line[1] for line in int_lines)

    return sum(abs(l - r) for l, r in zip(left, right))


def part_2(raw: str):
    int_lines = list(map(lib.extract_ints, raw.strip().splitlines()))
    left = sorted(line[0] for line in int_lines)
    right = sorted(line[1] for line in int_lines)

    occurrences = collections.Counter(right)
    return sum(num * occurrences[num] for num in left)


if __name__ == "__main__":
    print(part_1(lib.get_input(1)))
    print(part_2(lib.get_input(1)))
