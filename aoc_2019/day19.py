import enum

from lib import Tape


class StatusCode(enum.Enum):
    Stationary = 0
    Pulled = 1


def code_for_point(point):
    tape = Tape.tape_from_challenge(19, input_values=point)
    tape.run()
    return StatusCode(tape.output[-1])


def is_pulled(point):
    return code_for_point(list(point)) == StatusCode.Pulled


def part1():

    count = 0
    for y in range(50):
        for x in range(50):
            point = [x, y]

            code = code_for_point(point)
            if code == StatusCode.Pulled:
                count += 1

    return count


def bottom_function(x):
    import math

    bottom = math.floor(x * 1.31)
    top = math.ceil(x * 1.34)

    return range(top + 1, bottom, -1)


def bounding_function(x):
    import math

    low_slope, high_slope = 1.063, 1.324

    low, high = math.floor(x * low_slope), math.ceil(x * high_slope) + 1

    print(low, high)

    return range(high, low, -1)


def p_contains_square(point, square_size=99):
    other_corner = point[0] + square_size, point[1] - square_size
    print(point, other_corner)
    return is_pulled(point) and is_pulled(list(other_corner))


def part2():
    for x in range(780, 2000):
        print(x)
        for y in bounding_function(x):
            if not is_pulled([x, y]):
                continue

            if p_contains_square([x, y]):
                print(x, y)
                return x * 10000 + (y - 99)
            else:
                break


if __name__ == "__main__":
    print(part2())
