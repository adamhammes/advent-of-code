import lib


class Node:
    left: "Node"
    right: "Node"
    val: int

    def __init__(self, val: int):
        self.val = val

    def __str__(self) -> str:
        return f"Node({self.val})"


def parse_input(raw: str) -> [Node]:
    nums = [int(line) for line in raw.strip().splitlines()]
    nodes = [Node(n) for n in nums]

    for n1, n2 in zip(nodes, nodes[1:] + [nodes[0]]):
        n1.right = n2
        n2.left = n1

    return nodes


def place_between(node: Node, left: Node, right: Node):
    node.left.right = node.right
    node.right.left = node.left

    node.left = left
    left.right = node

    node.right = right
    right.left = node


def encrypt_nodes(nodes: [Node]):
    for original_node in nodes:
        node = original_node
        real_movement = node.val % (len(nodes) - 1)

        if real_movement:
            for _ in range(real_movement):
                node = node.right

            place_between(original_node, node, node.right)


def find_coordinates(nodes: [Node]) -> [int]:
    n = [n for n in nodes if n.val == 0][0]
    coordinates = []
    for _ in range(3):
        for _ in range(1000):
            n = n.right

        coordinates.append(n.val)

    return coordinates


def part_1(raw: str):
    nodes = parse_input(raw)
    encrypt_nodes(nodes)
    return sum(find_coordinates(nodes))


def part_2(raw: str):
    nodes = parse_input(raw)
    for n in nodes:
        n.val *= 811589153

    for _ in range(10):
        encrypt_nodes(nodes)

    return sum(find_coordinates(nodes))


if __name__ == "__main__":
    print(part_1(lib.get_input(20)))
    print(part_2(lib.get_input(20)))
