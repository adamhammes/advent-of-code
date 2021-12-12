from day12 import *

EXAMPLE_1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

EXAMPLE_2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""


def test_parse_input():
    caves = parse_input(EXAMPLE_1)
    assert len(caves) == 6

    assert Cave("b") in caves[Cave("A")]
    assert Cave("A") in caves[Cave("b")]


def test_explore_caves():
    paths_1 = explore_caves(parse_input(EXAMPLE_1), 1)
    assert len(paths_1) == 10

    paths_2 = explore_caves(parse_input(EXAMPLE_2), 1)
    assert len(paths_2) == 19


def test_part_2():
    assert part_2(EXAMPLE_1) == 36
    assert part_2(EXAMPLE_2) == 103
