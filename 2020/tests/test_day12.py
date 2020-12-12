from day12 import *

SAMPLE = """
F10
N3
F7
R90
F11
""".strip()


def test_movements():
    assert ShipState().move("N5").position == (0, 5)
    assert ShipState().move("E5").position == (5, 0)
    assert ShipState().move("S5").position == (0, -5)
    assert ShipState().move("W5").position == (-5, 0)

    assert ShipState().move("L90").orientation == Orientation.North


def test_sample():
    expected_positions = [
        (10, 0),
        (10, 3),
        (17, 3),
        (17, 3),
        (17, -8),
    ]

    ship = ShipState()
    for line, expected_position in zip(SAMPLE.splitlines(), expected_positions):
        ship.move(line)
        print(ship.orientation)
        assert expected_position == ship.position


def test_regression():
    assert part_1(SAMPLE) == 25
    assert part_2(SAMPLE) == 286

    assert part_1(get_input()) == 2280
    assert part_2(get_input()) == 38693


def test_waypoint_rotation():
    ship = ShipState()
    ship.waypoint = Point(0, 5)

    ship.move_waypoint("R90")
    assert ship.waypoint == (5, 0)
    ship.move_waypoint("L90")
    assert ship.waypoint == (0, 5)

    ship.move_waypoint("R180")
    assert ship.waypoint == (0, -5)
    ship.move_waypoint("L180")
    assert ship.waypoint == (0, 5)

    ship.move_waypoint("R270")
    assert ship.waypoint == (-5, 0)
    ship.move_waypoint("L270")
    assert ship.waypoint == (0, 5)


def test_waypoint():
    ship = ShipState()

    ship.move_waypoint("F10")
    assert ship.position == (100, 10)
    assert ship.waypoint == (10, 1)

    ship.move_waypoint("N3")
    assert ship.position == (100, 10)
    assert ship.waypoint == (10, 4)

    ship.move_waypoint("F7")
    assert ship.position == (170, 38)
    assert ship.waypoint == (10, 4)

    ship.move_waypoint("R90")
    assert ship.position == (170, 38)
    assert ship.waypoint == (4, -10)

    ship.move_waypoint("F11")
    assert ship.position == (214, -72)
    assert ship.waypoint == (4, -10)
