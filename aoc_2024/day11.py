import functools

import lib


@functools.cache
def change(num: int, num_iterations=1) -> int:
    if num_iterations == 0:
        return 1

    if num == 0:
        new_nums = [1]
    elif len(str(num)) % 2 == 0:
        stringified = str(num)
        a = stringified[: len(stringified) // 2]
        b = stringified[len(stringified) // 2 :]
        new_nums = [int(a), int(b)]
    else:
        new_nums = [num * 2024]

    return sum(change(n, num_iterations - 1) for n in new_nums)


def part_1(raw: str) -> int:
    nums = lib.extract_ints(raw)
    return sum(change(n, 25) for n in nums)


def part_2(raw: str) -> int:
    nums = lib.extract_ints(raw)
    return sum(change(n, 75) for n in nums)


if __name__ == "__main__":
    print(part_1(lib.get_input(11)))
    print(part_2(lib.get_input(11)))
