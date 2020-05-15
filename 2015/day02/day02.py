#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def calculate_wrapping_paper(l, w, h):
    areas = [l*w, w*h, h*l]
    return 2 * sum(areas) + min(areas)

def xx_to_lwh(xx):
    return {'l': int(xx.split('x')[0]),
            'w': int(xx.split('x')[1]),
            'h': int(xx.split('x')[2])
            }

def calculate_ribbon(l, w, h):
    perimeters = [2*l + 2*w, 2*h + 2*w, 2*h + 2*l]
    return min(perimeters) + (l * w * h)

def solve(input_data, func):
    return sum([func(**xx_to_lwh(x)) for x in input_data.split('\n') if x])

if __name__ == '__main__':

    data = sys.stdin.read()
    print(solve(data, calculate_wrapping_paper))
    print(solve(data, calculate_ribbon))
