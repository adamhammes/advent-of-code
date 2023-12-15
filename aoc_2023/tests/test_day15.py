import pytest

from day15 import *

EXAMPLE_1 = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""


@pytest.mark.parametrize("string,expected", [("HASH", 52), ("rn=1", 30), ("cm-", 253)])
def test_HASH(string: str, expected: int):
    assert HASH(string) == expected


def test_parse_input():
    i0 = Instruction("rn=1")
    assert i0.string == "rn=1"
    assert i0.label == "rn"
    assert i0.operation == "="
    assert i0.focal_length == 1

    parse_input(EXAMPLE_1)


def test_part_1():
    assert part_1(EXAMPLE_1) == 1320


def test_part_2():
    assert part_2(EXAMPLE_1) == 145
