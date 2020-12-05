import re
import typing as t

PASSWORD_PARSER = re.compile(r"(\d+)-(\d+) ([a-z]+): ([a-z]+)")


class PasswordLine(t.NamedTuple):
    low: int
    high: int
    character: str
    password: str


def parse_line(line: str) -> PasswordLine:
    low, high, character, password = PASSWORD_PARSER.match(line).groups("ALL")
    return PasswordLine(int(low), int(high), character, password)


def get_input() -> t.List[PasswordLine]:
    with open("inputs/day02.txt") as f:
        raw_lines = f.readlines()

    return list(map(parse_line, raw_lines))


def password_matches(line: PasswordLine) -> bool:
    count = line.password.count(line.character)
    return line.low <= count <= line.high


def part_1():
    passwords = get_input()
    return sum(map(password_matches, passwords))


def password_actually_matches(line: PasswordLine) -> bool:
    return (line.password[line.low - 1], line.password[line.high - 1]).count(
        line.character
    ) == 1


def part_2():
    passwords = get_input()
    return sum(map(password_actually_matches, passwords))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
