from day19 import *

EXAMPLE_1 = """
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


def test_parse_input():
    rule_map, parts = parse_input(EXAMPLE_1)

    assert len(rule_map) == 11
    """px{a<2006:qkq,m>2090:A,rfg}"""
    assert rule_map["px"] == WorkFlow(
        label="px",
        rules=[
            Rule(category="a", benchmark=2006, op=operator.lt, result=Goto("qkq")),
            Rule(category="m", benchmark=2090, op=operator.gt, result=Approve()),
        ],
        fallback=Goto("rfg"),
    )


def test_part_1():
    assert part_1(EXAMPLE_1) == 19114
