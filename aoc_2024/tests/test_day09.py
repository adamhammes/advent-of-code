from day09 import *

EXAMPLE_1 = "2333133121414131402"


def test_parse_input():
    parsed = parse_input(EXAMPLE_1)
    assert print_nodes(parsed) == "00...111...2...333.44.5555.6666.777.888899"


def test_compact_wide():
    e1 = parse_input(EXAMPLE_1)
    compact_wide(e1)
    assert print_nodes(e1).strip(".") == "0099811188827773336446555566"


def test_part_1():
    assert part_1(EXAMPLE_1) == 1928
