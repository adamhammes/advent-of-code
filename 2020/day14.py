import enum
import itertools
import re
import typing

import lib


class BitMask(enum.IntEnum):
    Zero = 0
    One = 1
    Indeterminate = 2

    @staticmethod
    def from_char(c: str):
        return {"0": BitMask.Zero, "1": BitMask.One, "X": BitMask.Indeterminate}[c]


class MemoryMode(enum.Enum):
    Fixed = enum.auto()
    Floating = enum.auto()


def to_bitstring(i: int) -> typing.List[str]:
    return list(f"{i:b}".zfill(36))


def from_bitstring(s: typing.List[int]) -> int:
    bit_string = "".join("1" if bit else "0" for bit in s)
    return int(bit_string, 2)


class Program:
    memory: typing.Dict[int, int]
    mask: typing.List[BitMask]
    mode: MemoryMode

    def __init__(self, mode: MemoryMode):
        self.mode = mode
        self.memory = dict()

    def set_mask(self, mask: str):
        self.mask = list(map(BitMask.from_char, mask))

    def apply_bitmask(self, value: int) -> int:
        padded_value = to_bitstring(value)
        set_bits = []

        for mask_value, bit in zip(self.mask, padded_value):
            if (
                mask_value == BitMask.Indeterminate
                or mask_value == BitMask.Zero
                and self.mode == MemoryMode.Floating
            ):
                set_bits.append(bit == "1")
            else:
                set_bits.append(mask_value)

        return from_bitstring(set_bits)

    def set_floating_memory(self, address: int, value: int):
        indeterminate_indices = [
            i
            for i, mask_value in enumerate(self.mask)
            if mask_value == BitMask.Indeterminate
        ]

        num_indeterminate_indices = len(indeterminate_indices)
        perms = list(itertools.product(["0", "1"], repeat=num_indeterminate_indices))

        address_bitstring = to_bitstring(self.apply_bitmask(address))
        for perm in perms:
            current_address = address_bitstring[:]

            for on_or_off, index in zip(perm, indeterminate_indices):
                current_address[index] = on_or_off

            bits = [b == "1" for b in current_address]
            self.memory[from_bitstring(bits)] = value

    def read_line(self, line: str):
        if line.startswith("mask = "):
            self.set_mask(line.split("mask = ")[1])
        else:
            address, value = list(map(int, re.findall(r"\d+", line)))

            if self.mode == MemoryMode.Fixed:
                self.memory[address - 1] = self.apply_bitmask(value)
            else:
                self.set_floating_memory(address, value)

    def sum(self) -> int:
        return sum(self.memory.values())


def part_1(raw: str):
    prog = Program(MemoryMode.Fixed)
    [prog.read_line(line) for line in raw.splitlines()]
    return prog.sum()


def part_2(raw: str):
    prog = Program(MemoryMode.Floating)
    [prog.read_line(line) for line in raw.splitlines()]
    return prog.sum()


if __name__ == "__main__":
    print(part_1(lib.get_input(14)))
    print(part_2(lib.get_input(14)))
