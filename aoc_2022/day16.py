import collections
import dataclasses
import itertools
import queue
import re

import lib

Graph = dict[str, list[str]]
FlowRates = dict[str, int]
Distances = dict[tuple[str, str], int]


@dataclasses.dataclass(frozen=True)
class State:
    distances: Distances
    rates: FlowRates
    time: int
    current_position: str = "AA"
    opened_at: dict[str, int] = dataclasses.field(default_factory=dict)

    def flow(self) -> int:
        return sum(
            self.rates[valve] * opened_at for valve, opened_at in self.opened_at.items()
        )

    def visited_valves(self) -> frozenset[str]:
        return frozenset(self.opened_at)

    def __lt__(self, other):
        return self.flow() < other.flow()

    def open(self, valve: str) -> "State":
        arrival_time = self.time - self.distances[(self.current_position, valve)] - 1
        return State(
            distances=self.distances,
            rates=self.rates,
            time=arrival_time,
            current_position=valve,
            opened_at=self.opened_at | {valve: arrival_time},
        )

    def possible_moves(self) -> list["State"]:
        unvisited_valves = [v for v in self.rates if v not in self.opened_at]
        states = list(map(self.open, unvisited_valves))
        return [s for s in states if s.time > 0]


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


def part_1(raw: str) -> int:
    distances, rates = parse_input(raw)

    initial_state = State(distances, rates, time=30)

    states_to_explore = collections.deque([initial_state])
    best_scores: dict[frozenset[str], int] = {}

    while states_to_explore:
        current_state: State = states_to_explore.popleft()

        visited = current_state.visited_valves()
        if visited not in best_scores:
            best_scores[visited] = current_state.flow()
        elif best_scores[visited] >= current_state.flow():
            continue

        best_scores[visited] = current_state.flow()

        moves = current_state.possible_moves()
        states_to_explore += moves

    return max(best_scores.values())


if __name__ == "__main__":
    print(part_1(lib.get_input(16)))
