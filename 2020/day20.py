from collections import defaultdict
import itertools
import re
from typing import *

import lib

MONSTER = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

Edge = Tuple[bool, ...]


def monster_points(m: str):
    points = []
    for y, row in enumerate(m.strip("\n").splitlines()):
        for x, c in enumerate(row):
            if c == "#":
                points.append(lib.Point(x, y))

    return points


MONSTER_PATTERN = monster_points(MONSTER)


class ImageTile(NamedTuple):
    tile_id: int
    pixels: Tuple[Tuple[bool, ...]]

    def flip(self) -> "ImageTile":
        pixels = tuple(reversed(self.pixels))
        return ImageTile(self.tile_id, pixels)

    def rotate(self, n=1) -> "ImageTile":
        tile = self
        for i in range(n):
            pixels = tuple(zip(*reversed(tile.pixels)))
            tile = ImageTile(self.tile_id, pixels)

        return tile

    def variations(self) -> List["ImageTile"]:
        return [
            *(self.rotate(i) for i in range(4)),
            *(self.flip().rotate(i) for i in range(4)),
        ]

    def left(self) -> Edge:
        return tuple(row[0] for row in self.pixels)

    def bottom(self) -> Edge:
        return self.pixels[-1]

    def right(self):
        return tuple(row[-1] for row in self.pixels)

    def top(self):
        return self.pixels[0]

    def edges(self) -> List[Edge]:
        return [v.top() for v in self.variations()]


def parse_input(raw: str) -> List[ImageTile]:
    tiles = []
    for raw_tile in raw.strip().split("\n\n"):
        tile_id: int = int(re.search(r"\d+", raw_tile).group(0))
        pixels: List[Tuple[bool]] = []

        for line in raw_tile.splitlines()[1:]:
            pixels.append(tuple(map("#".__eq__, line)))

        tiles.append(ImageTile(tile_id, tuple(pixels)))

    return tiles


SharedEdge = Tuple[Edge, ImageTile]

EdgeMap = Dict[ImageTile, Dict[Edge, ImageTile]]


def get_shared_edges(tiles: List[ImageTile]) -> EdgeMap:
    m: EdgeMap = defaultdict(dict)

    for t1, t2 in itertools.permutations(tiles, 2):
        for edge in t1.edges():
            if edge in t2.edges():
                m[t1][edge] = t2

    return m


def get_corners(tiles: List[ImageTile]) -> Set[ImageTile]:
    shared_edges = get_shared_edges(tiles)
    return set(tile for tile in shared_edges if len(shared_edges[tile]) == 4)


def part_1(raw: str) -> int:
    tiles = parse_input(raw)
    return lib.product(tile.tile_id for tile in get_corners(tiles))


def count_monsters(tile: ImageTile):
    size = len(tile.pixels)

    total = sum(sum(row) for row in tile.pixels)
    subtract: Set[lib.Point] = set()

    count = 0
    for dx in range(size):
        for dy in range(size):
            monster = True

            for p in MONSTER_PATTERN:
                x, y = p.displace(dx, dy)

                if x >= size or y >= size or not tile.pixels[y][x]:
                    monster = False

            if monster:
                for p in MONSTER_PATTERN:
                    x, y = p.displace(dx, dy)
                    subtract.add(lib.Point(x, y))

            count += monster

    return total - len(subtract)


def part_2(raw: str):
    tiles = parse_input(raw)
    size = int(len(tiles) ** 0.5)
    shared_edges: EdgeMap = get_shared_edges(tiles)
    tlc = lib.first(get_corners(tiles))

    top_left_edges = shared_edges[tlc].keys()
    while tlc.bottom() not in top_left_edges or tlc.right() not in top_left_edges:
        tlc = tlc.rotate()

    tile_grid: List[List[ImageTile]] = [[tlc]]

    for i in range(size - 1):
        current_tile = tile_grid[-1][0]

        key_tile = lib.first(current_tile.variations(), lambda v: v in shared_edges)

        downwards_tile = shared_edges[key_tile][current_tile.bottom()]
        variation = lib.first(
            downwards_tile.variations(), lambda v: v.top() == current_tile.bottom()
        )

        assert variation.top() == current_tile.bottom()
        tile_grid.append([variation])

    for row in tile_grid:
        for i in range(size - 1):
            current_tile = row[-1]

            key_tile = lib.first(current_tile.variations(), lambda v: v in shared_edges)

            rightwards_tile = shared_edges[key_tile][current_tile.right()]
            variation = lib.first(
                rightwards_tile.variations(), lambda v: v.left() == current_tile.right()
            )

            assert current_tile.right() == variation.left()
            row.append(variation)

    for row in tile_grid:
        for t1, t2 in lib.window(row, 2):
            assert t1.right() == t2.left()

    for i in range(len(tile_grid)):
        column = [row[i] for row in tile_grid]
        for t1, t2 in lib.window(column, 2):
            assert t1.bottom() == t2.top()

    pixel_ids = [tile.tile_id for row in tile_grid for tile in row]
    assert len(set(pixel_ids)) == len(list(pixel_ids))

    tile_size = len(tiles[0].pixels)
    pixels: List[List[bool]] = []
    for row in tile_grid:
        for i in range(1, tile_size - 1):
            pixels.append([])
            for tile in row:
                for pixel in tile.pixels[i][1:-1]:
                    pixels[-1].append(pixel)

    mega_tile = ImageTile(1, tuple(tuple(row) for row in pixels))
    return min(map(count_monsters, mega_tile.variations()))


if __name__ == "__main__":
    print(part_1(lib.get_input(20)))
    print(part_2(lib.get_input(20)))
