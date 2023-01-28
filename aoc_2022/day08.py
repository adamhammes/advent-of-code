from lib import Point
import lib


Forest = dict[Point, int]


def read_grid(raw: str) -> Forest:
    grid = {}
    for y, line in enumerate(raw.strip().splitlines()):
        for x, raw_height in enumerate(line):
            grid[Point(x, y)] = int(raw_height)

    return grid


def is_visible(p: Point, grid: Forest) -> bool:
    for direction in Point.directions4:
        cur_point = p
        while True:
            cur_point = cur_point.displace(*direction)
            if cur_point not in grid:
                return True
            if grid[cur_point] >= grid[p]:
                break

    return False


def count_scene(p: Point, grid: Forest) -> int:
    result = 1

    for direction in Point.directions4:
        cur_count = 0
        cur_point = p
        while True:
            cur_count += 1
            cur_point = cur_point.displace(*direction)
            if cur_point not in grid:
                # oops, we went out of the forest
                cur_count -= 1
                break
            elif grid[cur_point] >= grid[p]:
                break

        result *= cur_count

    return result


def part_1(raw: str) -> int:
    grid = read_grid(raw)
    return sum(is_visible(p, grid) for p in grid)


def part_2(raw: str) -> int:
    grid = read_grid(raw)
    scene_scores = {p: count_scene(p, grid) for p in grid}
    return max(scene_scores.values())


if __name__ == "__main__":
    print(part_1(lib.get_input(8)))
    print(part_2(lib.get_input(8)))
