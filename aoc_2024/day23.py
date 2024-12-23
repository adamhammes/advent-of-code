import collections

import lib

Graph = dict[str, set[str]]


def parse_input(raw: str) -> Graph:
    graph = collections.defaultdict(set)
    for line in raw.strip().splitlines():
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)

    return graph


def find_3k_neighbors(graph: Graph) -> set[frozenset[str]]:
    neighborhoods = set()
    ts = [n for n in graph if n.startswith("t")]
    for t in ts:
        for a in graph[t]:
            for b in graph[a]:
                if t in graph[b]:
                    neighborhoods.add(frozenset([t, a, b]))

    return neighborhoods


def part_1(raw: str):
    graph = parse_input(raw)
    return len(find_3k_neighbors(graph))


def find_maximal_clique(graph: Graph, starting_clique: frozenset[str]):
    clique = set(starting_clique)
    other_nodes = graph.keys() - starting_clique

    for o in other_nodes:
        if all(o in graph[n] for n in clique):
            clique.add(o)

    return clique


def part_2(raw: str):
    graph = parse_input(raw)
    three_cliques = find_3k_neighbors(graph)

    cliques = []
    for three_clique in three_cliques:
        cliques.append(find_maximal_clique(graph, three_clique))

    max_clique = max(cliques, key=len)
    return ",".join(sorted(max_clique))


if __name__ == "__main__":
    print(part_1(lib.get_input(23)))
    print(part_2(lib.get_input(23)))
