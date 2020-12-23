#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from circularlist import CircularList

def get_destination(circ_list):
    destination = circ_list._head.data - 1
    while destination not in circ_list:
        destination -= 1
        if destination < min_cup:
            destination = max_cup

    return destination

puzzle_input = sys.stdin.read().strip()

print(puzzle_input)

cups = CircularList()
for x in puzzle_input:
    cups.add(int(x))
min_cup = min(cups)
max_cup = max(cups)
current_cup = 0
destination = 0

while current_cup < 100:
    print(f'-- move {current_cup+1} --')

    print('cups: {}'.format(' '.join([str(x) for x in cups])))
    pick_up = []
    for _ in range(3):
        pick_up.append(cups.remove_next())
    print('pick up: {}'.format(pick_up))
    print(cups)
    destination = get_destination(cups)
    print('destination: {}'.format(destination))
    cups.insert_at(destination, pick_up)
    print(cups)
    cups.rotate()

    current_cup += 1

    print()

print('-- final --')
print('cups: {}'.format(cups))

# For final answer, rotate head until 1 is first.
while cups._head.data != 1:
    cups.rotate()

# Now the answer is the string minus the beginning 1.
print('Part 1 Answer: {}'.format(''.join([str(x) for x in cups if x != 1])))
