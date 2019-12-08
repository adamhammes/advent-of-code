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
        return chunks(map(int, chars), LAYER_WIDTH * LAYER_HEIGHT)


def print_layer(layer):
    printable_digit = lambda d: "█" if d else " "
    for chunk in chunks(layer, LAYER_WIDTH):
        print("".join(map(printable_digit, chunk)))


def part1():
    min_zeroes = min(get_input(), key=lambda c: c.count(0))
    return min_zeroes.count(1) * min_zeroes.count(2)


def part2():
    base = [2] * LAYER_WIDTH * LAYER_HEIGHT

    for layer in reversed(list(get_input())):
        for i, digit in enumerate(layer):
            if digit != 2:
                base[i] = digit

    return base


if __name__ == "__main__":
    print(part1())
    print_layer(part2())
