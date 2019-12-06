import collections
import copy
import unittest


def parse_input(lines):
    return [line.split(")") for line in lines]


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

    def distances_from(self, start_node="COM"):
        distances = {start_node: 0}
        queue = collections.deque([start_node])

        while queue:
            node = queue.popleft()
            distance = distances[node]

            unseen_neighbors = set(self.neighbors(node)) - distances.keys()
            for neighbor in unseen_neighbors:
                distances[neighbor] = distance + 1
                queue.append(neighbor)

        return distances


class TestDay06(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(42, part1(TEST_INPUT))
        self.assertEqual(4, part2(TEST_INPUT_2))

    def test_regressions(self):
        self.assertEqual(140608, part1(get_input()))
        self.assertEqual(337, part2(get_input()))


def part1(_input):
    g = Graph(_input)
    distances = g.distances_from()

    return sum(distances.values())


def part2(_input):
    g = Graph(_input, directed=False)
    return g.distances_from(start_node="YOU")["SAN"] - 2


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))
