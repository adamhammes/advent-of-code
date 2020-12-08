import collections
import re
import typing as t


Color = str
Rule = t.Tuple[Color, int]
Input = t.Iterable[t.Tuple[Color, t.List[Rule]]]
ColorGraph = t.Dict[Color, t.Dict[Color, int]]


def read_into_graph(challenge: Input, inversed: bool) -> ColorGraph:
    graph = collections.defaultdict(dict)
    for container, rules in challenge:
        for color, quantity in rules:
            if inversed:
                graph[color][container] = quantity
            else:
                graph[container][color] = quantity

    return graph


def get_input(inversed: bool) -> ColorGraph:
    with open("inputs/day07.txt") as f:
        challenge: Input = map(parse_line, f.readlines())

    return read_into_graph(challenge, inversed)


def parse_line(line: str) -> t.Tuple[Color, t.List[Rule]]:
    outer_color, rest = line.strip().split(" bags contain ")
    if "no other bags" in rest:
        return outer_color, []

    rule_pattern = re.compile(r"(\d+) (.*?) bag")
    return outer_color, [
        (color, int(raw_quantity)) for raw_quantity, color in rule_pattern.findall(rest)
    ]


def part_1():
    graph = get_input(inversed=True)
    seen_colors = set()
    colors_to_check = collections.deque(["shiny gold"])

    while colors_to_check:
        current_color = colors_to_check.popleft()
        seen_colors.add(current_color)
        colors_to_check += graph[current_color].keys() - seen_colors

    return len(seen_colors) - 1


def part_2() -> int:
    graph = get_input(inversed=False)
    colors_to_check = collections.deque([(1, "shiny gold")])
    bag_count = 0

    while colors_to_check:
        quantity, current_color = colors_to_check.popleft()
        bag_count += quantity

        colors_to_check += quantity * [
            (quantity, color) for color, quantity in graph[current_color].items()
        ]

    return bag_count - 1


if __name__ == "__main__":
    print(part_1())
    print(part_2())
