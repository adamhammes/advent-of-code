import collections
import dataclasses
import enum
import functools
import typing

import lib
from lib import Point


class PixelState(str, enum.Enum):
    On = "#"
    Off = "."


def bits_to_int(bits: list[bool]) -> int:
    return sum(2 ** i * b for i, b in enumerate(reversed(bits)))


@dataclasses.dataclass()
class Image:
    enhance: tuple[PixelState, ...]
    solved_pixels: dict[(int, Point), PixelState]

    @functools.cached_property
    def initial_max_x(self):
        return max(p.x for i, p in self.solved_pixels if i == 0)

    @functools.cached_property
    def initial_max_y(self):
        return max(p.y for i, p in self.solved_pixels if i == 0)

    def is_extremity(self, p: Point, gen: int) -> bool:
        x_bounds = range(0 - gen - 1, self.initial_max_x + gen + 1)
        y_bounds = range(0 - gen - 1, self.initial_max_y + gen + 1)
        return p.x not in x_bounds or p.y not in y_bounds

    def compute_value(self, p: Point, iteration: int) -> PixelState:
        if (iteration, p) in self.solved_pixels:
            return self.solved_pixels[(iteration, p)]
        # elif iteration < 1:
        #     return PixelState.Off
        elif self.is_extremity(p, iteration):
            value = (
                PixelState.Off
                if self.enhance[0] == PixelState.Off
                else [PixelState.Off, PixelState.On][iteration % 2]
            )
            self.solved_pixels[(iteration, p)] = value
            return value

        if p == Point(-1, 0):
            a = 1

        neighbors8 = p.neighbors8()
        spatial_neighbors = sorted(
            neighbors8[:4] + [p] + neighbors8[4:], key=lambda _p: (_p[1], _p[0])
        )

        neighbors_bits = [
            self.compute_value(n, iteration - 1) == PixelState.On
            for n in spatial_neighbors
        ]

        value = self.enhance[bits_to_int(neighbors_bits)]
        self.solved_pixels[(iteration, p)] = value
        return value

    def iterate(self, num_iterations: int):
        current_generation = 1
        while current_generation <= num_iterations:
            prev_points = [
                p for gen, p in self.solved_pixels if gen == current_generation - 1
            ]
            max_x = max(p.x for p in prev_points)
            min_x = min(p.x for p in prev_points)
            max_y = max(p.y for p in prev_points)
            min_y = min(p.y for p in prev_points)

            for x in range(min_x - 1, max_x + 2):
                for y in range(min_y - 1, max_y + 2):
                    self.compute_value(Point(x, y), current_generation)

            current_generation += 1

        return {
            p: state
            for (gen, p), state in self.solved_pixels.items()
            if gen == current_generation - 1
        }


def parse_input(raw: str) -> Image:
    first_line, raw_grid = raw.strip().split("\n\n")

    enhance = tuple(map(PixelState, first_line.replace("\n", "")))

    pixels = {
        (0, point): PixelState(c) for point, c in lib.parse_grid(raw_grid).items()
    }

    return Image(enhance=enhance, solved_pixels=pixels)


def solve(image, num_iterations) -> int:
    grid = image.iterate(num_iterations)
    return len([p for p in grid if grid[p] == PixelState.On])


def part_1(raw: str) -> int:
    return solve(parse_input(raw), 2)


def part_2(raw: str) -> int:
    return solve(parse_input(raw), 50)


if __name__ == "__main__":
    print(part_1(lib.get_input(20)))
    print(part_2(lib.get_input(20)))
