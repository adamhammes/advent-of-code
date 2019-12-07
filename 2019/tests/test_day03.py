import unittest

from day03 import *

TEST_INPUT_1 = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
""".strip()


class TestDay3(unittest.TestCase):
    def test_parsing(self):
        expected = [
            (Direction.Right, 8),
            (Direction.Up, 5),
            (Direction.Left, 5),
            (Direction.Down, 3),
        ]
        _in = "R8,U5,L5,D3"

        for expected, parsed in zip(expected, parse_wire(_in)):
            self.assertEqual(expected, parsed)

    def test_displace(self):
        origin = (1, 1)
        direction = Direction.Up
        magnitude = 3

        expected = [(1, 2), (1, 3), (1, 4)]
        self.assertEqual(expected, direction.displace(origin, magnitude))

    def test_plot_wire(self):
        graph = defaultdict(int)
        wire = parse_wire("U2,R2,D2,L2")
        expected = {
            (1, 2): 1,
            (1, 3): 1,
            (2, 3): 1,
            (3, 3): 1,
            (3, 2): 1,
            (3, 1): 1,
            (2, 1): 1,
            (1, 1): 1,
        }
        plot_wire(graph, wire)
        self.assertEqual(len(expected), len(graph))
        for key, val in graph.items():
            self.assertEqual(val, expected[key])

    def test1(self):
        wires = map(parse_wire, TEST_INPUT_1.split("\n"))
        self.assertEqual(159, part1(wires))

    def test2(self):
        wires = map(parse_wire, TEST_INPUT_1.split("\n"))
        self.assertEqual(610, part2(wires))
