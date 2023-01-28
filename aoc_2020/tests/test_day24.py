from day24 import *

SAMPLE_1 = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""


def test_parse_direction():
    directions = "esenee"
    assert parse_directions(directions) == [
        HexDirection.East,
        HexDirection.SouthEast,
        HexDirection.NorthEast,
        HexDirection.East,
    ]


def test_follow_directions():
    directions = parse_directions("esew")
    assert follow_directions(directions) == (0, -1, 1)


def test_part_1():
    assert part_1(SAMPLE_1) == 10


def test_part_2():
    assert part_2(SAMPLE_1) == 2208
