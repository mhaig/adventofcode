#!/usr/bin/env python
# vim:set fileencoding=utf8: #

import sys

debug = False

def debug_print(string=''):
    if debug:
        print(string)

def get_player_cards(string):

    cards = []
    for line in string.split('\n'):
        if line and 'Player' not in line and ':' not in line:
            cards.append(int(line))

    return cards

def print_deck(player_num, deck):
    if not deck: return
    debug_print("Player {}'s Deck: {}".format(player_num,
                                        ' '.join([str(x) for x in deck])))

def play_game(game_number, player_1_deck, player_2_deck, recursive=False):

    debug_print(f'=== Game {game_number} ===')
    debug_print()
    round_number = 1

    player_1_deck_history = set()
    player_2_deck_history = set()

    while player_1_deck and player_2_deck:
        debug_print(f'-- Round {round_number} (Game {game_number}) --')
        print_deck(1, player_1_deck)
        print_deck(2, player_2_deck)

        if recursive:
            # Check to see if this round has been played before...
            if (str(player_1_deck) in player_1_deck_history and
                str(player_2_deck) in player_2_deck_history):
                return player_1_deck, None
            else:
                player_1_deck_history.add(str(player_1_deck))
                player_2_deck_history.add(str(player_2_deck))

        player_1_card = player_1_deck.pop(0)
        player_2_card = player_2_deck.pop(0)

        debug_print(f'Player 1 plays: {player_1_card}')
        debug_print(f'Player 2 plays: {player_2_card}')

        if (recursive and (player_1_card <= len(player_1_deck) and
                           player_2_card <= len(player_2_deck))):
            # Play another game to determine winner of round
            debug_print('Playing a sub-game to determine the winner...')
            debug_print()
            a, b = play_game(game_number+1, player_1_deck[:player_1_card:], player_2_deck[:player_2_card:], recursive)
            debug_print(f'...anyway, back to game {game_number}')
            if a:
                debug_print('Player 1 wins round {round_number} of game {game_number}!')
                player_1_deck.append(player_1_card)
                player_1_deck.append(player_2_card)
            else:
                debug_print(f'Player 2 wins round {round_number} of game {game_number}!')
                player_2_deck.append(player_2_card)
                player_2_deck.append(player_1_card)
        else:
            if player_1_card > player_2_card:
                debug_print(f'Player 1 wins round {round_number} of game {game_number}!')
                player_1_deck.append(player_1_card)
                player_1_deck.append(player_2_card)
            else:
                debug_print(f'Player 2 wins round {round_number} of game {game_number}!')
                player_2_deck.append(player_2_card)
                player_2_deck.append(player_1_card)
        debug_print()
        round_number += 1

    return player_1_deck, player_2_deck

def score(deck):
    score = 0
    for i, c in enumerate(deck[::-1]):
        score += (i+1) * c
    return score

puzzle_input = sys.stdin.read().strip()

input_player_1_deck = get_player_cards(puzzle_input.split(' ')[1])
input_player_2_deck = get_player_cards(puzzle_input.split(' ')[2])

print(input_player_1_deck)
print(input_player_2_deck)

player_1, player_2 = play_game(1, input_player_1_deck[::],
                                  input_player_2_deck[::])

part_1_answer = score(player_1 or player_2)

print(f'Part 1 Answer: {part_1_answer}')

player_1, player_2 = play_game(1, input_player_1_deck[::],
                                  input_player_2_deck[::], True)

print()
debug_print('== Post-game results ==')
print_deck(1, player_1)
print_deck(2, player_2)
part_2_answer = score(player_1 or player_2)

print(f'Part 2 Answer: {part_2_answer}')
