import lib


def calculate_simple_cost(positions: list[int], target: int) -> int:
    return sum(abs(pos - target) for pos in positions)


def calculate_complex_cost(positions: list[int], target: int) -> int:
    series_sum = lambda i: int(i * (i + 1) / 2)
    return sum(series_sum(abs(pos - target)) for pos in positions)


def part_1(raw: str) -> int:
    positions = list(map(int, raw.strip().split(",")))
    min_pos, max_pos = min(positions), max(positions)
    return min(calculate_simple_cost(positions, pos) for pos in range(min_pos, max_pos))


def part_2(raw: str) -> int:
    positions = list(map(int, raw.strip().split(",")))
    min_pos, max_pos = min(positions), max(positions)
    return min(
        calculate_complex_cost(positions, pos) for pos in range(min_pos, max_pos)
    )


if __name__ == "__main__":
    print(part_1(lib.get_input(7)))
    print(part_2(lib.get_input(7)))
