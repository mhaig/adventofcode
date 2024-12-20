#!/usr/bin/env python3

import sys
from functools import cache

from aoc.node import LinkedList
from rich.progress import track


@cache
def count_digits(number: int) -> int:
    count = 0

    if number == 0:
        return 1

    while number != 0:
        number = number // 10
        count += 1

    return count


@cache
def split(number: int) -> tuple[int, int]:

    length = count_digits(number) // 2
    splitter = 1
    for _ in range(length):
        splitter *= 10

    right = number % splitter
    left = number // splitter

    return (left, right)


@cache
def blink(stone, count) -> int:

    if count == 0:
        return 1

    if stone == 0:
        return blink(1, count - 1)
    elif count_digits(stone) % 2 == 0:
        left, right = split(stone)
        return blink(left, count - 1) + blink(right, count - 1)
    else:
        return blink(stone * 2024, count - 1)


string_input = sys.stdin.read().strip()

stones = [int(x) for x in string_input.split()]

total_stones = 0
for s in track(stones):
    total_stones += blink(s, 25)
print(f"Day 11 Part 1 Solution: {total_stones}")

total_stones = 0
for s in track(stones):
    total_stones += blink(s, 75)
print(f"Day 11 Part 2 Solution: {total_stones}")
