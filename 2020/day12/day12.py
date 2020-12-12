#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import math
import sys

DIRECTIONS = ['N', 'E', 'S', 'W']
ship_x = 0
ship_y = 0
ship_d = 'E'
waypoint_x = 0
waypoint_y = 0

input_instructions = sys.stdin.read().strip()

for instruction in input_instructions.split('\n'):
    action = instruction[0]
    value = int(instruction[1:])

    # If action is to move forward, replace with current direction.
    if action == 'F':
        action = ship_d

    if action == 'N':
        ship_y += value
    elif action == 'S':
        ship_y -= value
    elif action == 'E':
        ship_x += value
    elif action == 'W':
        ship_x -= value
    elif action == 'L':
        value = value // 90
        index = (DIRECTIONS.index(ship_d) - value) % len(DIRECTIONS)

        ship_d = DIRECTIONS[index]
    elif action == 'R':
        value = value // 90
        index = (DIRECTIONS.index(ship_d) + value) % len(DIRECTIONS)

        ship_d = DIRECTIONS[index]

print('Part 1 Answer: {}'.format(abs(ship_x) + abs(ship_y)))

def rotate(x, y, deg):
    new_x = ((x*math.cos(math.radians(deg))) -
             (y*math.sin(math.radians(deg))))
    new_y = ((x*math.sin(math.radians(deg))) +
             (y*math.cos(math.radians(deg))))
    return round(new_x), round(new_y)

ship_x = 0
ship_y = 0
waypoint_x = 10
waypoint_y = 1
for instruction in input_instructions.split('\n'):
    action = instruction[0]
    value = int(instruction[1:])

    if action == 'R':
        value *= -1

    # If action is to move forward, move to the waypoint times equals value.
    if action == 'F':
        ship_x = ship_x + (waypoint_x * value)
        ship_y = ship_y + (waypoint_y * value)
    elif action == 'N':
        waypoint_y += value
    elif action == 'S':
        waypoint_y -= value
    elif action == 'E':
        waypoint_x += value
    elif action == 'W':
        waypoint_x -= value
    elif action in ['L', 'R']:
        waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, value)

print('Part 2 Answer: {}'.format(abs(ship_x) + abs(ship_y)))
