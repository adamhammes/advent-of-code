from day13 import *

EXAMPLE_1 = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

EXAMPLE_2 = """
#..###..#####
###..#.......
.##.#.#.###..
#####....####
#####....####
.##.#.#.###..
###..#.......
#..###..#####
#.##.##.....#
#########.###
#.##.#..#.###
#.##.#..#.###
#########.###
#.##.##.....#
#.####..#####
###..#.......
.##.#.#.###..
"""


def test_is_reflected_horizontally():
    m1 = parse_input(EXAMPLE_1)[0]

    assert is_reflected_horizontally(m1, 5)
    assert not is_reflected_horizontally(m1, 4)
    assert not is_reflected_horizontally(m1, 6)
    assert not is_reflected_horizontally(m1, 1)
    assert not is_reflected_horizontally(m1, 9)

    m2 = parse_input(EXAMPLE_1)[1]
    assert is_reflected_vertically(m2, 4)
    assert not is_reflected_vertically(m2, 1)
    assert not is_reflected_vertically(m2, 2)
    assert not is_reflected_vertically(m2, 3)
    assert not is_reflected_vertically(m2, 5)
    assert not is_reflected_vertically(m2, 6)
    assert not is_reflected_vertically(m2, 7)

    m3 = parse_input(EXAMPLE_2)[0]
    assert is_reflected_vertically(m3, 4)


def test_calc_score():
    m1, m2 = parse_input(EXAMPLE_1)

    assert calc_score(m1) == [5]
    assert calc_score(m2) == [400]
