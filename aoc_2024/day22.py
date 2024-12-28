import collections

import lib


def mix_and_prune(secret: int, number: int) -> int:
    return (secret ^ number) % 16777216


def evolve(secret: int, iterations: int = 1) -> int:
    for _ in range(iterations):
        secret = mix_and_prune(secret, secret * 64)
        secret = mix_and_prune(secret, secret // 32)
        secret = mix_and_prune(secret, secret * 2048)
    return secret


def part_1(raw: str):
    starting = lib.extract_ints(raw)
    return sum(evolve(start, 2_000) for start in starting)


def get_price_list(starting: int, iterations: int) -> list[int]:
    prices = []
    current = starting
    for _ in range(iterations + 1):
        prices.append(current % 10)
        current = evolve(current)

    return prices


def calculate_window_scores(price_list: list[int]):
    price_change_scores = dict()
    for window in lib.window(price_list, 5):
        deltas = tuple(b - a for a, b in zip(window, window[1:]))
        if deltas in price_change_scores:
            continue

        price_change_scores[deltas] = window[-1]

    return price_change_scores


def part_2(raw: str):
    starting_numbers = lib.extract_ints(raw)
    price_lists = [get_price_list(starting, 2_000) for starting in starting_numbers]

    scores_by_price_change = collections.defaultdict(lambda: 0)

    for price_list in price_lists:
        window_scores = calculate_window_scores(price_list)
        for window, score in window_scores.items():
            scores_by_price_change[window] += score

    return max(scores_by_price_change.values())


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
    print(part_2(lib.get_input(22)))
