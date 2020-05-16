#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse
import sys

from intcode import intcode_computer

class Nic(object):

    def __init__(self, identification, network):
        self._id = identification
        self._input_buffer = [identification]
        self._output_buffer = []
        self._network = network
        self._idle = False

    def input_handler(self):
        if self._input_buffer:
            self._idle = False
            return self._input_buffer.pop(0)
        else:
            self._idle = True
            return -1

    def add_input(self, value):
        self._input_buffer.append(value)
        self._idle = False

    def output_handler(self, output):
        self._output_buffer.append(output)

        if len(self._output_buffer) == 3:

            # Packet received, add to input of destination.
            self._network[self._output_buffer[0]].add_input(
                self._output_buffer[1])
            self._network[self._output_buffer[0]].add_input(
                self._output_buffer[2])

            self._output_buffer = []

    @property
    def idle(self):
        return self._idle

class Nat(object):

    def __init__(self, network):
        self._network = network
        self._input_buffer = []
        self._x = None
        self._y = None
        self._last_x = None
        self._last_y = None
        self._first = True

    @property
    def idle(self):
        return True

    def add_input(self, value):
        self._input_buffer.append(value)

        if len(self._input_buffer) == 2:
            self._x = self._input_buffer[0]
            self._y = self._input_buffer[1]
            self._input_buffer = []

            if self._first:
                print(f'Part 1 Answer: {self._y}')
                self._first = False

    def test_and_handle_idle(self):
        if all([v.idle for k,v in self._network.items()]):
            # First make sure someone is transmitting.
            if self._x == None or self._y == None:
                return

            # Then test for solution.
            if self._last_y == self._y:
                print(f'Part 2 Answer: {self._y}')
                sys.exit()

            self._network[0].add_input(self._x)
            self._network[0].add_input(self._y)
            self._last_x = self._x
            self._last_y = self._y

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

nics = {}

# Create 50 computers.
computers = []
for c in range(50):
    computers.append(intcode_computer.IntcodeComputer(program, True))
    nics[c] = (Nic(c, nics))
    computers[-1].set_input_handler(nics[c].input_handler)
    computers[-1].add_output_handler(nics[c].output_handler)

nics[255] = Nat(nics)

while True:
    for computer in computers:
        computer.execute_single()

    nics[255].test_and_handle_idle()
