import itertools


def get_input(day: int) -> str:
    with open(f"inputs/day{day:02}.txt") as f:
        return f.read()


def chunks(iterable, n):
    it = iter(iterable)
    while True:
        chunk_it = itertools.islice(it, n)
        try:
            first_el = next(chunk_it)
        except StopIteration:
            return
        yield itertools.chain((first_el,), chunk_it)
