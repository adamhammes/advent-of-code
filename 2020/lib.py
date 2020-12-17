import functools
import itertools
import math
import operator
import typing

T = typing.TypeVar("T")


def get_input(day: int) -> str:
    with open(f"inputs/day{day:02}.txt") as f:
        return f.read()


def first(iterable: typing.Iterable[T], condition: typing.Callable[[T], bool]) -> T:
    return next(item for item in iterable if condition(item))


def product(ints: typing.Iterable[int]) -> int:
    return functools.reduce(operator.mul, ints, 1)


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


class PointNd:
    def __init__(self, values: typing.Iterable[int]):
        self.values = tuple(values)
        self.num_dimensions = len(self.values)

    def displace(self, delta_array) -> "PointNd":
        if len(delta_array) != self.num_dimensions:
            raise ValueError(
                f"Tried to displace an {self.num_dimensions}d point by a {len(delta_array)}-length delta array"
            )
        return PointNd(val + delta for val, delta in zip(self.values, delta_array))

    def __hash__(self):
        return hash(self.values)

    def __eq__(self, other):
        if isinstance(other, PointNd):
            return self.values == other.values

        return False

    def __repr__(self):
        return f"PointNd{self.values}"

    def neighbors(self) -> typing.Set["PointNd"]:
        points = set()
        for displacement in itertools.product([-1, 0, 1], repeat=self.num_dimensions):
            points.add(self.displace(displacement))

        return points - {self}
