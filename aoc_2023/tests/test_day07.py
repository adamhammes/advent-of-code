from day07 import *

EXAMPLE_1 = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def test_ordering():
    assert Hand("2AAAA").p1_sort() < Hand("33332").p1_sort()
    assert Hand("77888").p1_sort() > Hand("77788").p1_sort()

    assert Hand("QQQJA").p1_sort() > Hand("KTJJT").p1_sort()


def test_part_1():
    assert part_1(EXAMPLE_1) == 6440


def test_scratchpad():
    assert Hand("QJJQ2").best_possible_type() == (4, 1)
    assert Hand("JJJ22").best_possible_type() == (5,)

    assert Hand("JKKK2").p2_sort() < Hand("QQQQ2").p2_sort()
    assert Hand("32T3K").best_possible_type() == (2, 1, 1, 1)
    assert Hand("T55J5").best_possible_type() == (4, 1)
    assert Hand("KTJJT").best_possible_type() == (4, 1)
    assert Hand("QQQJA").best_possible_type() == (4, 1)
    assert Hand("JJJJJ").best_possible_type() == (5,)
    assert Hand("1122J").best_possible_type() == (3, 2)


def test_part_2():
    assert part_2(EXAMPLE_1) == 5905
