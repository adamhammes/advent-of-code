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

    visited_dd = State(
        distances, rates, num_agents=2, time=(30, 30), current_positions=("AA", "AA")
    ).open("DD", 0)

    assert visited_dd == State(
        distances,
        rates,
        num_agents=2,
        time=(28, 30),
        current_positions=("DD", "AA"),
        opened_at={"DD": 28},
    )

    visited_dd_bb = visited_dd.open("BB", 0)
    assert visited_dd_bb == State(
        distances,
        rates,
        num_agents=2,
        time=(25, 30),
        current_positions=("BB", "AA"),
        opened_at={"DD": 28, "BB": 25},
    )

    visited_dd_bb_jj = visited_dd_bb.open("JJ", 1)
    assert visited_dd_bb_jj == State(
        distances,
        rates,
        num_agents=2,
        time=(25, 27),
        current_positions=("BB", "JJ"),
        opened_at={"DD": 28, "BB": 25, "JJ": 27},
    )


def test_possible_moves():
    distances, rates = parse_input(EXAMPLE)

    state = State(
        distances, rates, num_agents=2, time=(30, 30), current_positions=("AA", "AA")
    )
    moves = state.possible_moves()

    assert len(moves) == 12

    assert set(m.current_positions[0] for m in moves) == {
        "AA",
        "BB",
        "CC",
        "DD",
        "EE",
        "HH",
        "JJ",
    }


def test_state_flow():
    distances, rates = parse_input(EXAMPLE)
    state = State(distances, rates, time=(30,), num_agents=1, current_positions=("AA",))

    assert state.open("BB", 0).flow() == 364
    assert state.open("BB", 0).open("CC", 0).flow() == 364 + 52


def test_fairy_tale_score():
    distances, rates = parse_input(EXAMPLE)
    state = State(
        distances, rates, time=(30, 15), num_agents=2, current_positions=("AA", "AA")
    )

    s = state.fairy_tale_score()
    assert s == (13 + 2 + 20 + 3 + 22 + 21) * 30


def test_part_1():
    assert part_1(EXAMPLE) == 1651


def test_part_2():
    assert part_2(EXAMPLE) == 1707
