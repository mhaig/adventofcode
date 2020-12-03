#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def part1(nums):
    """Find the two numbers that sum to 2020 and print their product."""
    for n in nums:

        find = 2020 - n
        if find < 0:
            continue

        if find in nums:
            product = n * find
            print('Part 1 Answer: {} * {} = {}'.format(n, find, product))
            return [n, find, product]

def part2(nums):
    """Find the three numbers that sum to 2020 and print their product."""
    for i, n in enumerate(nums):
        for j, o in enumerate(nums[i+1:]):
            for k, p in enumerate(nums[i+1+j+1:]):
                if n + o + p == 2020:
                    print('Part 2 Answer: {} * {} * {} = {}'.format(n, o, p,
                                                                    (n*o*p)))
                    return [n, o, p, (n*o*p)]



nums = [int(x) for x in sys.stdin.readlines()]

part1(nums)
part2(nums)
