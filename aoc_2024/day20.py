import typing

from lib import Point, Grid
import lib


def parse_input(raw: str) -> tuple[Grid, Point, Point]:
    grid = lib.parse_grid(raw)
    start = lib.first(grid, lambda p: grid[p] == "S")
    end = lib.first(grid, lambda p: grid[p] == "E")
    grid[start] = "."
    grid[end] = "."
    return grid, start, end


class Distance(typing.NamedTuple):
    from_start: int
    from_end: int


def calc_distances(grid: Grid, start: Point, end: Point) -> dict[Point, Distance]:
    distances = {}
    current_position = start
    num_steps = 0
    while True:
        distances[current_position] = num_steps
        if current_position == end:
            break

        current_position = lib.first(
            current_position.neighbors4(),
            lambda p: p not in distances and grid[p] == ".",
        )
        num_steps += 1

    return {
        p: Distance(distance_from_start, num_steps - distance_from_start)
        for p, distance_from_start in distances.items()
    }


def find_cheat_positions(start_position: Point, cheat_distance: int):
    deltas = list(range(-cheat_distance, cheat_distance + 1))
    points = []
    for x in deltas:
        for y in deltas:
            moved = start_position.displace(x, y)
            if start_position.cartesian_distance_to(moved) <= cheat_distance:
                points.append(moved)
    return points


def cheat(raw: str, threshold: int, cheat_length: int):
    grid, start, end = parse_input(raw)
    distances = calc_distances(grid, start, end)
    non_cheat_distance = max(d.from_end for d in distances.values())

    winners = 0
    target = non_cheat_distance - threshold
    for cheat_start_position, start_position_distance in distances.items():
        cheat_positions = find_cheat_positions(cheat_start_position, cheat_length)
        cheat_distances = [
            start_position_distance.from_start
            + distances[cheat_ending_position].from_end
            + cheat_start_position.cartesian_distance_to(cheat_ending_position)
            for cheat_ending_position in cheat_positions
            if cheat_ending_position in distances
        ]

        for distance in cheat_distances:
            if distance <= target:
                winners += 1

    return winners


def part_1(raw: str, threshold=100):
    return cheat(raw, threshold, 2)


def part_2(raw: str, threshold=100):
    return cheat(raw, threshold, 20)


if __name__ == "__main__":
    print(part_1(lib.get_input(20)))
    print(part_2(lib.get_input(20)))
