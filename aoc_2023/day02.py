import dataclasses
import functools

import lib


@dataclasses.dataclass
class BagContents:
    red: int
    blue: int
    green: int

    @staticmethod
    def from_random_sample(sample: str) -> "BagContents":
        parts = sample.strip().split(", ")

        contents = BagContents(0, 0, 0)
        for part in parts:
            raw_num, color = part.split(" ")
            contents.__dict__[color] = max(contents.__dict__[color], int(raw_num))

        return contents

    def fits_in(self, other: "BagContents") -> bool:
        return (
            self.blue <= other.blue
            and self.green <= other.green
            and self.red <= other.red
        )

    def maxify(self, other: "BagContents") -> "BagContents":
        self.blue = max(self.blue, other.blue)
        self.green = max(self.green, other.green)
        self.red = max(self.red, other.red)
        return self

    def power(self):
        return self.red * self.blue * self.green


def parse_input(raw: str) -> list[list[BagContents]]:
    to_return = []
    for line in raw.strip().splitlines():
        parts = line.split(": ")[1].split(";")
        to_return.append([BagContents.from_random_sample(p) for p in parts])

    return to_return


def part_1(raw: str) -> int:
    target = BagContents(red=12, green=13, blue=14)
    total = 0
    for game_id, parts in enumerate(parse_input(raw), start=1):
        final = functools.reduce(BagContents.maxify, parts)

        if final.fits_in(target):
            total += game_id

    return total


def part_2(raw: str) -> int:
    total = 0
    for game_id, parts in enumerate(parse_input(raw), start=1):
        final = functools.reduce(BagContents.maxify, parts)
        total += final.power()

    return total


if __name__ == "__main__":
    print(part_1(lib.get_input(2)))
    print(part_2(lib.get_input(2)))
