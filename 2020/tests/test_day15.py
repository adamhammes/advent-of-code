from day15 import *


def test_examples():
    counter = Counter([0, 3, 6])
    assert counter.say() == 0
    assert counter.say() == 3
    assert counter.say() == 3
    assert counter.say() == 1
    assert counter.say() == 0
    assert counter.say() == 4
    assert counter.say() == 0


def test_part_1():
    assert part_1("1,3,2") == 1


def test_part_2():
    assert part_2("0,3,6") == 175594
