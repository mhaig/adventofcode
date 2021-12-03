from command import Direction

class Submarine(object):

    def __init__(self, aim=False):
        self._horizontal = 0
        self._depth = 0
        self._track_aim = False
        if aim:
            self._track_aim = True
            self._aim = 0

    def execute_command(self, command):

        if self._track_aim:
            if command.direction() == Direction.DOWN:
                self._aim += command.units()
            elif command.direction() == Direction.UP:
                 self._aim -= command.units()
            else:
                self._horizontal += command.horizontal()
                self._depth += self._aim * command.units()
        else:
            self._horizontal += command.horizontal()
            self._depth += command.depth()

    def horizontal(self):
        return self._horizontal

    def depth(self):
        return self._depth
