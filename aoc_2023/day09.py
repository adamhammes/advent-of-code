import lib


def diff(nums: list[int]) -> (bool, list[int]):
    diffs = []
    stop = True
    for a, b in lib.window(nums, 2):
        diffs.append(b - a)
        stop = stop and (b - a == 0)

    return stop, diffs


def repeated_diff(nums: list[int]) -> list[list[int]]:
    rows = [nums]
    while True:
        stop, diffs = diff(rows[-1])
        rows.append(diffs)
        if stop:
            return rows


def calc_next(nums: list[int]) -> int:
    rows = repeated_diff(nums)

    for below, current in lib.window(rows[::-1], 2):
        from_below = below[-1]
        left = current[-1]
        current.append(from_below + left)

    return rows[0][-1]


def calc_before(nums: list[int]) -> int:
    rows = repeated_diff(nums)
    for below, current in lib.window(rows[::-1], 2):
        from_below = below[0]
        left = current[0]
        current.insert(0, left - from_below)

    return rows[0][0]


def part_1(raw: str) -> int:
    return sum(calc_next(lib.extract_ints(line)) for line in raw.strip().splitlines())


def part_2(raw: str) -> int:
    return sum(calc_before(lib.extract_ints(line)) for line in raw.strip().splitlines())


if __name__ == "__main__":
    print(part_1(lib.get_input(9)))
    print(part_2(lib.get_input(9)))
