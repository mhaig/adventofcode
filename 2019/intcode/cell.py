#!/usr/bin/env python
# vim:set fileencoding=utf8: #

class Cell(object):
    """Docstring for Cell."""

    def __init__(self):
        """
        @todo Document Cell.__init__ (along with arguments).
        """
        self._visited = False
        self._content = ''

    @property
    def visited(self):
        return self._visited
    @visited.setter
    def visited(self, value):
        self._visited = value

    @property
    def content(self):
        return self._content

    def __str__(self):
        return self._content
