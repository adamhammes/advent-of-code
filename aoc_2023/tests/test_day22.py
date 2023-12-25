from day22 import *

EXAMPLE_1 = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""


def test_parse_cube():
    cubes = parse_input(EXAMPLE_1)

    assert cubes[0].points == {P3D(1, 0, 1), P3D(1, 1, 1), P3D(1, 2, 1)}
    assert cubes[0].above == {P3D(1, 0, 2), P3D(1, 1, 2), P3D(1, 2, 2)}


def test_supports():
    cubes = parse_input(EXAMPLE_1)
    cubes = settle(cubes)
    a, b, c, d, e, f, g = cubes

    assert a.supports(b)
    assert a.supports(c)


def test_do_something():
    cubes = parse_input(EXAMPLE_1)
    cubes = settle(cubes)
    a, b, c, d, e, f, g = cubes

    assert do_the_thing(cubes) == [b, c, d, e, g]


def test_part_1():
    assert part_1(EXAMPLE_1) == 5
