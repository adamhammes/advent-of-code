from day18 import *


def test_part_2():
    assert shunting_yard("2 * 3 + (4 * 5)") == 26
    assert shunting_yard("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 ") == 13632


def test_part_2():
    assert shunting_yard("1") == 1
    assert shunting_yard("(1)") == 1
    assert shunting_yard("1 + 1") == 2
    assert shunting_yard("2 * 2") == 4
    assert shunting_yard("2 + 3 * 4") == 20
    assert shunting_yard("2 * 3 + 4") == 14
    assert shunting_yard("(2 * 3) + 4") == 10
    assert shunting_yard("2 * 3 + (4 * 5)") == 46
    assert shunting_yard("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert shunting_yard("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert shunting_yard("1 * 4 + 2 + 2 * 2") == 16
