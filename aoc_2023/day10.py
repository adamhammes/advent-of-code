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


def is_curve_character(c: str) -> bool:
    return c in "LJ7F"


COMPLEMENT = {"J": "F", "F": "J", "L": "7", "7": "L"}


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


def part_2(raw: str) -> int:
    field = parse_input(raw)
    loop_points = {field.start}

    queue = collections.deque([field.start])
    while queue:
        current = queue.popleft()

        unexplored_neighbors = [n for n in field.edges[current] if n not in loop_points]
        for n in unexplored_neighbors:
            queue.append(n)
            loop_points.add(n)

    x_max, y_max = max(p.x for p in field.grid), max(p.y for p in field.grid)
    total = 0
    for y in range(0, y_max + 1):
        inside = False
        last_loop_char = None
        for x in range(-1, x_max + 1):
            cur_point = Point(x, y)

            if cur_point in loop_points:
                loop_char = field.grid[cur_point]
                if loop_char == "|":
                    inside = not inside
                    last_loop_char = None
                elif is_curve_character(loop_char) and last_loop_char is None:
                    last_loop_char = loop_char
                elif (
                    is_curve_character(loop_char)
                    and loop_char == COMPLEMENT[last_loop_char]
                ):
                    inside = not inside
                    last_loop_char = None
                elif is_curve_character(loop_char):
                    last_loop_char = None
            elif cur_point not in loop_points and inside:
                total += 1

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(10)))
    print(part_2(lib.get_input(10)))
