import lib


def parse_input(raw: str) -> [[int]]:
    groups = raw.strip().split("\n\n")
    return [[int(g) for g in group.split("\n")] for group in groups]


def part_1(raw: str) -> int:
    return max(map(sum, parse_input(raw)))


def part_2(raw: str) -> int:
    calories = list(map(sum, parse_input(raw)))
    calories.sort(reverse=True)
    return sum(calories[:3])


if __name__ == "__main__":
    print(part_1(lib.get_input(1)))
    print(part_2(lib.get_input(1)))
