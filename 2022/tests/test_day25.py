import pytest

from day25 import *

EXAMPLE_1 = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
"""

snafu_scenarios = [
    (1, "1"),
    (2, "2"),
    (3, "1="),
    (4, "1-"),
    (5, "10"),
    (6, "11"),
    (7, "12"),
    (8, "2="),
    (9, "2-"),
    (10, "20"),
    (15, "1=0"),
    (20, "1-0"),
    (2022, "1=11-2"),
    (12345, "1-0---0"),
    (314159265, "1121-1110-1=0"),
    (4890, "2=-1=0"),
]


@pytest.mark.parametrize("decimal_number,snafu_number", snafu_scenarios)
def test_to_snafu(decimal_number, snafu_number):
    assert to_snafu(decimal_number) == snafu_number


@pytest.mark.parametrize("decimal_number,snafu_number", snafu_scenarios)
def test_from_snafu(decimal_number, snafu_number):
    assert from_snafu(snafu_number) == decimal_number


def test_part_1():
    assert part_1(EXAMPLE_1) == "2=-1=0"
