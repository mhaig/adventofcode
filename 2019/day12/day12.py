#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import copy
import math
import numpy
import sys

import moon

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

moons = []
for line in sys.stdin.read().split('\n'):
    if len(line):
        print(line)
        xyz = [x.split('=')[1] for x in line.strip('<>').split(',')]
        moons.append(moon.Moon(xyz[0], xyz[1], xyz[2]))

print('\n'.join([str(x) for x in moons]))

original = copy.deepcopy(moons)

count = 0
while True:
    for m in moons:
        for o in moons:
            m.update_velocity(o)

    for m in moons:
        m.apply_velocity()

    count += 1

    if count == 1000:
        break

print('\n'.join([str(x) for x in moons]))
print(f'Part 1 solution: {sum([x.total_energy for x in moons])}')

def find_repeat(moonss, pos):
    count = 0
    while True:
        for m in moonss:
            for o in moonss:
                if pos == 'x':
                    m.update_velocity_x(o)
                elif pos == 'y':
                    m.update_velocity_y(o)
                elif pos == 'z':
                    m.update_velocity_z(o)

        for m in moonss:
            if pos == 'x':
                m.apply_velocity_x()
            elif pos == 'y':
                m.apply_velocity_y()
            elif pos == 'z':
                m.apply_velocity_z()

        count += 1
        if pos == 'x':
            if (moonss[0].xvx == original[0].xvx and
                moonss[1].xvx == original[1].xvx and
                moonss[2].xvx == original[2].xvx and
                moonss[3].xvx == original[3].xvx):
                print(f'Repeat found in x at: {count}')
                return count
        if pos == 'y':
            if (moonss[0].yvy == original[0].yvy and
                moonss[1].yvy == original[1].yvy and
                moonss[2].yvy == original[2].yvy and
                moonss[3].yvy == original[3].yvy):
                print(f'Repeat found in y at: {count}')
                return count
        if pos == 'z':
            if (moonss[0].zvz == original[0].zvz and
                moonss[1].zvz == original[1].zvz and
                moonss[2].zvz == original[2].zvz and
                moonss[3].zvz == original[3].zvz):
                print(f'Repeat found in z at: {count}')
                return count


moons = copy.deepcopy(original)
x = find_repeat(moons, 'x')
y = find_repeat(moons, 'y')
z = find_repeat(moons, 'z')

print(x, y, z)
lcm = numpy.lcm.reduce([x, y, z])
print(f'Part 2 Solution: {lcm}')
