from day19 import *

EXAMPLE_BLUE_PRINT_1 = (
    "Blueprint 1:"
    "Each ore robot costs 4 ore."
    "Each clay robot costs 2 ore."
    "Each obsidian robot costs 3 ore and 14 clay."
    "Each geode robot costs 2 ore and 7 obsidian."
)

EXAMPLE_BLUE_PRINT_2 = (
    "Blueprint 2:"
    "Each ore robot costs 2 ore."
    "Each clay robot costs 3 ore."
    "Each obsidian robot costs 3 ore and 8 clay."
    "Each geode robot costs 3 ore and 12 obsidian."
)


def test_parse_line():
    blueprint = parse_blueprint(EXAMPLE_BLUE_PRINT_1)

    assert blueprint == Blueprint(
        robot_id=1,
        ore_robot=Robot(ore=4, is_ore_robot=True),
        clay_robot=Robot(ore=2, is_clay_robot=True),
        obsidian_robot=Robot(ore=3, clay=14, is_obsidian_robot=True),
        geode_robot=Robot(ore=2, obsidian=7, is_geode_robot=True),
    )


def test_build_robot():
    blueprint = parse_blueprint(EXAMPLE_BLUE_PRINT_1)

    first_clay_robot = ConstructionState(remaining_time=24).build_robot(
        blueprint.clay_robot
    )

    assert first_clay_robot == ConstructionState(
        remaining_time=21, ore=1, ore_robots=1, clay_robots=1
    )

    second_clay_robot = first_clay_robot.build_robot(blueprint.clay_robot)

    assert second_clay_robot == ConstructionState(
        remaining_time=19, ore=1, clay=2, clay_robots=2
    )


def test_evaluate_blueprint():
    assert evaluate_blueprint(parse_blueprint(EXAMPLE_BLUE_PRINT_1), 24) == 9
    assert evaluate_blueprint(parse_blueprint(EXAMPLE_BLUE_PRINT_2), 24) == 12


def test_evaluate_long_blueprint():
    assert evaluate_blueprint(parse_blueprint(EXAMPLE_BLUE_PRINT_1), 32) == 56


def test_part_1():
    sample_input = EXAMPLE_BLUE_PRINT_1 + "\n" + EXAMPLE_BLUE_PRINT_2
    assert part_1(sample_input) == 33
