#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def line_to_list(line):
    result = []
    for c in line:
        if c == ' ':
            next
        else:
            result.append(c)

    return result


def do_math(equation):

    i = 0
    answer = 0
    while i < len(equation):
        if equation[i] == '+':
            i += 1
            if equation[i] == '(':
                i += 1
                t = do_math(equation[i:])
                answer += t[1]
                i += t[0]
            else:
                answer += int(equation[i])
            i += 1
        elif equation[i] == '*':
            i += 1
            if equation[i] == '(':
                i += 1
                t = do_math(equation[i:])
                answer *= t[1]
                i += t[0]
            else:
                answer *= int(equation[i])
            i += 1
        elif equation[i] == '(':
            i += 1
            t = do_math(equation[i:])
            answer += t[1]
            i += t[0]
            i += 1
        elif equation[i].isdigit():
            answer = int(equation[i])
            i += 1
        else:
            break

    return i, answer

puzzle_input = sys.stdin.read().strip()

answers = []
for line in puzzle_input.split('\n'):

    answers.append(do_math(line_to_list(line))[1])

print('Part 1 Answer: {}'.format(sum(answers)))

def solve_addition(equation):

    i = 0
    while '+' in equation:
        while i < len(equation):
            if equation[i] == '+':
                i += 1
                if equation[i] == '(':
                    i += 1
                    t = solve_addition(equation[i:])
                    answer += t[1]
                    i += t[0]
                else:
                    answer += int(equation[i])
                i += 1
            # elif equation[i] == '*':
            #     i += 1
            #     if equation[i] == '(':
            #         i += 1
            #         t = do_math(equation[i:])
            #         answer *= t[1]
            #         i += t[0]
            #     else:
            #         answer *= int(equation[i])
            #     i += 1
            elif equation[i] == '(':
                i += 1
                t = do_math(equation[i:])
                answer += t[1]
                i += t[0]
                i += 1
            elif equation[i].isdigit():
                answer = int(equation[i])
                i += 1
            else:
                break

        return i, answer



answers = []
for line in puzzle_input.split('\n'):

    answers.append(solve_addition(line_to_list(line)))
