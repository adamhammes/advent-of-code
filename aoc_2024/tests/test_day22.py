from day22 import *

EXAMPLE_1 = """
1
10
100
2024
"""

EXAMPLE_2 = """
1
2
3
2024
"""


def test_evolve():
    assert evolve(123) == 15887950
    assert evolve(15887950) == 16495136


def test_part_1():
    assert part_1(EXAMPLE_1) == 37327623


def test_calculate_window_scores():
    price_list = get_price_list(123, 10)
    scores = calculate_window_scores(price_list)
    assert scores[(-1, -1, 0, 2)] == 6


def test_part_2():
    assert part_2(EXAMPLE_2) == 23
