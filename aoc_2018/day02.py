import collections
import itertools

import lib


def contains_n(line: str, n: int):
    counter = collections.Counter(line)
    return n in dict(counter).values()


def part_1(raw: str) -> int:
    lines = raw.strip().splitlines()

    two_counts = sum(contains_n(line, 2) for line in lines)
    three_counts = sum(contains_n(line, 3) for line in lines)

    return two_counts * three_counts


def part_2(raw: str) -> str:
    lines = raw.strip().splitlines()

    for l1, l2 in itertools.combinations(lines, 2):
        overlap = "".join(c1 for c1, c2 in zip(l1, l2) if c1 == c2)
        if len(overlap) == len(l1) - 1:
            return overlap


if __name__ == "__main__":
    print(part_1(lib.get_input(2)))
    print(part_2(lib.get_input(2)))
