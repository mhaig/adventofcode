#!/usr/bin/env python3

import sys


def digit_word(word: str) -> str | None:
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for k, v in digits.items():
        if len(word) >= len(k):
            if word[: len(k)] in digits:
                return digits[word[: len(k)]]

    return None


def get_calibration_value(line: str) -> tuple[int, int]:
    digits_1 = []
    digits_2 = []

    for i, c in enumerate(line):
        if c.isdigit():
            digits_1.append(c)
            digits_2.append(c)
            continue

        d = digit_word(line[i:])
        if d:
            digits_2.append(d)

    # part1 = int(digits_1[0] + digits_1[-1])
    part1 = 0
    part2 = int(digits_2[0] + digits_2[-1])

    return (part1, part2)


calibration_document = list(sys.stdin.readlines())

calibration_value_1 = 0
calibration_value_2 = 0
for line in calibration_document:
    calibration_values = get_calibration_value(line)
    calibration_value_1 += calibration_values[0]
    calibration_value_2 += calibration_values[1]

print(f"Part 1 Solution: {calibration_value_1}")
print(f"Part 2 Solution: {calibration_value_2}")
