import collections
import dataclasses
import itertools
import re

import lib

Graph = dict[str, list[str]]
FlowRates = dict[str, int]
Distances = dict[tuple[str, str], int]


@dataclasses.dataclass(frozen=True)
class State:
    distances: Distances
    rates: FlowRates
    num_agents: int
    time: tuple[int, ...]
    current_positions: tuple[str, ...]
    opened_at: dict[str, int] = dataclasses.field(default_factory=dict)

    def flow(self) -> int:
        return sum(
            self.rates[valve] * opened_at for valve, opened_at in self.opened_at.items()
        )

    def finger_print(self) -> tuple[frozenset[str], tuple[str, ...]]:
        valves = frozenset(self.opened_at)
        return valves, self.current_positions

    def fairy_tale_score(self) -> int:
        time_remaining = max(self.time)
        return (
            sum(
                time_remaining * rate
                for v, rate in self.rates.items()
                if v not in self.opened_at
            )
            + self.flow()
        )

    def __lt__(self, other):
        return self.flow() < other.flow()

    def open(self, valve: str, agent_index: int) -> "State":
        agent_current_position = self.current_positions[agent_index]
        agent_current_time = self.time[agent_index]

        arrival_time = (
            agent_current_time - self.distances[(agent_current_position, valve)] - 1
        )

        new_positions = list(self.current_positions)
        new_positions[agent_index] = valve

        new_times = list(self.time)
        new_times[agent_index] = arrival_time

        return State(
            distances=self.distances,
            num_agents=self.num_agents,
            rates=self.rates,
            time=tuple(new_times),
            current_positions=tuple(new_positions),
            opened_at=self.opened_at | {valve: arrival_time},
        )

    def possible_moves(self) -> list["State"]:
        moves = []
        for agent_index in range(self.num_agents):
            unvisited_valves = [v for v in self.rates if v not in self.opened_at]
            states = [self.open(valve, agent_index) for valve in unvisited_valves]
            moves += states

        return [state for state in moves if all(t > 0 for t in state.time)]


def parse_input(raw: str) -> (Distances, FlowRates):
    graph: Graph = {}
    rates: FlowRates = {}

    for line in raw.strip().splitlines():
        label = line.split()[1]
        rate = lib.extract_ints(line)[0]

        edges = re.split("valves? ", line)[1].split(", ")

        graph[label] = edges

        if rate:
            rates[label] = rate

    distances = precompute_distances(graph)

    return distances, rates


def find_distance(graph: Graph, n1: str, n2: str) -> int:
    seen = set(n1)
    to_visit = collections.deque([(n1, 0)])

    while to_visit:
        cur_node, distance = to_visit.popleft()

        if cur_node == n2:
            return distance

        for other_node in graph[cur_node]:
            if other_node not in seen:
                to_visit.append((other_node, distance + 1))
                seen.add(other_node)


def precompute_distances(graph: Graph) -> Distances:
    nodes = graph.keys()

    return {
        (n1, n2): find_distance(graph, n1, n2)
        for n1, n2 in itertools.product(nodes, nodes)
        if n1 != n2
    }


def explore(distances: Distances, rates: FlowRates, time: int, num_agents: int) -> int:
    initial_state = State(
        distances,
        rates,
        num_agents=num_agents,
        time=(time,) * num_agents,
        current_positions=("AA",) * num_agents,
    )

    states_to_explore = collections.deque([initial_state])
    best_scores: dict[tuple[frozenset[str], tuple[str, ...]], int] = {}
    max_flow = 0

    while states_to_explore:
        current_state: State = states_to_explore.popleft()

        fingerprint = current_state.finger_print()
        if fingerprint not in best_scores:
            best_scores[fingerprint] = current_state.flow()
        elif best_scores[fingerprint] >= current_state.flow():
            continue
        elif current_state.fairy_tale_score() < max_flow:
            continue

        best_scores[fingerprint] = max(best_scores[fingerprint], current_state.flow())
        max_flow = max(max_flow, current_state.flow())

        moves = current_state.possible_moves()
        states_to_explore += moves

    return max(best_scores.values())


def part_1(raw: str) -> int:
    distances, rates = parse_input(raw)
    return explore(distances, rates, time=30, num_agents=1)


def part_2(raw: str) -> int:
    distances, rates = parse_input(raw)
    return explore(distances, rates, time=26, num_agents=2)


if __name__ == "__main__":
    print(part_1(lib.get_input(16)))
    print(part_2(lib.get_input(16)))
