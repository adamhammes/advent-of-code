import collections
import lib
from lib import Point

Map = dict[Point, int]


def parse_input(raw: str) -> Map:
    point_map = {}
    for y, line in enumerate(raw.strip().splitlines()):
        for x, char in enumerate(line.strip()):
            point_map[Point(x, y)] = int(char)

    return point_map


def find_low_points(point_map: Map) -> list[Point]:
    low_points = []
    for point in point_map:
        neighbors = [n for n in point.neighbors4() if n in point_map]
        if all(point_map[n] > point_map[point] for n in neighbors):
            low_points.append(point)

    return low_points


def part_1(raw: str) -> int:
    point_map = parse_input(raw)
    low_points = find_low_points(point_map)
    return sum(point_map[p] + 1 for p in low_points)


def flood_fill(point_map: Map, cur_point: Point) -> set[Point]:
    queue = collections.deque([cur_point])

    flooded_points = {cur_point}
    while queue:
        cur_point = queue.popleft()

        neighbors = {
            n
            for n in cur_point.neighbors4()
            if n in point_map and point_map[n] < 9 and n not in flooded_points
        }

        flooded_points |= neighbors
        queue.extend(neighbors)

    return flooded_points


def part_2(raw: str) -> int:
    point_map = parse_input(raw)
    possible_flood_points = {p for p in point_map if point_map[p] != 9}
    flood_areas = []

    while possible_flood_points:
        start_point = next(iter(possible_flood_points))

        flood_area = flood_fill(point_map, start_point)
        possible_flood_points.difference_update(flood_area)
        flood_areas.append(flood_area)

    flood_area_sizes = [(len(area), area) for area in flood_areas]
    flood_area_sizes = list(sorted(flood_area_sizes))
    biggest_3_sizes = [size for size, _ in flood_area_sizes[-3:]]

    return lib.product(biggest_3_sizes)


if __name__ == "__main__":
    print(part_1(lib.get_input(9)))
    print(part_2(lib.get_input(9)))
