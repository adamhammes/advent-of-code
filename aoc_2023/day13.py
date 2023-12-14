from lib import Point
import lib

Mirror = list[list[str]]


def parse_input(raw: str) -> list[Mirror]:
    return [
        [list(line) for line in group.splitlines()]
        for group in raw.strip().split("\n\n")
    ]


def find_horizontal_mistakes(mirror: Mirror, column_index: int) -> list[Point]:
    width = len(mirror[0])
    if column_index in [0, width]:
        return [Point(-1, -1)] * 2

    mistakes = []
    for y, line in enumerate(mirror):
        left = list(range(0, column_index))[::-1]
        right = list(range(column_index, width))

        for x1, x2 in zip(left, right):
            if line[x1] != line[x2]:
                mistakes.append(Point(x1, y))

    return mistakes


def is_reflected_horizontally(mirror: Mirror, column_index: int) -> bool:
    return not find_horizontal_mistakes(mirror, column_index)


def find_vertical_mistakes(mirror: Mirror, row_index: int) -> list[Point]:
    height = len(mirror)
    if row_index in [0, height]:
        return [Point(-1, -1)] * 2

    mistakes = []
    for x in range(len(mirror[0])):
        line = "".join(row[x] for row in mirror)

        top = list(range(0, row_index))[::-1]
        bottom = list(range(row_index, height))

        for y1, y2 in zip(top, bottom):
            if line[y1] != line[y2]:
                mistakes.append(lib.Point(x, y1))

    return mistakes


def is_reflected_vertically(mirror: Mirror, row_index: int) -> bool:
    return not find_vertical_mistakes(mirror, row_index)


def calc_score(mirror: Mirror) -> list[int]:
    scores = []
    for x in range(1, len(mirror[0])):
        if is_reflected_horizontally(mirror, x):
            scores.append(x)

    for y in range(1, len(mirror)):
        if is_reflected_vertically(mirror, y):
            scores.append(y * 100)

    if not scores:
        raise Exception("No mirroring found")

    return scores


def find_and_correct_mistake(mirror: Mirror) -> Mirror:
    mistake = None
    for x in range(1, len(mirror[0])):
        mistakes = find_horizontal_mistakes(mirror, x)
        if len(mistakes) == 1:
            mistake = mistakes[0]

    for y in range(1, len(mirror)):
        mistakes = find_vertical_mistakes(mirror, y)
        if len(mistakes) == 1:
            mistake = mistakes[0]

    if mistake is None:
        raise Exception("no error found")

    m2 = [line.copy() for line in mirror]
    c = mirror[mistake.y][mistake.x]
    m2[mistake.y][mistake.x] = "#" if c == "." else "."
    return m2


def part_1(raw: str) -> int:
    return sum(calc_score(mirror)[0] for mirror in parse_input(raw))


def calc_p2_score(mirror: Mirror) -> int:
    p1_score = calc_score(mirror)[0]

    p2_scores = calc_score(find_and_correct_mistake(mirror))
    if len(p2_scores) == 1:
        return p2_scores[0]

    return sum(p2_scores) - p1_score


def part_2(raw: str) -> int:
    return sum(calc_p2_score(mirror) for mirror in parse_input(raw))


if __name__ == "__main__":
    print(part_1(lib.get_input(13)))
    print(part_2(lib.get_input(13)))
