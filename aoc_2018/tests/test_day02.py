from day02 import *

EXAMPLE_1 = """
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""

EXAMPLE_2 = """
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""


def test_part_1():
    assert part_1(EXAMPLE_1) == 12


def test_part_2():
    assert part_2(EXAMPLE_2) == "fgij"
