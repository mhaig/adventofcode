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


    def input_handler(self):
        if self._input_buffer:
            return self._input_buffer.pop(0)
        else:
            return -1

    def add_input(self, value):
        self._input_buffer.append(value)

    def output_handler(self, output):
        self._output_buffer.append(output)

        if len(self._output_buffer) == 3:

            if self._output_buffer[0] == 255:
                print(f'Part 1 Answer: {self._output_buffer[2]}')
                sys.exit()

            # Packet received, add to input of destination.
            self._network[self._output_buffer[0]].add_input(
                self._output_buffer[1])
            self._network[self._output_buffer[0]].add_input(
                self._output_buffer[2])

            self._output_buffer = []


parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

input_buffers = []

# Create 50 computers.
computers = []
for c in range(50):
    computers.append(intcode_computer.IntcodeComputer(program, True))
    input_buffers.append(Nic(c, input_buffers))
    computers[-1].set_input_handler(input_buffers[-1].input_handler)
    computers[-1].add_output_handler(input_buffers[-1].output_handler)

while True:
    for computer in computers:
        computer.execute_single()
