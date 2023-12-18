from day18 import *

EXAMPLE_1 = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


def test_parse_input():
    digs = parse_input(EXAMPLE_1)
    assert digs[0] == Dig(Direction.Right, 6, "70c710")
    assert digs[-1] == Dig(Direction.Up, 2, "7a21e3")


def test_calc_area():
    dig_points = [
        (Point(-2, -2), Point(0, 4)),
        (Point(0, 4), Point(3, -1)),
        (Point(3, -1), Point(1, -1)),
        (Point(1, -1), Point(-2, -2)),
    ]

    assert calc_area(dig_points) == 13


def test_hex_conversion():
    dig = parse_input(EXAMPLE_1)[0]
    assert dig.as_hex() == Dig(Direction.Right, 461937, dig.color)


def test_part_1():
    assert part_1(EXAMPLE_1) == 62
