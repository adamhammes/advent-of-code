import collections

import lib

EelLifecycle = dict[int, int]


def parse_input(raw: str) -> EelLifecycle:
    eels = map(int, raw.strip().split(","))
    return collections.Counter(eels)


def simulate_day(state: EelLifecycle) -> EelLifecycle:
    updated = {day - 1: eel_count for day, eel_count in state.items()}

    if -1 in updated:
        updated[6] = updated.get(6, 0) + updated[-1]
        updated[8] = updated.get(8, 0) + updated[-1]
        del updated[-1]

    return updated


def run_simulation(raw: str, days: int) -> int:
    eels = parse_input(raw)

    for _ in range(days):
        eels = simulate_day(eels)

    return sum(eels.values())


def part_1(raw: str) -> int:
    return run_simulation(raw, 80)


def part_2(raw: str) -> int:
    return run_simulation(raw, 256)


if __name__ == "__main__":
    print(part_1(lib.get_input(6)))
    print(part_2(lib.get_input(6)))
