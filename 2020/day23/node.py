class Node(object):
    """Docstring for Node."""

    def __init__(self, data):
        """
        @todo Document Node.__init__ (along with arguments).

        val - @todo Document argument val.
        """
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node
