import dataclasses
import itertools
import math
import re
import typing


import lib


class Node(typing.NamedTuple):
    label: str
    left: str
    right: str


@dataclasses.dataclass
class Network:
    directions: str
    nodes: dict[str, Node]


def parse_input(raw: str) -> Network:
    directions, raw_nodes = raw.strip().split("\n\n")

    nodes = [Node(*re.findall(r"[A-Z]+", line)) for line in raw_nodes.splitlines()]
    return Network(nodes={node.label: node for node in nodes}, directions=directions)


def time_to_reach(network: Network, start: Node) -> int:
    directions_iter = itertools.cycle(network.directions)

    cur_node = start
    for step, c in enumerate(directions_iter, start=1):
        cur_node = network.nodes[cur_node.left if c == "L" else cur_node.right]

        if cur_node.label[-1] == "Z":
            return step


def part_1(raw: str) -> int:
    network = parse_input(raw)
    return time_to_reach(network, network.nodes["AAA"])


def part_2(raw: str) -> int:
    network = parse_input(raw)

    start_nodes = [node for node in network.nodes.values() if node.label[-1] == "A"]
    times = [time_to_reach(network, node) for node in start_nodes]
    return math.lcm(*times)


if __name__ == "__main__":
    print(part_1(lib.get_input(8)))
    print(part_2(lib.get_input(8)))
