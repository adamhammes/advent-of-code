from day03 import *

EXAMPLE_1 = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_part_1():
    assert part_1(EXAMPLE_1) == 157
    assert part_1(lib.get_input(3)) == 7878


def test_part_2():
    assert part_2(EXAMPLE_1) == 70
