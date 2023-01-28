from day10 import *

SMALL_INPUT = """
16
10
15
5
1
11
7
19
6
12
4
""".strip()

MEDIUM_INPUT = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip()


def test():
    assert part_1(SMALL_INPUT) == 7 * 5
    assert part_1(MEDIUM_INPUT) == 22 * 10

    assert part_2(SMALL_INPUT) == 8
    assert part_2(MEDIUM_INPUT) == 19208
