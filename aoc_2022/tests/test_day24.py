from day24 import *

EXAMPLE = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""


def test_parse_input():
    blizzard_system = parse_input(EXAMPLE)

    assert blizzard_system.dimensions == Dimensions(width=6, height=4)

    blizzards = blizzard_system.blizzards

    assert len(blizzards) == 19

    assert blizzards[Point(0, 0)] == [Point(1, 0)]
    assert blizzards[Point(5, 0)] == [Point(-1, 0)]
    assert blizzards[Point(1, 2)] == [Point(0, 1)]

    assert blizzard_system.start_position == Point(0, -1)
    assert blizzard_system.end_position == Point(5, 4)


def test_advance_blizzard():
    original_system = parse_input(EXAMPLE)
    next_system = original_system.advance()

    assert original_system.dimensions == next_system.dimensions

    blizzards = next_system.blizzards
    assert len(blizzards) == 14
    assert set(blizzards[Point(2, 0)]) == {Point(1, 0), Point(-1, 0), Point(0, 1)}


def test_generate_possible_moves():
    blizzard = parse_input(EXAMPLE)

    start_moves = blizzard.generate_possible_moves(blizzard.start_position)
    assert set(start_moves) == {blizzard.start_position, Point(0, 0)}

    assert not blizzard.generate_possible_moves(Point(0, 2))

    assert set(blizzard.generate_possible_moves(Point(5, 0))) == {
        Point(5, 0),
        Point(5, 1),
    }

    assert blizzard.generate_possible_moves(Point(5, 3)) == [blizzard.end_position]


def test_part_1():
    assert part_1(EXAMPLE) == 18


def test_part_2():
    assert part_2(EXAMPLE) == 54
