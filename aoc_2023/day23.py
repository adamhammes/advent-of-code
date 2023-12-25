import collections
import typing

import lib
from lib import Point

Graph = dict[Point, list[Point]]
WALL = "#"


def parse_input(raw: str) -> Graph:
    grid = lib.parse_grid(raw, rev_y=True)

    graph = {point: [] for point, val in grid.items() if val != WALL}

    for point in graph:
        graph[point] = {
            ".": [n for n in point.neighbors4() if grid.get(n, WALL) != WALL],
            ">": [point.east()],
            "v": [point.south()],
            "<": [point.west()],
            "^": [point.north()],
        }[grid[point]]

    return graph


class ExploreState(typing.NamedTuple):
    position: Point
    seen: set[Point]


def find_longest_path(graph: Graph) -> set[Point]:
    max_x, max_y = max(p.x for p in graph), max(p.y for p in graph)

    start = Point(1, max_y)
    end = Point(max_x, 0)

    paths = []

    queue = collections.deque([ExploreState(start, {start})])
    while queue:
        state = queue.popleft()

        if state.position == end:
            paths.append(state.seen)
            continue

        neighbors = [n for n in graph[state.position] if n not in state.seen]

        for n in neighbors:
            queue.append(ExploreState(n, state.seen.union([n])))

    return max(paths, key=len)


def part_1(raw: str) -> int:
    graph = parse_input(raw)
    return len(find_longest_path(graph)) - 1


if __name__ == "__main__":
    print(part_1(lib.get_input(23)))
