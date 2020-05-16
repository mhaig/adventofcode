#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from operator import add

KEY = {'^': [0, 1],
       'v': [0, -1],
       '>': [1, 0],
       '<': [-1, 0]}

def solve(data, santas):

    pos = []
    houses = {}
    for s in range(santas):
        pos.append((0, 0))
        houses[pos[s]] = 0

    for s,c in enumerate(data):
        pos[s % santas] = tuple(map(add, pos[s % santas], KEY[c]))
        houses[pos[s % santas]] = 0

    return len(houses)

if __name__ == '__main__':

    data = sys.stdin.read()
    print(solve(data.strip(), 1))
    print(solve(data.strip(), 2))
