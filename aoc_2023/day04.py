import dataclasses
import typing

import lib


class Card(typing.NamedTuple):
    winning_numbers: list[int]
    your_numbers: list[int]

    def num_winning(self) -> int:
        return sum(num in self.winning_numbers for num in self.your_numbers)

    def score(self):
        matches = self.num_winning()
        if matches == 0:
            return 0

        return 2 ** (matches - 1)


@dataclasses.dataclass
class QuantumCard:
    winning_numbers: list[int]
    your_numbers: list[int]
    quantity: int = 0

    def num_winning(self) -> int:
        return sum(num in self.winning_numbers for num in self.your_numbers)


def parse_input(raw: str) -> typing.Iterable[Card]:
    for line in raw.strip().splitlines():
        _, number_part = line.split(":")
        winning, your = number_part.split("|")
        yield Card(lib.extract_ints(winning), lib.extract_ints(your))


def part_1(raw: str) -> int:
    cards = parse_input(raw)
    return sum(map(Card.score, cards))


def part_2(raw: str) -> int:
    cards = [QuantumCard([], [], 0)]
    cards += [QuantumCard(*card, quantity=1) for card in parse_input(raw)]

    for i, card in enumerate(cards):
        num_wins = card.num_winning()

        for ci in range(i + 1, i + 1 + num_wins):
            cards[ci].quantity += card.quantity

    return sum(c.quantity for c in cards)


if __name__ == "__main__":
    print(part_1(lib.get_input(4)))
    print(part_2(lib.get_input(4)))
