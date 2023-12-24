import itertools
import typing

import lib


class P3D(typing.NamedTuple):
    x: int
    y: int
    z: int


class HailStone(typing.NamedTuple):
    position: P3D
    velocity: P3D

    def second_point(self) -> P3D:
        return P3D(
            self.position.x + self.velocity.x,
            self.position.y + self.velocity.y,
            self.position.z + self.velocity.z,
        )

    def is_in_future(self, p: tuple[float, float]) -> bool:
        x_diff = p[0] - self.position.x
        return x_diff / self.velocity.x > 0


def parse_hailstone(raw: str) -> HailStone:
    px, py, pz, vx, vy, vz = lib.extract_ints(raw)
    return HailStone(position=P3D(px, py, pz), velocity=P3D(vx, vy, vz))


def parse_input(raw: str) -> list[HailStone]:
    return list(map(parse_hailstone, raw.strip().splitlines()))


def find_2d_intersection(h1: HailStone, h2: HailStone) -> tuple[float, float] | None:
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    h1_prime = h1.second_point()
    h2_prime = h2.second_point()

    x1 = h1.position.x
    x2 = h1_prime.x
    x3 = h2.position.x
    x4 = h2_prime.x

    y1 = h1.position.y
    y2 = h1_prime.y
    y3 = h2.position.y
    y4 = h2_prime.y

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None

    x_numerator = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    y_numerator = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)

    return x_numerator / denominator, y_numerator / denominator


def find_colliding_points(
    points: list[HailStone], bounds: range
) -> typing.Iterable[tuple[float, float]]:
    for h1, h2 in itertools.combinations(points, 2):
        intersection = find_2d_intersection(h1, h2)
        if intersection is None:
            continue

        x, y = intersection
        if (
            bounds.start < x < bounds.stop
            and bounds.start < y < bounds.stop
            and h1.is_in_future(intersection)
            and h2.is_in_future(intersection)
        ):
            yield intersection


def part_1(raw: str) -> int:
    hailstones = parse_input(raw)
    bounds = range(200000000000000, 400000000000000)
    return len(list(find_colliding_points(hailstones, bounds)))


if __name__ == "__main__":
    print(part_1(lib.get_input(24)))
