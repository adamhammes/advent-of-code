import itertools
import re
import typing

T = typing.TypeVar("T")


def get_input(day: int) -> str:
    with open(f"inputs/day{day:02}.txt") as f:
        return f.read()


def extract_ints(string: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", string)))


def first(
    iterable: typing.Iterable[T],
    condition: typing.Optional[typing.Callable[[T], bool]] = None,
) -> T:
    return next(item for item in iterable if condition is None or condition(item))


class Point(typing.NamedTuple):
    x: int
    y: int

    def cartesian_distance_to(self, o: "Point") -> int:
        return abs(o.x - self.x) + abs(o.y - self.y)

    def times(self, i: int) -> "Point":
        return Point(self.x * i, self.y * i)

    def displace(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def delta_to(self, o: "Point") -> "Point":
        return Point(o.x - self.x, o.y - self.y)

    def north(self) -> "Point":
        return self.displace(0, 1)

    def east(self) -> "Point":
        return self.displace(1, 0)

    def south(self):
        return self.displace(0, -1)

    def west(self):
        return self.displace(-1, 0)

    def neighbors4(self) -> list["Point"]:
        return [self.north(), self.east(), self.south(), self.west()]

    # fmt: off
    directions8 = [
        [-1,  1], [0,  1], [1,  1],
        [-1,  0],          [1,  0],
        [-1, -1], [0, -1], [1, -1],
    ]
    # fmt: on

    def neighbors8(self) -> typing.List["Point"]:
        return [self.displace(x, y) for x, y in self.directions8]


Grid = dict[Point, str]


def parse_grid(raw: str, rev_y=False) -> Grid:
    points = {}

    lines = raw.strip().splitlines()
    if rev_y:
        lines.reverse()

    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            points[Point(x, y)] = c

    return points


def product(nums: typing.Iterable[int]) -> int:
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
