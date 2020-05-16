#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse

from intcode import intcode_computer

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

program_output = []
def output_handler(output):
    try:
        program_output.append(chr(output))
    except:
        program_output.append(str(output))

computer = intcode_computer.IntcodeComputer(program, True)

# AND X Y
# OR  X Y
# NOT X Y
# A B C D, T J

# Make sure we need to jump, see if there is an empty tile in the next four
# blocks.
#
#  OR A T
#  AND B T
#  AND C T
#  AND D T
#  NOT T T
#
# T should be TRUE if there is an empty block in the next four steps
# Only jump if safe to land (there is a block 4 steps away)
#  AND D T
# T should be TRUE if it's safe to land
#  NOT T T
#  NOT T J

springscript= """OR A T
AND B T
AND C T
AND D T
NOT T T
AND D T
NOT T T
NOT T J
WALK
"""

computer.add_output_handler(output_handler)
computer.set_input([ord(x) for x in springscript])

computer.execute()

print(''.join(program_output))

computer.reset()
program_output = []

# AND X Y
# OR  X Y
# NOT X Y
# A B C D E F G H I, T J

# Make sure we need to jump, see if there is an empty tile in the next four
# blocks.
#
#  OR A T
#  AND B T
#  AND C T
#  AND D T
#  NOT T T
#
# T should be TRUE if there is an empty block in the next four steps
# Only jump if safe to land (there is a block 4 and 5 steps away)
#  AND D T
#  AND E T
# T should be TRUE if it's safe to land
#  NOT T T
#  NOT T J
springscript= """OR A T
AND B T
AND C T
AND D T
NOT T T
AND D T
AND E T
NOT T T
NOT T J
RUN
"""
computer.set_input([ord(x) for x in springscript])
computer.execute()

print(''.join(program_output))
