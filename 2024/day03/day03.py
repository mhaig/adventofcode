#!/usr/bin/env python3

import re
import sys


def sum_all_muls(line):
    result = 0
    for mul in re.findall(r"mul\(\d+,\d+\)", line):
        digits = re.findall(r"\d+", mul)
        if len(digits) == 2:
            result += int(digits[0]) * int(digits[1])
        else:
            print("something happened!")
            exit()

    return result


program_memory = "\n".join(sys.stdin.readlines())

result = sum_all_muls(program_memory)

print(f"Day 3 Part 1 Solution: {result}")

result = 0

for match in re.finditer(
    r"^.*?(?=don't|do)|(don't.*?(?=don't|do)|do.*?(?=don't|do))|(?=don't|do).*?$",
    program_memory,
    re.MULTILINE | re.DOTALL,
):
    if match.group(0)[0:5] == "don't":
        continue

    result += sum_all_muls(match.group(0))

print(f"Day 3 Part 2 Solution: {result}")
