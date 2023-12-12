#!/usr/bin/env python3

import sys

from rich.progress import track


class Map:
    """Docstring for Map."""

    def __init__(self, from_name: str, to_name: str):
        self._from_name = from_name
        self._to_name = to_name
        self._pairs: list[list[int]] = []

    def add_pair(self, from_num: int, to_num: int, count: int) -> None:
        self._pairs.append([from_num, from_num + count, to_num, count])

    def get_to(self, from_num: int) -> int:
        for p in self._pairs:
            if from_num >= p[0] and from_num <= p[1]:
                return from_num - p[0] + p[2]
        return from_num

    def get_to_name(self) -> str:
        return self._to_name


game_input = list(sys.stdin.readlines())

seeds = []
maps = {}

for i, line in enumerate(game_input):
    if "seeds" in line:
        seeds = [int(x) for x in line.split()[1:]]
    elif "map" in line:
        j = 1
        maps[line.split()[0].split("-")[0]] = Map(
            line.split()[0].split("-")[0], line.split()[0].split("-")[2]
        )
        while i + j < len(game_input) and game_input[i + j] != "\n":
            maps[line.split()[0].split("-")[0]].add_pair(
                int(game_input[i + j].split()[1]),
                int(game_input[i + j].split()[0]),
                int(game_input[i + j].split()[2]),
            )
            j += 1

print(seeds)
for k, v in maps.items():
    print(k, v)

locations = []
for s in track(seeds):
    num = s
    next_step = "seed"
    while next_step != "location":
        m = maps[next_step]
        temp_num = m.get_to(num)
        num = temp_num
        next_step = m.get_to_name()

    locations.append(num)

print("Part 1 Solution: {}".format(min(locations)))
