import functools
import typing

import lib

Groups = tuple[int, ...]


class Spring(typing.NamedTuple):
    record: str
    groups: Groups

    def expand(self, n: int) -> "Spring":
        record = "?".join([self.record] * n)
        return Spring(record, self.groups * n)


def is_viable(record: str, groups: Groups):
    min_length = len(groups) - 1 + sum(groups)
    return len(record) > min_length


@functools.lru_cache
def possible_placements(record: str, group_size: int, force=False) -> list[str]:
    if group_size == 0:  # base case
        if not record:
            return [""]
        if record[0] == "#":
            return []
        return ["." + record[1:]]

    if not record:  # no more string left, but there is group left, prune
        return []

    if record[0] == ".":
        if force:  # we ran into a blank while trying to keep a group going, bail
            return []
        # keep looking until we see an interesting character
        return [p for p in possible_placements(record.lstrip("."), group_size)]

    if record[0] == "#":  # eat the #, group size is one smaller
        return [p for p in possible_placements(record[1:], group_size - 1, force=True)]

    # ????
    _with = possible_placements(record[1:], group_size - 1, force=True)
    if force:
        return _with

    _without = possible_placements("." + record[1:], group_size)
    return list(set(_without + _with))


@functools.lru_cache
def count(record: str, groups: tuple[int, ...]):
    if len(groups) == 0:
        return "#" not in record

    places = possible_placements(record, groups[0])
    if not places:
        return 0

    groups = groups[1:]
    return sum(count(place, groups) for place in places if is_viable(place, groups))


def parse_input(raw: str) -> list[Spring]:
    return [
        Spring(record=line.split(" ")[0], groups=tuple(lib.extract_ints(line)))
        for line in raw.strip().splitlines()
    ]


def part_1(raw: str) -> int:
    return sum(count(spring.record, spring.groups) for spring in parse_input(raw))


def part_2(raw: str) -> int:
    springs = [spring.expand(5) for spring in parse_input(raw)]
    return sum(count(spring.record, spring.groups) for spring in springs)


if __name__ == "__main__":
    print(part_1(lib.get_input(12)))
    print(part_2(lib.get_input(12)))
