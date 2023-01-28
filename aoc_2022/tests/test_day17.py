from day17 import *

EXAMPLE = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""


def test_part_1():
    assert part_1(EXAMPLE) == 3068


# def test_part_2():
#     for i in range(1, 10):
#         iterations = i * 2738 * 2
#         print(part_1(actual, iterations))
