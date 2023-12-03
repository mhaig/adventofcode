#!/usr/bin/env python3

import sys

game_input = list(sys.stdin.readlines())
good_games: list[int] = []
game_powers: list[int] = []

contents = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for game in game_input:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_number = int(game.split(":")[0].split()[1])
    draws = game.split(":")[1].strip().split(";")
    draws = [x.strip() for x in draws]
    valid_game = True
    min_cubes: dict[str, int] = {}
    for draw in draws:
        cubes = [x.strip() for x in draw.split(",")]
        for cube in cubes:
            color = cube.split()[1].strip()
            count = int(cube.split()[0])
            if count > contents[color]:
                valid_game = False

            if color in min_cubes:
                if count > min_cubes[color]:
                    min_cubes[color] = count
            else:
                min_cubes[color] = count

    if valid_game:
        good_games.append(game_number)

    game_power = 1
    for k, v in min_cubes.items():
        game_power *= v
    game_powers.append(game_power)

print("Part 1 Solution: {}".format(sum(good_games)))

print("Part 2 Solution: {}".format(sum(game_powers)))
