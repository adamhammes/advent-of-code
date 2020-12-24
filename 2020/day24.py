from collections import defaultdict
from typing import *

import lib
from lib import HexDirection, HexPoint

Directions = List[HexDirection]


def parse_directions(raw: str) -> Directions:
    directions = []
    while raw:
        if raw[0] == "e":
            directions.append(HexDirection.East)
            raw = raw[1:]
        elif raw[:2] == "ne":
            directions.append(HexDirection.NorthEast)
            raw = raw[2:]
        elif raw[:2] == "nw":
            directions.append(HexDirection.NorthWest)
            raw = raw[2:]
        elif raw[0] == "w":
            directions.append(HexDirection.West)
            raw = raw[1:]
        elif raw[:2] == "sw":
            directions.append(HexDirection.SouthWest)
            raw = raw[2:]
        elif raw[:2] == "se":
            directions.append(HexDirection.SouthEast)
            raw = raw[2:]

    return directions


def parse_input(raw: str) -> List[Directions]:
    return [parse_directions(line) for line in raw.strip().splitlines()]


def follow_directions(directions: Directions) -> HexPoint:
    p = HexPoint.origin()
    for d in directions:
        p = p.move(d)

    return p


def get_flipped_tiles(all_directions: List[Directions]) -> Set[HexPoint]:
    flipped_points = defaultdict(int)
    for directions in all_directions:
        flipped_points[follow_directions(directions)] += 1

    return {point for point in flipped_points if flipped_points[point] % 2 == 1}


def part_1(raw: str):
    all_directions = parse_input(raw)
    return len(get_flipped_tiles(all_directions))


def part_2(raw: str):
    points = get_flipped_tiles(parse_input(raw))

    for _ in range(100):
        new_points = set()
        points_to_consider = set(points)
        for p in points:
            points_to_consider.update(p.neighbors6())

        for p in points_to_consider:
            num_neighbors = p.neighbors6().intersection(points)
            if p not in points and len(num_neighbors) == 2:
                new_points.add(p)
            elif p in points and len(num_neighbors) in [1, 2]:
                new_points.add(p)

        points = new_points

    return len(points)


if __name__ == "__main__":
    print(part_1(lib.get_input(24)))
    print(part_2(lib.get_input(24)))
