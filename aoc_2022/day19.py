import collections
import re
import typing as t

import math

import lib


class Robot(t.NamedTuple):
    ore: int = 0
    clay: int = 0
    obsidian: int = 0

    is_ore_robot: bool = False
    is_clay_robot: bool = False
    is_obsidian_robot: bool = False
    is_geode_robot: bool = False


class Blueprint(t.NamedTuple):
    robot_id: int
    ore_robot: Robot
    clay_robot: Robot
    obsidian_robot: Robot
    geode_robot: Robot


def parse_blueprint(line: str) -> Blueprint:
    sentences = re.split("[.:]", line)

    robot_id = lib.extract_ints(sentences[0])[0]
    ore_robot = Robot(ore=lib.extract_ints(sentences[1])[0], is_ore_robot=True)
    clay_robot = Robot(ore=lib.extract_ints(sentences[2])[0], is_clay_robot=True)

    obsidian_costs = lib.extract_ints(sentences[3])
    obsidian_robot = Robot(
        ore=obsidian_costs[0], clay=obsidian_costs[1], is_obsidian_robot=True
    )

    geode_costs = lib.extract_ints(sentences[4])
    geode_robot = Robot(
        ore=geode_costs[0], obsidian=geode_costs[1], is_geode_robot=True
    )

    return Blueprint(robot_id, ore_robot, clay_robot, obsidian_robot, geode_robot)


RobotType = (
    t.Literal["ore"] | t.Literal["clay"] | t.Literal["obsidian"] | t.Literal["geode"]
)


class ConstructionState(t.NamedTuple):
    remaining_time: int = 0

    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geodes: int = 0

    ore_robots: int = 1
    clay_robots: int = 0
    obsidian_robots: int = 0
    geode_robots: int = 0

    def potential_geodes(self) -> int:
        return self.geodes + sum(
            i + self.geode_robots for i in range(self.remaining_time)
        )

    def num_geodes(self) -> int:
        return self.geodes + self.geode_robots * self.remaining_time

    def time_to_build(self, cost: Robot) -> int:
        remaining_ore = cost.ore - self.ore
        remaining_clay = cost.clay - self.clay
        remaining_obsidian = cost.obsidian - self.obsidian

        time_per_material = [
            remaining_ore / self.ore_robots if self.ore_robots else 0,
            remaining_clay / self.clay_robots if self.clay_robots else 0,
            remaining_obsidian / self.obsidian_robots if self.obsidian_robots else 0,
        ]

        time_per_material = [max(time, 0) for time in time_per_material]

        longest_time = max(time_per_material)
        return int(math.ceil(longest_time)) + 1

    def build_robot(self, robot: Robot) -> t.Optional["ConstructionState"]:
        if robot.clay > 0 and not self.clay_robots:
            return None

        if robot.obsidian > 0 and not self.obsidian_robots:
            return None

        elapsed_time = self.time_to_build(robot)

        return ConstructionState(
            remaining_time=self.remaining_time - elapsed_time,
            ore=self.ore + elapsed_time * self.ore_robots - robot.ore,
            clay=self.clay + elapsed_time * self.clay_robots - robot.clay,
            obsidian=self.obsidian
            + elapsed_time * self.obsidian_robots
            - robot.obsidian,
            geodes=self.geodes + elapsed_time * self.geode_robots,
            ore_robots=self.ore_robots + robot.is_ore_robot,
            clay_robots=self.clay_robots + robot.is_clay_robot,
            obsidian_robots=self.obsidian_robots + robot.is_obsidian_robot,
            geode_robots=self.geode_robots + robot.is_geode_robot,
        )

    def generate_children(
        self, blueprint: Blueprint, must_outproduce: int
    ) -> list["ConstructionState"]:
        robots = [
            blueprint.ore_robot,
            blueprint.clay_robot,
            blueprint.obsidian_robot,
            blueprint.geode_robot,
        ]

        max_ore_requirement = max(robot.ore for robot in robots)
        max_clay_requirement = max(robot.clay for robot in robots)
        max_obsidian_requirement = max(robot.obsidian for robot in robots)

        children = [self.build_robot(blueprint.geode_robot)]

        if self.ore_robots < max_ore_requirement:
            children.append(self.build_robot(blueprint.ore_robot))

        if self.clay_robots < max_clay_requirement:
            children.append(self.build_robot(blueprint.clay_robot))

        if self.obsidian_robots < max_obsidian_requirement:
            children.append(self.build_robot(blueprint.obsidian_robot))

        return [
            child
            for child in children
            if child is not None
            and child.remaining_time >= 0
            and child.potential_geodes() > must_outproduce
        ]


def parse_input(raw: str) -> list[Blueprint]:
    raw_blueprints = raw.strip().splitlines()
    return list(map(parse_blueprint, raw_blueprints))


def evaluate_blueprint(blueprint: Blueprint, time: int) -> int:
    states_to_visit = collections.deque([ConstructionState(remaining_time=time)])
    best_score_so_far = 0

    while states_to_visit:
        current_state = states_to_visit.popleft()
        best_score_so_far = max(best_score_so_far, current_state.num_geodes())
        states_to_visit += current_state.generate_children(blueprint, best_score_so_far)

    return best_score_so_far


def part_1(raw: str) -> int:
    blueprints = parse_input(raw)

    return sum(
        blueprint.robot_id * evaluate_blueprint(blueprint, 24)
        for blueprint in blueprints
    )


def part_2(raw: str) -> int:
    blueprints = parse_input(raw)[:3]
    return math.prod(evaluate_blueprint(blueprint, 32) for blueprint in blueprints)


if __name__ == "__main__":
    print(part_1(lib.get_input(19)))
    print(part_2(lib.get_input(19)))
