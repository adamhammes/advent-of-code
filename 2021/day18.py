import itertools
import math
from typing import Optional, Union

import lib


class Number:
    parent: Optional["Number"] = None
    left: Optional["Number"]
    right: Optional["Number"]
    value: Optional[int]

    def __repr__(self):
        if self.is_leaf():
            return str(self.value)

        return f"[{repr(self.left)},{repr(self.right)}]"

    def root(self) -> "Number":
        return self if self.parent is None else self.parent.root()

    def traverse(self) -> list["Number"]:
        if self.is_leaf():
            return [self]

        return self.left.traverse() + self.right.traverse()

    def __init__(self, *, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

        if self.left is not None:
            self.left.parent = self

        if self.right is not None:
            self.right.parent = self

    def __eq__(self, other: "Number"):
        return (
            self.left == other.left
            and self.right == other.right
            and self.value == other.value
        )

    def clone(self) -> "Number":
        return parse_number(str(self))

    def is_leaf(self):
        return self.value is not None

    def explode(self, level: int = 1) -> bool:
        if self.is_leaf():
            return False

        if level <= 4:
            return self.left.explode(level + 1) or self.right.explode(level + 1)

        in_order = self.root().traverse()
        l_index = [i for i, num in enumerate(in_order) if num is self.left][0]
        r_index = [i for i, num in enumerate(in_order) if num is self.right][0]

        if l_index > 0:
            in_order[l_index - 1].value += self.left.value

        if r_index < len(in_order) - 1:
            in_order[r_index + 1].value += self.right.value

        self.left = None
        self.right = None
        self.value = 0

        return True

    def split(self) -> bool:
        if not self.is_leaf():
            return self.left.split() or self.right.split()

        if self.is_leaf() and self.value < 10:
            return False

        lval, rval = math.floor(self.value / 2), math.ceil(self.value / 2)
        self.value = None
        self.left, self.right = Number(value=lval), Number(value=rval)
        self.left.parent = self
        self.right.parent = self

        return True

    def add(self, other: "Number") -> "Number":
        n = Number(left=self.clone(), right=other.clone())

        while n.explode() or n.split():
            pass

        return n

    def magnitude(self) -> int:
        if self.is_leaf():
            return self.value

        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def parse_recursive(_in: Union[list[Number], int]) -> Number:
    if isinstance(_in, int):
        return Number(value=_in)

    left, right = _in
    return Number(left=parse_recursive(left), right=parse_recursive(right))


def parse_number(raw: str) -> Number:
    raw_list = eval(raw.strip())
    return parse_recursive(raw_list)


def parse_input(raw: str) -> list[Number]:
    return list(map(parse_number, raw.strip().splitlines()))


def add_many(nums: list[Number]) -> Number:
    current, rest = nums[0], nums[1:]

    for num in rest:
        current = current.add(num)

    return current


def part_1(raw: str) -> int:
    return add_many(parse_input(raw)).magnitude()


def part_2(raw: str) -> int:
    nums = parse_input(raw)

    highest = 0
    for n1, n2 in itertools.permutations(nums, 2):
        highest = max(n1.add(n2).magnitude(), highest)

    return highest


if __name__ == "__main__":
    print(part_1(lib.get_input(18)))
    print(part_2(lib.get_input(18)))
