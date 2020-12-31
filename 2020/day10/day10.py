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

def build_chain(chain, sources, rated):
    in3 = []
    for x in sources:
        if x - chain[-1] > 3:
            break
        elif x - chain[-1] > 0:
            in3.append(x)

    total = 0
    if not in3:
        # See if the end is 3 within our final value.
        if (rated - chain[-1]) in [1, 2, 3]:
            return 1
        else:
            return 0
    for t in in3:
        total += build_chain(chain + [t], sources[:sources.index(t)]+sources[sources.index(t)+1:], rated)

    return total

joltage_adapters = [int(x) for x in puzzle_input.split()]
# print('Part 2 Answer: {}'.format(build_chain([0], sorted(joltage_adapters), rated)))

joltage_adapters = [0] + joltage_adapters + [rated]
joltage_adapters = sorted(joltage_adapters)
reach = [1]
for i,v in enumerate(joltage_adapters):
    print(v)
    if i:
        reach.append(0)
        for j in [1,2,3]:
            if i-j >= 0 and v - joltage_adapters[i-j] <= 3:
                reach[-1] += 1

print(reach)
