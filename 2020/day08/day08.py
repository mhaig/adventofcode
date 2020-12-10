#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

class Instruction(object):
    """Docstring for Instruction."""

    def __init__(self, operation, argument):
        """
        @todo Document Instruction.__init__ (along with arguments).

        operation - @todo Document argument operation.
        argument - @todo Document argument argument.
        """
        self._operation = operation
        self._argument = int(argument)

    @property
    def operation(self):
        return self._operation
    @operation.setter
    def operation(self, op):
        self._operation = op

    @property
    def argument(self):
        return self._argument

    def __str__(self):
        return f'{self.operation} {self.argument}'

class Machine(object):
    """Docstring for Machine."""

    def __init__(self, program):
        """
        @todo Document Machine.__init__ (along with arguments).

        program - @todo Document argument program.
        """
        if isinstance(program, str):
            self._program = program.split('\n')

        self._program = program
        self._last_fixed = 0

        self.reset()

    def reset(self):
        self._pc = 0
        self._accumulator = 0
        self._instructions = []
        self._pc_track = []
        # Convert program text into instructions.
        for line in self._program:
            self._instructions.append(Instruction(line.split()[0], int(line.split()[1])))

    def test(self):
        """Determine if next instruction to execute has already run."""
        return not self._pc in self._pc_track

    def terminated(self):
        return self._pc == len(self._instructions)

    def step(self):
        """Execute a single instruction."""

        if self.terminated():
            return

        # Track execution of instruction.
        self._pc_track.append(self._pc)

        # Fetch instruction.
        instruction = self._instructions[self._pc]
        if instruction.operation == 'nop':
            self._pc += 1
        elif instruction.operation == 'acc':
            self._accumulator += instruction.argument
            self._pc += 1
        elif instruction.operation == 'jmp':
            self._pc += instruction.argument

        return

    def run(self):
        while computer.test() and not computer.terminated():
            computer.step()

    def fix(self):

        if self._instructions[self._last_fixed].operation == 'nop':
            self._instructions[self._last_fixed].operation = 'jmp'
            self._last_fixed += 1
        elif self._instructions[self._last_fixed].operation == 'jmp':
            self._instructions[self._last_fixed].operation = 'nop'
            self._last_fixed += 1
        else:
            self._last_fixed += 1
            self.fix()

    @property
    def accumulator(self):
        """Description of function accumulator."""
        return self._accumulator

    def __str__(self):
        return '\n'.join(self._instructions)


code = sys.stdin.read().strip().split('\n')
computer = Machine(code)

computer.run()

if not computer.test():
    print(f'Part 1 Answer {computer.accumulator}')
else:
    print('Part 1 failed!')

computer.reset()
while not computer.terminated():
    computer.fix()
    computer.run()

    if computer.terminated():
        print(f'Part 2 Answer {computer.accumulator}')
    else:
        computer.reset()
