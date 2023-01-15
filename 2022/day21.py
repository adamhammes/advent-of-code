import functools
import operator
import typing

import lib


class FrozenDict(dict):
    def __hash__(self):
        return hash(tuple(self.items()))


class Operation(typing.NamedTuple):
    lval: str
    rval: str
    op: "str"


MonkeyVal = int | Operation

op_map = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.floordiv,
    "*": operator.mul,
}


def parse_line(line: str) -> (str, MonkeyVal):
    name, raw_value = line.split(": ")

    try:
        return name, int(raw_value)
    except ValueError:
        lval, raw_op, rval = raw_value.split(" ")
        return name, Operation(lval, rval, raw_op)


def parse_input(raw: str) -> FrozenDict[str, MonkeyVal]:
    lines = raw.strip().splitlines()
    return FrozenDict(map(parse_line, lines))


@functools.cache
def calc_value(value_map: dict[str, MonkeyVal], monkey: str) -> int:
    match value_map[monkey]:
        case int():
            return value_map[monkey]
        case Operation(lval, rval, op):
            actual_op = op_map[op]
            left_val = calc_value(value_map, lval)
            right_val = calc_value(value_map, rval)
            return actual_op(left_val, right_val)


def part_1(raw: str) -> int:
    value_map = parse_input(raw)
    return calc_value(value_map, "root")


@functools.cache
def p2_eval(value_map: dict[str, MonkeyVal], monkey: str) -> int | None:
    if monkey == "humn":
        return None

    match value_map[monkey]:
        case int():
            return value_map[monkey]
        case Operation(lval, rval, op):
            actual_op = op_map[op]
            left_val = p2_eval(value_map, lval)
            right_val = p2_eval(value_map, rval)
            if left_val is None or right_val is None:
                return None

            return actual_op(left_val, right_val)


def determine_value(value_map: dict[str, MonkeyVal], value_to_match: int, node: str):
    if node == "humn":
        return value_to_match

    node_val = value_map[node]
    left, right = p2_eval(value_map, node_val.lval), p2_eval(value_map, node_val.rval)

    match left, right, node_val.op:
        case None, int(), "+":
            return determine_value(value_map, value_to_match - right, node_val.lval)
        case int(), None, "+":
            return determine_value(value_map, value_to_match - left, node_val.rval)
        case None, int(), "*":
            return determine_value(value_map, value_to_match // right, node_val.lval)
        case int(), None, "*":
            return determine_value(value_map, value_to_match // left, node_val.rval)
        case None, int(), "-":
            return determine_value(value_map, value_to_match + right, node_val.lval)
        case int(), None, "-":
            return determine_value(value_map, left - value_to_match, node_val.rval)
        case None, int(), "/":
            return determine_value(value_map, value_to_match * right, node_val.lval)
        case int(), None, "/":
            return determine_value(value_map, left // value_to_match, node_val.rval)


def part_2(raw: str) -> int:
    value_map = parse_input(raw)
    root = value_map["root"]
    left, right = p2_eval(value_map, root.lval), p2_eval(value_map, root.rval)

    if left is None:
        return determine_value(value_map, right, root.lval)
    else:
        return determine_value(value_map, left, root.rval)


if __name__ == "__main__":
    # print(part_1(lib.get_input(22)))
    print(part_2(lib.get_input(22)))
