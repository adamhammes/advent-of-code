from collections.abc import Iterable
import re

import lib


def parse_input(raw: str) -> Iterable[tuple[range, range]]:
    for line in raw.strip().splitlines():
        min_1, max_1, min_2, max_2 = re.findall(r"\d+", line)

        yield range(int(min_1), int(max_1) + 1), range(int(min_2), int(max_2) + 1)


def range_is_subset(r1: range, r2: range) -> bool:
    return min(r1) <= min(r2) and max(r1) >= max(r2)


def part_1(raw: str) -> int:
    ranges = parse_input(raw)

    total = 0
    for r1, r2 in ranges:
        total += range_is_subset(r1, r2) or range_is_subset(r2, r1)

    return total


def ranges_overlap(r1: range, r2: range) -> bool:
    return bool(set(r1) & set(r2))


def part_2(raw: str) -> int:
    total = 0

    for r1, r2 in parse_input(raw):
        total += ranges_overlap(r1, r2)

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(4)))
    print(part_2(lib.get_input(4)))
