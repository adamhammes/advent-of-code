import itertools
import math


def chunks(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def first(iterable, condition):
    return next(item for item in iterable if condition(item))


def lcm(*args):

    lcm = args[0]
    for i in args[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm
