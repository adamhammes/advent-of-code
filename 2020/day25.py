import itertools

MOD_VALUE = 20201227


def compute_handshake(subject_number: int, loop_size: int):
    value = 1

    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value


def determine_loop_size(public_key: int) -> int:
    value = 1
    for loop_size in itertools.count(start=1):
        value *= 7
        value %= MOD_VALUE

        if value == public_key:
            return loop_size


def part_1():
    door_key, card_key = 6930903, 19716708
    door_loop_size = determine_loop_size(card_key)
    return compute_handshake(door_key, door_loop_size)


if __name__ == "__main__":
    print(part_1())
