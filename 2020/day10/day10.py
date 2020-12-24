#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

puzzle_input = sys.stdin.read().strip()

joltage_adapters = [int(x) for x in puzzle_input.split()]
rated = max(joltage_adapters) + 3

chain = [0]
diff1 = 0
diff3 = 0
while joltage_adapters:
    # Find the adapter(s) that are within 3 of the last added to the chain.
    in3 = [x for x in joltage_adapters if (x - chain[-1]) in [1, 2, 3]]
    a = min(in3)
    if a - chain[-1] == 3:
        diff3 += 1
    elif a - chain[-1] == 1:
        diff1 += 1
    chain.append(a)
    joltage_adapters.remove(a)

if rated - chain[-1] == 3:
    diff3 += 1
elif rated - chain[-1] == 1:
    diff1 += 1
chain.append(rated)
print(f'{diff1} differences of 1 jolt and {diff3} differences of 3 jolts')
print('Part 1 Answer: {}'.format(diff1 * diff3))
