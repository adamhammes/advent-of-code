import heapq
import typing
from typing import Tuple

import lib


class Block(typing.NamedTuple):
    is_file: bool
    id: int
    size: int

    def as_str(self) -> str:
        return str(self.id) if self.is_file else "."


def parse_input(raw: str, *, wide: bool) -> list[Block]:
    nums = [int(c) for c in raw.strip()]
    blocks = []
    for index, size in enumerate(nums):
        is_file = not bool(index % 2)
        block_id = index // 2 if is_file else 0
        if wide:
            for _ in range(size):
                blocks.append(Block(is_file, block_id, 1))
        else:
            blocks.append(Block(is_file, block_id, size))

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


def the_thing(blocks: list[Block]) -> int:
    free_lists: list[list[int]] = [[] for _ in range(10)]
    file_indices = {}
    current_index = 0
    for block in blocks:
        if block.is_file:
            file_indices[block] = current_index
        else:
            heapq.heappush(free_lists[block.size], current_index)

        current_index += block.size

    for file in reversed([b for b in blocks if b.is_file]):
        free_sizes = [
            (free_spaces[0], size)
            for size, free_spaces in enumerate(free_lists)
            if free_spaces and size >= file.size
        ]
        if not free_sizes:
            continue
        new_index, free_size = min(free_sizes)
        if new_index > file_indices[file]:
            continue

        heapq.heappop(free_lists[free_size])
        remaining_size = free_size - file.size
        file_indices[file] = new_index
        if remaining_size:
            heapq.heappush(free_lists[remaining_size], new_index + file.size)

    total = 0
    for block, start_index in file_indices.items():
        for i in range(block.size):
            total += block.id * (start_index + i)

    return total


def part_1(raw: str):
    nodes = parse_input(raw, wide=True)
    compact_wide(nodes)

    return sum(i * block.id for i, block in enumerate(nodes))


def part_2(raw: str):
    blocks = parse_input(raw, wide=False)
    return the_thing(blocks)


if __name__ == "__main__":
    print(part_1(lib.get_input(9)))
    print(part_2(lib.get_input(9)))
