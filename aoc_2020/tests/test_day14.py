from day14 import *
import lib

SAMPLE_1 = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip()

SAMPLE_2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip()


def test_basic_operations():
    lines = iter(SAMPLE_1.splitlines())
    prog = Program(MemoryMode.Fixed)

    prog.read_line(next(lines))
    assert prog.mask[-2:] == [
        BitMask.Zero,
        BitMask.Indeterminate,
    ]


def test_part_1():
    prog = Program(MemoryMode.Fixed)
    [prog.read_line(line) for line in SAMPLE_1.splitlines()]
    assert prog.sum() == 165


def test_part_2():
    prog = Program(MemoryMode.Floating)
    [prog.read_line(line) for line in SAMPLE_2.splitlines()]
    assert prog.sum() == 208


def test_regressions():
    assert part_1(lib.get_input(14)) == 13865835758282
    assert part_2(lib.get_input(14)) == 4195339838136
