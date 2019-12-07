#!/usr/bin/env python
# vim:set fileencoding=utf8: #

class IntcodeComputer(object):
    """Docstring for IntcodeComputer."""

    def __init__(self, program: str, headless=False):
        """
        @todo Document IntcodeComputer.__init__ (along with arguments).

        program - initial program code as a string.
        """
        self._program = program
        self._headless = headless

        self._input = []
        self._output = 0

        self.reset()

    @property
    def output(self):
        return self._output

    @property
    def running(self):
        return self._memory[self._pc] != 99

    @property
    def need_input(self):
        return self._memory[self._pc] == 3 and not self._input

    def _fetch_a(self):
        return self._memory[self._memory[self._pc + 1]]

    def _store_a(self, value):
        self._memory[self._memory[self._pc + 1]] = value

    def _fetch_b(self):
        return self._memory[self._memory[self._pc + 2]]

    def _store_c(self, value):
        self._memory[self._memory[self._pc + 3]] = value

    def reset(self):
        self._input = []
        self._output = 0
        self._memory = [int(x) for x in self._program.split(',')]
        self._pc = 0

    def set_input(self, value):
        if isinstance(value, list):
            self._input = value
        else:
            self._input.append(value)

    def set_value(self, position, value):
        self._memory[position] = value

    def get_value(self, position):
        return self._memory[position]

    def execute_single(self):
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

        if opcode in [1, 2, 5, 6, 7, 8]:
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
            if self._headless:
                self._store_a(self._input.pop(0))
            else:
                self._store_a(int(input('input: ')))
            inst_size = 2
        elif opcode == 4: # opcode 4: output
            if self._headless:
                self._output = a
            else:
                print(f'output: {a}')
            inst_size = 2
        elif opcode == 5: # opcode 5: jump-if-true
            if a != 0:
                self._pc = b
                return
            inst_size = 3
        elif opcode == 6: # opcode 6: jump-if-false
            if a == 0:
                self._pc = b
                return
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

    def execute(self):
        while self._memory[self._pc] != 99:
            self.execute_single()

    def __str__(self):
        return ','.join([str(x) for x in self._memory])
