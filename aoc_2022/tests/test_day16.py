from day16 import *

EXAMPLE = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


def test_state_visit():
    distances, rates = parse_input(EXAMPLE)

    visited_dd = State(distances, rates, 30).open("DD")
    assert visited_dd == State(
        distances, rates, time=28, current_position="DD", opened_at={"DD": 28}
    )

    visited_dd_bb = visited_dd.open("BB")
    assert visited_dd_bb == State(
        distances,
        rates,
        time=25,
        current_position="BB",
        opened_at={"DD": 28, "BB": 25},
    )


def test_possible_moves():
    distances, rates = parse_input(EXAMPLE)

    state = State(distances, rates, time=30)
    moves = state.possible_moves()

    assert len(moves) == 6

    assert set(m.current_position for m in moves) == {
        "BB",
        "CC",
        "DD",
        "EE",
        "HH",
        "JJ",
    }


def test_state_flow():
    distances, rates = parse_input(EXAMPLE)
    state = State(distances, rates, time=30)

    assert state.open("BB").flow() == 364
    assert state.open("BB").open("CC").flow() == 364 + 52


def test_part_1():
    assert part_1(EXAMPLE) == 1651
