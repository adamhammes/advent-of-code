import typing as t

import lib

TEST_INPUT_1 = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()


class Point(t.NamedTuple):
    x: float
    y: float


def get_input() -> t.Tuple[int, t.Dict[Point, bool]]:
    with open('inputs/day03.txt') as f:
        lines = f.read().strip().splitlines()

    points = {}
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            points[Point(x, y)] = character == "#"

    return len(lines[0]), points


def check_slope(dx, dy):
    width, points = get_input()

    tree_count = 0
    current_point = Point(0, 0)

    while True:
        if current_point not in points:
            return tree_count

        tree_count += points[current_point]

        x, y = (current_point.x + dx) % width, current_point.y + dy
        current_point = Point(x, y)


def part_1():
    return check_slope(3, 1)


def part_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return lib.product(check_slope(dx, dy) for dx, dy in slopes)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
