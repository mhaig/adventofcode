#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def draw_line_down(start: list, steps: int):

    start_x = start[0]
    start_y = start[1]

    segment = [(start_x, start_y - y) for y in range(1, steps+1)]
    return segment

def draw_line_up(start: list, steps: int):

    start_x = start[0]
    start_y = start[1]

    segment = [(start_x, start_y + y) for y in range(1, steps+1)]
    return segment

def draw_line_left(start: list, steps: int):

    start_x = start[0]
    start_y = start[1]

    segment = [(start_x - x, start_y) for x in range(1, steps+1)]
    return segment

def draw_line_right(start: list, steps: int):

    start_x = start[0]
    start_y = start[1]

    segment = [(start_x + x, start_y) for x in range(1, steps+1)]
    return segment

def draw_line(line_xy: list, directions: list):

    for direction in directions:

        if direction[0] == 'D':
            line_xy.extend(draw_line_down(line_xy[-1], int(direction[1:])))
        elif direction[0] == 'U':
            line_xy.extend(draw_line_up(line_xy[-1], int(direction[1:])))
        elif direction[0] == 'R':
            line_xy.extend(draw_line_right(line_xy[-1], int(direction[1:])))
        elif direction[0] == 'L':
            line_xy.extend(draw_line_left(line_xy[-1], int(direction[1:])))

    return line_xy

input_lines = [x.split(',') for x in sys.stdin.read().split('\n') if x]
line_points = list()

for input_line in input_lines:

    line = [(0,0)]

    line_points.append(draw_line(line, input_line))

# intersections = [xy for xy in line_points[0] if xy in line_points[1]]
# intersections.remove((0,0))
# print(intersections)

intersections = set(line_points[0]) & set(line_points[1])
intersections.remove((0,0))
print(intersections)

md = [abs(x[0])+abs(x[1]) for x in intersections]
print(md)
md.sort()
print(md[0])

# For each intersection, calculate the sum of the length for each wire to hit
# it and find the best one.
intersections_lengths = []
for intersection in intersections:

    wire_1_location = line_points[0].index(intersection)
    wire_2_location = line_points[1].index(intersection)

    wire_1_steps = len(line_points[0][0:wire_1_location])
    wire_2_steps = len(line_points[1][0:wire_2_location])

    intersections_lengths.append(wire_1_steps + wire_2_steps)

intersections_lengths.sort()
print(intersections_lengths[0])
