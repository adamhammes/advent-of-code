import re
from typing import NamedTuple

import lib

EXAMPLE_1 = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

Board = list[list[str]]


class Instruction(NamedTuple):
    quantity: int
    from_position: int
    to_position: int


def parse_input(raw: str):
    raw_board, raw_instructions = raw.strip("\n").split("\n\n")

    transposed_board = [list(line) for line in raw_board.splitlines()]

    stacks: Board = []
    for line in list(zip(*transposed_board[::-1])):
        if line[0].isdigit():
            stacks.append([c for c in line if c.isalpha()])

    instructions = []
    for line in raw_instructions.splitlines():
        quantity, from_pos, to_pos = re.findall(r"\d+", line)
        instruction = Instruction(int(quantity), int(from_pos) - 1, int(to_pos) - 1)
        instructions.append(instruction)

    return stacks, instructions


def part_1(raw: str) -> str:
    board, instructions = parse_input(raw)

    for instruction in instructions:
        for _ in range(instruction.quantity):
            popped = board[instruction.from_position].pop()
            board[instruction.to_position].append(popped)

    return "".join(crate[-1] for crate in board)


def part_2(raw: str) -> str:
    board, instructions = parse_input(raw)

    for instruction in instructions:
        to_move = board[instruction.from_position][-instruction.quantity :]
        board[instruction.from_position] = board[instruction.from_position][
            : -instruction.quantity
        ]

        board[instruction.to_position] += to_move
    return "".join(crate[-1] for crate in board)


if __name__ == "__main__":
    print(part_1(lib.get_input(5)))
    print(part_2(lib.get_input(5)))
