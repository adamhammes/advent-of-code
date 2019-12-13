import collections
import re

from lib import lcm

COORDS = ["x", "y", "z"]

CHALLENGE_INPUT = """
<x=-17, y=9, z=-5>
<x=-1, y=7, z=13>
<x=-19, y=12, z=5>
<x=-6, y=-6, z=-4>
""".strip()


class Moon(collections.namedtuple("Moon", ["position", "velocity"])):
    def apply_gravity(self, other_moon):
        for coord in COORDS:
            diff = other_moon.position[coord] - self.position[coord]
            if diff == 0:
                continue

            self.velocity[coord] += int(diff / abs(diff))

    def step(self):
        for coord in COORDS:
            self.position[coord] += self.velocity[coord]

    def energy(self):
        potential_energy = sum(map(abs, self.position.values()))
        kinetic_energy = sum(map(abs, self.velocity.values()))
        return potential_energy * kinetic_energy


def parse_input(_in):
    zero_velocity = lambda: {coord: 0 for coord in COORDS}

    moons = []
    for line in _in.splitlines():
        nums = map(int, re.findall(r"-?\d+", line))
        positions = dict(zip(COORDS, nums))
        moons.append(Moon(positions, zero_velocity()))

    return Simulation(moons)


class Simulation:
    def __init__(self, moons):
        self.moons = moons

    def apply_gravity(self):
        for moon in self.moons:
            for other_moon in self.moons:
                moon.apply_gravity(other_moon)

    def step(self):
        self.apply_gravity()
        [moon.step() for moon in self.moons]

    def total_energy(self):
        return sum(map(Moon.energy, self.moons))

    def positions_in_dimension(self, dim):
        return tuple(moon.position[dim] for moon in self.moons)

    def velocities_in_dimension(self, dim):
        return tuple(moon.velocity[dim] for moon in self.moons)


def part1():
    sim = parse_input(CHALLENGE_INPUT)
    [sim.step() for _ in range(1000)]
    return sim.total_energy()


def find_loop_in_dimension(dim, _in):
    i = 0
    seen_positions = set()
    sim = parse_input(_in)

    while True:
        if sim.velocities_in_dimension(dim) == (0, 0, 0, 0):
            positions = sim.positions_in_dimension(dim)
            if positions in seen_positions:
                return i

            seen_positions.add(positions)

        i += 1
        sim.step()


def part2(_in=CHALLENGE_INPUT):
    sim = parse_input(_in)
    seen_positions = set()

    cycles = (find_loop_in_dimension(coord, _in) for coord in COORDS)
    return lcm(*cycles)


if __name__ == "__main__":
    print(part1())
    print(part2())
