#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

def execute(p: list):

    pc = 0

    while p[pc] != 99:

        if p[pc] == 1: # opcode 1: add
            p[p[pc+3]] = (p[p[pc+1]] + p[p[pc+2]])
        elif p[pc] == 2: # opcode 2: multiply
            p[p[pc+3]] = (p[p[pc+1]] * p[p[pc+2]]) 

        pc += 4

    return p


program = [int(x) for x in sys.stdin.read().split(',')]
original_program = list(program)

# Make adjustments per problem:
#   program[1] = 12
#   program[2] = 2
program[1] = 12
program[2] = 2

program = execute(program)


print(','.join([str(x) for x in program]))
print('Result: {}'.format(program[0]))

output = int(sys.argv[1])

found = False
for n in range(100):
    for v in range(100):
        program = list(original_program)

        program[1] = n
        program[2] = v

        program = execute(program)

        if program[0] == output:
            print('noun {} verb {} answer {}'.format(n, v, 100 * n + v))
            found = True
            break

    if found:
        break
