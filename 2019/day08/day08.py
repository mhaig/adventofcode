#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

class Layer(object):
    """Docstring for Layer."""

    def __init__(self, height, width, name='', chars=None):
        """
        @todo Document Layer.__init__ (along with arguments).

        height - @todo Document argument height.
        width - @todo Document argument width.
        """
        self._height = height
        self._width = width
        self._name = str(name)

        self._layer = [[0 for i in range(width)] for j in range(height)] 

        if chars:
            for i in range(height):
                for j in range(width):
                    self._layer[i][j] = chars[i*width+j]

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def count_digit(self, digit):
        count = 0
        for i in range(height):
            for j in range(width):
                if self._layer[i][j] == digit:
                    count += 1
        return count

    def __getitem__(self, key):
        return self._layer[key[0]][key[1]]

    def __str__(self):
        string = ''

        string += self._name
        string += '\n'
        for i in range(height):
            for j in range(width):
                string += self._layer[i][j]
            string +='\n'

        return string

    def __add__(self, bottom):

        if self.height != bottom.height or self.width != bottom.width:
            raise TypeError()

        new = Layer(self.height, self.width)

        for i in range(height):
            for j in range(width):
                if self._layer[i][j] == '2':
                    new._layer[i][j] = bottom._layer[i][j]
                else:
                    new._layer[i][j] = self._layer[i][j]

        return new


image_data = sys.stdin.read().strip()

width = 25
height = 6
# width = 3
# height = 2
layer_length = width*height

layers = []
current = 0
while current < len(image_data):
    layer = Layer(height,
                  width,
                  name=current // layer_length + 1,
                  chars=image_data[current:current+layer_length])
    current += layer_length
    layers.append(layer)

zero_count = layers[0].count_digit('0')
zero = layers[0]
for l in layers[1:]:
    if l.count_digit('0') < zero_count:
        zero_count = l.count_digit('0')
        zero = l

print(f"layer {zero_count}: {zero.count_digit('1') * zero.count_digit('2')}")

total = layers[0]
for l in layers:
    total = total + l

from PIL import Image

img = Image.new('1', (total.width, total.height))
pixels = img.load()
pixels[0,0] = 0
for i in range(total.height):
    for j in range(total.width):
        pixels[j,i] = int(total[i, j])

img.show()
