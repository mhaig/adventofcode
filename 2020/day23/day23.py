#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from circularlist import CircularList

def get_destination(circ_list, min_cup, max_cup):
    destination = circ_list._head.data - 1
    while destination not in circ_list:
        destination -= 1
        if destination < min_cup:
            destination = max_cup

    return destination

def move(move_number, cup_list, min_cup, max_cup, debug=True):
    if debug:
        print(f'-- move {move_number} --')

    if debug:
        print('cups: {}'.format(' '.join([str(x) for x in cup_list])))
    pick_up = []
    for _ in range(3):
        pick_up.append(cup_list.remove_next())
    if debug:
        print('pick up: {}'.format(pick_up))
    destination = get_destination(cup_list, min_cup, max_cup)
    if debug:
        print('destination: {}'.format(destination))
    cup_list.insert_at(destination, pick_up)
    cup_list.rotate()

    if debug:
        print()
    return cup_list

puzzle_input = sys.stdin.read().strip()

print(puzzle_input)

cups = CircularList()
for x in puzzle_input:
    cups.add(int(x))
min_cup = min(cups)
max_cup = max(cups)
destination = 0

move_number = 1
while move_number <= 100:
    cups = move(move_number, cups, min_cup, max_cup, False)
    move_number += 1

print('-- final --')
print('cups: {}'.format(cups))

# For final answer, rotate head until 1 is first.
while cups._head.data != 1:
    cups.rotate()

# Now the answer is the string minus the beginning 1.
print('Part 1 Answer: {}'.format(''.join([str(x) for x in cups if x != 1])))
