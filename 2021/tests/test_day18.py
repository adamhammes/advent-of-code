from day18 import *

EXAMPLE_1 = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""


def test_parse_input():
    num = parse_number("[[3,4],5]")
    assert num == Number(
        left=Number(
            left=Number(value=3),
            right=Number(value=4),
        ),
        right=Number(value=5),
    )

    assert num.left.parent == num


explosion_test_cases = {
    "[[[[[9,8],1],2],3],4]": "[[[[0,9],2],3],4]",
    "[7,[6,[5,[4,[3,2]]]]]": "[7,[6,[5,[7,0]]]]",
    "[[6,[5,[4,[3,2]]]],1]": "[[6,[5,[7,0]]],3]",
    "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]": "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
    "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]": "[[3,[2,[8,0]]],[9,[5,[7,0]]]]",
}


def test_explode():
    assert not parse_number("[[3,4],5]").explode()

    for before, after in explosion_test_cases.items():
        num = parse_number(before)
        assert num.explode()
        assert num == parse_number(after)


def test_traver():
    traversed = parse_number("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").traverse()
    assert list(n.value for n in traversed) == [0, 7, 4, 7, 8, 6, 0, 8, 1]


def test_split():
    assert not parse_number("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").split()

    n = parse_number("[[[[0,7],4],[15,[0,13]]],[1,1]]")
    assert n.split()
    assert n == parse_number("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")


def test_add():
    n1 = parse_number("[[[[4,3],4],4],[7,[[8,4],9]]]")
    n2 = parse_number("[1,1]")

    assert n1.add(n2) == parse_number("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")

    n1 = parse_number("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
    n2 = parse_number("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
    assert n1.add(n2) == parse_number(
        "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"
    )


def test_n():
    n = parse_number(
        "[[[[5,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],[[[5,[2,8]],4],[5,[[9,9],0]]]]"
    )
    n.explode()


def test_part_1():
    assert part_1(EXAMPLE_1) == 4140


def test_part_2():
    assert part_2(EXAMPLE_1) == 3993
