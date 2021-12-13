#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

from collections import Counter

def can_explore1(cave, explored):
    """Test if a cave can be explored with the rules for Part 1."""
    return (not (cave in explored and cave.islower()))

def can_explore2(cave, explored):
    """Test if a cave can be explored with the rules for Part2."""
    # If the cave is large it can always be explored.
    if cave.isupper():
        return True

    # If the cave is small and has not been visited, it can be visited.
    if cave not in explored:
        return True

    # If the cave is lower case and has been explored, it can be explored again
    # if it's the first small cave to be explored twice.
    counts = Counter(explored)
    # Put all the lower counts into a list.
    lower_counts = [v for k,v in counts.items() if k.islower() and v > 1]
    if not lower_counts:
        return True

    return False

def explore_path(paths, current, explored, total_explore, check):
    explored.append(current)

    if current == 'end':
        total_explore.append(explored)
        return

    for p in paths[current]:
        if p == 'start':
            continue
        if check(p, explored):
            explore_path(paths, p, list(explored), total_explore, check)


paths = {}
for line in sys.stdin.readlines():
    start, end = line.split('-')
    if start in paths:
        paths[start].append(end.strip())
    else:
        paths[start] = [end.strip()]

    if end.strip() in paths:
        paths[end.strip()].append(start)
    else:
        paths[end.strip()] = [start]

total_explore=[]
explore_path(paths, 'start', [], total_explore, can_explore1)
print('Part 1 Solution: {}'.format(len(total_explore)))

total_explore=[]
explore_path(paths, 'start', [], total_explore, can_explore2)
print('Part 2 Solution: {}'.format(len(total_explore)))
