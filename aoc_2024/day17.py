import dataclasses
import enum

import lib


class OpCode(enum.IntEnum):
    DivisionA = 0
    XorLiteral = 1
    Modulo = 2
    Jump = 3
    XorRegister = 4
    Output = 5
    DivisionB = 6
    DivisionC = 7


@dataclasses.dataclass
class Computer:
    program: list[int]
    registers: dict[str, int] = dataclasses.field(
        default_factory=lambda: {"A": 0, "B": 0, "C": 0}
    )

    instruction_pointer = 0
    output: list[int] = dataclasses.field(default_factory=list)

    def combo_operand(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3 | 7:
                return operand
            case 4:
                return self.registers["A"]
            case 5:
                return self.registers["B"]
            case 6:
                return self.registers["C"]

    def step(self):
        current_instruction = OpCode(self.program[self.instruction_pointer])

        operand = self.program[self.instruction_pointer + 1]
        combo_operand = self.combo_operand(operand)

        next_pointer = self.instruction_pointer + 2

        match current_instruction:
            case OpCode.DivisionA:
                self.registers["A"] //= 2**combo_operand
            case OpCode.XorLiteral:
                self.registers["B"] ^= operand
            case OpCode.Jump:
                if self.registers["A"] != 0:
                    next_pointer = operand
            case OpCode.Modulo:
                self.registers["B"] = combo_operand % 8
            case OpCode.XorRegister:
                self.registers["B"] ^= self.registers["C"]
            case OpCode.Output:
                self.output.append(combo_operand % 8)
            case OpCode.DivisionB:
                self.registers["B"] = self.registers["A"] // 2**combo_operand
            case OpCode.DivisionC:
                self.registers["C"] = self.registers["A"] // 2**combo_operand
            case _:
                raise Exception("unknown opcode")

        self.instruction_pointer = next_pointer

    def execute(self) -> list[int]:
        while 0 <= self.instruction_pointer < len(self.program):
            self.step()

        return self.output


def parse_input(raw: str) -> Computer:
    raw_registers, raw_program = raw.split("\n\n")
    a, b, c = lib.extract_ints(raw_registers)
    return Computer(
        registers={"A": a, "B": b, "C": c}, program=lib.extract_ints(raw_program)
    )


def part_1(raw: str):
    computer = parse_input(raw)
    computer.execute()
    return ",".join(map(str, computer.output))


if __name__ == "__main__":
    print(part_1(lib.get_input(17)))
