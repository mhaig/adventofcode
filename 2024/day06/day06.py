#!/usr/bin/env python3

import signal
import sys
from collections import defaultdict

from aoc.grid import Grid
from tqdm import tqdm

from guard import Guard

current_grid = None


def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    print(current_grid)
    sys.exit(0)


def inside_map(grid, guard) -> bool:

    return (
        guard.x >= 0
        and guard.x < grid.width
        and guard.y >= 0
        and guard.y < grid.height
    )


def solve(a_map):
    # Find the guard starting position.
    guard = Guard()
    guard.pos = a_map.get_indices("^")[0]
    hit_tracker = defaultdict(lambda: 0)
    while inside_map(a_map, guard):

        # Mark the guards current spot.
        a_map[*guard.pos] = "X"

        # Move the guard.
        if guard._char == "^":
            # See if the spot to the North is open.
            n = a_map.get_n(*guard.pos, 2)
            if len(n) == 2:
                if n[1] in ["O", "#"]:
                    hit_tracker[guard.x, guard.y - 1] += 1
                    guard.turn()
                else:
                    guard.move()
            else:
                break
        elif guard._char == ">":
            # See if the spot to the East is open.
            e = a_map.get_e(*guard.pos, 2)
            if len(e) == 2:
                if e[1] in ["#", "O"]:
                    hit_tracker[guard.x + 1, guard.y] += 1
                    guard.turn()
                else:
                    guard.move()
            else:
                break
        elif guard._char == "v":
            # See if the spot to the South is open.
            s = a_map.get_s(*guard.pos, 2)
            if len(s) == 2:
                if s[1] in ["O", "#"]:
                    hit_tracker[guard.x, guard.y + 1] += 1
                    guard.turn()
                else:
                    guard.move()
            else:
                break
        elif guard._char == "<":
            # See if the spot to the West is open.
            w = a_map.get_w(*guard.pos, 2)
            if len(w) == 2:
                if w[1] in ["O", "#"]:
                    hit_tracker[guard.x, guard.y + 1] += 1
                    guard.turn()
                else:
                    guard.move()
            else:
                break
        else:
            raise Exception()

        a_map[*guard.pos] = guard._char

        if 4 in hit_tracker.values():
            return 0
    a_map[*guard.pos] = "X"

    return len(a_map.get_indices("X"))


string_input = sys.stdin.read()

lab_map = Grid()
lab_map.build(string_input)

height = lab_map.height
width = lab_map.width

print(f"Day 6 Part 1 Solution: {solve(lab_map)}")

signal.signal(signal.SIGINT, signal_handler)
loop_count = 0
for j in tqdm(range(height)):
    for k in tqdm(range(width), leave=False):
        # Reset the grid.
        lab_map = Grid()
        lab_map.build(string_input)
        # If guard, skip
        if lab_map[k, j] == "^":
            continue
        # If already #, skip
        if lab_map[k, j] == "#":
            continue
        # Add O at position and see if solvable
        lab_map[k, j] = "O"
        current_grid = lab_map
        if solve(lab_map) == 0:
            loop_count += 1

print(f"Day 6 Part 2 Solution: {loop_count}")
