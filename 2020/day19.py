import re
import typing as t

import lib


def parse_input(raw: str) -> t.Tuple[t.Dict[int, str], t.Tuple[str]]:
    raw_rules, raw_messages = raw.strip().split("\n\n")

    rules = {}
    for line in raw_rules.splitlines():
        split = line.split(":")
        key, value = int(split[0]), split[1].strip()
        rules[key] = value

    messages = tuple(raw_messages.splitlines())
    return rules, messages


def replace_8(forty_two: str, depth=5) -> str:
    repetitions = []
    for i in range(1, depth + 1):
        repeated = "(" + "".join([forty_two] * i) + ")"
        repetitions.append(repeated)

    return "(" + "|".join(repetitions) + ")"


def replace_11(forty_two: str, thirty_one: str, depth=5) -> str:
    repetitions = []
    for i in range(1, depth + 1):
        repeated = "(" + "".join([f"({forty_two})"] * i + [f"({thirty_one})"] * i) + ")"
        repetitions.append(repeated)

    return "(" + "|".join(repetitions) + ")"


def _regex_recursive(all_rules: t.Dict[int, str], rule: str, solved) -> str:
    if rule[0] == '"' and rule[-1] == '"':
        return rule[1:-1]
    elif rule.isnumeric():
        if int(rule) in solved:
            return solved[int(rule)]
        return _regex_recursive(all_rules, all_rules[int(rule)], solved)
    elif "|" in rule:
        alternatives = rule.split(" | ")
        inner_expression = "|".join(
            f"({_regex_recursive(all_rules, alternative, solved)})"
            for alternative in alternatives
        )
        return f"({inner_expression})"
    else:
        return "".join(
            _regex_recursive(all_rules, sub_rule, solved) for sub_rule in rule.split()
        )


def convert_to_regex(
    all_rules: t.Dict[int, str], rule: str, solved=None
) -> t.Pattern[str]:
    if solved is None:
        solved = {}

    return re.compile(_regex_recursive(all_rules, rule, solved))


def part_1(raw: str):
    rules, messages = parse_input(raw)
    principal_rule = convert_to_regex(rules, rules[0])
    return sum(bool(principal_rule.fullmatch(message)) for message in messages)


def part_2(raw: str) -> int:
    rules, messages = parse_input(raw)
    forty_two = convert_to_regex(rules, rules[42]).pattern
    thirty_one = convert_to_regex(rules, rules[31]).pattern

    solved = {8: replace_8(forty_two), 11: replace_11(forty_two, thirty_one)}

    principal_rule = convert_to_regex(rules, rules[0], solved)
    return sum(bool(principal_rule.fullmatch(message)) for message in messages)


if __name__ == "__main__":
    print(part_1(lib.get_input(19)))
    print(part_2(lib.get_input(19)))
