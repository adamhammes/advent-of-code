from day04 import *

EXAMPLE_1 = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def test_bingo_board_parse():
    raw = """
        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
         2  0 12  3  7
    """

    board = BingoBoard.from_str(raw)
    assert len(board.squares) == 5
    assert board.squares[0] == [14, 21, 17, 24, 4]
    assert board.squares[4] == [2, 0, 12, 3, 7]


def test_bingo_board_update():
    board = BingoBoard.from_str(
        """
        14 21 2 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
         2  0 12  3  7
        """
    )

    updated = board.update(2)
    flat_squares = [n for row in updated.squares for n in row]

    assert not any(s == 2 for s in flat_squares)
    assert len([s for s in flat_squares if s is None]) == 2


def test_is_winner():
    board = BingoBoard.from_str(
        """
        2 2 2
        3 4 5
        6 7 8
        """
    )

    assert not board.is_winner()

    updated = board.update(2)
    assert updated.is_winner()
    assert updated.score() == 33

    board = BingoBoard.from_str(
        """
        2 3 4
        2 5 6
        2 7 8
        """
    )

    assert not board.is_winner()
    updated = board.update(2)
    assert updated.is_winner()


def test_parse_input():
    calls, boards = parse_input(EXAMPLE_1)

    assert calls[:3] == [7, 4, 9]
    assert len(boards) == 3
    assert boards[2] == BingoBoard.from_str(
        """
        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
         2  0 12  3  7
        """
    )


def test_part_1():
    assert part_1(EXAMPLE_1) == 4512


def test_part_2():
    assert part_2(EXAMPLE_1) == 1924
