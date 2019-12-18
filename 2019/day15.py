import collections
import enum

from lib import Tape, Point, CardinalDirection


class StatusCode(enum.Enum):
    Wall = 0
    Step = 1
    Oxygen = 2


def direction_to_int(direction):
    return {
        CardinalDirection.Up: 1,
        CardinalDirection.Down: 2,
        CardinalDirection.Left: 3,
        CardinalDirection.Right: 4,
    }[direction]


def print_world(graph, oxygen=None):
    start_x = min(p.x for p in graph.keys())
    end_x = max(p.x for p in graph.keys())

    start_y = min(p.y for p in graph.keys())
    end_y = max(p.y for p in graph.keys())

    for y in range(end_y, start_y - 1, -1):
        row = []
        for x in range(start_x, end_x + 1):
            row.append("*" if Point(x, y) in graph else " ")

            if Point(x, y) == oxygen:
                row[-1] = "O"

        print("".join(row))


class Explorer:
    def __init__(self, tape):
        self.tape = tape
        self.position = Point(0, 0)
        self.graph = collections.defaultdict(set)
        self.oxygen = None

    def explore(self):
        places_to_visit = collections.deque([self.position])
        visited = {self.position}

        while places_to_visit:
            next_point = places_to_visit.pop()
            self.move_to(next_point)

            unvisited_neighbors = set(self.position.neighbors()) - visited
            for neighbor in unvisited_neighbors:
                status = self.explore_adjacent_point(neighbor)

                if status == StatusCode.Wall:
                    visited.add(neighbor)

                if status in [StatusCode.Step, StatusCode.Oxygen]:
                    self.graph[self.position].add(neighbor)
                    self.graph[neighbor].add(self.position)
                    places_to_visit.append(neighbor)

                if status == StatusCode.Oxygen:
                    self.oxygen = neighbor

            visited.add(self.position)

    def find_path(self, start, end):
        import heapq as h

        distances = {start: 0}
        heap = [(0, start)]
        prev_node = dict()

        while end not in prev_node:
            weight, node = h.heappop(heap)

            unvisited_neighbors = self.graph[node] - distances.keys()

            for neighbor in unvisited_neighbors:
                prev_node[neighbor] = node

                distance = weight + 1
                distances[neighbor] = weight
                h.heappush(heap, (distance, neighbor))

        cur_node = end
        path = [end]

        while cur_node != start:
            previous_node = prev_node[cur_node]
            path.append(previous_node)
            cur_node = previous_node

        return list(reversed(path))[1:]

    def distances_from(self, start):
        import heapq as h

        distances = {start: 0}
        heap = [(0, start)]

        while heap:
            weight, node = h.heappop(heap)

            unvisited_neighbors = self.graph[node] - distances.keys()

            for neighbor in unvisited_neighbors:
                distance = weight + 1
                distances[neighbor] = weight
                h.heappush(heap, (distance, neighbor))

        return distances

    def move_direction(self, direction):
        input_code = direction_to_int(direction)
        status_code = self.tape.run_until_output(provide_input=input_code)[0]
        status = StatusCode(status_code)

        if status != StatusCode.Wall:
            self.position = self.position.displace(*direction.value)

        return status

    def move_to(self, destination):
        if self.position == destination:
            return

        for point in self.find_path(self.position, destination):
            self.move_direction(self.position.direction_to(point))

    def explore_adjacent_point(self, point):
        direction = self.position.direction_to(point)
        status = self.move_direction(direction)

        if status != StatusCode.Wall:
            self.move_direction(direction.inverse_direction())

        return status


def part1():
    explorer = Tape.tape_from_challenge(15, Explorer)
    explorer.explore()
    path_to_oxygen = explorer.find_path(Point(0, 0), explorer.oxygen)
    return len(path_to_oxygen)


def part2():
    explorer = Tape.tape_from_challenge(15, Explorer)
    explorer.explore()

    return max(explorer.distances_from(explorer.oxygen).values()) + 1


if __name__ == "__main__":
    print(part1())
    print(part2())
