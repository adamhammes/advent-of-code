import unittest

from day10 import *


MY_EXAMPLE = """
..#..
..#..
#####
..#..
..#..
"""

MY_EXAMPLE_2 = """
######
"""

EXAMPLE_1 = """
.#..#
.....
#####
....#
...##
""".strip()

EXAMPLE_2 = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
""".strip()

EXAMPLE_3 = """
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
""".strip()


LARGE_EXAMPLE = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""".strip()


class TestDay10(unittest.TestCase):
    def run_get_station(self, _in):
        points = parse_input(_in)
        vector_map = make_vector_map(points)
        return get_station(vector_map)

    def test_examples(self):
        self.assertEqual(6, part1(parse_input(MY_EXAMPLE)))
        self.assertEqual(2, part1(parse_input(MY_EXAMPLE_2)))
        self.assertEqual(8, part1(parse_input(EXAMPLE_1)))
        self.assertEqual(33, part1(parse_input(EXAMPLE_2)))

    def test_regressions(self):
        self.assertEqual(269, part1(parse_input(get_input())))

    def test_center_point(self):
        self.assertEqual(Point(3, 4), self.run_get_station(EXAMPLE_1))
        self.assertEqual(Point(5, 8), self.run_get_station(EXAMPLE_2))
        self.assertEqual(Point(1, 2), self.run_get_station(EXAMPLE_3))
        self.assertEqual(Point(11, 13), self.run_get_station(LARGE_EXAMPLE))

    def test_kill_asteroids(self):
        points = parse_input(LARGE_EXAMPLE)

        asteroids = [
            asteroid for _, asteroid in zip(range(299), kill_asteroids(points))
        ]

        kill_order = {
            1: (11, 12),
            2: (12, 1),
            3: (12, 2),
            10: (12, 8),
            20: (16, 0),
            50: (16, 9),
            100: (10, 16),
            199: (9, 6),
            200: (8, 2),
            201: (10, 9),
        }

        for order in sorted(kill_order.keys()):
            asteroid = kill_order[order]
            self.assertEqual(asteroid, asteroids[order - 1], order)

    def test_regressions(self):
        points = parse_input(get_input())
        self.assertEqual(part1(points), 269)
        self.assertEqual(part2(points), 612)
