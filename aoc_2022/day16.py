import collections
import itertools
import math
import re

import lib

Graph = dict[str, list[str]]
FlowRates = dict[str, int]
Distances = dict[tuple[str, str], int]

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


def parse_input(raw: str) -> tuple[Graph, FlowRates]:
    graph: Graph = {}
    rates: FlowRates = {}

    for line in raw.strip().splitlines():
        label = line.split()[1]
        rate = lib.extract_ints(line)[0]

        edges = re.split("valves? ", line)[1].split(", ")

        graph[label] = edges
        rates[label] = rate

    return graph, rates


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


def calc_flow(distances: Distances, rates: FlowRates, nodes: tuple[str, ...]) -> int:
    time = flow = 0

    cur_node = "AA"

    for node in nodes:
        time += distances[cur_node, node] + 1
        if time > 30:
            break

        flow += (30 - time) * rates[node]
        cur_node = node

    return flow


def part_1(raw: str) -> int:
    graph, rates = parse_input(raw)
    distances = precompute_distances(graph)

    flowing_nodes = [n for n, rate in rates.items() if rate and n != "AA"]
    permutations = itertools.permutations(flowing_nodes, r=10)

    # return len(flowing_nodes)

    max_flow = 0
    num_perms = math.factorial(len(flowing_nodes))
    for i, perm in enumerate(permutations):
        flow = calc_flow(distances, rates, perm)
        max_flow = max(max_flow, flow)

        if i % 100_000 == 0:
            print(f"{i}/{num_perms}")

    return max_flow


if __name__ == "__main__":
    # print(part_1(EXAMPLE))
    print(part_1(lib.get_input(16)))
