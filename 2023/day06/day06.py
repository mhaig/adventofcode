#!/usr/bin/env python3

# Input:
#  Time:      7  15   30
#  Distance:  9  40  200

import sys
from functools import reduce


class Race:
    def __init__(self, time: (int | str), distance: (int | str)):
        self._time = int(time)
        self._distance = int(distance)

    @property
    def time(self) -> int:
        return self._time

    @property
    def distance(self) -> int:
        return self._distance

    def __repr__(self):
        return f"Race(time={self._time}, distance={self._distance})"

    def winners(self) -> int:
        # x axis is time
        # y axis is velocity (mm/ms)
        max_speed = 0
        min_speed = 0
        for i in range(self._time, 0, -1):
            # See if speed can make it
            speed = i
            if (self._time - i) * i > self._distance:
                max_speed = i
                break
        for i in range(self._time):
            if (self._time - i) * i > self._distance:
                min_speed = i
                break

        return (max_speed - min_speed) + 1


game_input = list(sys.stdin.readlines())

races = []
times = game_input[0].split()[1:]
distances = game_input[1].split()[1:]

for i in zip(times, distances):
    races.append(Race(i[0], i[1]))


margin_of_error = reduce(lambda x, y: x * y, [r.winners() for r in races])
print("Part 1 Solution: {}".format(margin_of_error))

mega_time = ""
mega_distance = ""
for r in races:
    mega_time += str(r.time)
    mega_distance += str(r.distance)

mega_race = Race(mega_time, mega_distance)
print(mega_race)
print(mega_race.winners())
