from typing import NamedTuple, Tuple
import re

from lib import Point

PROBLEM_INPUT = "target area: x=102..157, y=-146..-90"


class TargetRange(NamedTuple):
    x_range: range
    y_range: range

    def __contains__(self, p: "Probe") -> bool:
        return p.position.x in self.x_range and p.position.y in self.y_range

    def out_of_range(self, p: "Probe"):
        return p.position.x > max(self.x_range) or p.position.y < min(self.y_range)

    def possible_x_velocities(self) -> range:
        import math

        left_border = min(self.x_range)
        # https://en.wikipedia.org/wiki/Triangular_number#Triangular_roots_and_tests_for_triangular_numbers
        min_x = math.ceil(((8 * left_border + 1) ** 0.5 - 1) / 2)
        max_x = max(self.x_range)
        return range(min_x, max_x + 1)

    def possible_y_velocities(self) -> range:
        min_y = min(self.y_range)
        max_y = max(self.possible_x_velocities())  # is this right?
        return range(min_y - 1, max_y + 1)

    @staticmethod
    def from_str(raw: str) -> "TargetRange":
        x1, x2, y1, y2 = list(map(int, re.findall(r"-?\d+", raw)))
        return TargetRange(range(x1, x2 + 1), range(y2, y1 - 1, -1))


class Probe(NamedTuple):
    position: Point
    velocity: Point

    def step(self) -> "Probe":
        new_x_velocity = max(0, self.velocity.x - 1)
        return Probe(
            velocity=Point(new_x_velocity, self.velocity.y - 1),
            position=self.position.displace(*self.velocity),
        )

    @staticmethod
    def create(velocity: Point) -> "Probe":
        return Probe(velocity=velocity, position=Point(0, 0))


def simulate_shot(probe: Probe, target: TargetRange) -> Tuple[bool, int]:
    highest_y = 0

    while not target.out_of_range(probe):
        highest_y = max(probe.position.y, highest_y)
        if probe in target:
            return True, highest_y

        probe = probe.step()

    return False, 0


def brute_force(target: TargetRange) -> dict[Point, int]:
    shot_results = {}

    for x_velocity in target.possible_x_velocities():
        for y_velocity in target.possible_y_velocities():
            velocity = Point(x_velocity, y_velocity)
            probe = Probe.create(velocity)
            hit_target, y = simulate_shot(probe, target)
            if hit_target:
                shot_results[velocity] = y

    return shot_results


if __name__ == "__main__":
    results = brute_force(TargetRange.from_str(PROBLEM_INPUT))
    print(max(results.values()))
    print(len(results))
