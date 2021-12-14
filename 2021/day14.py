import collections
from typing import Tuple

import lib

PairCounts = dict[str, int]
PairRules = dict[str, str]
LetterCounts = collections.Counter[str]


def parse_input(raw: str) -> Tuple[PairCounts, PairRules, LetterCounts]:
    start, raw_rules = raw.strip().split("\n\n")
    rules = dict(line.strip().split(" -> ") for line in raw_rules.splitlines())
    pairs = (c1 + c2 for c1, c2 in zip(start, start[1:]))
    return collections.Counter(pairs), rules, collections.Counter(start)


def expand_polymer(
    pair_counts: PairCounts, rules: PairRules, letter_counts: LetterCounts
) -> Tuple[PairCounts, LetterCounts]:
    new_pair_counts: dict[str, int] = collections.defaultdict(int)
    new_letter_counts = letter_counts.copy()
    for pair in pair_counts:
        produced_letter = rules[pair]

        new_letter_counts[produced_letter] += pair_counts[pair]
        pair_1 = pair[0] + produced_letter
        pair_2 = produced_letter + pair[1]

        new_pair_counts[pair_1] += pair_counts[pair]
        new_pair_counts[pair_2] += pair_counts[pair]

    return new_pair_counts, new_letter_counts


def part_1(raw: str, num_iterations: int) -> int:
    pairs, rules, letter_counts = parse_input(raw)

    for _ in range(num_iterations):
        pairs, letter_counts = expand_polymer(pairs, rules, letter_counts)

    occurrences = letter_counts.most_common()
    return occurrences[0][1] - occurrences[-1][1]


if __name__ == "__main__":
    print(part_1(lib.get_input(14), 10))
    print(part_1(lib.get_input(14), 40))
