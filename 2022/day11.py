import dataclasses
import math
import re

import lib


def extract_ints(line: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", line)))


@dataclasses.dataclass
class Monkey:
    index: int
    items: list[int]
    operation: str
    test_modulo: int
    throw_to: tuple[int, int]
    activity_level: int = 0

    def eval_condition(self, old: int):
        return eval(self.operation, {}, {"old": old})


def parse_monkey(monkey_raw: str) -> Monkey:
    lines = monkey_raw.splitlines()

    index = extract_ints(lines[0])[0]
    starting_items = extract_ints(lines[1])
    operation = lines[2].split("new = ")[1]
    test_modulo = extract_ints(lines[3])[0]
    throw_to_success = extract_ints(lines[4])[0]
    throw_to_failure = extract_ints(lines[5])[0]

    return Monkey(
        index,
        starting_items,
        operation,
        test_modulo,
        (throw_to_failure, throw_to_success),
    )


def parse_input(raw: str) -> list[Monkey]:
    raw_monkeys = raw.strip().split("\n\n")
    return list(map(parse_monkey, raw_monkeys))


def simulate(monkeys: list[Monkey], is_part_2: bool):
    modulo_key = math.lcm(*[m.test_modulo for m in monkeys])

    for monkey in monkeys:
        for item in monkey.items:
            monkey.activity_level += 1
            adjusted_by_operation = monkey.eval_condition(item)

            adjusted_by_relief = adjusted_by_operation % modulo_key
            if is_part_2:
                adjusted_by_relief = adjusted_by_relief % modulo_key
            else:
                adjusted_by_relief //= 3

            is_divisible = adjusted_by_relief % monkey.test_modulo == 0
            throw_to = monkeys[monkey.throw_to[is_divisible]]

            throw_to.items.append(adjusted_by_relief)

        monkey.items = []


def part_1(raw: str):
    monkeys = parse_input(raw)

    for i in range(20):
        simulate(monkeys, False)

    monkeys.sort(key=lambda m: m.activity_level, reverse=True)

    a1, a2 = monkeys[0].activity_level, monkeys[1].activity_level
    return a1 * a2


def part_2(raw: str):
    monkeys = parse_input(raw)

    for i in range(10000):
        simulate(monkeys, True)

    monkeys.sort(key=lambda m: m.activity_level, reverse=True)

    a1, a2 = monkeys[0].activity_level, monkeys[1].activity_level
    return a1 * a2


if __name__ == "__main__":
    print(part_1(lib.get_input(11)))
    print(part_2(lib.get_input(11)))
