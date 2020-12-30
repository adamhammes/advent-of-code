from day22 import *

SAMPLE_INPUT_1 = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

RECURSIVE_SAMPLE = """
Player 1:
43
19

Player 2:
2
29
14
"""


def test_parse_input():
    player_1, player_2 = parse_input(SAMPLE_INPUT_1)

    assert player_1 == deque([9, 2, 6, 3, 1])
    assert player_2 == deque([5, 8, 4, 7, 10])


def test_deck_code():
    assert deck_code(deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])) == 306


def test_part_1():
    assert part_1(SAMPLE_INPUT_1) == 306
    assert part_1(lib.get_input(22)) == 34005


def test_part_2():
    # check that this terminates
    assert part_2(RECURSIVE_SAMPLE)

    assert part_2(SAMPLE_INPUT_1) == 291
