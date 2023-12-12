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


def test_guesses():
    springs = parse_input(EXAMPLE_1)
    records = {guess.record for guess in springs[0].guesses()}

    assert records == {
        "....###",
        "#...###",
        ".#..###",
        "##..###",
        "..#.###",
        "#.#.###",
        ".##.###",
        "###.###",
    }


def test_is_coherent():
    assert Spring("#.#.###", (1, 1, 3)).is_coherent()
    assert not Spring("#.#####", (1, 1, 3)).is_coherent()

    assert Spring(record=".###.##....#", groups=(3, 2, 1)).is_coherent()

    assert Spring(record="???.###", groups=(1, 1, 3)).num_coherent() == 1
    assert Spring(record="?###????????", groups=(3, 2, 1)).num_coherent() == 10


def test_part_1():
    assert part_1(EXAMPLE_1) == 21
