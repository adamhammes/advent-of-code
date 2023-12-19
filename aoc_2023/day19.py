import dataclasses
import operator
import typing

import lib


@dataclasses.dataclass
class Reject:
    pass


@dataclasses.dataclass
class Approve:
    pass


@dataclasses.dataclass
class Goto:
    destination: str


RuleResult = Reject | Approve | Goto


def result_from_str(raw: str) -> RuleResult:
    match raw:
        case "A":
            return Approve()
        case "R":
            return Reject()
        case _:
            return Goto(raw)


class Part(typing.NamedTuple):
    x: int
    m: int
    a: int
    s: int

    def rating(self) -> int:
        return sum(self)


class Rule(typing.NamedTuple):
    category: str
    benchmark: int
    op: typing.Callable[[int, int], bool]
    result: RuleResult

    def matches(self, part: Part) -> bool:
        return self.op(part._asdict()[self.category], self.benchmark)


class WorkFlow(typing.NamedTuple):
    label: str
    rules: list[Rule]
    fallback: RuleResult

    def process(self, part: Part) -> RuleResult:
        for rule in self.rules:
            if rule.matches(part):
                return rule.result

        return self.fallback


def parse_rule_set(line: str) -> WorkFlow:
    """px{a<2006:qkq,m>2090:A,rfg}"""
    label = line.split("{")[0]

    rule_section = line.split("{")[1]
    raw_rules = rule_section.split(",")

    rules = []
    for raw_rule in raw_rules[:-1]:
        category = raw_rule[0]
        op = {">": operator.gt, "<": operator.lt}[raw_rule[1]]
        benchmark = lib.extract_ints(raw_rule)[0]
        result = result_from_str(raw_rule.split(":")[1])
        rules.append(Rule(category=category, op=op, benchmark=benchmark, result=result))

    fallback = result_from_str(raw_rules[-1][:-1])

    return WorkFlow(label, rules, fallback)


def parse_input(raw: str) -> tuple[dict[str, WorkFlow], list[Part]]:
    raw_rules, raw_parts = raw.strip().split("\n\n")

    rules = map(parse_rule_set, raw_rules.splitlines())
    rule_map = {rule.label: rule for rule in rules}

    parts = []
    for line in raw_parts.splitlines():
        ints = lib.extract_ints(line)
        parts.append(Part(*ints[:4]))

    return rule_map, parts


def process_part(rule_map: dict[str, WorkFlow], part: Part) -> bool:
    current_workflow = rule_map["in"]

    while True:
        result = current_workflow.process(part)

        match result:
            case Approve():
                return True
            case Reject():
                return False
            case Goto(destination):
                current_workflow = rule_map[destination]


def part_1(raw: str) -> int:
    rule_map, parts = parse_input(raw)

    total = 0
    for part in parts:
        if process_part(rule_map, part):
            total += part.rating()

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(19)))
