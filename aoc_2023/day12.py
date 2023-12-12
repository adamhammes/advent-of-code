import collections
import re
import typing

import lib


class Spring(typing.NamedTuple):
    record: str
    groups: tuple[int, ...]

    def is_determinate(self) -> bool:
        return "?" not in self.record

    def replace_indeterminate(self, c: str) -> "Spring":
        new_record = self.record.replace("?", c, 1)
        return Spring(record=new_record, groups=self.groups)

    def guesses(self) -> list["Spring"]:
        guesses = []

        queue = collections.deque([self])
        while queue:
            current = queue.popleft()

            if current.is_determinate():
                guesses.append(current)
            else:
                queue.append(current.replace_indeterminate("#"))
                queue.append(current.replace_indeterminate("."))

        return guesses

    def is_coherent(self) -> bool:
        actual_groups = tuple(
            len(group) for group in re.split(r"\.+", self.record) if group
        )
        return actual_groups == self.groups

    def num_coherent(self) -> int:
        return sum(guess.is_coherent() for guess in self.guesses())


def parse_input(raw: str) -> list[Spring]:
    return [
        Spring(record=line.split(" ")[0], groups=tuple(lib.extract_ints(line)))
        for line in raw.strip().splitlines()
    ]


def part_1(raw: str) -> int:
    return sum(spring.num_coherent() for spring in parse_input(raw))


if __name__ == "__main__":
    print(part_1(lib.get_input(12)))
