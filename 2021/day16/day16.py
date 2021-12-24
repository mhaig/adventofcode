#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys
from packet import Packet

def add_version_numbers(packet):

    return packet.version + sum([add_version_numbers(x) for x in packet.sub_packets])

line = sys.stdin.read().strip()
print(line)
p = Packet(line)

print('Part 1 Solution: {}'.format(add_version_numbers(p)))
