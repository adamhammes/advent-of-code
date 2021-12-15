import itertools
import math
import typing

from typing import Iterable

T = typing.TypeVar("T")


def get_input(day: int) -> str:
    with open(f"inputs/day{day:02}.txt") as f:
        return f.read()


def product(nums: Iterable[int]) -> int:
    p = 1
    for n in nums:
        p *= n

    return p


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

    directions4 = [[0, 1], [-1, 0], [1, 0], [0, -1]]

    def neighbors4(self) -> list["Point"]:
        return [self.displace(x, y) for x, y in self.directions4]

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


def parse_grid(raw: str) -> dict[Point, str]:
    points = {}
    for y, line in enumerate(raw.strip().splitlines()):
        for x, c in enumerate(line.strip()):
            points[Point(x, y)] = c

    return points
