from day07 import *

EMPTY_RULE = """
dotted black bags contain no other bags.
"""

SINGLE_RULE = """
bright white bags contain 1 shiny gold bag.
"""

MULTIPLE_RULES = """
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
"""

def test_parser():
    assert parse_line(EMPTY_RULE) == ("dotted black", [])
    assert parse_line(SINGLE_RULE) == ("bright white", [("shiny gold", 1)])
    assert parse_line(MULTIPLE_RULES) == ("shiny gold", [("dark olive", 1), ("vibrant plum", 2)])
