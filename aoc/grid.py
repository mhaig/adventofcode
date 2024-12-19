#!/usr/bin/env python3


class Grid(dict):
    """Docstring for Grid."""

    def __init__(self, text_grid, *args):
        dict.__init__(self, args)
        self._height = 0
        self._width = 0

        self.build(text_grid)

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        if key[0] >= self._width:
            self._width = key[0] + 1
        if key[1] >= self._height:
            self._height = key[1] + 1

    def __str__(self) -> str:
        string = ""
        for y in range(self.height):
            for x in range(self.width):
                string += str(self[x, y])
            string += "\n"

        return string

    def __hash__(self):
        return hash(self.__str__())

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> int:
        return self._width

    def get_row(self, y) -> list[int]:
        return [x for k, x in self.items() if k[1] == y]

    def get_column(self, x) -> list[int]:
        return [v for k, v in self.items() if k[0] == x]

    def build(self, string: str) -> None:
        for y, row in enumerate(string.split("\n")):
            if not row:
                continue

            for x, c in enumerate(row):
                if c:
                    self[x, y] = c

    def get_e(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "east" from `x`,`y`"""
        # First see if it's possible to get count
        if x + count > self.width:
            return []

        return [self[x + i, y] for i in range(count)]

    def get_w(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "west" from `x`,`y`"""
        # First see if it's possible to get count
        if x - (count - 1) < 0:
            return []

        return [self[x - i, y] for i in range(count)]

    def get_n(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "north" from `x`,`y`"""
        # First see if it's possible to get count
        if y - (count - 1) < 0:
            return []

        return [self[x, y - i] for i in range(count)]

    def get_s(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "south" from `x`,`y`"""
        # First see if it's possible to get count
        if y + count > self.height:
            return []

        return [self[x, y + i] for i in range(count)]

    def get_ne(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "north east" from `x`,`y`"""
        if x + count > self.width or y - (count - 1) < 0:
            return []

        return [self[x + i, y - i] for i in range(count)]

    def get_se(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "south east" from `x`,`y`"""
        if x + count > self.width or y + count > self.height:
            return []

        return [self[x + i, y + i] for i in range(count)]

    def get_nw(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "north west" from `x`,`y`"""
        if x - (count - 1) < 0 or y - (count - 1) < 0:
            return []

        return [self[x - i, y - i] for i in range(count)]

    def get_sw(self, x: int, y: int, count: int) -> list[int]:
        """Get `count` cells "south west" from `x`,`y`"""
        if x - (count - 1) < 0 or y + count > self.height:
            return []

        return [self[x - i, y + i] for i in range(count)]

    def get_adjacent(self, x: int, y: int) -> list[int]:
        adjacent = []
        if x:
            adjacent.append(self[x - 1, y])
        if y:
            adjacent.append(self[x, y - 1])
        if x + 1 < self.width:
            adjacent.append(self[x + 1, y])
        if y + 1 < self.height:
            adjacent.append(self[x, y + 1])

        return adjacent

    def get_adjacent_diagonal(self, x: int, y: int) -> list[int]:
        adjacent = self.get_adjacent(x, y)

        if x + 1 < self.width and y + 1 < self.height:
            adjacent.append(self[x + 1, y + 1])
        if x and y:
            adjacent.append(self[x - 1, y - 1])
        if x + 1 < self.width and y:
            adjacent.append(self[x + 1, y - 1])
        if x and y + 1 < self.height:
            adjacent.append(self[x - 1, y + 1])

        return adjacent

    def get_diagonal(self, x: int, y: int) -> list[int]:
        adjacent = []

        if x + 1 < self.width and y + 1 < self.height:
            adjacent.append(self[x + 1, y + 1])
        if x and y:
            adjacent.append(self[x - 1, y - 1])
        if x + 1 < self.width and y:
            adjacent.append(self[x + 1, y - 1])
        if x and y + 1 < self.height:
            adjacent.append(self[x - 1, y + 1])

        return adjacent

    def get_indices(self, c: str) -> list[tuple[int, int]]:
        """Given a character, return all indices that contain that character."""
        return [k for k, v in self.items() if v == c]
