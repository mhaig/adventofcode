#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import math
import sys

def lcd(nominator, denominator):
    gcd = math.gcd(nominator, denominator)
    return (nominator / gcd, denominator / gcd)

class Station(object):
    """Docstring for Station."""

    def __init__(self, location):
        """
        @todo Document Station.__init__ (along with arguments).

        location - @todo Document argument location.
        """
        self._location = location
        self._slopes = []
        self._points = []

    def add_point(self, point):
        self._points.append(point)

    def add_slope(self, slope):
        self._slopes.append(slope)

    def get_asteroid_count(self):
        return len(set(self._slopes))

    def print_slopes(self):
        print(self._slopes)

    def to_sorted_polar(self):
        # First convert each point to x, y centered around self.
        centered = []
        polar = []
        for p in self._points:
            centered.append([[p[0], p[1]], [p[0] - self._location[0], p[1] - self._location[1]]])
        # Now calculate r and theta
        for b, c in centered:
            r = math.sqrt((c[0] ** 2) + (c[1] ** 2))
            if c[0] == 0:
                if c[1] > 0:
                    theta = 90.0
                else:
                    theta = 270.0
            else:
                theta = math.degrees(math.atan(c[1] / c[0]))
                if c[0] < 0:
                    theta += 180
                elif c[1] < 0:
                    theta += 360
            # print(r, theta)
            # Rotate theta by 90
            theta += 90
            if theta >= 360:
                theta -= 360
            polar.append([b, [r, theta]])

        # print(len(set([x[1] for b, x in polar])))
        return sorted(polar, key=lambda p: (p[1][1], p[1][0]))


    def __str__(self):
        return '({}, {}), {}'.format(self._location[0],
                                     self._location[1],
                                     self.get_asteroid_count())

with open(sys.argv[1], 'r') as f:
    asteroid_map = f.read()

cartesian = []
for y, row in enumerate(asteroid_map.split('\n')):
    for column in range(len(row)):
        if row[column] == '#':
            cartesian.append([column, y])

stations = []
for c in cartesian:
    station = Station(c)
    for d in cartesian:
        if c == d:
            next
        else:
            # Calculate slope
            if d[0] - c[0] == 0:
                if d[1] - c[1] > 0:
                    slope = 'INFU'
                else:
                    slope = 'INFD'
            elif d[1] - c[1] == 0:
                if d[0] - c[0] > 0:
                    slope = 'ZEROR'
                else:
                    slope = 'ZEROL'
            else:
                slope = lcd((d[1] - c[1]) , (d[0] - c[0]))
            station.add_slope(slope)
            station.add_point(d)
    stations.append(station)


best = max(stations, key=lambda s: s.get_asteroid_count())
print(f"Max: {best}")

sorted_polar = best.to_sorted_polar()
last_deleted_angle = None
deleted_count = 0
for x, p in enumerate(sorted_polar[:]):

    if last_deleted_angle != None:
        if last_deleted_angle == p[1][1]:
            continue

    sorted_polar.remove(p)
    last_deleted_angle = p[1][1]
    deleted_count += 1

    if deleted_count >= 200:
        print(f'({p[0][0]}, {p[0][1]}) Answer: {(p[0][0]*100) + p[0][1]}')
        break
