from day19 import *

EXAMPLE_1 = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


def test_can_match():
    patterns = tuple("r, wr, b, g, bwu, rb, gb, br".split(", "))

    assert can_match(patterns, "brwrr") == 2
    assert not can_match(patterns, "bbrgwb")


def test_part_1():
    assert part_1(EXAMPLE_1) == 6


def test_part_2():
    assert part_2(EXAMPLE_1) == 16
