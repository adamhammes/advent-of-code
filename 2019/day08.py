import itertools

LAYER_WIDTH = 25
LAYER_HEIGHT = 6


def chunks(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def get_input():
    with open("inputs/day08.txt") as f:
        chars = f.read().strip()
        return chunks(list(map(int, chars)), LAYER_WIDTH * LAYER_HEIGHT)


def print_layer(layer):
    for i, digit in enumerate(layer):
        print(" " if digit == 0 else "█", end="")
        if i % LAYER_WIDTH == LAYER_WIDTH - 1:
            print()


def part1():
    max_zeroes = min(get_input(), key=lambda c: c.count(0))
    return max_zeroes.count(1) * max_zeroes.count(2)


def part2():
    layers = list(reversed(list(get_input())))
    base = list(layers[0])

    for layer in layers[1:]:
        for i, digit in enumerate(layer):
            if digit != 2:
                base[i] = digit

    return base


if __name__ == "__main__":
    print(part1())
    print_layer(part2())
