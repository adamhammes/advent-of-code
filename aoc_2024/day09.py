import typing
from typing import Tuple

import lib


class Block(typing.NamedTuple):
    is_file: bool
    id: int

    def as_str(self) -> str:
        return str(self.id) if self.is_file else "."


def parse_input(raw: str) -> list[Block]:
    nums = [int(c) for c in raw.strip()]
    blocks = []
    for index, size in enumerate(nums):
        is_file = not bool(index % 2)
        block_id = index // 2 if is_file else 0
        for _ in range(size):
            blocks.append(Block(is_file, block_id))

    return blocks


def print_nodes(nodes: list[Block]) -> str:
    return "".join(b.as_str() for b in nodes)


def find_first_free_block(nodes: list[Block], *, start_at=0) -> Tuple[int, Block]:
    for i in range(start_at, len(nodes) + 1):
        node = nodes[i]
        if not node.is_file:
            return i, node


def find_last_file(nodes: list[Block]) -> Tuple[int, Block]:
    for i, node in enumerate(reversed(nodes)):
        if node.is_file:
            return len(nodes) - i - 1, node


def compact_wide(nodes: list[Block]):
    free_index = 0
    while True:
        free_index, free_block = find_first_free_block(nodes, start_at=free_index)
        file_index, file_block = find_last_file(nodes)

        if free_index > file_index:
            return

        nodes[free_index] = file_block
        nodes[file_index] = free_block

        del nodes[-1]


def part_1(raw: str):
    nodes = parse_input(raw)
    compact_wide(nodes)

    return sum(i * block.id for i, block in enumerate(nodes))


if __name__ == "__main__":
    print(part_1(lib.get_input(9)))
