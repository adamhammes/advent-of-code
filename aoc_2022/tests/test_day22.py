from day22 import *

EXAMPLE = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""

"""
     1111 2222
     1111 2222
     1111 2222
     
     3333
     3333
     3333
    
4444 5555
4444 5555
4444 5555

6666
6666
6666

"""

EXAMPLE_2 = """
    ...#.#..
    .#......
    #.....#.
    ........
    ...#
    #...
    ....
    ..#.
..#....#
........
.....#..
........
#...
..#.
....
....

10R5L5R10L4R5L5
"""


def test_parse_grid():
    grid, _ = parse_input(EXAMPLE)
    fifth_row = grid[4]
    assert fifth_row[:4] == [Contents.Air, Contents.Air, Contents.Air, Contents.Wall]


def test_edge_size():
    grove = parse_input(EXAMPLE_2)
    assert grove.edge_size == 4


def test_square_id():
    grove = parse_input(EXAMPLE_2)

    assert grove.square_id(Point(5, 3)) == 1

    unique_ids = set()
    for y, line in enumerate(grove.grid):
        for x, contents in enumerate(line):
            if contents != Contents.Empty:
                unique_ids.add(grove.square_id(Point(x, y)))

    assert unique_ids == {1, 2, 3, 4, 5, 6}


def test_initial_position():
    grove = parse_input(EXAMPLE_2)
    assert grove.current_position == Point(4, 0)


def test_peek_step():
    grove = parse_input(EXAMPLE_2)

    assert grove.peek_step(Dir.South) == (Point(4, 1), Dir.South)
    assert grove.peek_step(Dir.East) == (Point(5, 0), Dir.East)

    assert grove.peek_step(Dir.North) == (Point(0, 12), Dir.East)
    grove.current_position = Point(5, 0)
    assert grove.peek_step(Dir.North) == (Point(0, 13), Dir.East)

    grove.current_position = Point(4, 1)
    assert grove.peek_step(Dir.West) == (Point(0, 11), Dir.East)


def test_move():
    grove = parse_input(EXAMPLE_2)
    assert grove.do_thing() == 10_006
