import functools
import lib


def parse_input(raw: str) -> tuple[tuple[str, ...], list[str]]:
    patterns, goals = raw.strip().split("\n\n")
    return tuple(patterns.split(", ")), goals.split()


@functools.cache
def can_match(patterns: tuple[str], goal: str) -> int:
    if goal == "":
        return 1

    prefixes = [p for p in patterns if goal.startswith(p)]
    return sum(can_match(patterns, goal[len(prefix) :]) for prefix in prefixes)


def part_1(raw: str):
    patterns, goals = parse_input(raw)
    return sum(can_match(patterns, goal) != 0 for goal in goals)


def part_2(raw: str):
    patterns, goals = parse_input(raw)
    return sum(can_match(patterns, goal) for goal in goals)


if __name__ == "__main__":
    print(part_1(lib.get_input(19)))
    print(part_2(lib.get_input(19)))
