#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

PREAMBLE_LENGTH = 25

preamble = []
sum_list = []

numbers = [int(x) for x in sys.stdin.read().strip().split('\n')]

for num in numbers:

    num = int(num)
    if len(preamble) == PREAMBLE_LENGTH:
        # See if numbers in the preamble sum to current number.
        exists = False
        for n in preamble:
            # Make sure the difference is not the same number.
            if num - n == num:
                continue
            if num - n in preamble:
                exists = True
                break

        if not exists:
            # Found the answer to Part 1
            print(f'Part 1 Answer: {num}')
            break

        # Remove the first element of the preamble.
        preamble = preamble[1:]

    # Add the newest number to the preamble
    preamble.append(int(num))

# Found the missing number, now find the contiguous sum.
start = 0
end = 1
while (s := sum(numbers[start:end])) != num:
    if s > num:
        start += 1
    else:
        end += 1

print('Part 2 Answer: {}'.format(min(numbers[start:end])+max(numbers[start:end])))
