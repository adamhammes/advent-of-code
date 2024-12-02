import typing

import lib


class Report(typing.NamedTuple):
    values: list[int]

    def diffs(self) -> list[int]:
        return [b - a for a, b in zip(self.values, self.values[1:])]

    def is_safe(self):
        all_decreasing = all(n < 0 for n in self.diffs())
        all_increasing = all(n > 0 for n in self.diffs())

        in_range = all(abs(n) in [1, 2, 3] for n in self.diffs())
        return in_range and (all_increasing or all_decreasing)


def parse_input(raw: str) -> list[Report]:
    return [Report(lib.extract_ints(line)) for line in raw.strip().splitlines()]


def part_1(raw: str) -> int:
    reports = parse_input(raw)
    return sum(report.is_safe() for report in reports)


def part_2(raw: str) -> int:
    reports = parse_input(raw)

    count = 0
    for report in reports:
        for i in range(len(report.values)):
            value_copy = report.values.copy()
            value_copy.pop(i)
            modified_report = Report(value_copy)

            if modified_report.is_safe():
                count += 1
                break

    return count


if __name__ == "__main__":
    print(part_1(lib.get_input(2)))
    print(part_2(lib.get_input(2)))
