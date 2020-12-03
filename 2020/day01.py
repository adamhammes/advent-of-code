import functools
import itertools
import operator
import typing


def get_input():
    with open('inputs/day01.txt') as f:
        return list(map(int, f.readlines()))


def product(ints: typing.Iterable[int]) -> int:
    return functools.reduce(operator.mul, ints, 1)


def first(iterable, condition):
    return next(item for item in iterable if condition(item))


def find_entries(entries: typing.Iterable[int], num_dimensions: int, target: int) -> int:
    combinations = itertools.combinations(entries, num_dimensions)
    return product(first(combinations, lambda combo: sum(combo) == target))


if __name__ == "__main__":
    print(find_entries(get_input(), 2, 2020))
    print(find_entries(get_input(), 3, 2020))
