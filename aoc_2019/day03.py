from collections import defaultdict
import enum


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


def part1(wires=get_input()):
    graph = defaultdict(int)
    for wire in wires:
        plot_wire(graph, wire)

    intersection_points = [
        point
        for point, times_seen in graph.items()
        if times_seen > 1 and point != (1, 1)
    ]

    return list(sorted(map(cartesian_distance, intersection_points)))[0]


def part2(wires=get_input()):
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
    print(part1())
    print(part2())
