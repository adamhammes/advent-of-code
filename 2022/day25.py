import lib


def to_snafu(val: int) -> str:
    digits = []

    while val:
        digits.append(val % 5)
        val //= 5

    digits = [0] + digits[::-1]

    while any(d > 2 for d in digits):
        for i, digit_value in enumerate(digits):
            if digit_value > 2:
                digits[i] -= 5
                digits[i - 1] += 1

    digits = [{-1: "-", -2: "="}.get(d, d) for d in digits]
    return "".join(map(str, digits)).lstrip("0")


def from_snafu(snafu: str) -> int:
    parts = []
    for i, char in enumerate(snafu[::-1]):
        positional_value = {
            "0": 0,
            "1": 1,
            "2": 2,
            "=": -2,
            "-": -1,
        }[char]

        parts.append(positional_value * 5**i)

    return sum(parts)


def part_1(raw: str) -> str:
    lines = raw.strip().splitlines()
    nums = map(from_snafu, lines)
    return to_snafu(sum(nums))


if __name__ == "__main__":
    print(part_1(lib.get_input(25)))
