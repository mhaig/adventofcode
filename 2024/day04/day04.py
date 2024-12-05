#!/usr/bin/env python3

import sys

from aoc.grid import Grid

string_input = sys.stdin.read()

word_search = Grid()
word_search.build(string_input)

# Get all indices with an X to start search.
x_indices = word_search.get_indices("X")

count = 0
for x in x_indices:
    if "".join(word_search.get_e(x[0], x[1], 4)) == "XMAS":
        count += 1
    if "".join(word_search.get_w(x[0], x[1], 4)) == "XMAS":
        count += 1
    if "".join(word_search.get_n(x[0], x[1], 4)) == "XMAS":
        count += 1
    if "".join(word_search.get_s(x[0], x[1], 4)) == "XMAS":
        count += 1
    if "".join(word_search.get_ne(x[0], x[1], 4)) == "XMAS":
        count += 1
    if "".join(word_search.get_se(x[0], x[1], 4)) == "XMAS":
        count += 1
    if "".join(word_search.get_nw(x[0], x[1], 4)) == "XMAS":
        count += 1
    if "".join(word_search.get_sw(x[0], x[1], 4)) == "XMAS":
        count += 1

print(f"Day 4 Part 1 Solution: {count}")

# Get all indices with an A to start search.
a_indices = word_search.get_indices("A")
count = 0
for a in a_indices:
    diagonal = word_search.get_diagonal(a[0], a[1])
    if len(diagonal) != 4:
        continue

    if (
        "".join(diagonal) == "MSMS"
        or "".join(diagonal) == "MSSM"
        or "".join(diagonal) == "SMSM"
        or "".join(diagonal) == "SMMS"
    ):
        count += 1

print(f"Day 4 Part 2 Solution: {count}")
