from typing import Tuple

from lib import get_input, Point


def parse_input(raw: str) -> Tuple[set[Point], list[Tuple[str, int]]]:
    raw_points, raw_folds = raw.strip().split("\n\n")

    points = set()
    for line in raw_points.splitlines():
        x, y = line.strip().split(",")
        points.add(Point(int(x), int(y)))

    folds = []
    for line in raw_folds.splitlines():
        _, raw_fold = line.strip().split("fold along ")
        direction, raw_pos = raw_fold.split("=")
        folds.append((direction, int(raw_pos)))

    return points, folds


def fold_x(points: set[Point], line: int):
    new_points = set()
    for p in points:
        if p.x < line:
            new_points.add(p)
        else:
            diff = p.x - line
            new_points.add(Point(p.x - diff * 2, p.y))

    return new_points


def fold_y(points: set[Point], line: int):
    new_points = set()
    for p in points:
        if p.y < line:
            new_points.add(p)
        else:
            diff = p.y - line
            new_points.add(Point(p.x, p.y - diff * 2))

    return new_points


def fold(points: set[Point], fold_instruction: Tuple[str, int]) -> set[Point]:
    if fold_instruction[0] == "x":
        return fold_x(points, fold_instruction[1])
    else:
        return fold_y(points, fold_instruction[1])


def print_points(points: set[Point]):
    max_x = max(p.x for p in points)
    max_y = max(p.y for p in points)

    for y in range(max_y + 1):
        line = []
        for x in range(max_x + 1):
            line.append("█" if Point(x, y) in points else " ")

        print("".join(line))


def part_1(raw: str):
    points, folds = parse_input(raw)
    return len(fold(points, folds[0]))


def part_2(raw: str):
    points, folds = parse_input(raw)
    for instruction in folds:
        points = fold(points, instruction)
    print_points(points)


if __name__ == "__main__":
    print(part_1(get_input(13)))
    print(part_2(get_input(13)))
