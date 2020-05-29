#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def is_nice_string(string):

    if any(x in string for x in ['ab', 'cd', 'pq', 'xy']):
        return False

    letter_count = { 'a': 0,
                     'e': 0,
                     'i': 0,
                     'o': 0,
                     'u': 0,
                   }
    double_letter = False
    for i, c in enumerate(string):
        if not double_letter and i+1 < len(string) and string[i+1] == c:
            double_letter = True

        if c in letter_count.keys():
            letter_count[c] += 1

    return double_letter and sum(letter_count.values()) >= 3

def solve(strings):
    return sum([1 for x in strings.split('\n') if is_nice_string(x)])

if __name__ == '__main__':
    strings = sys.stdin.read()
    print(solve(strings))
