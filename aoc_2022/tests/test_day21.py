from day21 import *

EXAMPLE_1 = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
"""


def test_parse_line():
    root, operation = parse_line("root: pppw + sjmn")
    assert root == "root"
    assert operation == Operation("pppw", "sjmn", "+")

    root, operation = parse_line("dbpl: 5")
    assert root == "dbpl"
    assert operation == 5


def test_part_1():
    assert part_1(EXAMPLE_1) == 152


def test_part_2():
    assert part_2(EXAMPLE_1) == 301
