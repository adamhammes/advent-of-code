import itertools

PHOTO_SIZE = 25 * 6


def chunks(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def get_input():
    with open("inputs/day08.txt") as f:
        chars = f.read().strip()
        return chunks(list(map(int, chars)), PHOTO_SIZE)


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

    printable = []
    digits = iter(base)
    for i in range(6):
        printable.append([])
        for j in range(25):
            digit = next(digits)
            printable[-1].append("█" if digit == 0 else "░")

    for row in printable:
        print("".join(map(str, row)))


if __name__ == "__main__":
    print(part1())
    part2()
