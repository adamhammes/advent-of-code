from day13 import *

EXAMPLE_1 = """
[1,1,3,1,1]
[1,1,5,1,1]
"""


def test_compare_simple_lists():
    left, right = parse_input(EXAMPLE_1)[0]
    assert compare(left, right) > 0


EXAMPLE_2 = """
[[1],[2,3,4]]
[[1],4]
"""


def test_mixed_types():
    left, right = parse_input(EXAMPLE_2)[0]
    assert compare(left, right) > 0


EXAMPLE_3 = """
[9]
[[8,7,6]]
"""


def test_different_lengths():
    left, right = parse_input(EXAMPLE_3)[0]

    assert compare(left, right) < 0


EXAMPLE_4 = """
[[4,4],4,4]
[[4,4],4,4,4]
"""


def test_mixed_lengths_true():
    left, right = parse_input(EXAMPLE_4)[0]
    assert compare(left, right) > 0


EXAMPLE_5 = """
[7,7,7,7]
[7,7,7]
"""


def test_mixed_lengths_false():
    left, right = parse_input(EXAMPLE_5)[0]
    assert compare(left, right) < 0


EXAMPLE_6 = """
[]
[3]
"""


def test_example_6():
    left, right = parse_input(EXAMPLE_6)[0]
    assert compare(left, right) > 0


EXAMPLE_7 = """
[[[]]]
[[]]
"""


def test_example_7():
    left, right = parse_input(EXAMPLE_7)[0]
    assert compare(left, right) < 0


EXAMPLE_8 = """
[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def test_example_8():
    left, right = parse_input(EXAMPLE_8)[0]
    assert compare(left, right) < 0
