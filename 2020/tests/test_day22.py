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


def test_parse_input():
    player_1, player_2 = parse_input(SAMPLE_INPUT_1)

    assert player_1 == deque([9, 2, 6, 3, 1])
    assert player_2 == deque([5, 8, 4, 7, 10])


def test_play():
    player_1, player_2 = parse_input(SAMPLE_INPUT_1)

    play(player_1, player_2)

    assert player_1 == deque([2, 6, 3, 1, 9, 5])
    assert player_2 == deque([8, 4, 7, 10])

    play(player_1, player_2)

    assert player_1 == deque([6, 3, 1, 9, 5])
    assert player_2 == deque([4, 7, 10, 8, 2])


def test_deck_code():
    assert deck_code(deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])) == 306


def test_part_1():
    assert part_1(SAMPLE_INPUT_1) == 306
