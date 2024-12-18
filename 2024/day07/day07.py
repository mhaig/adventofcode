#!/usr/bin/env python3

import sys
from equation import Equation

string_input = sys.stdin.read()

test_value_sum = 0
unsolved = []
for line in string_input.split("\n"):

    if not line:
        continue

    eq = Equation(line)

    if eq.solve_add_mul():
        test_value_sum += eq._test_value
    else:
        unsolved.append(eq)

print(f"Day 7 Part 1 Solution: {test_value_sum}")

for eq in unsolved:

    if eq.solve_concat():
        test_value_sum += eq._test_value

print(f"Day 7 Part 2 Solution: {test_value_sum}")
