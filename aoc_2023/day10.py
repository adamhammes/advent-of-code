import collections

import lib
from lib import Grid, Point

char_to_grid = {
    "|": [Point.north, Point.south],
    "-": [Point.east, Point.west],
    "L": [Point.north, Point.east],
    "J": [Point.north, Point.west],
    "7": [Point.south, Point.west],
    "F": [Point.south, Point.east],
    ".": [],
    "S": [],
}


class Field:
    grid: Grid
    edges: dict[Point, set[Point]]
    loop_tiles = set[Point]
    start: Point

    def __init__(self, grid: Grid):
        self.grid = grid
        self.start = lib.first(self.grid, lambda p: grid[p] == "S")

        self.edges = collections.defaultdict(set)
        for point, char in grid.items():
            neighbors = [n for n in self.leads_to(point)]

            for n in neighbors:
                self.edges[point].add(n)
                if n == self.start:
                    self.edges[n].add(point)

    def leads_to(self, p: Point) -> list[Point]:
        return [f(p) for f in char_to_grid[self.grid[p]]]


def parse_input(raw: str) -> Field:
    lines = raw.splitlines()[::-1]
    grid = lib.parse_grid("\n".join(lines))
    return Field(grid)


def part_1(raw: str) -> int:
    field = parse_input(raw)
    distances: dict[Point, int] = {field.start: 0}

    queue = collections.deque([field.start])
    while queue:
        current = queue.popleft()

        unexplored_neighbors = [n for n in field.edges[current] if n not in distances]
        for n in unexplored_neighbors:
            queue.append(n)
            distances[n] = distances[current] + 1

    return max(distances.values())


if __name__ == "__main__":
    print(part_1(lib.get_input(10)))
