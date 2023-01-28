import re
import typing

import lib


class TicketRule(typing.NamedTuple):
    name: str
    constraints: typing.FrozenSet[int]

    def matches(self, num: int):
        return num in self.constraints


Ticket = typing.Tuple[int]


def parse_input(
    raw: str,
) -> typing.Tuple[typing.List[TicketRule], Ticket, typing.List[Ticket]]:
    raw_constraints, your_ticket, other_tickets = raw.split("\n\n")

    ticket_rules = []
    for line in raw_constraints.splitlines():
        name = line.split(":")[0]
        nums = []
        matches = re.findall(r"(\d+)-(\d+)", line)
        for start, end in matches:
            nums += range(int(start), int(end) + 1)

        ticket_rules.append(TicketRule(name, frozenset(nums)))

    your_ticket = tuple(int(num) for num in your_ticket.splitlines()[1].split(","))
    other_tickets = other_tickets.split("nearby tickets:\n")[1]

    other_tickets = list(
        tuple(int(num) for num in line.split(","))
        for line in other_tickets.splitlines()
    )

    return ticket_rules, your_ticket, other_tickets


def get_bad_tickets(ticket_rules, tickets) -> typing.List[Ticket]:
    bad_tickets = []
    for ticket in tickets:
        for num in ticket:
            if not any(rule.matches(num) for rule in ticket_rules):
                bad_tickets.append(ticket)
                break

    return bad_tickets


def part_1(raw: str):
    ticket_rules, your_ticket, other_tickets = parse_input(raw)

    bad_values = []
    for ticket in other_tickets:
        for num in ticket:
            if not any(rule.matches(num) for rule in ticket_rules):
                bad_values.append(num)

    return sum(bad_values)


def part_2(raw: str):
    ticket_rules, your_ticket, other_tickets = parse_input(raw)

    bad_tickets = set(get_bad_tickets(ticket_rules, other_tickets))
    other_tickets = set(other_tickets) - bad_tickets

    constraints = {rule: set(range(len(your_ticket))) for rule in ticket_rules}

    while any(len(indices) != 1 for indices in constraints.values()):
        for rule in ticket_rules:
            for ticket in other_tickets:
                for index, num in enumerate(ticket):
                    if not rule.matches(num):
                        constraints[rule].discard(index)

            if len(constraints[rule]) == 1:
                index = list(constraints[rule])[0]
                for other_rule in ticket_rules:
                    if rule != other_rule:
                        constraints[other_rule].discard(index)

    defined = {list(indices)[0]: rule.name for rule, indices in constraints.items()}

    return lib.product(
        [val for i, val in enumerate(your_ticket) if defined[i].startswith("departure")]
    )


if __name__ == "__main__":
    print(part_1(lib.get_input(16)))
    print(part_2(lib.get_input(16)))
