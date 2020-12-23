#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from circularlist import CircularList

def get_destination(circ_list, pick_list, min_cup, max_cup):
    destination = circ_list._head.data - 1
    if destination < min_cup:
        destination = max_cup

    while destination in pick_list:
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
    destination = get_destination(cup_list, pick_up, min_cup, max_cup)
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

print('Building Part 2 data set...')
cups = CircularList()
for x in puzzle_input:
    cups.add(int(x))
min_cup = min(cups)
max_cup = max(cups)
for x in range(max_cup+1, 1000000+1):
    cups.add(x)
max_cup = max(cups)
print('Done!')

move_number = 1
while move_number <= 10000000:
    cups = move(move_number, cups, min_cup, max_cup, False)
    move_number += 1

    if move_number % 1000000 == 0:
        print(f'movin... {move_number}')

one = cups.get(1)
next_after_one = one.next.data
next_next_after_one = one.next.next.data
print('Next two cups: {}, {}'.format(next_after_one, next_next_after_one))
print('Part 2 Answer: {}'.format(next_after_one * next_next_after_one))
