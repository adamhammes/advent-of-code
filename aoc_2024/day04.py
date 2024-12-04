import lib
from lib import Point


def part_1(raw: str) -> int:
    grid = lib.parse_grid(raw)

    strings = []
    for starting_point in grid:
        for direction in Point.directions8:
            chars = []
            for length in range(4):
                displacement = Point(*direction).times(length)
                current_point = starting_point.displace(*displacement)
                chars.append(grid.get(current_point))

            strings.append("".join(c for c in chars if c is not None))

    return strings.count("XMAS")


def part_2(raw: str) -> int:
    grid = lib.parse_grid(raw)

    def get_cross(p: Point) -> str:
        directions = [(0, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        points = [p.displace(*d) for d in directions]
        return "".join(grid[p] for p in points if p in grid)

    shapes = list(map(get_cross, grid.keys()))
    return sum(shape in ["ASSMM", "AMMSS", "ASMMS", "AMSSM"] for shape in shapes)


if __name__ == "__main__":
    print(part_1(lib.get_input(4)))
    print(part_2(lib.get_input(4)))
