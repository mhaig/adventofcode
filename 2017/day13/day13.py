"""
Day 13:

Sample input:
    0: 3
    1: 2
    4: 4
    6: 4

Sample output:
    0*3 + 6*4 = 24
"""
from __future__ import print_function
import sys

class FirewallLevel(object):

    def __init__(self, depth, range):
        self._depth = depth
        self._range = range
        self._list = [0] * range
        self._position = 0
        self._increment = True

        self._length = range
        self._packet = False
        self._detected = False

    def __repr__(self):
        pretty_list = map(lambda x: '[S]' if x =='S' else '[ ]', self._list)
        if self._packet:
            pretty_list[0] = pretty_list[0].replace('[', '(').replace(']', ')')
        return ' '.join(pretty_list)

    @property
    def depth(self):
        return self._depth

    @property
    def range(self):
        return self._range

    @property
    def packet(self):
        return self._packet

    @packet.setter
    def packet(self, value):
        self._packet = value

    @property
    def detected(self):
        return self._detected

    def initialize(self):
        self._position = 0
        self._list = [0] * self._range
        self._increment = True
        self._list[0] = 'S'
        self._detected = False

    def calculate_position(self, picosecond):
        """
        [0] [0]  [0] [0]  [0] [0]
        [1] [1]  [1] [1]  [1] [1]
                 [2] [2]  [2] [2]
                     [3]  [3] [3]
                              [4]
                              [5]
        """
        position = picosecond % ((self._length - 1) * 2)
        if position > (self._length - 1):
            offset = position - (self._length - 1)
            position = (self._length - 1) - offset

    def click(self, picosecond):
        position = self._position

        # Before moving, see if a packet was detected.
        if self._packet and position == 0:
            self._detected = True

        # if picosecond == 0:
        #     return

        if self._increment:
            if position + 1 >= self._length:
                self._increment = False
            else:
                new_position = position + 1

        if not self._increment:
            if position - 1 < 0:
                self._increment = True
                new_position = position + 1
            else:
                new_position = position - 1

        self._list[position] = 0
        self._list[new_position] = 'S'
        self._position = new_position

def clear_packet(firewall):
    for level in firewall:
        if level:
            level.packet = False

def move_firewall(firewall, picosecond):
    for level in firewall:
        if level:
            level.click(picosecond)

def init_firewall(firewall):
    for level in firewall:
        if level:
            level.initialize()

def main():
    """Main program execution."""

    # Process input.
    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    firewall_level_count = int(data.split('\n')[-1].split(': ')[0]) + 1
    firewall = [None] * firewall_level_count
    for line in data.split('\n'):
        depth = int(line.split(': ')[0])
        firewall[depth] = FirewallLevel(depth, int(line.split(': ')[1]))

    print(firewall)

    # Need to make this smarter.  There needs to be a way to calculate this or
    # at least weed out some delays based on when the first depth would hit,
    # etc.
    detected_flag = True
    delay = 0
    while detected_flag:
        if delay % 100 == 0:
            print('Delay %d' % delay)
        init_firewall(firewall)
        # print(firewall)

        for i in range(firewall_level_count + delay):
            # Set packet position.
            clear_packet(firewall)
            if i >= delay and firewall[i - delay]:
                firewall[i - delay].packet = True

            # print('Picosecond %d' % i)
            move_firewall(firewall, i)
            # print(firewall)
            # detected_flag = reduce(lambda x, y: x or y, [x.detected for x in firewall if x])
            detected_flag = True in [x.detected for x in firewall if x]
            if detected_flag:
                break

        # Detected anything?
        # print([x.detected for x in firewall if x])
        # detected_flag = reduce(lambda x, y: x or y, [x.detected for x in firewall if x])
        detected_flag = True in [x.detected for x in firewall if x]
        # print(detected_flag)
        if detected_flag:
            delay += 1


    detected_math = ['%d * %d' % (x.depth, x.range) if x and x.detected else 0 for x in firewall]
    print(detected_math)
    detected = reduce(lambda x, y: x + y, [x.depth * x.range if x and x.detected else 0 for x in firewall])
    # detected = reduce(lambda x: (x.depth * x.range) if x and x.detected else 0, firewall)
    print(detected)
    print(delay)


if __name__ == '__main__':
    main()
