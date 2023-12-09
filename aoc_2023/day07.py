import collections
import dataclasses

import lib

P1_ORDERING = "23456789TJQKA"
P2_ORDERING = "J23456789TQKA"


@dataclasses.dataclass
class Hand:
    cards: str
    bid: int = 0

    def types(self) -> tuple[int, ...]:
        counter = collections.Counter(self.cards)
        return tuple(sorted(counter.values(), reverse=True))

    def p1_card_indices(self) -> tuple[int, ...]:
        return tuple(P1_ORDERING.index(c) for c in self.cards)

    def p1_sort(self):
        return self.types(), self.p1_card_indices()

    def p2_card_indices(self) -> tuple[int, ...]:
        return tuple(P2_ORDERING.index(c) for c in self.cards)

    def best_possible_type(self) -> tuple[int, ...]:
        if self.cards == "JJJJJ":
            return (5,)

        most_common_character: str = collections.Counter(
            c for c in self.cards if c != "J"
        ).most_common(1)[0][0]
        return Hand(self.cards.replace("J", most_common_character)).types()

    def p2_sort(self):
        return self.best_possible_type(), self.p2_card_indices()


def parse_input(raw: str) -> list[Hand]:
    lines = raw.strip().splitlines()
    parts = [tuple(line.split(" ")) for line in lines]
    return [Hand(part[0], int(part[1])) for part in parts]


def sum_hands(hands: list[Hand]) -> int:
    return sum(rank * hand.bid for rank, hand in enumerate(hands, start=1))


def part_1(raw: str) -> int:
    hands = parse_input(raw)
    hands = list(sorted(hands, key=Hand.p1_sort))
    return sum_hands(hands)


def part_2(raw: str) -> int:
    hands = parse_input(raw)
    hands = list(sorted(hands, key=Hand.p2_sort))
    return sum_hands(hands)


if __name__ == "__main__":
    print(part_1(lib.get_input(7)))
    print(part_2(lib.get_input(7)))
