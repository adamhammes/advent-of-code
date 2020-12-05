import typing


def get_input():
    with open('inputs/day05.txt') as f:
        return f.readlines()


class Seat(typing.NamedTuple):
    row: int
    column: int

    def seat_id(self):
        return self.row * 8 + self.column


def parse_boarding_pass(boarding_pass: str) -> Seat:
    rows = list(range(0, 128))
    columns = list(range(0, 8))

    for direction in boarding_pass[:8]:
        if direction == "F":
            rows = rows[0: len(rows) // 2]
        else:
            rows = rows[len(rows) // 2:]

    for direction in boarding_pass[7:]:
        if direction == "L":
            columns = columns[0: len(columns) // 2]
        else:
            columns = columns[len(columns) // 2:]

    return Seat(row=rows[0], column=columns[0])


def part_1():
    seats = map(parse_boarding_pass, get_input())
    return max(seat.seat_id() for seat in seats)


def part_2():
    seats = map(parse_boarding_pass, get_input())
    seat_ids = list(sorted(seat.seat_id() for seat in seats))

    previous_seat_id = seat_ids[0]
    for seat_id in seat_ids:
        if (seat_id - previous_seat_id) > 1:
            return seat_id - 1

        previous_seat_id = seat_id


if __name__ == "__main__":
    print(part_1())
    print(part_2())
