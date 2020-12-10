import itertools
import lib


def get_input():
    with open("inputs/day09.txt") as f:
        return f.read()


def part_1():
    numbers = list(map(int, get_input().splitlines()))

    for window in lib.window(numbers, 25 + 1):
        inputs, end = window[:-1], window[-1]
        can_sum = any(x + y == end for x, y in itertools.combinations(inputs, 2))

        if not can_sum:
            return end


def part_2():
    numbers = list(map(int, get_input().splitlines()))
    magic_number = part_1()

    for window_size in range(2, len(numbers)):
        for window in lib.window(numbers, window_size):
            if sum(window) == magic_number:
                return min(window) + max(window)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
