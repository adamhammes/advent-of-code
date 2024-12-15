from day14 import *

EXAMPLE = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

EXAMPLE_BOUNDS = Bounds(11, 7)


def test_move():
    robot = Robot(Point(2, 4), Point(2, -3))

    robot.move(EXAMPLE_BOUNDS)
    assert robot.position == Point(4, 1)

    robot.move(EXAMPLE_BOUNDS)
    assert robot.position == Point(6, 5)


def test_part_1():
    assert part_1(EXAMPLE, EXAMPLE_BOUNDS) == 12
