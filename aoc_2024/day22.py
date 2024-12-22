import lib


def mix_and_prune(secret: int, number: int) -> int:
    return (secret ^ number) % 16777216


def evolve(secret: int, iterations: int = 1) -> int:
    for _ in range(iterations):
        secret = mix_and_prune(secret, secret * 64)
        secret = mix_and_prune(secret, secret // 32)
        secret = mix_and_prune(secret, secret * 2048)
    return secret


def part_1(raw: str):
    starting = lib.extract_ints(raw)
    return sum(evolve(start, 2_000) for start in starting)


if __name__ == "__main__":
    print(part_1(lib.get_input(22)))
