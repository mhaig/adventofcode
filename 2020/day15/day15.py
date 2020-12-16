#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

puzzle_input = sys.stdin.read().strip()

numbers = {int(x):[i+1] for i,x in enumerate(puzzle_input.split(','))}
print(numbers)
last_number = int(puzzle_input.split(',')[-1])
print(len(numbers))

for x in range(len(numbers)+1,2020+1):

    if len(numbers[last_number]) > 1:
        # Last number spoken has been spoken before.  Get the previous two
        # rounds that the number was spoken.
        previous = numbers[last_number][1]
        previous_1 = numbers[last_number][0]

        last_number = previous - previous_1

        if last_number not in numbers:
            numbers[last_number] = [x]
        elif len(numbers[last_number]) == 1:
            numbers[last_number].append(x)
        else:
            numbers[last_number][0] = numbers[last_number][1]
            numbers[last_number][1] = x
    else:
        # print('{} not in {}, adding 0'.format(numbers[-1], numbers[:-1]))
        if len(numbers[0]) == 1:
            numbers[0].append(x)
        else:
            numbers[0][0] = numbers[0][1]
            numbers[0][1] = x

        last_number = 0


print('Part 1 Answer: {}'.format(last_number))

# for x in range(2020+2, 30000000+1):
for x in range(2020+1, 30000000+1):

    if len(numbers[last_number]) > 1:
        # Last number spoken has been spoken before.  Get the previous two
        # rounds that the number was spoken.
        previous = numbers[last_number][1]
        previous_1 = numbers[last_number][0]

        last_number = previous - previous_1

        if last_number not in numbers:
            numbers[last_number] = [x]
        elif len(numbers[last_number]) == 1:
            numbers[last_number].append(x)
        else:
            numbers[last_number][0] = numbers[last_number][1]
            numbers[last_number][1] = x
    else:
        # print('{} not in {}, adding 0'.format(numbers[-1], numbers[:-1]))
        if len(numbers[0]) == 1:
            numbers[0].append(x)
        else:
            numbers[0][0] = numbers[0][1]
            numbers[0][1] = x

        last_number = 0

    if x % 1000000 == 0:
        print(x)

print(len(numbers))
print('Part 2 Answer: {}'.format(last_number))
