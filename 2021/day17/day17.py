#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

input_string = sys.stdin.read().strip()

x_loc = input_string.find('x=')
c_loc = input_string.find(',')
y_loc = input_string.find('y=')

x_string = input_string[x_loc+2:c_loc]
y_string = input_string[y_loc+2:]

target_x = [int(x) for x in x_string.split('..')]
target_y = [int(y) for y in y_string.split('..')]

print('Target x: {}'.format(target_x))
print('Target y: {}'.format(target_y))

def step(x, y, vx, vy):
    x += vx
    y += vy

    vy -= 1

    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1

    return x, y, vx, vy

max_y = 0
solved = []
for vx in range(0,target_x[1]+1):
    for vy in range(target_y[0], abs(target_y[0])):
        nvx = vx
        nvy = vy
        x = 0
        y = 0
        temp_max_y = max_y
        for s in range(1000):
            x, y, nvx, nvy = step(x, y, nvx, nvy)
            if y > temp_max_y:
                temp_max_y = y

            if ((x >= target_x[0] and x <= target_x[1]) and
                (y >= target_y[0] and y <= target_y[1])):
                if (vx, vy) not in solved:
                    solved.append((vx, vy))
                if temp_max_y > max_y:
                    max_y = temp_max_y

print('Part 1 Solution: {}'.format(max_y))
print('Part 2 Solution: {}'.format(len(solved)))
