#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def explore_path(paths, current, explored, total_explore):
    explored.append(current)

    if current == 'end':
        total_explore.append(explored)
        return

    for p in paths[current]:
        if p == 'start':
            continue
        if p in explored and p.islower():
            continue

        explore_path(paths, p, list(explored), total_explore)


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
explore_path(paths, 'start', [], total_explore)
print('Part 1 Solution: {}'.format(len(total_explore)))
