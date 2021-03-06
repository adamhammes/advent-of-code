from lib import chunks, first

LAYER_WIDTH = 25
LAYER_HEIGHT = 6


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
    rendered_pixel = lambda pixel_stack: first(pixel_stack, lambda p: p != 2)
    return map(rendered_pixel, zip(*get_input()))


if __name__ == "__main__":
    print(part1())
    print_layer(part2())
