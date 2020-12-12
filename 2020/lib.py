import functools
import itertools
import math
import operator
import typing


def product(ints: typing.Iterable[int]) -> int:
    return functools.reduce(operator.mul, ints, 1)


T = typing.TypeVar("T")


def window(seq: typing.Iterable[T], n=2) -> typing.Iterable[typing.Tuple[T]]:
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


class Point(typing.NamedTuple):
    x: int
    y: int

    def displace(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    # fmt: off
    directions8 = [
        [-1,  1], [0,  1], [1,  1],
        [-1,  0],          [1,  0],
        [-1, -1], [0, -1], [1, -1],
    ]
    # fmt: on

    def neighbors8(self) -> typing.List["Point"]:
        return [self.displace(x, y) for x, y in self.directions8]

    def manhattan_distance_to(self, p: "Point") -> int:
        dx, dy = p.x - self.x, p.y - self.y
        return abs(dx) + abs(dy)

    def times(self, n: int) -> "Point":
        return Point(self.x * n, self.y * n)

    def rotate(self, degrees: int) -> "Point":
        """
        Rotate the point counter-clockwise around the origin the specified number of degrees.
        Resulting x/y coordinates will be rounded to the nearest integer.
        """
        rads = math.radians(degrees)
        sin, cos = math.sin(rads), math.cos(rads)

        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos

        return Point(int(round(x)), int(round(y)))
