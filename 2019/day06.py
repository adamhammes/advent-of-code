import collections
import copy
import unittest


def parse_input(lines):
    return [list(reversed(line.split(")"))) for line in lines]


def get_input():
    with open("inputs/day06.txt") as f:
        return parse_input(f.read().splitlines())


TEST_INPUT = parse_input(
    ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
)

TEST_INPUT_2 = parse_input(
    [
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L",
        "K)YOU",
        "I)SAN",
    ]
)


class Graph:
    def __init__(self, edges, directed=True):
        self._directed = directed
        self._edges = edges
        self._nodes = list(set(node for edge in edges for node in edge))
        self._index = {node: i for i, node in enumerate(self._nodes)}

        num_nodes = len(self._nodes)
        self._matrix = [[False for i in range(num_nodes)] for j in range(num_nodes)]

        [self.add_edge(edge) for edge in edges]

    def nodes(self):
        return self._nodes

    def add_edge(self, edge):
        _from, to = edge
        self._matrix[self._index[_from]][self._index[to]] = True

        if not self._directed:
            self._matrix[self._index[to]][self._index[_from]] = True

    def neighbors(self, node):
        for index, is_connected in enumerate(self._matrix[self._index[node]]):
            if is_connected:
                yield self._nodes[index]

    def incoming_neighbors(self, node):
        node_index = self._index[node]
        for i in range(len(self._nodes)):
            is_connected = self._matrix[i][node_index]
            if is_connected:
                yield self._nodes[i]

    def remove_node(self, node):
        node_index = self._index[node]
        # remove incoming edges
        for node_edges in self._matrix:
            del node_edges[node_index]

        del self._matrix[node_index]
        del self._nodes[node_index]
        self._index = {node: i for i, node in enumerate(self._nodes)}

    def topological_ordering(self):
        g = Graph(self._edges)

        ordering = []
        while g.nodes():
            no_incoming = g.root_nodes()
            ordering += no_incoming
            [g.remove_node(node) for node in no_incoming]

        return ordering

    def root_nodes(self):
        return [
            node for node in self.nodes() if not list(self.incoming_neighbors(node))
        ]

    def distance(self, x, y):
        distances = {x: 0}
        queue = collections.deque([x])

        while True:
            node = queue.popleft()
            distance = distances[node]

            if node == y:
                return distances[node]

            for neighbor in self.neighbors(node):
                if neighbor not in distances:
                    distances[neighbor] = distance + 1
                    queue.append(neighbor)


class TestDay06(unittest.TestCase):
    def test_graph_construction(self):
        g = Graph(TEST_INPUT)
        self.assertEqual(12, len(list(g.nodes())))
        self.assertEqual(set(["C"]), set(g.neighbors("D")))
        self.assertEqual(set(["I", "E"]), set(g.incoming_neighbors("D")))

    def test_orbit_count(self):
        self.assertEqual(42, part1(TEST_INPUT))

    def test_directed(self):
        g = Graph(TEST_INPUT, directed=False)
        self.assertEqual(set(["C", "I", "E"]), set(g.neighbors("D")))

    def test_part2(self):
        self.assertEqual(4, part2(TEST_INPUT_2))

    def test_regressions(self):
        self.assertEqual(140608, part1(get_input()))
        self.assertEqual(337, part2(get_input()))


def part1(_input):
    g = Graph(_input)
    orbit_count = collections.defaultdict(int)

    for node in reversed(g.topological_ordering()):
        for neighbor in g.neighbors(node):
            orbit_count[node] = orbit_count[node] + 1 + orbit_count[neighbor]

    return sum(orbit_count.values())


def part2(_input):
    g = Graph(_input, directed=False)
    return g.distance("YOU", "SAN") - 2


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))
