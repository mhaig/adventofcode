import inspect
import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

class Tower(object):
    """Docstring for tower."""

    def __init__(self, name, weight, sub_towers=[]):
        """
        @todo Document tower.__init__ (along with arguments).

        name - @todo Document argument name.
        weight - @todo Document argument weight.
        sub_towers - @todo Document argument sub_towers.
        """
        self._name = name
        self._weight = int(weight)
        self._sub_towers = sub_towers

    def __repr__(self):
        return ('%s %d %s' % (self._name, self._weight, self._sub_towers))

    @property
    def sub_towers(self):
        return self._sub_towers

    @sub_towers.setter
    def sub_towers(self, val):
        self._sub_towers = map(lambda x: x.strip(','), val)

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

towers = []
for line in data.split('\n'):
    elements = line.split()

    towers.append(Tower(elements[0], elements[1][1:-1]))
    if (len(elements) > 2):
        print('Sub towers')
        print(elements[3:])
        towers[-1].sub_towers = list(elements[3:])

print(towers)
# Find the tower with sub-towers but that is not a sub-tower itself.
# towers.sort(key=lambda x: x._weight)
with_sub_towers = filter(lambda x: len(x.sub_towers) > 0, towers)
print(len(towers))
print(len(with_sub_towers))
all_sub_towers = []
for t in with_sub_towers:
    for i in t.sub_towers:
        all_sub_towers.append(i)

# print(all_sub_towers)
# for t in with_sub_towers:
#     if t._name not in all_sub_towers:
#         print(t._name)
#         exit()
# print(all_sub_towers)
bottom_program = filter(lambda x: x.name not in all_sub_towers, with_sub_towers)
print(len(bottom_program))
print(bottom_program)

bottom_program = bottom_program[0]

def get_program(name):
    return filter(lambda x: x.name == name, towers)[0]

def sum_tree(list_of_program_names, depth=0):

    sum = 0
    for p in list_of_program_names:
        if len(get_program(p).sub_towers) > 0:
            sum += sum_tree(get_program(p).sub_towers, depth + 1)
        sum += get_program(p).weight


        # print(len(inspect.stack()))
        # debug_str = len(inspect.stack()) * ' '
        # debug_str += '%s(%d)'
        # print('%s(%d)' % (get_program(p).name, get_program(p).weight))
        # print(debug_str % (get_program(p).name, get_program(p).weight))

    return sum

# Starting at the bottom, calculate the sum of each sub-tower.
tower_weight = []
odd_tower = None
for program in bottom_program.sub_towers:

    sum = get_program(program).weight + sum_tree(get_program(program).sub_towers)
    print('%s %d %d' % (get_program(program).name, get_program(program).weight, sum))

    tower_weight.append([get_program(program), sum])


# The following is brute force of finding the unbalanced tower.  If this is
# going to be reused, refactor this section to use recursion, etc.

# Find the odd tree.
tower_weight.sort(key=lambda x: x[1])
if tower_weight[0][1] != tower_weight[1][1]:
    odd_tower = tower_weight[0][0]
else:
    odd_tower = tower_weight[-1][0]

print(odd_tower.name)


tower_weight = []
for program in odd_tower.sub_towers:

    sum = get_program(program).weight + sum_tree(get_program(program).sub_towers)
    print('%s %d %d' % (get_program(program).name, get_program(program).weight, sum))

    tower_weight.append([get_program(program), sum])

# Find the odd tree.
tower_weight.sort(key=lambda x: x[1])
if tower_weight[0][1] != tower_weight[1][1]:
    odd_tower = tower_weight[0][0]
else:
    odd_tower = tower_weight[-1][0]

print('Odd Tower: %s' % odd_tower.name)




tower_weight = []
for program in odd_tower.sub_towers:

    sum = get_program(program).weight + sum_tree(get_program(program).sub_towers)
    print('%s %d %d' % (get_program(program).name, get_program(program).weight, sum))

    tower_weight.append([get_program(program), sum])

# Find the odd tree.
tower_weight.sort(key=lambda x: x[1])
if tower_weight[0][1] != tower_weight[1][1]:
    odd_tower = tower_weight[0][0]
else:
    odd_tower = tower_weight[-1][0]

print('Odd Tower: %s' % odd_tower.name)



tower_weight = []
for program in odd_tower.sub_towers:

    sum = get_program(program).weight + sum_tree(get_program(program).sub_towers)
    print('%s %d %d' % (get_program(program).name, get_program(program).weight, sum))

    tower_weight.append([get_program(program), sum])

# Find the odd tree.
tower_weight.sort(key=lambda x: x[1])
if tower_weight[0][1] != tower_weight[1][1]:
    odd_tower = tower_weight[0][0]
else:
    odd_tower = tower_weight[-1][0]

print('Odd Tower: %s' % odd_tower.name)
