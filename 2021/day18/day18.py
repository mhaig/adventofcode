#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import math
import sys

def reduce_r(a, depth):
    # print('Pair: {},{}  Depth: {}'.format(a[0], a[1], depth))
    remainder = (0,0)

    if depth == 4:
        # print('explode {},{}'.format(a[0], a[1]))
        return 0, (a[0], a[1])
    else:
        if isinstance(a[0], list):
            b,remainder = reduce(a[0], depth+1)
        else:
            b = a[0] + remainder[0]
            remainder = (0, remainder[1])

        if isinstance(a[1], list):
            c,remainder = reduce(a[1], depth+1)
        else:
            c = a[1] + remainder[1]
            remainder = (remainder[0], 0)

        if not isinstance(b, list):
            b += remainder[0]
            remainder = (0, remainder[1])


    return [b, c], remainder


def magnitude(a_list):

    if not isinstance(a_list, list):
        return a_list

    return 3*magnitude(a_list[0]) + 2*magnitude(a_list[1])

def get_pair(l):

    pair = ''
    i = 0
    while l[i] != ']':
        pair += l[i]
        i += 1
    pair += ']'

    pair = eval(pair)

    return pair, i

def get_int(l):
    integer = ''
    i = 0
    while l[i] not in ['[',',',']']:
        integer += l[i]
        i += 1

    return int(integer), i-1

def get_previous_int(l):

    nums_only = l.replace('[', '')
    nums_only = nums_only.replace(']', '')
    last_num = nums_only.strip(',').split(',')[-1]
    if last_num:
        return last_num

    return None


def reduce(l, explode=False, split=False):

    string_list = str(l)
    string_list = string_list.replace(' ','')
    reduced_list = ''
    depth = 0
    found_integer = False
    action = False
    right = 0
    integer = 0

    i = 0
    while i < len(string_list):
        if string_list[i] == '[':
            depth += 1
            # print('depth at {}'.format(depth))
        elif string_list[i] == ']':
            depth -= 1
            # print('depth at {}'.format(depth))
        elif string_list[i] >= '0' and string_list[i] <= '9':
            integer, consume = get_int(string_list[i:])
            i += consume
            found_integer = True

        if depth == 5 and not action and explode:
            # This pair needs to be exploded, consume the incoming pair to
            # process.
            pair,consume = get_pair(string_list[i:])
            i += consume
            depth -= 1
            print('exploding {}'.format(pair))
            # See if there was an integer to the left of this pair.  Work
            # backwards through the reduced list to find the first integer (if
            # any).
            last_num = get_previous_int(reduced_list)
            if last_num:
                # print('found an int {} at {}'.format(reduced_list[pos], pos))
                reduced_list = str(int(last_num) + pair[0]).join(reduced_list.rsplit(last_num,1))
                # reduced_list = (reduced_list[0:pos] +
                #                 str(int(reduced_list[pos]) + pair[0]) +
                #                 reduced_list[pos+1:])
            # Save right to add later as we continue to process.
            right = pair[1]


            reduced_list += '0'
            action = True
        elif integer >= 10 and not action and split:
            # This is a number that needs to be split.
            new_pair = ('[' +
                        str(math.floor(integer / 2)) +
                        ',' +
                        str(math.ceil(integer / 2)) +
                        ']')
            print('splitting {} into {}'.format(integer, new_pair))
            reduced_list += new_pair
            action = True
            found_integer = False
        else:
            if found_integer:
                reduced_list += str(integer + right)
                found_integer = False
                right = 0
            # if string_list[i] >= '0' and string_list[i] <= '9':
            #     reduced_list += str(int(string_list[i]) + right)
            #     right = 0
            else:
                reduced_list += string_list[i]

        i += 1

    return reduced_list

rolling_sum = ''
for line in sys.stdin.readlines():
    if rolling_sum:
        print('adding {} to {}'.format(rolling_sum, line.strip()))
        rolling_sum = str([eval(rolling_sum), eval(line.strip())])
    else:
        rolling_sum = line.strip()
    print(rolling_sum)

    reduced = ''
    original = rolling_sum
    while True:
        # while True:
        reduced = reduce(original, explode=True)
        print('step: {}'.format(reduced))
        if original != reduced:
            original = reduced
            continue

        reduced = reduce(original, split=True)
        print('step: {}'.format(reduced))
        if original != reduced:
            original = reduced
            continue
        else:
            break



    rolling_sum = reduced
    print('Reduced: {}'.format(rolling_sum))

print('Part 1 Solution: {}'.format(magnitude(eval(rolling_sum))))
