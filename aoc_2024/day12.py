import collections

from lib import Point
import lib


def get_perimeter(grid: lib.Grid, points: set[Point]) -> int:
    kind = grid[list(points)[0]]

    def count_perimeter(p: Point):
        return sum(grid.get(n) != kind for n in p.neighbors4())

    return sum(map(count_perimeter, points))


def find_area(grid: lib.Grid, start_point: Point) -> set[Point]:
    visited = {start_point}
    kind = grid[start_point]
    queue = collections.deque([start_point])
    while queue:
        current = queue.popleft()
        neighbors = {
            n
            for n in current.neighbors4()
            if n in grid and grid[n] == kind and n not in visited
        }
        visited |= neighbors
        queue.extend(neighbors)

    return visited


def part_1(raw: str) -> int:
    grid = lib.parse_grid(raw)
    points = set(grid)
    areas = []
    while points:
        start_point = list(points)[0]
        area = find_area(grid, start_point)
        points.difference_update(area)
        areas.append(area)

    return sum(len(area) * get_perimeter(grid, area) for area in areas)


if __name__ == "__main__":
    print(part_1(lib.get_input(12)))
