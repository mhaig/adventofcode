#!/usr/bin/env python3

import sys
from enum import Enum


class DiskMapState(Enum):
    FILES = 1
    FREE = 2


def build_file_system(string) -> list[str]:
    fs = []
    file_id = 0
    state = DiskMapState.FILES
    for c in string.strip():
        if state == DiskMapState.FILES:
            fs.extend([str(file_id)] * int(c))
            state = DiskMapState.FREE
            file_id += 1
        else:
            fs.extend(["."] * int(c))
            state = DiskMapState.FILES

    return fs


def checksum(fs) -> int:
    checksum = 0
    for i, c in enumerate(fs):
        if c != ".":
            checksum += i * int(c)

    return checksum


string_input = sys.stdin.read()

# blocks: list[AmphiPodsFile] = []
blocks = build_file_system(string_input)

next_free_idx = blocks.index(".")
for i in range(len(blocks) - 1, -1, -1):
    if blocks[i] != ".":
        if next_free_idx < i:
            blocks[next_free_idx] = blocks[i]
            blocks[i] = "."
            next_free_idx = blocks.index(".", next_free_idx)
        else:
            break


print(f"Day 9 Part 1 Solution: {checksum(blocks)}")

blocks = build_file_system(string_input)
i = len(blocks) - 1
while i >= 0:
    if blocks[i] != ".":
        current_file = blocks[i]
        # Find the start of the file.
        current_file_size = 1
        while blocks[i - 1] == current_file:
            i -= 1
            current_file_size += 1

        # From the start, look for a free block that would fit.
        j = 0
        while j < i:
            if blocks[j] == ".":
                free_space = j
                free_size = 1
                while blocks[j + 1] == ".":
                    j += 1
                    free_size += 1

                if current_file_size <= free_size:
                    for k in range(current_file_size):
                        blocks[free_space + k] = current_file
                        blocks[i + k] = "."
                    break
            j += 1

    i -= 1

print(f"Day 9 Part 2 Solution: {checksum(blocks)}")
