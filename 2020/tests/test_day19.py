from day19 import *

MY_SAMPLE_1 = """
0: 1 2
1: "a"
2: "b"

a
b
ab
abb
"""

SAMPLE_0 = """
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

aab
aba
abb
acc
aaa
bbb
"""

SAMPLE_1 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

REPLACE_EXAMPLE = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""

A = '"a"'
B = '"b"'


def test_parse_input():
    rules, messages = parse_input(SAMPLE_1)

    assert rules == {
        0: "4 1 5",
        1: "2 3 | 3 2",
        2: "4 4 | 5 5",
        3: "4 5 | 5 4",
        4: '"a"',
        5: '"b"',
    }

    assert list(messages) == [
        "ababbb",
        "bababa",
        "abbbab",
        "aaabbb",
        "aaaabbb",
    ]


def test_part_1():
    assert part_1(MY_SAMPLE_1) == 1
    assert part_1(SAMPLE_0) == 2
    assert part_1(SAMPLE_1) == 2


def test_replace_8():
    assert replace_8("a", depth=3) == "((a)|(aa)|(aaa))"


def test_replace_411():
    assert replace_11("a", "b", depth=3) == "((ab)|(aabb)|(aaabbb))"


def test_part_2():
    assert part_1(REPLACE_EXAMPLE) == 3
    assert part_2(REPLACE_EXAMPLE) == 12


def test_regression():
    assert part_1(lib.get_input(19)) == 285
    assert part_2(lib.get_input(19)) == 412
