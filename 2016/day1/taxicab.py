#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

i = 0
for line in sys.stdin:
    current_direction = ''
    current_distance = 0
    for step in line.split(','):
        step = step.strip()
        # step[0] is the direction
        # step[1:] is amount of blocks
        direction = step[0]
        distance = step[1:]

        print direction + ' ' + distance
        if current_direction == '':
            current_direction = direction
            current_distance = int(distance)
            continue

        if current_direction == direction:
            # Making the same turn, subtract.
            current_distance = abs(current_distance) - int(distance)
        else:
            # Changing direction, add.
            current_distance = abs(current_distance) + int(distance)
            current_direction = direction

        print current_distance

    print current_distance

