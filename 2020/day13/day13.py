#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import math
import sys
import numpy as np

puzzle_input = sys.stdin.read().strip()
departure = int(puzzle_input.split('\n')[0])
ids = puzzle_input.split('\n')[1].split(',')

print('Departure: {}'.format(departure))
print('IDs: {}'.format(ids))

earliest = []
for i in ids:
    if i == 'x':
        continue

    if departure % int(i) == 0:
        earliest.append([i, departure])
    else:
        e = math.ceil(departure / int(i)) * int(i)
        earliest.append([int(i), e])

# For the sample case...
#
#   t   %  7 = 0
#   t+1 % 13 = 0
#   t+4 % 59 = 0
#   t+6 % 31 = 0
#   t+7 % 19 = 0
#
#   t     = a*7
#   (t+1) = b*13
#   (t+4) = c*59
#   (t+6) = d*31
#   (t+7) = e*19
#
#   (t+0)/7  = a
#   (t+1)/13 = b
#   (t+4)/59 = c
#   (t+6)/31 = d   6*19*59*13*7
#   (t+7)/19 = e   7*31*59*13*7
#
#
#   t = a*7
#   t = b*13 - 1
#   t = c*59 - 4
#   t = d*31 - 6
#   t = e*19 - 7
#
#   5*t = a*7 + b*13 - 1 + c*59 - 4 + d*31 - 6 + e*19 - 7
#   5*t = a*7 + b*13 + c*59 + d*31 + e*19 - 18

A = np.array([[7, 0, 0, 0, 0, 1],
              [0, 13, 0, 0, 0, 1],
              [0, 0, 59, 0, 0, 1],
              [0, 0, 0, 31, 0, 1],
              [0, 0, 0, 0, 19, 1]])
B = np.array([0, 1, 4, 6, 7])
x = np.linalg.solve(A,B)

# Get the time and ID of earliest bus we can take.
min_id, min_time = min(earliest, key=lambda x: x[1])
print(min_id, min_time)
print('Part 1 Answer: {}'.format((min_time - departure) * min_id))

# Remove the 'x' IDs.
ids = [[x[0], int(x[1])] for x in enumerate(ids) if x[1] != 'x']
# Find the largest ID and index.
largest_id = max(ids, key=lambda x: int(x[1]))
print(f'Largest ID: {largest_id}')

time = 0
while True:
    time += int(largest_id[1])

    # See if the time fits the requirements.
    # First calculate t=0 and see if it fits
    t0 = time - largest_id[0]
    if t0 % ids[0][1] == 0:
        # t0 matches, check rest of list
        if all([((t0 + i[0]) % i[1]) == 0 for i in ids[1:]]):
            print(f'GOT IT!: {t0}')
            quit()
