from day17 import *
from lib import PointNd

SAMPLE_1 = """
.#.
..#
###
""".strip()


def test_parse_input():
    parsed = parse_input(SAMPLE_1, num_dimensions=3)
    assert len(parsed) == 9

    assert parsed[PointNd([2, 2, 0])]
    assert not parsed[PointNd([2, 0, 0])]


def test_part_1():
    assert part_1(SAMPLE_1) == 112


def test_part_2():
    assert part_2(SAMPLE_1) == 848
