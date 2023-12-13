import pytest

from day12 import *

EXAMPLE_1 = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


def test_parse_input():
    springs = parse_input(EXAMPLE_1)

    assert springs[0] == Spring(record="???.###", groups=(1, 1, 3))
    assert springs[-1] == Spring(record="?###????????", groups=(3, 2, 1))


@pytest.mark.parametrize(
    "record,group_size,expected",
    [
        (".....", 1, []),
        ("#..", 1, [".."]),
        (".#..", 1, [".."]),
        (".##...", 2, ["..."]),
        ("####", 3, []),
        ("?###", 3, [""]),
        ("??...", 1, ["...", "...."]),
        ("??", 1, [".", ""]),
        ("???", 1, [".", "", ".?"]),
        ("????", 5, []),
        ("?.##", 3, []),
    ],
)
def test_parameterized(record, group_size, expected):
    assert set(possible_placements(record, group_size)) == set(expected)


@pytest.mark.parametrize(
    "record,groups,expected",
    [
        ("???.###", (1, 1, 3), 1),
        (".??..??...?##.", (1, 1, 3), 4),
        ("?###????????", (3, 2, 1), 10),
        (
            "???.###????.###????.###????.###????.###",
            [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3],
            1,
        ),
    ],
)
def test_count(record, groups, expected):
    assert count(record, groups) == expected


def test_part_1():
    assert part_1(EXAMPLE_1) == 21


def test_part_2():
    assert part_2(EXAMPLE_1) == 525152
