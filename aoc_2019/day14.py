import collections
import math

ONE_TRILLION = 1000000000000


def get_input():
    with open("inputs/day14.txt") as f:
        return f.read()


Chemical = collections.namedtuple("Chemical", ["name", "quantity"])


def parse_chemical(chemical):
    num, name = chemical.strip().split(" ")
    return Chemical(name, int(num))


def parse_input(_in: str):
    dependencies = dict()

    for line in _in.strip().splitlines():
        reactants, product = line.split(" => ")

        reactants = list(map(parse_chemical, reactants.split(", ")))
        product = parse_chemical(product)

        assert product.name not in dependencies
        dependencies[product.name] = (reactants, product)

    return dependencies


def calculate_ore_cost(dependencies, chemical, excess):
    name, quantity_needed = chemical

    if name == "ORE":
        return quantity_needed

    excess_of_chemical = excess[name]
    quantity_needed -= excess_of_chemical
    excess[name] = 0

    reactants, product = dependencies[name]
    run_x_times = math.ceil(quantity_needed / product.quantity)

    excess[name] = run_x_times * product.quantity - quantity_needed

    cost = 0
    for reactant in reactants:
        required = Chemical(reactant.name, reactant.quantity * run_x_times)
        cost += calculate_ore_cost(dependencies, required, excess=excess)

    return cost


def part1(_in=None):
    if not _in:
        _in = get_input()

    dependencies = parse_input(_in)

    return calculate_ore_cost(
        dependencies, Chemical("FUEL", 1), excess=collections.defaultdict(int)
    )


def part2(_in=None):

    if not _in:
        _in = get_input()

    dependencies = parse_input(_in)

    low, high = 1, ONE_TRILLION + 1

    while low + 1 < high:
        value_to_guess = (low + high) // 2
        ore = calculate_ore_cost(
            dependencies,
            chemical=("FUEL", value_to_guess),
            excess=collections.defaultdict(int),
        )

        if ore == ONE_TRILLION:
            return value_to_guess
        elif ore < ONE_TRILLION:
            low, high = value_to_guess, high
        elif ore > ONE_TRILLION:
            low, high = low, value_to_guess

    return low


if __name__ == "__main__":
    print(part1())
    print(part2())
