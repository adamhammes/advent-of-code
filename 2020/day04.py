import typing
import re

REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


def parse_passport(raw: str) -> dict:
    return dict(item.split(":") for item in re.split(r"\s+", raw.strip()))


def has_required_fields(passport):
    return all(field in passport for field in REQUIRED_FIELDS)


def is_valid(passport: typing.Dict[str, str]) -> bool:
    if not has_required_fields(passport):
        return  False

    height_is_valid = False
    if not re.match(r"^\d+(cm|in)$", passport['hgt']):
        pass
    elif "cm" == passport['hgt'][-2:]:
        height_is_valid = 150 <= int(passport['hgt'][:-2]) <= 193
    elif "in" == passport['hgt'][-2:]:
        height_is_valid = 59 <= int(passport['hgt'][:-2]) <= 76

    return all([
        1920 <= int(passport['byr']) <= 2002,
        2010 <= int(passport['iyr']) <= 2020,
        2020 <= int(passport['eyr']) <= 2030,
        height_is_valid,
        re.match("^#[0-9a-f]{6}$", passport['hcl']),
        re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']),
        re.match(r"^\d{9}$", passport['pid']),
    ])


def get_input():
    with open('inputs/day04.txt') as f:
        raw_passports = f.read().split("\n\n")

    return map(parse_passport, raw_passports)


def part_1():
    return sum(map(has_required_fields, get_input()))


def part_2():
    return sum(map(is_valid, get_input()))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
