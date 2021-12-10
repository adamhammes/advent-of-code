import collections
import statistics
from typing import Optional

import lib

character_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

opening_chars = character_pairs.keys()
closing_chars = character_pairs.values()

p1_scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
p2_scoring = {")": 1, "]": 2, "}": 3, ">": 4}


def validate_line(line: str) -> Optional[str]:
    queue = collections.deque()

    for c in line:
        if c in opening_chars:
            queue.append(c)
        elif c in closing_chars:
            hopefully_matching_char = queue.pop()

            if character_pairs[hopefully_matching_char] != c:
                return c

    return None


def part_1(raw: str) -> int:
    lines = raw.strip().splitlines()

    validations = map(validate_line, lines)
    errors = (v for v in validations if v is not None)
    return sum(map(p1_scoring.get, errors))


def complete_line(line: str) -> str:
    queue = collections.deque()

    for c in line:
        if c in opening_chars:
            queue.append(c)
        else:
            queue.pop()

    remaining_unclosed = "".join(c for c in queue)
    return "".join(character_pairs.get(c) for c in reversed(remaining_unclosed))


def score_completion(completion: str) -> int:
    score = 0
    for c in completion:
        score *= 5
        score += p2_scoring[c]

    return score


def part_2(raw: str) -> int:
    lines = raw.strip().splitlines()
    incomplete_lines = [line for line in lines if validate_line(line) is None]

    completions = list(map(complete_line, incomplete_lines))
    scores = list(map(score_completion, completions))
    return statistics.median(scores)


if __name__ == "__main__":
    print(part_1(lib.get_input(10)))
    print(part_2(lib.get_input(10)))
