#!/usr/bin/env python3

import sys

game_input = list(sys.stdin.readlines())

game_points: dict[int, tuple[int, int]] = {}
for card in game_input:
    card_number = int(card.split(":")[0].split()[1])
    winning_numbers = [
        int(x) for x in card.split("|")[0].split(":")[1].split()
    ]

    points = 0
    winners = 0
    for number in card.split("|")[1].split():
        if int(number) in winning_numbers:
            winners += 1
            if points == 0:
                points += 1
            else:
                points *= 2

    game_points[card_number] = (winners, points)

print(
    "Part 1 Solution: {}".format(sum([v[1] for k, v in game_points.items()]))
)

instances = {}


def get_copy_count(card: int) -> None:
    if not game_points[card][0]:
        return

    winning_cards = list(range(card + 1, card + game_points[card][0] + 1))

    for i in winning_cards:
        if i not in instances:
            instances[i] = 1
        else:
            instances[i] += 1
        get_copy_count(i)


for i in range(1, len(game_points) + 1):
    if i not in instances:
        instances[i] = 1
    else:
        instances[i] += 1

    get_copy_count(i)

print("Part 2 Solution: {}".format(sum([v for k, v in instances.items()])))
