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

    def _store_a(self, value):
        self._memory[self._memory[self._pc + 1]] = value

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

            full_opcode = str(self._memory[self._pc])
            while len(full_opcode) != 5:
                full_opcode = '0' + full_opcode

            opcode = int(full_opcode[3:])
            first_mode = int(full_opcode[2])
            second_mode = int(full_opcode[1])
            third_mode = int(full_opcode[0])

            if first_mode == 1:
                a = self._memory[self._pc + 1]
            else:
                a = self._fetch_a()
            if second_mode == 1:
                b = self._memory[self._pc + 2]
            else:
                b = self._fetch_b()

            if opcode == 1: # opcode 1: add
                self._store_c((a + b))
                inst_size = 4
            elif opcode == 2: # opcode 2: multiply
                self._store_c((a * b))
                inst_size = 4
            elif opcode == 3: # opcode 3: input
                self._store_a(int(input('input: ')))
                inst_size = 2
            elif opcode == 4: # opcode 4: output
                print(f'output: {a}')
                inst_size = 2
            elif opcode == 5: # opcode 5: jump-if-true
                if a != 0:
                    self._pc = b
                    continue
                inst_size = 3
            elif opcode == 6: # opcode 6: jump-if-false
                if a == 0:
                    self._pc = b
                    continue
                inst_size = 3
            elif opcode == 7: # opcode 7: less than
                if a < b:
                    self._store_c(1)
                else:
                    self._store_c(0)
                inst_size = 4
            elif opcode == 8: # opcode 8: equals
                if a == b:
                    self._store_c(1)
                else:
                    self._store_c(0)
                inst_size = 4

            self._pc += inst_size

    def __str__(self):
        return ','.join([str(x) for x in self._memory])
