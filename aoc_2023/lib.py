import re


def get_input(day: int) -> str:
    with open(f"inputs/day{day:02}.txt") as f:
        return f.read()


def extract_ints(string: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", string)))
