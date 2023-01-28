import unittest

from day18 import *
from lib import Point

EXAMPLE_1 = """
#########
#b.A.@.a#
#########
"""

EXAMPLE_2 = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""

EXAMPLE_3 = """
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
"""

EXAMPLE_4 = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
"""

EXAMPLE_5 = """
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
"""

REDDIT_EXAMPLE_1 = """
#########
#.....b.#
#.#####.#
#.a.@.a.#
#########
"""

REDDIT_EXAMPLE_2 = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""

REDDIT_EXAMPLE_3 = """
#########
#.....c.#
#.#####.#
#.a.@.b.#
#########
"""


class TestDay18(unittest.TestCase):
    def test_parse_input(self):
        world = parse_input(EXAMPLE_1)

        self.assertEqual(7, len(world.points))
        self.assertEqual(2, len(world.keys))
        self.assertEqual(1, len(world.doors))

        self.assertEqual(Point(5, 1), world.entrance)

    def test_neighbors(self):
        world = parse_input(EXAMPLE_1)

        point = Point(4, 1)
        expected = {Point(5, 1)}

        self.assertEqual(expected, world.neighbors(point, set()))

        expected = {Point(3, 1), Point(5, 1)}
        self.assertEqual(expected, world.neighbors(point, set("a")))

    def test_collect_keys(self):
        test_cases = [
            (EXAMPLE_1, 8),
            (EXAMPLE_2, 86),
            (EXAMPLE_3, 132),
            (EXAMPLE_4, 136),
            (EXAMPLE_5, 81),
            (REDDIT_EXAMPLE_1, 6),
            (REDDIT_EXAMPLE_2, 86),
            (REDDIT_EXAMPLE_3, 10),
        ]

        for example, answer in test_cases:
            world = parse_input(example)
            self.assertEqual(answer, world.collect_keys())
