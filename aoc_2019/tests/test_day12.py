import unittest

from day12 import *

TEST_INPUT_1 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
""".strip()

TEST_INPUT_2 = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
""".strip()


class TestDay12(unittest.TestCase):
    def test_parse_input(self):
        moons = parse_input(TEST_INPUT_1).moons
        self.assertEqual(4, len(moons))
        io = moons[0]

        self.assertEqual(dict(x=-1, y=0, z=2), io.position)
        self.assertEqual(dict(x=0, y=0, z=0), io.velocity)

    def test_step(self):
        io, europa, _, __ = parse_input(TEST_INPUT_1).moons

        io.apply_gravity(europa)

        self.assertEqual(dict(x=1, y=-1, z=-1), io.velocity)
        io.step()
        self.assertEqual(dict(x=0, y=-1, z=1), io.position)

    def test_simulate(self):
        simulation = parse_input(TEST_INPUT_1)
        moons = simulation.moons

        simulation.step()
        self.assertEqual(dict(x=3, y=-1, z=-1), moons[0].velocity)
        self.assertEqual(dict(x=2, y=-1, z=1), moons[0].position)

        [simulation.step() for _ in range(9)]

        self.assertEqual(dict(x=2, y=1, z=-3), moons[0].position)

    def test_total_energy(self):
        sim = parse_input(TEST_INPUT_2)
        [sim.step() for _ in range(10)]
        self.assertEqual(179, sim.total_energy())

    def test_part_2(self):
        self.assertEqual(2772, part2(_in=TEST_INPUT_1))

    def test_regressions(self):
        self.assertEqual(8742, part1())
        self.assertEqual(325433763467176, part2())
