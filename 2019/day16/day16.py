#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

base_pattern = [0, 1, 0, -1]
original_signal = [int(x) for x in sys.stdin.read().strip()]

input_signal = original_signal
# Build the patterns up front.
patterns = []
print('Part 1, generating patterns')
for i in range(1, len(input_signal)+1):
    pattern = []
    spot = 0
    while len(pattern) < len(input_signal) + 1:
        pattern.extend([base_pattern[spot % 4]]*i)
        spot += 1
    patterns.append(pattern[1:len(input_signal)+1])

# Part 1
print('Part 1, solving')
for _ in range(100):
    new_signal = []
    for i in range(len(input_signal)):
        # Build the real pattern
        d = str(sum([x[0] * x[1] for x in zip(input_signal, patterns[i])]))[-1]
        new_signal.append(int(d))

    input_signal = new_signal

print(''.join([str(x) for x in new_signal][0:8]))

# Part 2
input_signal = original_signal * 2
# Build the patterns up front.
print('Part 2, generating patterns')
patterns = []
for i in range(1, len(input_signal)+1):
    pattern = []
    spot = 0
    while len(pattern) < len(input_signal) + 1:
        pattern.extend([base_pattern[spot % 4]]*i)
        spot += 1
    patterns.append(pattern[1:len(input_signal)+1])


print('Part 2, solving')
steps = []
for _ in range(100):
    new_signal = []
    for i in range(len(input_signal)):
        # Build the real pattern
        d = str(sum([x[0] * x[1] for x in zip(input_signal, patterns[i])]))[-1]
        new_signal.append(int(d))

    input_signal = new_signal
    # steps.append(''.join([str(x) for x in new_signal]))
    steps.append(new_signal)

# print(steps[2] - steps[1])
# print(steps[3] - steps[2])
# print(steps[4] - steps[3])
# print(steps[5] - steps[4])
print(''.join([str(x) for x in steps[0]]))
print(''.join([str(x) for x in steps[1]]))
print(''.join([str(x) for x in steps[2]]))
print(''.join([str(x) for x in steps[3]]))
print(''.join([str(x) for x in steps[4]]))
print(''.join([str(x) for x in steps[5]]))
print(''.join([str(x) for x in steps[6]]))
print(''.join([str(x) for x in steps[7]]))
print(''.join([str(x) for x in steps[8]]))
print(''.join([str(x) for x in steps[9]]))
