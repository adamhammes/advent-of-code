import lib


def get_input():
    with open("inputs/day01.txt") as f:
        return list(map(int, f.readlines()))


def part_1(nums):
    pairs = zip(nums, nums[1:])

    return sum(y > x for x, y in pairs)


def part_2(nums):
    window3 = lib.window(nums, 3)
    sum3 = list(map(sum, window3))

    return part_1(sum3)


if __name__ == "__main__":
    print(part_1(get_input()))
    print(part_2(get_input()))
