from node import Node

class CircularList(object):
    """Docstring for CircularList."""

    def __init__(self):
        """
        @todo Document CircularList.__init__ (along with arguments).

        f - @todo Document argument f.
        """
        self._head = None
        self._tail = None
        self._current = None
        self._hash_table = {}

    def add(self, data):

        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
            new_node.next = self._head
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._tail.next = self._head

        self._hash_table[data] = new_node

    def rotate(self):
        """Move 'head' to the next item in list."""
        self._head = self._head.next
        self._tail = self._tail.next

    def insert_at(self, target_data, data):
        # First find the target node.
        current = self._hash_table[target_data]

        for x in data:
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node
            current = current.next
            self._hash_table[x] = new_node

    def get(self, target_data):
        """Get a node that has a particular data."""
        return self._hash_table[target_data]

    def remove_next(self):
        """Remove the next item in the buffer."""
        if self._head.next != self._head:
            removed_node = self._head.next
            self._head.next = removed_node.next
            self._hash_table[removed_node.data] = None
            return removed_node.data

    def __str__(self):

        string = '(empty)'
        if self._head:
            current = self._head
            string = str(self._head.data)
            while not current.next == self._head:
                string += ' '
                current = current.next
                string += str(current.data)
        return string

    def __iter__(self):

        if self._head:
            current = self._head
            yield current.data
            while not current.next == self._head:
                current = current.next
                yield current.data
