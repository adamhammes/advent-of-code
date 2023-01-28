from collections import deque
import enum
from typing import Set, Tuple, Deque

import lib

Deck = Deque[int]
SeenPositions = Set[Tuple[Tuple[int, ...], Tuple[int, ...]]]


class Player(enum.Enum):
    Player1 = enum.auto()
    Player2 = enum.auto()


def parse_input(raw: str) -> Tuple[Deck, Deck]:
    top, bottom = raw.strip().split("\n\n")

    player_1 = deque(int(line) for line in top.splitlines() if line.isnumeric())
    player_2 = deque(int(line) for line in bottom.splitlines() if line.isnumeric())

    return player_1, player_2


def deck_code(deck: Deck) -> int:
    total = 0
    for i, card in enumerate(reversed(deck)):
        total += (i + 1) * card

    return total


class Game:
    def __init__(self, player_1: Deck, player_2: Deck):
        self.player_1 = player_1
        self.player_2 = player_2

        self.seen_positions = set()

    def winning_deck_code(self):
        return deck_code(self.player_1 or self.player_2)

    def current_position(self):
        return tuple(self.player_1), tuple(self.player_2)

    def recurse(self, num_p1: int, num_p2: int) -> "Game":
        player_1 = deque(list(self.player_1)[:num_p1])
        player_2 = deque(list(self.player_2)[:num_p2])

        return Game(player_1, player_2)

    def play(self, *, recursive: bool) -> Player:
        while self.player_1 and self.player_2:
            if self.current_position() in self.seen_positions:
                return Player.Player1

            self.seen_positions.add(self.current_position())

            left, right = self.player_1.popleft(), self.player_2.popleft()

            if recursive and len(self.player_1) >= left and len(self.player_2) >= right:
                sub_game = self.recurse(left, right)
                winner = sub_game.play(recursive=True)
            else:
                winner = Player.Player1 if left > right else Player.Player2

            if winner == Player.Player2:
                self.player_2 += [right, left]
            else:
                self.player_1 += [left, right]

        return Player.Player1 if self.player_1 else Player.Player2


def part_1(raw: str):
    player_1, player_2 = parse_input(raw)
    game = Game(player_1, player_2)
    game.play(recursive=False)
    return game.winning_deck_code()


def part_2(raw: str):
    player_1, player_2 = parse_input(raw)
    game = Game(player_1, player_2)
    game.play(recursive=True)
    return game.winning_deck_code()


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
    print(part_2(lib.get_input(22)))
