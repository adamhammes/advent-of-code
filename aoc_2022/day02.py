from collections.abc import Iterable
import enum

import lib


class Option(str, enum.Enum):
    Rock = "X"
    Paper = "Y"
    Scissors = "Z"


beats = {
    Option.Rock: Option.Scissors,
    Option.Paper: Option.Rock,
    Option.Scissors: Option.Paper,
}

loses = {b: a for a, b in beats.items()}


def parse_input(raw: str) -> Iterable[tuple[Option, Option]]:
    str_to_opt = {
        "A": Option.Rock,
        "B": Option.Paper,
        "C": Option.Scissors,
        "X": Option.Rock,
        "Y": Option.Paper,
        "Z": Option.Scissors,
    }

    for line in raw.strip().splitlines():
        opp, us = line.split()
        yield str_to_opt[opp], str_to_opt[us]


def score_match(opponent_choice, our_choice):
    score = {
        Option.Rock: 1,
        Option.Paper: 2,
        Option.Scissors: 3,
    }[our_choice]

    if beats[our_choice] == opponent_choice:
        score += 6
    elif loses[our_choice] == opponent_choice:
        score += 0
    else:
        score += 3

    return score


def part_1(raw: str) -> int:
    scores = [score_match(opp, us) for opp, us in parse_input(raw)]
    return sum(scores)


def part_2(raw: str) -> int:
    total_score = 0

    for opp, should_do in parse_input(raw):
        us = opp  # draw by default
        if should_do == "X":  # lose
            us = beats[opp]
        elif should_do == "Z":  # win
            us = loses[opp]

        total_score += score_match(opp, us)

    return total_score


if __name__ == "__main__":
    print(part_1(lib.get_input(2)))
    print(part_2(lib.get_input(2)))
