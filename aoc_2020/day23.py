from typing import *

import lib


class Node:
    next: "Node"
    value: int

    def __init__(self, value):
        self.value = value


class Game:
    current_cup: Node

    def __init__(self, values: List[int]):
        self.min_val, self.max_val = min(values), max(values)

        self.nodes: Dict[int, Node] = {value: Node(value) for value in values}

        for prev, _next in lib.window(values):
            self.nodes[prev].next = self.nodes[_next]

        self.current_cup: Node = self.nodes[values[0]]
        self.nodes[values[-1]].next = self.current_cup

    def get_next_three(self):
        cur = self.current_cup
        l = []
        for _ in range(3):
            l.append(cur.next)
            cur = cur.next

        self.current_cup.next = cur.next
        return l

    def destination_cup(self, next_three: List[Node]) -> Node:
        cur_label = self.current_cup.value

        i = 1
        while True:
            if cur_label - i < self.min_val:
                i = cur_label - self.max_val

            next_cup = cur_label - i
            if next_cup not in [n.value for n in next_three]:
                return self.nodes[next_cup]

            i += 1

    def play(self, n=1):
        for _ in range(n):
            picked_up = self.get_next_three()
            destination_cup = self.destination_cup(picked_up)
            destination_cup.next, picked_up[-1].next = (
                picked_up[0],
                destination_cup.next,
            )

            self.current_cup = self.current_cup.next

        return self

    def arrangement(self, n):
        values = []
        node = self.nodes[1]
        for _ in range(n):
            values.append(node.next)
            node = node.next

        return [n.value for n in values]


def part_1(raw: str):
    ints = list(map(int, raw))
    return "".join(map(str, Game(ints).play(100).arrangement(8)))


def part_2(raw: str):
    ints = list(map(int, raw)) + list(range(10, 1000000 + 1))

    return lib.product(Game(ints).play(10000000).arrangement(2))


if __name__ == "__main__":
    print(part_1("496138527"))
    print(part_2("496138527"))
