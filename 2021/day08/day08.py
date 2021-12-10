#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from seven_segment import SevenSegment

signal_pattern = []
output_value = []

for line in sys.stdin.readlines():
    sp, ov = line.split('|')
    signal_pattern.append([x.strip() for x in sp.split(' ') if x])
    output_value.append([x.strip() for x in ov.split(' ') if x])

entries = list(zip(signal_pattern, output_value))

# Part 1, in the output values, count the number of 1, 4, 7, and 8 digits
unique_segments = 0
for e in entries:
    for digit in e[1]:
        if len(digit) in [2, 4, 3, 7]:
            unique_segments += 1

print('Part 1 Solution: {}'.format(unique_segments))

total = 0
for e in entries:

    segment = SevenSegment()
    output = []

    for i in range(len(e[0]+e[1])):
        for digit in e[0] + e[1]:
            # print('working on digit {}'.format(digit))
            segment.set_unknown(digit)
        if segment.solved():
            break

    for digit in e[1]:
        output.append(segment.get_digit(digit))
    total += int(''.join([str(i) for i in output]))

print('Part 2 Solution: {}'.format(total))
