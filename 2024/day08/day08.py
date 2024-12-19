#!/usr/bin/env python3
import itertools
import sys

from aoc.grid import Grid


def get_antinodes(p0, p1, width, height, harmonics=False):
    rise = p1[1] - p0[1]
    run = p1[0] - p0[0]
    next_x, next_y = max(p0, p1, key=lambda x: x[0])
    prev_x, prev_y = min(p0, p1, key=lambda x: x[0])

    antinodes = []

    for x in range(next_x + 1, width):
        y = (x - next_x) * rise
        if y % run == 0:
            y = y // run
            y += next_y
            if y >= 0 and y < height:
                antinodes.append([x, y])
                # antenna_map[x, y] = "#"
                if not harmonics:
                    break

    for x in range(prev_x - 1, -1, -1):
        y = (x - prev_x) * rise
        if y % run == 0:
            y = y // run
            y += prev_y
            if y >= 0 and y < height:
                # antenna_map[x, y] = "#"
                antinodes.append([x, y])
                if not harmonics:
                    break

    return antinodes


string_input = sys.stdin.read()

antenna_map = Grid(string_input)

# Build a new dictionary with antennas as keys and locations as values
antennas: dict[str, list] = {}
for k, v in antenna_map.items():
    if v == ".":
        continue

    if v in antennas:
        antennas[v].append(k)
    else:
        antennas[v] = [k]

# For each frequency, calculate the line for each antenna pair.
for k in antennas.keys():
    for c in itertools.combinations(antennas[k], 2):
        p0 = c[0]
        p1 = c[1]
        antinodes = get_antinodes(
            c[0], c[1], antenna_map.width, antenna_map.height
        )
        for a in antinodes:
            antenna_map[*a] = "#"


print(f"Day 8 Part 1 Solution: {len(antenna_map.get_indices('#'))}")

for k in antennas.keys():
    for c in itertools.combinations(antennas[k], 2):
        p0 = c[0]
        p1 = c[1]
        antinodes = get_antinodes(
            c[0], c[1], antenna_map.width, antenna_map.height, True
        )
        for a in antinodes:
            antenna_map[*a] = "#"

antinode_count = len([x for x in antenna_map.values() if x != "."])
print(f"Day 8 Part 2 Solution: {antinode_count}")
