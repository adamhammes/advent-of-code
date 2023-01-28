import collections
import heapq
import typing as t

from lib import Point


class SearchState(t.NamedTuple):
    position: Point
    collected_keys: t.FrozenSet[str]


class World:
    def __init__(self, points, keys, doors, entrance):
        self.points: t.Set[Point] = points
        self.keys: t.Dict[Point, str] = keys
        self.doors: t.Dict[Point, str] = doors
        self.entrance: Point = entrance

        self.compressed: t.Dict[Point, t.Dict[Point, int]] = self.compress()

    def points_of_interest(self) -> t.List[Point]:
        return [self.entrance, *self.keys.keys(), *self.doors.keys()]

    def compress(self) -> t.Dict[Point, t.Dict[Point, int]]:
        """Build a 'compressed' version of the maze. In this graph, the only points are keys/doors/the entrance, and
        edges are weighted by distance."""
        return {
            point: dict(self.get_compressed_neighbors(point))
            for point in self.points_of_interest()
        }

    def neighbors(self, point: Point, collected_keys: t.Set[str]):
        """Get neighbors (including open passages) to a point, taking into account collected keys"""
        unopened_doors = {
            point
            for point, door_name in self.doors.items()
            if door_name.lower() not in collected_keys
        }

        return self.points.intersection(point.neighbors()) - unopened_doors

    def get_compressed_neighbors(self, point: Point):
        """Perform BFS from a point, traversing all open passages and stopping at keys/doors/the entrances. Yields
        (point, distance) pairs."""
        distances: t.Dict[Point, int] = {point: 0}
        queue = collections.deque([point])

        while queue:
            cur_point = queue.popleft()
            distance = distances[cur_point]

            if cur_point != point and cur_point in self.points_of_interest():
                # If we've hit a point of interest, then we will yield it and treat the point as a dead end by skipping
                # over its neighbors.
                yield cur_point, distance
                continue

            for neighbor in self.neighbors(
                cur_point, collected_keys=set(self.keys.values())
            ):
                if neighbor not in distances:
                    distances[neighbor] = distance + 1
                    queue.append(neighbor)

    def compressed_neighbors(self, point: Point, collected_keys: t.FrozenSet[str]):
        """Get neighbors to a point, skipping over open passages and taking into account doors. Yields (weight, point)
        pairs."""
        unopened_doors = {
            point
            for point, door_name in self.doors.items()
            if door_name.lower() not in collected_keys
        }

        return (
            (weight, point)
            for point, weight in self.compressed[point].items()
            if point not in unopened_doors
        )

    def collect_keys(self):
        """Find the shortest number of steps to collect all keys."""

        # Our priority queue will contain (point, collected_keys) pairs.
        start_state = SearchState(self.entrance, frozenset())
        queue: t.List[t.Tuple[int, SearchState]] = [(0, start_state)]
        distances = collections.defaultdict(lambda: float("inf"))
        distances[start_state] = 0

        while queue:
            popped: t.Tuple[int, SearchState] = heapq.heappop(queue)
            distance, current_state = popped

            # If we're on a new key, add it to our collected keys.
            if (
                current_state.position in self.keys
                and self.keys[current_state.position]
                not in current_state.collected_keys
            ):
                collected_keys = frozenset(
                    [*current_state.collected_keys, self.keys[current_state.position]]
                )
            else:
                collected_keys = current_state.collected_keys

            if collected_keys == frozenset(self.keys.values()):
                return distance

            for weight, neighbor in self.compressed_neighbors(
                current_state.position, collected_keys
            ):
                new_state = SearchState(neighbor, collected_keys)
                new_distance = distance + weight

                if new_distance < distances[new_state]:
                    distances[new_state] = new_distance
                    heapq.heappush(queue, (new_distance, new_state))


def parse_input(_in: str) -> World:
    _in = _in.strip()
    points = set()
    keys, doors = dict(), dict()
    entrance = None

    for y, row in enumerate(_in.splitlines()):
        for x, character in enumerate(row):
            if character == "#":
                continue

            point = Point(x, y)
            points.add(point)

            if character.isalpha() and character.islower():
                keys[point] = character

            if character.isalpha() and character.isupper():
                doors[point] = character

            if character == "@":
                entrance = point

    return World(points, keys, doors, entrance)


def get_input():
    with open("inputs/day18.txt") as f:
        return parse_input(f.read().strip())


def part1():
    world = get_input()
    return world.collect_keys()


if __name__ == "__main__":
    print(part1())
