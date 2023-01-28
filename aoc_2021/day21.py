from typing import Iterable, Tuple


def create_die() -> Iterable[int]:
    while True:
        yield from range(1, 100 + 1)


def roll_3(die) -> Tuple[int, int, int]:
    return next(die), next(die), next(die)


def wrap(num: int) -> int:
    while num > 10:
        num -= 10

    return num


def part_1(p1: int, p2: int) -> int:
    die = create_die()

    p1_score, p2_score = 0, 0

    num_dice_rolls = 0

    while True:
        p1 = wrap(p1 + sum(roll_3(die)))
        num_dice_rolls += 3
        p1_score += p1

        if p1_score >= 1000:
            break

        p2 = wrap(p2 + sum(roll_3(die)))
        num_dice_rolls += 3
        p2_score += p2

        if p2_score >= 1000:
            break

    return min(p1_score, p2_score) * num_dice_rolls


if __name__ == "__main__":
    print(part_1(7, 8))
