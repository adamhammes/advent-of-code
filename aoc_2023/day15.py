import lib


def parse_input(raw: str) -> list[str]:
    return raw.strip().split(",")


def HASH(cs: str) -> int:
    total = 0
    for c in cs:
        total += ord(c)
        total *= 17
        total %= 256

    return total


def part_1(raw: str) -> int:
    return sum(HASH(string) for string in parse_input(raw))


if __name__ == "__main__":
    print(part_1(lib.get_input(15)))
