from day03 import part_1, part_2

EXAMPLE_1 = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()


def test_example_1():
    assert part_1(EXAMPLE_1) == 198
    assert part_2(EXAMPLE_1) == 230
