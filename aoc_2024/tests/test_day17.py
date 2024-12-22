from day17 import *

EXAMPLE_1 = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


def test_1():
    comp = Computer(
        registers={"A": 0, "B": 0, "C": 9},
        program=[2, 6],
    )

    comp.step()
    assert comp.registers == {"A": 0, "B": 1, "C": 9}
    assert comp.instruction_pointer == 2


def test_2():
    comp = Computer(registers={"A": 10, "B": 0, "C": 0}, program=[5, 0, 5, 1, 5, 4])
    assert comp.execute() == [0, 1, 2]
    assert comp.instruction_pointer == 6


def test_3():
    comp = Computer(registers={"A": 2024, "B": 0, "C": 0}, program=[0, 1, 5, 4, 3, 0])
    assert comp.execute() == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert comp.registers["A"] == 0


def test_4():
    comp = Computer(registers={"A": 0, "B": 29, "C": 0}, program=[1, 7])
    comp.execute()
    assert comp.registers["B"] == 26


def test_5():
    comp = Computer(registers={"A": 0, "B": 2024, "C": 43690}, program=[4, 0])
    comp.execute()
    assert comp.registers["B"] == 44354


def test_part_1():
    assert part_1(EXAMPLE_1) == "4,6,3,5,6,3,5,2,1,0"
