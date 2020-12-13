from day13 import *
import lib

EASY = """
1
7,13
""".strip()

SAMPLE_1 = """
939
7,13,x,x,59,x,31,19
""".strip()

SAMPLE_2 = """
1
17,x,13,19
""".strip()


def test_regressions():
    assert part_1(lib.get_input(13)) == 1895
    assert part_2(lib.get_input(13)) == 840493039281088


def test_part_1():
    assert part_1(SAMPLE_1) == 295


def test_part_2():
    assert part_2(EASY) == 77
    assert part_2(SAMPLE_1) == 1068781
    assert part_2(SAMPLE_2) == 3417
