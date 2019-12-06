#!/usr/bin/env python
# vim:set fileencoding=utf8: #

class IntcodeComputer(object):
    """Docstring for IntcodeComputer."""

    def __init__(self, program: str):
        """
        @todo Document IntcodeComputer.__init__ (along with arguments).

        program - @todo Document argument program.
        """
        self._program = program

        self.reset()

    def _fetch_a(self):
        return self._memory[self._memory[self._pc + 1]]

    def _fetch_b(self):
        return self._memory[self._memory[self._pc + 2]]

    def _store_c(self, value):
        self._memory[self._memory[self._pc + 3]] = value

    def reset(self):
        self._memory = [int(x) for x in self._program.split(',')]
        self._pc = 0

    def set_value(self, position, value):
        self._memory[position] = value

    def get_value(self, position):
        return self._memory[position]

    def execute(self):

        while self._memory[self._pc] != 99:

            a = self._fetch_a()
            b = self._fetch_b()

            if self._memory[self._pc] == 1: # opcode 1: add
                self._store_c((a + b))
                inst_size = 4
            elif self._memory[self._pc] == 2: # opcode 2: multiply
                self._store_c((a * b))
                inst_size = 4

            self._pc += inst_size
