import itertools
import typing

import lib


def get_input():
    with open("inputs/day01.txt") as f:
        return list(map(int, f.readlines()))


def find_entries(
    entries: typing.Iterable[int], num_dimensions: int, target: int
) -> int:
    combinations = itertools.combinations(entries, num_dimensions)
    return lib.product(lib.first(combinations, lambda combo: sum(combo) == target))


if __name__ == "__main__":
    print(find_entries(get_input(), 2, 2020))
    print(find_entries(get_input(), 3, 2020))
