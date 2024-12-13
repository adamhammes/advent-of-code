import typing
from fractions import Fraction

import lib


class Game(typing.NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int

    a: int
    b: int

    def solve(self):
        determinant = self.y2 * self.x1 - self.x2 * self.y1
        x = self.a * self.y2 - self.b * self.y1
        y = -self.a * self.x2 + self.b * self.x1

        return Fraction(x, determinant), Fraction(y, determinant)

    def is_solvable(self):
        a, b = self.solve()
        return a.is_integer() and b.is_integer() and a > 0 and b > 0


def parse_game(raw: str, smudge_factor: int):
    x1, y1, x2, y2, a, b = lib.extract_ints(raw)
    return Game(x1, x2, y1, y2, a + smudge_factor, b + smudge_factor)


def parse_input(raw: str, smudge_factor: int = 0) -> list[Game]:
    return [parse_game(chunk, smudge_factor) for chunk in raw.split("\n\n")]


def part_1(raw: str) -> int:
    games = parse_input(raw)
    solutions = [g.solve() for g in games if g.is_solvable()]
    return sum(3 * a.numerator + b.numerator for a, b in solutions)


def part_2(raw: str) -> int:
    smudge_factor = 10000000000000
    games = parse_input(raw, smudge_factor)
    solutions = [g.solve() for g in games if g.is_solvable()]
    return sum(3 * a.numerator + b.numerator for a, b in solutions)


if __name__ == "__main__":
    print(part_1(lib.get_input(13)))
    print(part_2(lib.get_input(13)))
