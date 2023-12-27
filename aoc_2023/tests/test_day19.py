from day19 import *

FULL_EXAMPLE = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

EXAMPLE_1 = """
lxb{x>2186:R,A}
"""


def test_split():
    rule = Rule("x", 2186, ">", Reject())
    accepted, rejected = rule.apply(Domain.new())
    print("asdf")


def test_the_thing():
    w = parse_rule_set(EXAMPLE_1)
    assert w == WorkFlow("lxb", [Rule("x", 2186, ">", Reject())], Approve())

    rule_map = {"lxb": w}

    d = process(rule_map, Domain.new(), "lxb")[0]
    assert d == Domain(
        {
            "x": Range(1, 2186),
            "m": Range(1, 4000),
            "a": Range(1, 4000),
            "s": Range(1, 4000),
        }
    )

    assert d.size() == 4000 * 4000 * 4000 * 2186

    print("here")


def test_the_thing_2():
    w = parse_rule_set("lxb{x>2186:A,a>1000:A,R}")
    rule_map = {"lxb": w}

    ds = process(rule_map, Domain.new(), "lxb")

    d1 = 4000 * 4000 * 4000 * (4000 - 2186)
    d2 = 4000 * 4000 * (4000 - 1000) * 2186
    total = sum(map(Domain.size, ds))
    assert total == d1 + d2

    print("here")


def test_part_2():
    assert part_2(FULL_EXAMPLE) == 167409079868000
