from collections import defaultdict
import enum
import unittest

TEST_INPUT_1 = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
""".strip()


def cartesian_distance(point, origin=(1, 1)):
    return abs(point[0] - origin[0]) + abs(point[1] - origin[1])


class Direction(enum.Enum):
    Left = "L"
    Right = "R"
    Up = "U"
    Down = "D"

    def displace(self, origin, magnitude):
        translate = {
            Direction.Left: (-1, 0),
            Direction.Right: (1, 0),
            Direction.Up: (0, 1),
            Direction.Down: (0, -1),
        }[self]

        points = []
        x, y = origin
        for i in range(1, magnitude + 1):
            points.append((x + i * translate[0], y + i * translate[1]))

        return points


def parse_wire(line):
    parts = line.split(",")
    vectors = []
    for part in parts:
        letter, magnitude = part[0], part[1:]
        vectors.append((Direction(letter), int(magnitude)))

    return vectors


def get_input():
    with open("inputs/day03.txt") as f:
        return map(parse_wire, f.readlines())


def plot_wire(graph, parsed_wire, steps_taken=None):
    origin = (1, 1)
    seen_points = set()

    steps = 0
    for direction, magnitude in parsed_wire:
        points = direction.displace(origin, magnitude)

        if steps_taken is not None:
            for point in points:
                steps += 1
                if not point in steps_taken:
                    steps_taken[point] = steps

        seen_points.update(points)
        origin = points[-1]

    for point in seen_points:
        graph[point] += 1


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


def part1(wires):
    graph = defaultdict(int)
    for wire in wires:
        plot_wire(graph, wire)

    intersection_points = [
        point
        for point, times_seen in graph.items()
        if times_seen > 1 and point != (1, 1)
    ]

    return list(sorted(map(cartesian_distance, intersection_points)))[0]


def part2(wires):
    graph = defaultdict(int)
    time_taken = {}

    step_aggregate = []
    for wire in wires:
        steps = {}
        plot_wire(graph, wire, steps)
        step_aggregate.append(steps)

    intersection_points = [
        point
        for point, times_seen in graph.items()
        if times_seen > 1 and point != (1, 1)
    ]

    min_steps = defaultdict(list)
    for point in intersection_points:
        for path_steps in step_aggregate:
            min_steps[point].append(path_steps[point])

    min_steps = list(sorted(min_steps.items(), key=lambda x: sum(x[1])))

    return sum(min_steps[0][1])


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))
