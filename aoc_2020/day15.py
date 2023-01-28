from collections import defaultdict, deque
import typing

INPUT = "0,5,4,1,10,14,7"


class Counter:
    def __init__(self, starting_numbers: typing.List[int]):
        self.memory = defaultdict(deque)
        for i, num in enumerate(starting_numbers):
            self.memory[num].append(i)
            self.last_number = num

        self.cur_index = len(starting_numbers) - 1

    def next_number(self):
        entries = self.memory[self.last_number]
        if len(entries) <= 1:
            return 0

        return entries[-1] - entries[-2]

    def say(self):
        self.cur_index += 1
        self.last_number = self.next_number()
        self.memory[self.last_number].append(self.cur_index)

        if len(self.memory[self.last_number]) > 2:
            self.memory[self.last_number].popleft()

        return self.last_number


def part_1(raw: str):
    nums = list(map(int, raw.split(",")))

    counter = Counter(nums)
    said = [counter.say() for _ in range(2020 - len(nums))]
    return said[-1]


def part_2(raw: str):
    nums = list(map(int, raw.split(",")))

    counter = Counter(nums)
    last_said = 0
    for i in range(30000000 - len(nums)):
        last_said = counter.say()
        if i % 1000 == 0:
            print(i)

    return last_said


if __name__ == "__main__":
    print(part_1(INPUT))
    print(part_2(INPUT))
