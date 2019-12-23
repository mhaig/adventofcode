#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import argparse
from intcode import cell
from intcode import grid

class Cell(cell.Cell):
    """Docstring for Cell."""

    def __init__(self, content):
        """
        @todo Document Cell.__init__ (along with arguments).
        """
        super(Cell, self).__init__()

        self._portal = None
        self._inside_portal = False
        self._content = content

    @property
    def portal(self):
        return self._portal

    @portal.setter
    def portal(self, value):
        self._portal = value

    @property
    def inside_portal(self):
        return self._inside_portal

    @inside_portal.setter
    def inside_portal(self, value):
        self._inside_portal = value

def print_grid(a_grid):

    print_str = ''
    for y in range(a_grid.height):
        for x in range(a_grid.width):
            print_str += str(a_grid[x, y])

        print_str += '\n'

    print(print_str)

def get_neighbors(a_grid, x, y):
    """Given a grid and an x,y position, return all nodes that connect."""

    neighbors = {}
    if a_grid[x+1,y].content == '.':
        neighbors[x+1,y] = a_grid[x+1, y]
    if a_grid[x-1,y].content == '.':
        neighbors[x-1,y] = a_grid[x-1, y]
    if a_grid[x, y+1].content == '.':
        neighbors[x, y+1] = a_grid[x, y+1]
    if a_grid[x, y-1].content == '.':
        neighbors[x, y-1] = a_grid[x, y-1]
    if grid[x,y].portal:
        for k, v in grid.items():
            if v.portal == grid[x,y].portal and v != grid[x,y]:
                neighbors[k[0], k[1]] = v


    return neighbors

def is_portal_wall(x, y, z, cell):
    if not cell.portal:
        # If no portal can't be a wall.
        return False

    if cell.portal in ['AA', 'ZZ']:
        # AA and ZZ are walls if Z is not 0.
        if z == 0:
            return False
        else:
            return True

    if z == 0:
        if cell.inside_portal:
            return False
        else:
            # Only inside portals work at the first level.
            return True

    return False



def get_neighbors_z(a_grid, x, y, z):
    """Given a grid and an x,y,z position, return all nodes that connect."""

    neighbors = {}

    if a_grid[x+1,y].content == '.' and not is_portal_wall(x+1,y,z,a_grid[x+1,y]):
        neighbors[x+1,y,z] = a_grid[x+1, y]
    if a_grid[x-1,y].content == '.' and not is_portal_wall(x-1,y,z,a_grid[x-1,y]):
        neighbors[x-1,y,z] = a_grid[x-1, y]
    if a_grid[x,y+1].content == '.' and not is_portal_wall(x,y+1,z,a_grid[x,y+1]):
        neighbors[x, y+1,z] = a_grid[x, y+1]
    if a_grid[x,y-1].content == '.' and not is_portal_wall(x,y-1,z,a_grid[x,y-1]):
        neighbors[x, y-1,z] = a_grid[x, y-1]
    if a_grid[x,y].portal and not is_portal_wall(x,y,z,a_grid[x,y]):
        for k, v in a_grid.items():
            if v.portal == a_grid[x,y].portal and v != a_grid[x,y]:
                # Cell has a portal and is not itself.  Add it to the list
                # adjusting z appropriately.
                if a_grid[x,y].inside_portal:
                    neighbors[k[0], k[1], z+1] = v
                else:
                    if z-1 < 0:
                        print(x,y,z,a_grid[x,y])
                        raise NotImplemented()
                    neighbors[k[0], k[1], z-1] = v

    return neighbors



# Read in the entire map.
parser = argparse.ArgumentParser()
parser.add_argument('file_name')
args = parser.parse_args()

with open(args.file_name, 'r') as f:
    raw_map = f.read()

grid = grid.Grid()

for y, row in enumerate(raw_map.split('\n')):
    if not row:
        continue

    for x, c in enumerate(row):
        if c:
            grid[x,y] = Cell(c)

# Check each item in grid to see if it should have a portal.
for k,v in grid.items():
    x,y = k
    if v.content == '.':
        # Check and see if a letter is around the open space.
        if grid[x,y-1].content not in ['#', '.']:
            grid[x,y].portal = grid[x,y-2].content + grid[x,y-1].content
            if y != 2:
                grid[x,y].inside_portal = True
        elif grid[x,y+1].content not in ['#', '.']:
            grid[x,y].portal = grid[x,y+1].content + grid[x,y+2].content
            if y != (grid.height - 3):
                grid[x,y].inside_portal = True
        elif grid[x-1,y].content not in ['#', '.']:
            grid[x,y].portal = grid[x-2,y].content + grid[x-1,y].content
            if x != 2:
                grid[x,y].inside_portal = True
        elif grid[x+1,y].content not in ['#', '.']:
            grid[x,y].portal = grid[x+1,y].content + grid[x+2,y].content
            if x != (grid.width - 3):
                grid[x,y].inside_portal = True

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbors = get_neighbors(graph, node[0], node[1])

            # add neighbours of node to queue
            for neighbor in neighbors:
                queue.append(neighbor)
    return explored

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbors = get_neighbors(graph, node[0], node[1])
            # go through all neighbor nodes, construct a new path and
            # push it into the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # return path if neighbor is goal
                if neighbor == goal:
                    return new_path

            # mark node as explored
            explored.append(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path_z(graph, start, goal):
    # keep track of explored nodes
    explored = set()
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbors = get_neighbors_z(graph, node[0], node[1], node[2])
            # go through all neighbor nodes, construct a new path and
            # push it into the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # return path if neighbor is goal
                if neighbor == goal:
                    return new_path

            # mark node s explored
            explored.add(node)

    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("

# Get the start position.
for k,v in grid.items():
    if v.portal == 'AA':
        start_x = k[0]
        start_y = k[1]
        start_z = 0

# Get the end position.
for k,v in grid.items():
    if v.portal == 'ZZ':
        end_x = k[0]
        end_y = k[1]
        end_z = 0

print(f'Start: {start_x}, {start_y}')
print(f'End:   {end_x}, {end_y}')

answer = len(bfs_shortest_path(grid, (start_x, start_y), (end_x, end_y))) - 1
print(f'Part 1 Solution: {answer}')

short = bfs_shortest_path_z(grid, (start_x, start_y, start_z),
                                  (end_x, end_y, end_z))
answer = len(short) - 1
print(f'Part 2 Solution: {answer}')
