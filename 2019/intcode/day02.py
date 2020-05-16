#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
import intcode_computer

program = sys.stdin.read()
computer = intcode_computer.IntcodeComputer(program)

# Make adjustments per problem:
#   program[1] = 12
#   program[2] = 2
computer.set_value(1, 12)
computer.set_value(2, 2)

computer.execute()

print(f'Result: {computer.get_value(0)}')

output = int(sys.argv[1])

found = False
for n in range(100):
    for v in range(100):
        computer.reset()

        computer.set_value(1, n)
        computer.set_value(2, v)

        computer.execute()

        if computer.get_value(0) == output:
            print(f'noun {n} verb {v} answer {100 * n + v}')
            found = True
            break

    if found:
        break
