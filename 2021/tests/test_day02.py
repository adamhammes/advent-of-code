from day02 import part_1, part_2, parse_input

EXAMPLE_1 = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()


def test_example_1():
    assert part_1(parse_input(EXAMPLE_1)) == 150
    assert part_2(parse_input(EXAMPLE_1)) == 900
