import collections

import lib


class Cave(str):
    def is_big_cave(self):
        return self.isupper()

    def is_small_cave(self):
        return self.islower()


CaveSystem = dict[Cave, set[Cave]]


def explore_caves(
    cave_system: CaveSystem, allow_double_explore=False
) -> list[list[Cave]]:
    start_state = Cave("start"), []
    queue = collections.deque([start_state])

    paths = []

    while queue:
        current_cave, current_path = queue.popleft()
        current_path.append(current_cave)

        if current_cave == "end":
            paths.append(current_path)
            continue

        seen_small_caves = list(filter(Cave.is_small_cave, current_path))
        already_double_explored = len(seen_small_caves) != len(set(seen_small_caves))
        neighbors_to_explore = [
            cave
            for cave in cave_system[current_cave]
            if cave.is_big_cave()
            or not current_path.count(cave)
            or (
                allow_double_explore
                and not already_double_explored
                and cave not in ["start", "end"]
            )
        ]

        for neighbor in neighbors_to_explore:
            neighbor_state = neighbor, current_path.copy()
            queue.append(neighbor_state)

    return paths


def parse_input(raw: str) -> CaveSystem:
    system = collections.defaultdict(set)

    for line in raw.strip().splitlines():
        left, right = line.strip().split("-")
        system[Cave(left)].add(Cave(right))
        system[Cave(right)].add(Cave(left))

    return system


def part_1(raw: str) -> int:
    cave_system = parse_input(raw)
    return len(explore_caves(cave_system))


def part_2(raw: str) -> int:
    cave_system = parse_input(raw)
    return len(explore_caves(cave_system, allow_double_explore=True))


if __name__ == "__main__":
    print(part_1(lib.get_input(12)))
    print(part_2(lib.get_input(12)))
