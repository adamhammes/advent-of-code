from day22 import *

EXAMPLE_1 = """
1
10
100
2024
"""


def test_evolve():
    assert evolve(123) == 15887950
    assert evolve(15887950) == 16495136


def test_part_1():
    assert part_1(EXAMPLE_1) == 37327623
