import enum
import typing


class TerminationReason(enum.Enum):
    InfiniteLoop = enum.auto()
    Completed = enum.auto()


class TapeResult(typing.NamedTuple):
    result: TerminationReason
    accumulator: int


def get_input():
    with open("inputs/day08.txt") as f:
        return f.read()


def run_program(lines: typing.List[str]) -> TapeResult:
    seen_lines = set()
    index, accumulator = 0, 0

    while index < len(lines):
        if index in seen_lines:
            return TapeResult(TerminationReason.InfiniteLoop, accumulator)

        seen_lines.add(index)

        command, raw_value = lines[index].split()
        value = int(raw_value)

        if command == "nop":
            index += 1
        elif command == "acc":
            accumulator += value
            index += 1
        elif command == "jmp":
            index += value

    return TapeResult(TerminationReason.Completed, accumulator)


def part_1():
    lines = get_input().splitlines()
    return run_program(lines).accumulator


def part_2():
    lines = get_input().splitlines()
    indexes_to_flip = [i for i, val in enumerate(lines) if "nop" in val or "jmp" in val]

    for index in indexes_to_flip:
        cloned = lines[:]
        old_command, val = cloned[index].split()

        new_command = "nop" if old_command == "jmp" else "jmp"
        cloned[index] = f"{new_command} {val}"

        termination_reason, accumulator = run_program(cloned)
        if termination_reason == TerminationReason.Completed:
            return accumulator


if __name__ == "__main__":
    print(part_1())
    print(part_2())
