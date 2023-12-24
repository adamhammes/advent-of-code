from day24 import *

EXAMPLE_1 = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


def test_parse_input():
    hailstones = parse_input(EXAMPLE_1)
    assert hailstones[-1] == HailStone(
        position=P3D(20, 19, 15),
        velocity=P3D(1, -5, -3),
    )


def test_find_2d_intersection():
    h1 = parse_hailstone("18, 19, 22 @ -1, -1, -2")
    h2 = parse_hailstone("20, 25, 34 @ -2, -2, -4")

    assert find_2d_intersection(h1, h2) is None

    h1 = parse_hailstone("19, 13, 30 @ -2, 1, -2")
    h2 = parse_hailstone("18, 19, 22 @ -1, -1, -2")

    assert find_2d_intersection(h1, h2) == (14.33333, 15.33333)


def test_colliding_points():
    points = parse_input(EXAMPLE_1)
    bounds = range(7, 27)

    collisions = list(find_colliding_points(points, bounds))
    assert len(collisions) == 2
