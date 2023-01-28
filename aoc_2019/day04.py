def split_digits(num):
    return list(map(int, str(num)))


def get_input():
    start, end = 357253, 892942
    return list(map(split_digits, range(start + 1, end)))


def never_decreases(digits):
    return all(x <= y for x, y in zip(digits, digits[1:]))


def contains_adjacent_pair(digits):
    return any(x == y for x, y in zip(digits, digits[1:]))


def limited_to_pair(digits):
    string = "".join(map(str, digits))
    pairs = (x for x, y in zip(digits, digits[1:]) if x == y)

    return any(str(digit) * 3 not in string for digit in pairs)


def part_1():
    for digit_set in get_input():
        if never_decreases(digit_set) and contains_adjacent_pair(digit_set):
            yield digit_set


def part_2():
    return filter(limited_to_pair, part_1())


if __name__ == "__main__":
    print(len(list(part_1())))
    print(len(list(part_2())))
