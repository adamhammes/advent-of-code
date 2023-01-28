import ast
import functools
import lib
from typing import Union

Packets = Union[int, list["Packets"]]


def parse_input(raw: str) -> list[tuple[Packets, Packets]]:
    packet_pairs = []

    for pairing in raw.strip().split("\n\n"):
        a, b = pairing.splitlines()
        packet_pairs.append((ast.literal_eval(a), ast.literal_eval(b)))

    return packet_pairs


def compare(p1: Packets, p2: Packets) -> int:
    match p1, p2:
        case int(), int():
            return p2 - p1
        case int(), list():
            return compare([p1], p2)
        case list(), int():
            return compare(p1, [p2])
        case list(), list():
            for sub_left, sub_right in zip(p1, p2):
                if c := compare(sub_left, sub_right):
                    return c

            return compare(len(p1), len(p2))

    return 1


def part_1(raw: str) -> int:
    total = 0
    for index, pairing in enumerate(parse_input(raw), start=1):
        comparison = compare(*pairing)
        if comparison > 0:
            total += index

    return total


def part_2(raw: str) -> int:
    pairings = parse_input(raw)
    flat_pairings = [p for pairing in pairings for p in pairing]

    flat_pairings.append([[2]])
    flat_pairings.append([[6]])

    sorted_pairings = list(
        sorted(flat_pairings, key=functools.cmp_to_key(compare), reverse=True)
    )

    index_2 = sorted_pairings.index([[2]]) + 1
    index_6 = sorted_pairings.index([[6]]) + 1
    return index_2 * index_6


if __name__ == "__main__":
    print(part_1(lib.get_input(13)))
    print(part_2(lib.get_input(13)))
