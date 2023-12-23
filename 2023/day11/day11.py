#!/usr/bin/env python3

import sys

import numpy as np

game_input = [x.strip() for x in sys.stdin.readlines()]

image = np.empty(shape=(len(game_input), len(game_input[0])), dtype=str)

for i, line in enumerate(game_input):
    for j, c in enumerate(line):
        image[i, j] = c


def expand(image, axis):
    i = 0
    while i < len(image.take(indices=0, axis=[1, 0][axis])):
        if all([x == "." for x in image.take(indices=i, axis=axis)]):
            # Insert a new row or column.
            image = np.insert(image, i, ".", axis=axis)
            # Skip the inserted row or column.
            i += 2
        else:
            i += 1
    return image


# Traverse image columns and insert empty columns when one is reached.
image = expand(image, 1)

# Traverse image rows and insert empty rows when one is reached.
image = expand(image, 0)

# Get location of all galaxies.
galaxies = list(zip(*np.where(image == "#")))
combinations = [
    (a, b) for idx, a in enumerate(galaxies) for b in galaxies[idx + 1 :]
]
distances = []
for a in combinations:
    start, stop = a
    distances.append(abs(start[0] - stop[0]) + abs(start[1] - stop[1]))

print("Part 1 Solution: {}".format(sum(distances)))
