import typing
from typing import Literal

import lib

Operator = Literal["AND"] | Literal["OR"] | Literal["XOR"]


class Wire(typing.NamedTuple):
    key: str
    value: int

    @staticmethod
    def from_str(line: str):
        key, value = line.split(": ")
        return Wire(key, int(value))


class Gate(typing.NamedTuple):
    a: str
    b: str
    operator: Operator
    key: str

    @staticmethod
    def from_str(line: str):
        parts = line.split()
        del parts[3]
        a, operator, b, key = parts
        return Gate(a, b, operator, key)


def parse_input(raw: str):
    raw_literals, raw_connections = raw.strip().split("\n\n")
    literals = {
        wire.key: wire for wire in map(Wire.from_str, raw_literals.splitlines())
    }
    gates = {
        gate.key: gate for gate in map(Gate.from_str, raw_connections.splitlines())
    }
    return literals, gates


def evaluate(wires: dict[str, Wire], gates: dict[str, Gate], key: str) -> int:
    if key in wires:
        return wires[key].value

    gate = gates[key]
    a, b = evaluate(wires, gates, gate.a), evaluate(wires, gates, gate.b)

    match gate.operator:
        case "OR":
            return a | b
        case "AND":
            return a & b
        case "XOR":
            return a ^ b


def part_1(raw: str):
    wires, gates = parse_input(raw)

    zs = [key for key in gates if key.startswith("z")]
    zs.sort(reverse=True)
    bits = [evaluate(wires, gates, z) for z in zs]
    bits = "".join(map(str, bits))
    return int(bits, 2)


if __name__ == "__main__":
    print(part_1(lib.get_input(24)))
