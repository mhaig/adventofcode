#!/usr/bin/env python3

import sys
from typing import NamedTuple

from rich.progress import track


class MapEntry(NamedTuple):
    destination_range_start: int
    source_range_start: int
    range_length: int


class Map:
    """Docstring for Map."""

    def __init__(self, source_name: str, destination_name: str):
        self._source_name = source_name
        self._destination_name = destination_name
        self._ranges: list[MapEntry] = []

    def add_range(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        self._ranges.append(
            MapEntry(destination_range_start, source_range_start, range_length)
        )

    def get_destination(self, source: int) -> int:
        for p in self._ranges:
            if (
                source >= p.source_range_start
                and source <= p.source_range_start + p.range_length
            ):
                return (
                    source - p.source_range_start + p.destination_range_start
                )
        return source

    def get_source(self, destination: int) -> int:
        for p in self._ranges:
            if destination >= p.destination_range_start and destination <= (
                p.destination_range_start + p.range_length
            ):
                return (
                    destination
                    - p.destination_range_start
                    + p.source_range_start
                )
        return destination

    # def get_from_name(self): -> str:
    #     return self._from_name

    @property
    def destination_name(self) -> str:
        return self._destination_name

    @property
    def source_name(self) -> str:
        return self._source_name


game_input = list(sys.stdin.readlines())

seeds = []
maps_forward = {}
maps_backward = {}

for i, line in enumerate(game_input):
    if "seeds" in line:
        seeds = [int(x) for x in line.split()[1:]]
    elif "map" in line:
        j = 1
        new_map = Map(
            line.split()[0].split("-")[0], line.split()[0].split("-")[2]
        )
        while i + j < len(game_input) and game_input[i + j] != "\n":
            new_map.add_range(
                int(game_input[i + j].split()[0]),
                int(game_input[i + j].split()[1]),
                int(game_input[i + j].split()[2]),
            )
            j += 1
        maps_forward[line.split()[0].split("-")[0]] = new_map
        maps_backward[line.split()[0].split("-")[2]] = new_map

locations = []
for s in track(seeds):
    num = s
    next_step = "seed"
    while next_step != "location":
        m = maps_forward[next_step]
        temp_num = m.get_destination(num)
        num = temp_num
        next_step = m.destination_name

    locations.append(num)

print("Part 1 Solution: {}".format(min(locations)))


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


valid_seeds = []
for s1, s2 in pairwise(seeds):
    valid_seeds.append((s1, s1 + s2))

# Need to run the numbers backwards
s = 0
while True:
    num = s
    next_step = "location"
    while next_step != "seed":
        m = maps_backward[next_step]
        temp_num = m.get_source(num)
        num = temp_num
        next_step = m.source_name

    # See if resulting seed is valid.
    valid = False
    for vs in valid_seeds:
        if num >= vs[0] and num < vs[1]:
            valid = True
            break

    if valid:
        break
    s += 1


print("Part 2 Solution: {}".format(s))
