import collections
from dataclasses import dataclass, field
import re
from typing import Optional

import lib


@dataclass
class INode:
    is_dir: bool
    name: str
    file_size: int = 0
    parent: Optional["INode"] = None
    children: list["INode"] = field(default_factory=list)

    def computed_size(self):
        if self.is_dir:
            return sum(child.computed_size() for child in self.children)

        return self.file_size

    def flatten(self) -> list["INode"]:
        nodes = [self]
        for c in self.children:
            nodes += c.flatten()
        return nodes


def parse_ls_output(ls_line: str, cur_node: INode) -> INode:
    is_dir = ls_line.startswith("dir")
    digits = re.findall(r"\d+", ls_line)
    size = 0 if is_dir else int(digits[0])

    name = ls_line.split(" ", maxsplit=2)[1]

    return INode(is_dir=is_dir, name=name, file_size=size, parent=cur_node)


def parse_input(raw: str) -> INode:
    cur_node = root = INode(is_dir=True, name="/")

    lines = collections.deque(raw.strip().splitlines())

    while lines:
        line = lines.popleft()

        if line == "$ cd /":
            cur_node = root
        elif line == "$ cd ..":
            cur_node = cur_node.parent
        elif line.startswith("$ cd"):
            cd_dest = line.split(" ")[-1]
            for child in cur_node.children:
                if child.is_dir and child.name == cd_dest:
                    cur_node = child
                    break
        elif line == "$ ls":
            while lines and not lines[0].startswith("$"):
                line = lines.popleft()
                cur_node.children.append(parse_ls_output(line, cur_node))

    return root


def part_1(raw: str) -> int:
    nodes = parse_input(raw).flatten()
    directories = (n for n in nodes if n.is_dir)
    return sum(d.computed_size() for d in directories if d.computed_size() <= 100000)


def part_2(raw: str) -> int:
    root = parse_input(raw)
    need_to_delete = 30000000 - (70000000 - root.computed_size())

    valid_nodes_to_delete = [
        n for n in root.flatten() if n.is_dir and n.computed_size() > need_to_delete
    ]
    return min(n.computed_size() for n in valid_nodes_to_delete)


if __name__ == "__main__":
    print(part_1(lib.get_input(7)))
    print(part_2(lib.get_input(7)))
