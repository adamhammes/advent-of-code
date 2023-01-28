import collections
import itertools

from lib import Tape


def get_input():
    with open("inputs/day07.txt") as f:
        return list(map(int, f.read().split(",")))


def calculate_amplitude(settings):
    previous_signal = 0

    for setting in settings:
        input_values = (i for i in [setting, previous_signal])
        tape = Tape(get_input(), input_values=input_values)
        tape.run()
        previous_signal = tape.output[-1]

    return previous_signal


def calculate_amplitude_2(settings):
    tapes = []

    for setting in settings:
        tapes.append(Tape(get_input(), input_values=[setting]))

    tapes[0].add_input(0)

    while all(not tape.finished for tape in tapes):
        for tape_index, tape in enumerate(tapes):
            should_continue = tape.step()
            while should_continue and not tape.finished:
                should_continue = tape.step()

            output = tape.output[-1]
            tapes[(tape_index + 1) % 5].add_input(output)

    return tapes[-1].output[-1]


def part1():
    phase_settings = itertools.permutations(range(5))
    return max(map(calculate_amplitude, phase_settings))


def part2():
    phase_settings = itertools.permutations(range(5, 10))
    return max(map(calculate_amplitude_2, phase_settings))


if __name__ == "__main__":
    print(part1())
    print(part2())
