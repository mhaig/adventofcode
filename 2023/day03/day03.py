#!/usr/bin/env python3

import sys

game_input = list(sys.stdin.readlines())
schematic: dict[tuple[int, int], str] = {}

y = 0
for line in game_input:
    x = 0
    for c in line.strip():
        if c != ".":
            schematic[(x, y)] = c
        x += 1
    y += 1


def get_full_number(p: tuple[int, int]) -> int:
    # Build a number out of all the adjacent digits on the same row.
    digits: list[str] = []
    x = 0
    while (p[0] + x, p[1]) in schematic:
        digit = schematic[(p[0] + x, p[1])]
        if not digit.isnumeric():
            break
        digits.insert(0, digit)
        x -= 1
    x = 1
    while (p[0] + x, p[1]) in schematic:
        digit = schematic[(p[0] + x, p[1])]
        if not digit.isnumeric():
            break
        digits.append(digit)
        x += 1

    return int("".join(digits))


def get_adjacent(p: tuple[int, int]) -> list[int]:
    adjacent_numbers: set[int] = set()
    for j in [-1, 0, 1]:
        for k in [-1, 0, 1]:
            if j == 0 and k == 0:
                continue

            p_new = (p[0] + j, p[1] + k)
            if p_new in schematic:
                adjacent_numbers.add(get_full_number(p_new))

    return list(adjacent_numbers)


part_numbers = []
gear_ratios = []
for k, v in schematic.items():
    if not v.isnumeric():
        part_numbers.extend(get_adjacent(k))

    gears = []
    if v == "*":
        gears.extend(get_adjacent(k))
        if len(gears) == 2:
            gear_ratios.append(gears[0] * gears[1])


print("Part 1 Solution: {}".format(sum(part_numbers)))
print("Part 2 Solution: {}".format(sum(gear_ratios)))
