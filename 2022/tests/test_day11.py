from day11 import *

EXAMPLE_1 = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


def test_parse_monkey():
    test_monkey = """
    Monkey 0:
      Starting items: 64
      Operation: new = old * 7
      Test: divisible by 13
        If true: throw to monkey 1
        If false: throw to monkey 3
    """.lstrip()

    assert parse_monkey(test_monkey) == Monkey(
        index=0, items=[64], operation="old * 7", test_modulo=13, throw_to=(3, 1)
    )

    assert parse_monkey(test_monkey).eval_condition(2) == 14


def test_simulate():
    monkeys = parse_input(EXAMPLE_1)
    simulate(monkeys, is_part_2=False)

    items = [monkey.items for monkey in monkeys]
    assert items == [[20, 23, 27, 26], [2080, 25, 167, 207, 401, 1046], [], []]


def test_part_1():
    assert part_1(EXAMPLE_1) == 10605


def test_part_2():
    assert part_2(EXAMPLE_1) == 2713310158
