from day06 import *

EXAMPLE_1 = "3,4,3,1,2"


def test_parse_input():
    assert parse_input(EXAMPLE_1) == {3: 2, 4: 1, 1: 1, 2: 1}


def test_simulate_day():
    eels = parse_input(EXAMPLE_1)
    assert simulate_day(simulate_day(eels)) == {1: 2, 2: 1, 6: 1, 0: 1, 8: 1}


def test_run_simulation():
    assert run_simulation(EXAMPLE_1, 18) == 26
    assert run_simulation(EXAMPLE_1, 80) == 5934
