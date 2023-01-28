from day20 import *

EXAMPLE_4x4 = """
Tile 2311:
..
##

Tile 1951:
#.
#.

Tile 1171:
##
#.

Tile 1427:
##
.#
"""

SINGLE_10 = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###
"""

SAMPLE_1 = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""


def test_parser():
    tiles = parse_input(EXAMPLE_4x4)

    assert len(tiles) == 4
    assert [tile.tile_id for tile in tiles] == [2311, 1951, 1171, 1427]

    assert tiles[-1].pixels == ((True, True), (False, True))


def test_edges():
    tile = parse_input(SINGLE_10)[-1]
    edges = tile.edges()

    assert len(edges) == 8
    assert all(len(edge) == 10 for edge in edges)

    # ..##.#..#.
    top = (False, False, True, True, False, True, False, False, True, False)
    assert top in edges
    assert tuple(reversed(top)) in edges


def test_flip():
    tile = parse_input(EXAMPLE_4x4)[-1]

    flipped = tile.flip()
    assert tile.tile_id == flipped.tile_id
    assert flipped.pixels == ((False, True), (True, True))
    assert set(tile.edges()) == set(flipped.edges())
    assert tile == tile.flip().flip()


def test_rotate():
    tile = parse_input(EXAMPLE_4x4)[-1]
    assert tile.pixels == ((True, True), (False, True))

    rotated = tile.rotate()
    assert tile.tile_id == rotated.tile_id
    assert rotated.pixels == ((False, True), (True, True))
    assert set(tile.edges()) == set(rotated.edges())

    assert tile.rotate(4) == tile


def test_part_1():
    assert part_1(SAMPLE_1) == 20899048083289
