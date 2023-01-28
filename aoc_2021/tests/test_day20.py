from day20 import *

SAMPLE_INPUT = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


def test_parse_input():
    image = parse_input(SAMPLE_INPUT)
    assert len(image.enhance) == 512

    assert len(image.solved_pixels) == 25
    assert image.solved_pixels[(0, Point(0, 0))] == PixelState.On
    assert (0, Point(-1, -1)) not in image.solved_pixels


def test_bits_to_int():
    assert bits_to_int([False, True, False, False, True]) == 9


def test_the_thing():
    image = parse_input(SAMPLE_INPUT)
    answer = image.iterate(1)

    on_pixels = list(sorted(p for p, s in answer.items() if s == PixelState.On))
    assert len(on_pixels) == 24

    assert Point(0, 0) not in on_pixels
    assert Point(-1, 0) in on_pixels
    assert Point(-1, 1) in on_pixels
    assert Point(0, -1) in on_pixels
    assert Point(6, 6) not in on_pixels

    answer2 = image.iterate(2)
    on_pixels2 = list(sorted(p for p, s in answer2.items() if s == PixelState.On))
    assert len(on_pixels2) == 35


def test_answers():
    assert part_1(SAMPLE_INPUT) == 5249
    assert part_2(SAMPLE_INPUT) == 15741
