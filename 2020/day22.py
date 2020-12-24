from collections import deque
from typing import *

import lib

Deck = Deque[int]
SeenPositions = Set[Tuple[Tuple[int, ...], Tuple[int, ...]]]


def parse_input(raw: str) -> Tuple[Deck, Deck]:
    top, bottom = raw.strip().split("\n\n")

    player_1 = deque(int(line) for line in top.splitlines() if line.isnumeric())
    player_2 = deque(int(line) for line in bottom.splitlines() if line.isnumeric())

    return player_1, player_2


def play(player_1: Deck, player_2: Deck):
    left, right = player_1.popleft(), player_2.popleft()

    if left < right:
        player_2 += sorted([left, right], reverse=True)
    elif left > right:
        player_1 += sorted([left, right], reverse=True)
    else:
        player_1.append(left)
        player_2.append(right)


def deck_code(deck: Deck) -> int:
    total = 0
    for i, card in enumerate(reversed(deck)):
        total += (i + 1) * card

    return total


def part_1(raw: str):
    player_1, player_2 = parse_input(raw)

    while player_1 and player_2:
        play(player_1, player_2)

    winner = player_1 or player_2
    return deck_code(winner)


def play_recursive(seen_positions: SeenPositions, player_1: Deck, player_2: Deck):
    pass


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
