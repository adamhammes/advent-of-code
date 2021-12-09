import collections
from typing import NamedTuple, Tuple

import lib

numbers_to_segments = {
    0: frozenset("abcefg"),
    1: frozenset("cf"),
    2: frozenset("acdeg"),
    3: frozenset("acdfg"),
    4: frozenset("bcdf"),
    5: frozenset("abdfg"),
    6: frozenset("abdefg"),
    7: frozenset("acf"),
    8: frozenset("abcdefg"),
    9: frozenset("abcdfg"),
}

segments_to_numbers = {segments: num for num, segments in numbers_to_segments.items()}

all_letters = set("abcdefg")
all_numbers = set(numbers_to_segments.keys())

segment_occurrence_count = collections.Counter(
    "".join("".join(s) for s in numbers_to_segments.values())
)


numbers_by_segment_count = collections.defaultdict(set)
for num, segments in numbers_to_segments.items():
    numbers_by_segment_count[len(segments)].add(num)


def generate_deductions() -> dict[str, set[str]]:
    return {letter: all_letters.copy() for letter in all_letters}


class Observation(NamedTuple):
    signal_patterns: Tuple[set[str], ...]
    output_values: Tuple[set[str], ...]

    def letter_occurrences(self) -> dict[str, int]:
        return collections.Counter("".join("".join(s) for s in self.signal_patterns))

    @staticmethod
    def from_line(line: str) -> "Observation":
        left, right = line.split("|")
        signals = tuple(map(set, left.split()))
        values = tuple(map(set, right.split()))
        return Observation(signal_patterns=signals, output_values=values)


def parse_input(raw: str) -> list[Observation]:
    return list(map(Observation.from_line, raw.strip().splitlines()))


def part_1(raw: str):
    observations = parse_input(raw)

    segment_counts = collections.Counter(map(len, numbers_to_segments.values()))
    unique_segment_counts = [
        num for num in numbers_to_segments if segment_counts[num] == 1
    ]

    all_output_values = [val for obs in observations for val in obs.output_values]
    return sum(len(val) in unique_segment_counts for val in all_output_values)


def letters_in_numbers(nums: set[int]) -> set[str]:
    to_return = set()
    for n in nums:
        to_return.update(numbers_to_segments[n])
    return to_return


def solve_observation(obs: Observation) -> int:
    deductions = generate_deductions()
    unique_frequencies = {9: "f", 4: "e", 6: "b"}

    for count, unique_letter in unique_frequencies.items():
        for letter in all_letters:
            if obs.letter_occurrences()[letter] == count:
                deductions[letter] = set(unique_letter)
            else:
                deductions[letter].discard(unique_letter)

    for pattern in obs.signal_patterns:
        possible_numbers = numbers_by_segment_count[len(pattern)]

        possible_letters = set()
        for number in possible_numbers:
            possible_letters.update(numbers_to_segments[number])

        for letter in pattern:
            deductions[letter].intersection_update(possible_letters)

        if len(possible_numbers) == 1:
            for letter in all_letters - pattern:
                deductions[letter].difference_update(possible_letters)

    solved = {l: list(solutions)[0] for l, solutions in deductions.items()}

    digits = []
    for word in obs.output_values:
        mapped_letters = frozenset(map(solved.get, word))
        digits.append(segments_to_numbers[mapped_letters])

    return int("".join(map(str, digits)))


def part_2(raw: str) -> int:
    observations = parse_input(raw)
    return sum(map(solve_observation, observations))


if __name__ == "__main__":
    print(part_1(lib.get_input(8)))
    print(part_2(lib.get_input(8)))
