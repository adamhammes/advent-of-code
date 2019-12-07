import collections


def parse_input(lines):
    return [line.split(")") for line in lines]


def get_input():
    with open("inputs/day06.txt") as f:
        return parse_input(f.read().splitlines())


class Graph:
    def __init__(self, edges, directed=True):
        self._edges = collections.defaultdict(set)

        [self._edges[x].add(y) for x, y in edges]
        if not directed:
            [self._edges[y].add(x) for x, y in edges]

    def neighbors(self, node):
        return self._edges[node]

    def distances_from(self, start_node="COM"):
        distances = {start_node: 0}
        queue = collections.deque([start_node])

        while queue:
            node = queue.popleft()
            distance = distances[node]

            unseen_neighbors = self.neighbors(node) - distances.keys()
            for neighbor in unseen_neighbors:
                distances[neighbor] = distance + 1
                queue.append(neighbor)

        return distances


def part1(_input):
    return sum(Graph(_input).distances_from().values())


def part2(_input):
    return Graph(_input, directed=False).distances_from(start_node="YOU")["SAN"] - 2


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))
