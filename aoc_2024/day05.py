import typing

import lib


class Ordering(typing.NamedTuple):
    first: int
    second: int


def parse_input(raw: str) -> typing.Tuple[list[Ordering], list[list[int]]]:
    raw_orderings, raw_sequences = raw.strip().split("\n\n")
    orderings = [
        Ordering(*lib.extract_ints(line)) for line in raw_orderings.splitlines()
    ]
    sequences = list(map(lib.extract_ints, raw_sequences.splitlines()))
    return orderings, sequences


def sort_sequence(orderings: list[Ordering], sequence: list[int]) -> list[int]:
    if len(sequence) < 2:
        return sequence

    sequence_set = set(sequence)
    orderings = [
        o for o in orderings if o.first in sequence_set and o.second in sequence_set
    ]

    def can_go_first(num):
        return all(o.second != num for o in orderings)

    first = lib.first(sequence, can_go_first)
    rest = [n for n in sequence if n != first]
    return [first] + sort_sequence(orderings, rest)


def part_1(raw: str):
    orderings, sequences = parse_input(raw)
    valid_sequences = [seq for seq in sequences if sort_sequence(orderings, seq) == seq]
    return sum(seq[len(seq) // 2] for seq in valid_sequences)


def part_2(raw: str):
    orderings, sequences = parse_input(raw)
    sequences = [
        sort_sequence(orderings, seq)
        for seq in sequences
        if sort_sequence(orderings, seq) != seq
    ]
    return sum(seq[len(seq) // 2] for seq in sequences)


if __name__ == "__main__":
    print(part_1(lib.get_input(5)))
    print(part_2(lib.get_input(5)))
