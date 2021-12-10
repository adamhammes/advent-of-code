from day10 import *

EXAMPLE_1 = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def test_validate_line():
    assert validate_line("{()()()}") is None
    assert validate_line("<([{}])>") is None
    assert validate_line("[<>({}){}[([])<>]]") is None
    assert validate_line("(((((((((())))))))))") is None

    assert validate_line("{([(<{}[<>[]}>{[]{[(<()>") == "}"
    assert validate_line("[[<[([]))<([[{}[[()]]]") == ")"


def test_part_1():
    assert part_1(EXAMPLE_1) == 26397


def test_complete_line():
    assert complete_line("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"


def test_part_2():
    assert part_2(EXAMPLE_1) == 288957
