import lib


def find_marker(packets: str, window_size: int) -> int:
    for index, values in enumerate(lib.window(packets, window_size)):
        if len(set(values)) == window_size:
            return index + window_size


def part_1(raw: str) -> int:
    return find_marker(raw, 4)


def part_2(raw: str) -> int:
    return find_marker(raw, 14)


if __name__ == "__main__":
    print(part_1(lib.get_input(6)))
    print(part_2(lib.get_input(6)))
