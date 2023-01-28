from day14 import *


def test_parse_input():
    assert parse_input(EXAMPLE_1)[0] == {"NN": 1, "NC": 1, "CB": 1}


def test_expand_polymer():
    pairs, rules, letter_counts = parse_input(EXAMPLE_1)

    expanded_pairs_1, letter_counts_1 = expand_polymer(pairs, rules, letter_counts)
    # NCNBCHB
    assert letter_counts_1 == collections.Counter("NCNBCHB")
    assert expanded_pairs_1 == {
        "NC": 1,
        "CN": 1,
        "NB": 1,
        "BC": 1,
        "CH": 1,
        "HB": 1,
    }

    expanded_pairs_2, letter_counts_2 = expand_polymer(
        expanded_pairs_1, rules, letter_counts_1
    )
    # NBCCNBBBCBHCB
    assert letter_counts_2 == collections.Counter("NBCCNBBBCBHCB")
    assert expanded_pairs_2 == {
        "NB": 2,
        "BC": 2,
        "CC": 1,
        "CN": 1,
        "BB": 2,
        "CB": 2,
        "BH": 1,
        "HC": 1,
    }

    expanded_pairs_3, letter_counts_3 = expand_polymer(
        expanded_pairs_2, rules, letter_counts_2
    )
    assert letter_counts_3 == collections.Counter("NBBBCNCCNBBNBNBBCHBHHBCHB")


def test_part_1():
    assert part_1(EXAMPLE_1, 10) == 1588


EXAMPLE_1 = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
