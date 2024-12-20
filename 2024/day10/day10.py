#!/usr/bin/env python3
import sys

from aoc.grid import Grid


def bfs(grid, start):
    # Keep track of explored nodes.
    explored = []
    # Keep track of all the paths to be checked.
    queue = [[start]]

    valid_paths = []

    # Keep looping until all possible paths have been checked.
    while queue:
        # Pop the first path from the queue.
        path = queue.pop(0)
        # Get the last position from the path.
        node = path[-1]
        if node not in explored:
            if grid[*node] == "9":
                valid_paths.append(list(path))

            neighbors = grid.get_neighbors(*node)
            # Go through all neighbor nodes, construct a new path and push it
            # into the queue.
            for neighbor in neighbors:
                if grid[*neighbor] == ".":
                    continue
                if int(grid[*neighbor]) == int(grid[*node]) + 1:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

            # Mark node as explored.
            explored.append(node)

    return valid_paths


def bfs_greedy(grid, start):
    # Keep track of explored nodes.
    explored = []
    # Keep track of all the paths to be checked.
    queue = [[start]]

    valid_paths = []

    # Keep looping until all possible paths have been checked.
    while queue:
        # Pop the first path from the queue.
        path = queue.pop(0)
        # Get the last position from the path.
        node = path[-1]

        if grid[*node] == "9":
            valid_paths.append(list(path))

        neighbors = grid.get_neighbors(*node)
        # Go through all neighbor nodes, construct a new path and push it
        # into the queue.
        for neighbor in neighbors:
            if grid[*neighbor] == ".":
                continue
            if int(grid[*neighbor]) == int(grid[*node]) + 1:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return valid_paths


string_input = sys.stdin.read()

topographic_map = Grid(string_input)

trail_heads = topographic_map.get_indices("0")

trails = []
for trail_head in trail_heads:
    trails.extend(bfs(topographic_map, trail_head))

print(f"Day 10 Part 1 Solution: {len(trails)}")

trails = []
for trail_head in trail_heads:
    trails.extend(bfs_greedy(topographic_map, trail_head))

print(f"Day 10 Part 2 Solution: {len(trails)}")
