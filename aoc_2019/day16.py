BASE_PATTERN = [0, 1, 0, -1]


def get_input():
    with open("inputs/day16.txt") as f:
        content = f.read().strip()
        return list(map(int, content))


def generate_pattern(_position, num_values):
    position = _position + 1
    pattern = []

    num_iterations = num_values // (position * len(BASE_PATTERN)) + 1

    for _ in range(num_iterations):
        for value in BASE_PATTERN:
            pattern += [value] * position

    return pattern[1 : num_values + 1]


def apply_pattern(nums):
    new_nums = []

    for i in range(len(nums)):
        pattern_at_position = generate_pattern(i, len(nums))
        val = abs(sum(p * v for p, v in zip(pattern_at_position, nums))) % 10
        new_nums.append(val)

    return new_nums


def iterate_pattern(start, num_iterations):
    nums = start
    for i in range(num_iterations):
        nums = apply_pattern(nums)
        print("".join(map(str, nums[:30])))

    return nums


def part1(_in=get_input()):
    final_pattern = iterate_pattern(_in, 100)
    return "".join(map(str, final_pattern[:8]))


if __name__ == "__main__":
    print(part1())
