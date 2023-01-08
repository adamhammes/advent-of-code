import itertools
import math
import re
import typing


T = typing.TypeVar("T")

PRINTABLE_SQUARE = "█"


def get_input(day: int) -> str:
    with open(f"inputs/day{day:02}.txt") as f:
        return f.read()


def product(nums: typing.Iterable[int]) -> int:
    p = 1
    for n in nums:
        p *= n
    return p


def chunks(iterable, n):
    it = iter(iterable)
    while True:
        chunk_it = itertools.islice(it, n)
        try:
            first_el = next(chunk_it)
        except StopIteration:
            return
        yield itertools.chain((first_el,), chunk_it)


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


def extract_ints(string: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", string)))
