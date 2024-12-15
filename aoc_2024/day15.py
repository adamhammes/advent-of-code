import lib
from lib import parse_grid, Grid, Point


def parse_input(raw: str, wide=False) -> tuple[Grid, list[Point]]:
    raw_grid, raw_directions = raw.strip().split("\n\n")

    replacements = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    if wide:
        for old, new in replacements.items():
            raw_grid = raw_grid.replace(old, new)

    grid = parse_grid(raw_grid)
    direction_map = {
        "v": Point(0, 1),
        ">": Point(1, 0),
        "^": Point(0, -1),
        "<": Point(-1, 0),
    }
    directions = map(direction_map.get, raw_directions.replace("\n", ""))
    return grid, list(directions)


def find_robot(grid: Grid) -> Point:
    return lib.first(grid, lambda k: grid[k] == "@")


def move(grid: Grid, direction: Point) -> Point:
    start_position = find_robot(grid)
    current_position = start_position
    stack = [{current_position}]
    while True:
        next_positions = {p.displace(*direction) for p in stack[-1]}
        next_values = set(map(grid.get, next_positions))
        if "#" in next_values:
            return start_position
        elif next_values == {"."}:
            break

        next_positions = {p for p in next_positions if grid[p] != "."}

        if direction.x == 0:
            for p in next_positions.copy():
                if grid[p] == "[":
                    next_positions.add(p.east())
                elif grid[p] == "]":
                    next_positions.add(p.west())

        stack.append(next_positions)

    for pos_set in reversed(stack):
        for position in pos_set:
            grid[position.displace(*direction)] = grid[position]
            grid[position] = "."

    return start_position.displace(*direction)


def score_point(grid, point: Point):
    if grid[point] in "[O":
        return point.x + 100 * point.y
    else:
        return 0


def part_1(raw: str):
    grid, directions = parse_input(raw)
    for direction in directions:
        move(grid, direction)

    return sum(score_point(grid, p) for p in grid)


def part_2(raw: str):
    grid, directions = parse_input(raw, wide=True)
    for direction in directions:
        move(grid, direction)

    return sum(score_point(grid, p) for p in grid)


if __name__ == "__main__":
    print(part_1(lib.get_input(15)))
    print(part_2(lib.get_input(15)))
