from aoc.grid import Grid

class Tile(Grid):
    """Docstring for Tile."""

    def __init__(self, id_num):
        """
        @todo Document Tile.__init__ (along with arguments).

        arg - @todo Document argument arg.
        """
        self._id_num = id_num
        self._shared_edges = []

        Grid.__init__(self)

    @staticmethod
    def from_string(tile_id, string):
        t = Tile(tile_id)
        t.build(string)
        return t

    def add_shared_edge(self, tile):
        if tile not in self._shared_edges:
            self._shared_edges.append(tile)

    def get_edge(self, edge):
        if edge == 'top':
            return ''.join(self.get_row(0))
        elif edge == 'bottom':
            return ''.join(self.get_row(self.height-1))
        elif edge == 'left':
            return ''.join(self.get_column(0))
        elif edge == 'right':
            return ''.join(self.get_column(self.width-1))

    def get_edges(self):
        edges = []
        for e in ['top', 'bottom', 'left', 'right']:
            edge = self.get_edge(e)
            edges.append(edge)
            edges.append(edge[::-1])

        return edges

    def __str__(self):
        string = f'Tile {self._id_num}:\n'
        string += Grid.__str__(self)

        return string
