#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse

import intcode_computer

class Cell(object):
    """Docstring for Cell."""

    def __init__(self, content):
        """
        @todo Document Cell.__init__ (along with arguments).
        """
        self._visited = False
        if content == 0:
            self._content = '#'
        elif content == 1:
            self._content = '.'
        elif content == 2:
            self._content = '2'
        else:
            raise NotImplemented()

    @property
    def visited(self):
        return self._visited
    @visited.setter
    def visited(self, value):
        self._visited = value

    @property
    def content(self):
        return self._content
    @content.setter
    def content(self, value):
        if value == 'O':
            self._content = value

    def __str__(self):
        return self._content

class Area(object):
    """Docstring for Area."""

    def __init__(self, computer):
        """
        @todo Document Area.__init__ (along with arguments).
        """
        self._current_x = 0
        self._current_y = 0

        self._oxygen_x = 0
        self._oxygen_y = 0

        self._move_count = 0

        self._computer = computer
        self._computer.add_output_handler(self._output_handler)
        self._output = None

        self._area = {}
        self._area[0, 0] = Cell(1)

    def _output_handler(self, output):
        self._output = output

    def _run_computer(self, x, y):
        # Make sure we're not already there...
        if x == self._current_x and y == self._current_y:
            return

        new_x = self._current_x
        new_y = self._current_y
        # Set input to match direction
        if y > self._current_y:
            self._computer.set_input(1)
            new_y += 1
        elif y < self._current_y:
            self._computer.set_input(2)
            new_y -= 1
        elif x < self._current_x:
            self._computer.set_input(3)
            new_x -= 1
        elif x > self._current_x:
            self._computer.set_input(4)
            new_x += 1
        else:
            raise NotImplemented()

        # Run computer until output is available.
        self._output = None
        while self._output == None:
            self._computer.execute_single()

        # Store output at new cell
        if (new_x, new_y) not in self._area:
            self._area[new_x, new_y] = Cell(self._output)

        # Only update position if an actual movement occurred.
        if self._output:
            self._current_x = new_x
            self._current_y = new_y

        return self._output

    def search(self, x, y, prev=None):


        # Run the computer to the new spot.
        if self._run_computer(x, y):
            self._move_count += 1

        if self._area[x, y].content == '2':
            print('Found it!')
            self._oxygen_x = x
            self._oxygen_y = y
            print(f'Part 1 Answer: {self._move_count}')
            return True
        elif self._area[x, y].content == '#':
            if prev:
                self._run_computer(prev[0], prev[1])
            return False
        elif self._area[x, y].visited:
            # Need to move back here I think...
            if prev:
                self._run_computer(prev[0], prev[1])
                self._move_count -= 1
            return False

        self._area[x, y].visited = True

        if (self.search(x+1, y, (x, y)) or
                self.search(x, y-1, (x, y)) or
                self.search(x-1, y, (x, y)) or
                self.search(x, y+1, (x, y))):
            return True

        if prev:
            self._run_computer(prev[0], prev[1])
            self._move_count -= 1

        return False

    def __str__(self):

        system = ''
        # Find the min x and max x
        min_x = min([x[0] for x in self._area.keys()])
        max_x = max([x[0] for x in self._area.keys()])

        min_y = min([y[1] for y in self._area.keys()])
        max_y = max([y[1] for y in self._area.keys()])

        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                if x == 0 and y == 0:
                    system += 'D'
                else:
                    system += str(self._area.get((x, y), '#'))
            system += '\n'

        return system

    def fill(self):
        # First switch the oxygen system to O
        self._area[self._oxygen_x, self._oxygen_y].content = 'O'

        total_blank = len([v for v in self._area.values() if v.content == '.'])
        total_blank += 1

        minutes = 0
        # Make a new dict of only oxygen cells
        while True:
            o = {k: v for (k, v) in self._area.items() if v.content == 'O'}
            if len(o) == total_blank:
                break

            for k,v in o.items():
                if self._area.get((k[0]+1, k[1]), Cell(0)).content == '.':
                    self._area[k[0]+1, k[1]].content = 'O'
                if self._area.get((k[0]-1, k[1]), Cell(0)).content == '.':
                    self._area[k[0]-1, k[1]].content = 'O'
                if self._area.get((k[0], k[1]+1), Cell(0)).content == '.':
                    self._area[k[0], k[1]+1].content = 'O'
                if self._area.get((k[0], k[1]-1), Cell(0)).content == '.':
                    self._area[k[0], k[1]-1].content = 'O'

            minutes += 1

        return minutes



parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    program = f.read()

comp = intcode_computer.IntcodeComputer(program, True)
area = Area(comp)

area.search(0,0)

# Switch to filling oxygen.
print(f'Part 2 Answer: {area.fill()}')
