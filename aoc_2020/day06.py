import typing as t


def get_input() -> t.Iterator[t.Iterator[t.Set[str]]]:
    with open("inputs/day06.txt") as f:
        groups = f.read().split("\n\n")

    return (map(set, group.splitlines()) for group in groups)


def part_1():
    return sum(map(len, [set.union(*group) for group in get_input()]))


def part_2():
    return sum(map(len, [set.intersection(*group) for group in get_input()]))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
