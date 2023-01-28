from typing import NamedTuple, Optional, Tuple

import lib

Calls = list[int]


class BingoBoard(NamedTuple):
    squares: list[list[Optional[int]]]

    @staticmethod
    def from_str(raw: str) -> "BingoBoard":
        squares = [[int(c) for c in line.split()] for line in raw.strip().splitlines()]
        return BingoBoard(squares)

    def update(self, new_num: int) -> "BingoBoard":
        squares = [[None if n == new_num else n for n in row] for row in self.squares]
        return BingoBoard(squares)

    def is_winner(self) -> bool:
        for row in self.squares:
            if all(s is None for s in row):
                return True

        for col_i in range(len(self.squares[0])):
            if all(r[col_i] is None for r in self.squares):
                return True

        return False

    def score(self) -> int:
        return sum(s for row in self.squares for s in row if s)


def parse_input(raw: str) -> Tuple[Calls, list[BingoBoard]]:
    raw = raw.strip()
    first_line, other_lines = raw.split("\n\n", maxsplit=1)

    calls = list(map(int, first_line.split(",")))
    boards = list(map(BingoBoard.from_str, other_lines.split("\n\n")))
    return calls, boards


def part_1(raw) -> int:
    calls, boards = parse_input(raw)

    for call in calls:
        boards = [board.update(call) for board in boards]

        winners = [board for board in boards if board.is_winner()]
        if winners:
            return winners[0].score() * call


def part_2(raw) -> int:
    calls, boards = parse_input(raw)

    for call in calls:
        boards = [board.update(call) for board in boards]
        if len(boards) == 1 and boards[0].is_winner():
            return boards[0].score() * call

        boards = [b for b in boards if not b.is_winner()]


if __name__ == "__main__":
    print(part_1(lib.get_input(4)))
    print(part_2(lib.get_input(4)))
