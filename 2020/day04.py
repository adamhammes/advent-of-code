import typing
import re


class Passport(typing.NamedTuple):
    byr: typing.Optional[str] = None
    iyr: typing.Optional[str] = None
    eyr: typing.Optional[str] = None
    hgt: typing.Optional[str] = None
    hcl: typing.Optional[str] = None
    ecl: typing.Optional[str] = None
    pid: typing.Optional[str] = None
    cid: typing.Optional[str] = None

    @staticmethod
    def required_fields():
        return [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        ]

    def has_required_fields(self):
        return all(self._asdict().get(field) is not None for field in self.required_fields())

    def is_valid(self):
        if not self.has_required_fields():
            return False

        height_is_valid = False
        if not re.match(r"^\d+(cm|in)$", self.hgt):
            pass
        elif "cm" == self.hgt[-2:]:
            height_is_valid = 150 <= int(self.hgt[:-2]) <= 193
        elif "in" == self.hgt[-2:]:
            height_is_valid = 59 <= int(self.hgt[:-2]) <= 76

        return all([
            1920 <= int(self.byr) <= 2002,
            2010 <= int(self.iyr) <= 2020,
            2020 <= int(self.eyr) <= 2030,
            height_is_valid,
            re.match("^#[0-9a-f]{6}$", self.hcl),
            re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", self.ecl),
            re.match(r"^\d{9}$", self.pid),
        ])


def parse_passport(raw: str) -> Passport:
    as_dict = dict(item.split(":") for item in re.split(r"\s+", raw.strip()))
    return Passport(**as_dict)


def get_input():
    with open('inputs/day04.txt') as f:
        raw_passports = f.read().split("\n\n")

    return map(parse_passport, raw_passports)


def part_1():
    return sum(map(Passport.has_required_fields, get_input()))


def part_2():
    return sum(map(Passport.is_valid, get_input()))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
