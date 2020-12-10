import functools
import itertools
import operator
import typing


def product(ints: typing.Iterable[int]) -> int:
    return functools.reduce(operator.mul, ints, 1)


T = typing.TypeVar("T")


def window(seq: typing.Iterable[T], n=2) -> typing.Generator[typing.Tuple[T]]:
    """Returns a sliding window (of width n) over data from the iterable
    s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...
    """
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result
