import typing

import lib
from lib import extract_ints


class P(typing.NamedTuple):
    x: int
    y: int
    z: int

    # fmt: off
    adjacent = [
        ( 1,  0,  0),
        (-1,  0,  0),
        ( 0,  1,  0),
        ( 0, -1,  0),
        ( 0,  0,  1),
        ( 0,  0, -1),
    ]
    # fmt: off

    def neighbors(self) -> typing.Iterable["P"]:
        return (self.displace(P(*d)) for d in P.adjacent)

    def displace(self, vector: "P") -> "P":
        return P(self.x + vector.x, self.y + vector.y, self.z + vector.z)


def parse_input(raw: str) -> set[P]:
    lines = raw.strip().splitlines()
    return {P(*ints) for ints in map(extract_ints, lines)}


def part_1(raw: str) -> int:
    points = parse_input(raw)

    count = 0
    for p in points:
        count += sum(n not in points for n in p.neighbors())

    return count


if __name__ == "__main__":
    print(part_1(lib.get_input(18)))
