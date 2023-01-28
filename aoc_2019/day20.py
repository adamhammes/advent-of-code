import collections

from lib import Point


def bfs(graph, start, end):
    distances = {start: 0}
    queue = collections.deque([start])

    while queue:
        point = queue.popleft()
        distance = distances[point]

        if point == end:
            return distance

        for neighbor in graph[point]:
            if neighbor not in distances:
                distances[neighbor] = distance + 1
                queue.append(neighbor)


def parse_input(string):
    points = set()

    grid = []
    for y, row in enumerate(string.strip("\n").splitlines()):
        grid.append([])
        for x, character in enumerate(row):
            grid[-1].append(character)
            if character == ".":
                points.add(Point(x, y))

    portal_pairs = collections.defaultdict(list)
    for y, row in enumerate(grid):
        for x, character in enumerate(row):
            if not character.isalpha():
                continue

            character_point = Point(x, y)

            neighboring_points = points.intersection(character_point.neighbors())
            if not neighboring_points:
                continue

            neighboring_point = list(neighboring_points)[0]
            direction_to_other_letter = character_point.direction_to(
                neighboring_point
            ).inverse_direction()
            other_letter_coords = character_point.move_by_direction(
                direction_to_other_letter
            )
            other_letter = grid[other_letter_coords.y][other_letter_coords.x]

            portal_pairs["".join(sorted(other_letter + character))].append(
                neighboring_point
            )

    graph = collections.defaultdict(set)

    for p in points:
        graph[p].update(points.intersection(p.neighbors()))

    for point_pair in portal_pairs.values():
        if len(point_pair) < 2:
            continue

        p1, p2, = point_pair
        graph[p1].add(p2)
        graph[p2].add(p1)

    graph = dict(graph.items())

    start, end = portal_pairs["AA"][0], portal_pairs["ZZ"][0]

    return graph, start, end


def get_input():
    with open("inputs/day20.txt") as f:
        return f.read()


def part1(_input=None):
    _input = _input or get_input()
    return bfs(*parse_input(_input))


if __name__ == "__main__":
    print(part1())
