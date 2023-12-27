import dataclasses
import math
import typing

import lib

Category = typing.Literal["x", "m", "a", "s"]
Op = typing.Literal[">", "<"]


class Part(typing.NamedTuple):
    x: int
    m: int
    a: int
    s: int

    def rating(self) -> int:
        return sum(self)


@dataclasses.dataclass
class Range:
    start: int
    end: int

    def __len__(self) -> int:
        return self.end - self.start + 1

    def __contains__(self, i: int) -> bool:
        return self.start <= i <= self.end

    def split(self, benchmark: int, op: Op) -> tuple["Range", "Range"]:
        if op == "<":
            matching = Range(self.start, benchmark - 1)
            not_matching = Range(benchmark, self.end)
        else:
            matching = Range(benchmark + 1, self.end)
            not_matching = Range(self.start, benchmark)

        return matching, not_matching


class Ranges(typing.TypedDict):
    x: Range
    m: Range
    a: Range
    s: Range


@dataclasses.dataclass
class Domain:
    ranges: Ranges

    def size(self) -> int:
        return math.prod(map(len, self.ranges.values()))

    def contains_part(self, p: Part) -> bool:
        x = self.ranges["x"]
        m = self.ranges["m"]
        a = self.ranges["a"]
        s = self.ranges["s"]

        return p.x in x and p.m in m and p.a in a and p.s in s

    @staticmethod
    def new():
        return Domain(
            {
                "x": Range(1, 4000),
                "m": Range(1, 4000),
                "a": Range(1, 4000),
                "s": Range(1, 4000),
            }
        )


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


class Rule(typing.NamedTuple):
    category: Category
    benchmark: int
    op: Op
    result: RuleResult

    def apply(self, d: Domain) -> list[Domain]:
        range_to_work_on: Range = d.ranges[self.category]
        matched, not_matched = range_to_work_on.split(self.benchmark, self.op)

        d_matched = d.ranges.copy()
        d_matched[self.category] = matched

        d_not_matched = d.ranges.copy()
        d_not_matched[self.category] = not_matched
        return [Domain(d_matched), Domain(d_not_matched)]


class WorkFlow(typing.NamedTuple):
    label: str
    rules: list[Rule]
    fallback: RuleResult


def parse_rule_set(line: str) -> WorkFlow:
    """px{a<2006:qkq,m>2090:A,rfg}"""
    line = line.strip()
    label = line.split("{")[0]

    rule_section = line.split("{")[1]
    raw_rules = rule_section.split(",")

    rules = []
    for raw_rule in raw_rules[:-1]:
        category = raw_rule[0]
        op = raw_rule[1]
        benchmark = lib.extract_ints(raw_rule)[0]
        result = result_from_str(raw_rule.split(":")[1])
        rules.append(Rule(category=category, op=op, benchmark=benchmark, result=result))

    fallback = result_from_str(raw_rules[-1][:-1])

    return WorkFlow(label, rules, fallback)


def process(
    rule_map: dict[str, WorkFlow], domain: Domain, current_label="in"
) -> list[Domain]:
    current_workflow = rule_map[current_label]

    domains = []

    for rule in current_workflow.rules:
        accepted, rejected = rule.apply(domain)

        match rule.result:
            case Approve():
                domains.append(accepted)
            case Reject():
                pass
            case Goto(destination):
                domains += process(rule_map, accepted, destination)

        domain = rejected

    match current_workflow.fallback:
        case Approve():
            domains.append(domain)
            return domains
        case Reject():
            return domains
        case Goto(destination):
            return domains + process(rule_map, domain, destination)


def parse_input(raw: str) -> tuple[dict[str, WorkFlow], list[Part]]:
    raw_rules, raw_parts = raw.strip().split("\n\n")

    rules = map(parse_rule_set, raw_rules.splitlines())
    rule_map = {rule.label: rule for rule in rules}

    parts = []
    for line in raw_parts.splitlines():
        ints = lib.extract_ints(line)
        parts.append(Part(*ints[:4]))

    return rule_map, parts


def part_1(raw: str) -> int:
    rules, parts = parse_input(raw)
    ds = process(rules, Domain.new(), "in")
    return sum(p.rating() for p in parts if any(d.contains_part(p) for d in ds))


def part_2(raw: str) -> int:
    rules, parts = parse_input(raw)

    ds = process(rules, Domain.new(), "in")
    return sum(map(Domain.size, ds))


if __name__ == "__main__":
    print(part_1(lib.get_input(19)))
    print(part_2(lib.get_input(19)))
