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


def is_almost_pair(l1: str, l2: str) -> bool:
    return sum(c1 != c2 for c1, c2 in zip(l1, l2)) == 1


def part_2(raw: str) -> str:
    lines = raw.strip().splitlines()

    for l1, l2 in itertools.combinations(lines, 2):
        if is_almost_pair(l1, l2):
            return "".join(c1 for c1, c2 in zip(l1, l2) if c1 == c2)


if __name__ == "__main__":
    print(part_1(lib.get_input(2)))
    print(part_2(lib.get_input(2)))
