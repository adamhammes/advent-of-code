from day14 import *


def test_parse_line():
    line = "498,4 -> 498,6 -> 496,6"

    assert parse_line(line) == [Point(498, 4), Point(498, 6), Point(496, 6)]


def test_build_line():
    p1, p2 = Point(498, 4), Point(498, 6)

    assert list(build_line(p2, p1)) == [Point(498, 4), Point(498, 5), Point(498, 6)]
