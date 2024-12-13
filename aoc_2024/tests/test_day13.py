from day13 import *

EXAMPLE_1 = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def test_solve():
    games = parse_input(EXAMPLE_1)
    assert games[0].is_solvable()
    assert not games[1].is_solvable()
    assert games[2].is_solvable()
    assert not games[3].is_solvable()


def test_part_1():
    assert part_1(EXAMPLE_1) == 480
