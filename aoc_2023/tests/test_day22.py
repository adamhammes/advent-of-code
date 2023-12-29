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


def test_settle():
    cubes = settle(parse_input(EXAMPLE_1))

    start = set(cubes)

    not_start = [*cubes[:2], *cubes[3:]]
    settled = settle(not_start)

    for c in settled:
        assert c in start


def test_part_1():
    assert part_1(EXAMPLE_1) == 5


def test_part_2():
    assert part_2(EXAMPLE_1) == 7
