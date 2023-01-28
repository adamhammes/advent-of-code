import collections
import itertools

import lib


def get_input():
    with open("inputs/day10.txt") as f:
        return f.read()


def count_contiguous_combinations(n: int):
    count = 0
    for i in range(n):
        for combo in itertools.combinations(range(1, n), i):
            sequence = [0, *combo, n]
            differences = [hi - lo for lo, hi in lib.window(sequence, 2)]
            count += max(differences) <= 3

    return count


def part_1(raw: str):
    adapters = list(sorted(map(int, raw.splitlines())))
    adapters = [0] + adapters + [max(adapters) + 3]

    differences = collections.defaultdict(int)
    for lower, higher in lib.window(adapters, 2):
        differences[higher - lower] += 1

    return differences[1] * differences[3]


def part_2(raw: str):
    adapters = [0] + list(sorted(map(int, raw.splitlines())))

    one_differences = [0]

    for lower, higher in lib.window(adapters, 2):
        if higher - lower == 1:
            one_differences[-1] += 1
        else:
            one_differences.append(0)

    one_differences = [num for num in one_differences if num > 0]
    individual_combinations = map(count_contiguous_combinations, one_differences)
    return lib.product(individual_combinations)


if __name__ == "__main__":
    print(part_1(get_input()))
    print(part_2(get_input()))
