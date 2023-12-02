from day02 import *

EXAMPLE = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def test_from_random_sample():
    assert BagContents.from_random_sample("7 green, 4 blue, 3 red ") == BagContents(
        red=3, blue=4, green=7
    )

    assert BagContents.from_random_sample("7 green, 2 green") == BagContents(
        red=0, blue=0, green=7
    )

    assert BagContents.from_random_sample("2 green, 7 green") == BagContents(
        red=0, blue=0, green=7
    )


def test_part_1():
    assert part_1(EXAMPLE) == 8


def test_part_2():
    assert part_2(EXAMPLE) == 2286
