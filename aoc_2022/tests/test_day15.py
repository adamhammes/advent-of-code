from day15 import *


def test_get_range_at_altitude():
    assert get_range_at_altitude(Point(8, 7), 9, -2) == range(8, 8 + 1)
    assert get_range_at_altitude(Point(8, 7), 9, 0) == range(6, 10 + 1)
    assert get_range_at_altitude(Point(8, 7), 9, 7) == range(-1, 17 + 1)


def test_find_gaps_in_ranges():
    r1 = range(0, 5)
    r2 = range(6, 10)

    assert find_gaps_in_ranges([r1, r2]) == [5]

    r1 = range(0, 10)
    r2 = range(5, 11)
    assert find_gaps_in_ranges([r1, r2]) == []

    r1 = range(0, 2)
    r2 = range(4, 8)
    r3 = range(6, 10)
    r4 = range(13, 15)

    assert find_gaps_in_ranges([r4, r3, r2, r1]) == [2, 3, 10, 11, 12]
