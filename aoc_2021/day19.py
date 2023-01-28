import itertools
import typing

# 3 2 1
import lib
from p3d import P


class Scanner(typing.NamedTuple):
    scanner_id: int
    beacons: set[P]

    def rotations(self) -> typing.Iterable["Scanner"]:
        for i in range(24):
            yield Scanner(
                beacons={beacon.rotations(i) for beacon in self.beacons},
                scanner_id=self.scanner_id,
            )

    def translate(self, vector: P) -> "Scanner":
        return Scanner(
            beacons={beacon.translate(vector) for beacon in self.beacons},
            scanner_id=self.scanner_id,
        )


def parse_input(raw: str) -> list[Scanner]:
    scanners = []
    for scanner_id, raw_scanner in enumerate(raw.strip().split("\n\n")):
        beacons = {
            P(*list(map(int, line.split(",")))) for line in raw_scanner.split("\n")[1:]
        }
        scanners.append(Scanner(beacons=beacons, scanner_id=int(scanner_id)))

    return scanners


def try_solve(
    solved: Scanner, unsolved: Scanner
) -> typing.Tuple[typing.Optional[Scanner], P]:
    for orientation in unsolved.rotations():
        for p1 in solved.beacons:
            for p2 in orientation.beacons:
                correctly_translated = orientation.translate(p1.sub(p2))
                matching_beacons = solved.beacons.intersection(
                    correctly_translated.beacons
                )
                if len(matching_beacons) >= 12:
                    return correctly_translated, p2.sub(p1)


def solve_all(scanners: list[Scanner]) -> typing.Tuple[Scanner, set[P]]:
    mega_scanner, unsolved = scanners[0], scanners[1:]
    scanner_positions = {P(0, 0, 0)}

    while unsolved:
        for scanner_to_solve in unsolved:
            solution = try_solve(mega_scanner, scanner_to_solve)

            if solution is not None:
                corrected_scanner, position = solution
                mega_scanner.beacons.update(corrected_scanner.beacons)
                unsolved.remove(scanner_to_solve)
                scanner_positions.add(position)
                break

    return mega_scanner, scanner_positions


def part_1(raw: str) -> int:
    scanners = parse_input(raw)
    return len(solve_all(scanners)[0].beacons)


def part_2(raw: str) -> int:
    scanners = parse_input(raw)
    _, positions = solve_all(scanners)

    return max(
        p1.manhattan_distance(p2) for p1, p2 in itertools.product(positions, repeat=2)
    )


if __name__ == "__main__":
    print(part_1(lib.get_input(19)))
    print(part_2(lib.get_input(19)))
