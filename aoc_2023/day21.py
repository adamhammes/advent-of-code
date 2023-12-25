from lib import Point
import lib


Graph = dict[Point, list[Point]]


def parse_input(raw: str) -> tuple[Graph, Point]:
    grid = lib.parse_grid(raw)

    start = lib.first(grid, lambda p: grid[p] == "S")

    graph: Graph = {p: [] for p in grid}
    for p in graph:
        for n in p.neighbors4():
            if grid.get(n, "#") != "#":
                graph[p].append(n)

    return graph, start


def find_spots(graph: Graph, start: Point, distance: int) -> int:
    current_spots = {start}
    for _ in range(distance):
        current_spots = {n for p in current_spots for n in graph[p]}

    return len(current_spots)


def part_1(raw: str) -> int:
    graph, start = parse_input(raw)
    return find_spots(graph, start, 64)


if __name__ == "__main__":
    print(part_1(lib.get_input(21)))
