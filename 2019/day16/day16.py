#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

base_pattern = [0, 1, 0, -1]
input_signal = [int(x) for x in sys.stdin.read().strip()]

for _ in range(100):
    new_signal = []
    for i in range(1, len(input_signal)+1):
        # Build the real pattern
        pattern = []
        spot = 0
        while len(pattern) < len(input_signal) + 1:
            pattern.extend([base_pattern[spot % 4]]*i)
            spot += 1
        pattern = pattern[1:len(input_signal)+1]
        d = str(sum([x[0] * x[1] for x in zip(input_signal, pattern)]))[-1]
        new_signal.append(int(d))

    input_signal = new_signal

print(''.join([str(x) for x in new_signal][0:8]))
