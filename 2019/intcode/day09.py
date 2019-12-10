#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
import intcode_computer

with open(sys.argv[1], 'r') as f:
    program = f.read()
computer = intcode_computer.IntcodeComputer(program)

computer.execute()
