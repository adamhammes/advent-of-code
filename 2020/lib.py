import functools
import operator
import typing


def product(ints: typing.Iterable[int]) -> int:
    return functools.reduce(operator.mul, ints, 1)
