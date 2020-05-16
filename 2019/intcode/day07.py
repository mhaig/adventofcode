#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse
import sys
import intcode_computer

parser = argparse.ArgumentParser()
parser.add_argument('--part1', action='store_true')
parser.add_argument('--part2', action='store_true')
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

amps = []
for i in range(5):
    amps.append(intcode_computer.IntcodeComputer(program, True))

if args.part1:
    max_to_thrusters = []
    for a in range(5):
        amps[0].reset()
        amps[0].set_input([a, 0])
        amps[0].execute()
        for b in range(5):
            if b == a:
                continue
            amps[1].reset()
            amps[1].set_input([b, amps[0].output])
            amps[1].execute()
            for c in range(5):
                if c in [a, b]:
                    continue
                amps[2].reset()
                amps[2].set_input([c, amps[1].output])
                amps[2].execute()
                for d in range(5):
                    if d in [a, b, c]:
                        continue
                    amps[3].reset()
                    amps[3].set_input([d, amps[2].output])
                    amps[3].execute()
                    for e in range(5):
                        if e in [a, b, c, d]:
                            continue
                        amps[4].reset()
                        amps[4].set_input([e, amps[3].output])
                        amps[4].execute()

                        if not max_to_thrusters:
                            max_to_thrusters = [str(a)+str(b)+str(c)+str(d)+str(e),
                                                amps[4].output]
                        else:
                            if amps[4].output > max_to_thrusters[1]:
                                max_to_thrusters = (
                                    [str(a)+str(b)+str(c)+str(d)+str(e),
                                     amps[4].output])


    print(max_to_thrusters)

for a in amps:
    a.reset()

def run_computers(amp_a, amp_b, amp_c, amp_d, amp_e):

    while amp_e.running:
        amp_a.set_input(amp_e.output)
        # Run a until it needs input or ends
        while amp_a.running and not amp_a.need_input:
            amp_a.execute_single()

        amp_b.set_input(amp_a.output)
        while amp_b.running and not amp_b.need_input:
            amp_b.execute_single()

        amp_c.set_input(amp_b.output)
        while amp_c.running and not amp_c.need_input:
            amp_c.execute_single()

        amp_d.set_input(amp_c.output)
        while amp_d.running and not amp_d.need_input:
            amp_d.execute_single()

        amp_e.set_input(amp_d.output)
        while amp_e.running and not amp_e.need_input:
            amp_e.execute_single()

    return amp_e.output

if args.part2:
    max_to_thrusters = []
    for a in range(5, 10):
        for b in range(5, 10):
            if b == a:
                continue
            for c in range(5, 10):
                if c in [a, b]:
                    continue
                for d in range(5, 10):
                    if d in [a, b, c]:
                        continue
                    for e in range(5, 10):
                        if e in [a, b, c, d]:
                            continue

                        # Run the state machine.
                        for amp in amps:
                            amp.reset()
                        amps[0].set_input(a)
                        amps[1].set_input(b)
                        amps[2].set_input(c)
                        amps[3].set_input(d)
                        amps[4].set_input(e)
                        run_computers(amps[0], amps[1], amps[2], amps[3], amps[4])

                        if not max_to_thrusters:
                            max_to_thrusters = [str(a)+str(b)+str(c)+str(d)+str(e),
                                                amps[4].output]
                        else:
                            if amps[4].output > max_to_thrusters[1]:
                                max_to_thrusters = (
                                    [str(a)+str(b)+str(c)+str(d)+str(e),
                                     amps[4].output])


    print(max_to_thrusters)
