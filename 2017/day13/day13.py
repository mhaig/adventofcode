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
        self._max_index = (self._length - 1)
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
        position = picosecond % (self._max_index * 2)
        if position > self._max_index:
            offset = position - self._max_index
            position = self._max_index - offset

        return position

    def click(self, picosecond):
        position = self._position
        new_position = self.calculate_position(picosecond)

        # Before moving, see if a packet was detected.
        if self._packet and new_position == 0:
            self._detected = True

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
    init_firewall(firewall)
    print(firewall)

    for i in range(firewall_level_count):
        # Set packet position.
        clear_packet(firewall)
        if firewall[i]:
            firewall[i].packet = True

        print('Picosecond %d' % i)
        move_firewall(firewall, i)
        print(firewall)

    detected_math = ['%d * %d' % (x.depth, x.range) if x and x.detected else 0 for x in firewall]
    print(detected_math)
    detected = reduce(lambda x, y: x + y, [x.depth * x.range if x and x.detected else 0 for x in firewall])
    # detected = reduce(lambda x: (x.depth * x.range) if x and x.detected else 0, firewall)
    print(detected)

    # Find the delay that will allow the packet to progress.  Instead of
    # running the whole "click" stuff, use the new method on each layer to see
    # if the detector will be in position 0 at a particular picosecond.
    delay = 0
    picosecond = 0
    while True:
        if delay % 1000 == 0:
            print(delay)
        detected = False
        # print('Testing delay %d' % delay)
        for i in range(len(firewall)):
            # print('Picosecond %d' % (i + delay))
            if firewall[i]:
                position = firewall[i].calculate_position(i + delay)
                if position == 0:
                    # Detected, break!
                    # print('Detected, break!')
                    detected = True
                    break
        
        if detected:
            delay += 1
        else:
            print('Final delay %d' % delay)
            break
            
        # for level in firewall:
        #     if level:
        #         picosecond = picosecond + delay
        #         print('Picosecond %d' % picosecond)
        #         position = level.calculate_position(picosecond)
        #         print(position)
        #         if position == 0:
        #             # Detected, break
        #             print('Detected, break!')
        #             detected = True
        #             break
        #     picosecond += 1
        # if not detected:
        #     # Made i through undetected!
        #     print('Proper delay %d' % delay)
        #     break
        # delay += 1



if __name__ == '__main__':
    main()
