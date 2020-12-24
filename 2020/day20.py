from collections import defaultdict
import itertools
import re
from typing import *

import lib


Edge = Tuple[bool]


class ImageTile(NamedTuple):
    tile_id: int
    pixels: Tuple[Tuple[bool]]

    def flip(self) -> "ImageTile":
        pixels = tuple(reversed(self.pixels))
        return ImageTile(self.tile_id, pixels)

    def rotate(self, n=1) -> "ImageTile":
        tile = self
        for i in range(n):
            print(i)
            pixels = tuple(zip(*reversed(self.pixels)))
            tile = ImageTile(self.tile_id, pixels)

        return tile

    def edges(self) -> List[Edge]:
        top, bottom = self.pixels[0], self.pixels[-1]
        left = [row[0] for row in self.pixels]
        right = [row[-1] for row in self.pixels]

        edges = []
        for edge in top, bottom, left, right:
            edges.append(tuple(edge))
            edges.append(tuple(reversed(edge)))

        return edges


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


def get_shared_edges(
    tiles: List[ImageTile],
) -> Dict[ImageTile, List[SharedEdge]]:
    edges_to_tiles: DefaultDict[Edge, List[ImageTile]] = defaultdict(list)

    for tile in tiles:
        for edge in tile.edges():
            edges_to_tiles[edge].append(tile)

    shared_edges: DefaultDict[ImageTile, List[SharedEdge]] = defaultdict(list)
    for edge, tiles in edges_to_tiles.items():
        for t1, t2 in itertools.permutations(tiles, 2):
            shared_edges[t1].append((edge, t2))

    return shared_edges


def part_1(raw: str) -> int:
    tiles = parse_input(raw)
    shared_edges = get_shared_edges(tiles)
    corner_tiles = [tile for tile in shared_edges if len(shared_edges[tile]) == 4]
    return lib.product(tile.tile_id for tile in corner_tiles)


if __name__ == "__main__":
    print(part_1(lib.get_input(20)))
