import lib

from day01 import *

EXAMPLE_1 = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_part_1():
    assert part_1(EXAMPLE_1) == 24000
    assert part_1(lib.get_input(1)) == 69883


def test_part_2():
    assert part_2(EXAMPLE_1) == 45000
    assert part_2(lib.get_input(1)) == 207576
