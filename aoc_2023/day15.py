import dataclasses
import re

import lib


def HASH(cs: str) -> int:
    total = 0
    for c in cs:
        total += ord(c)
        total *= 17
        total %= 256

    return total


@dataclasses.dataclass
class Instruction:
    string: str
    label: str = dataclasses.field(init=False)
    operation: str = dataclasses.field(init=False)
    focal_length: int | None = dataclasses.field(init=False)

    def __post_init__(self):
        self.label = re.split("[-=]", self.string)[0]
        self.operation = "-" if "-" in self.string else "="

        ints = lib.extract_ints(self.string)
        if not ints and self.operation == "=":
            print("here")
        self.focal_length = (
            lib.extract_ints(self.string)[0] if self.operation == "=" else None
        )

    def total_hash(self) -> int:
        return HASH(self.string)

    def label_hash(self) -> int:
        return HASH(self.label)


def parse_input(raw: str) -> list[Instruction]:
    return list(map(Instruction, raw.strip().split(",")))


def part_1(raw: str) -> int:
    return sum(instruction.total_hash() for instruction in parse_input(raw))


def part_2(raw: str) -> int:
    boxes: list[list[Instruction]] = [[] for _ in range(256)]

    for instruction in parse_input(raw):
        boxi = instruction.label_hash()
        box = boxes[boxi]
        if instruction.operation == "-":
            box = [i for i in boxes[boxi] if i.label != instruction.label]
        else:
            matches = [i for i in box if i.label == instruction.label]
            if matches:
                matches[0].focal_length = instruction.focal_length
            else:
                box.append(instruction)

        boxes[boxi] = box

    total = 0
    for boxi, box in enumerate(boxes, start=1):
        for sloti, instruction in enumerate(box, start=1):
            total += boxi * sloti * instruction.focal_length

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(15)))
    print(part_2(lib.get_input(15)))
