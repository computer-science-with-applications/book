"""
A program to estimate the success rates of different mains in the game Hazard.

Sample use:

    $ python3 hazard.py
    Number of rounds: 1000
    5 0.498
    6 0.499
    7 0.483
    8 0.504
    9 0.493
"""

import random
import sys

def throw_dice():
    """
    Throw a pair of six-sided dice

    Returns (int): the sum of the dice
    """
    num_sides = 6
    return random.randint(1, num_sides) + random.randint(1, num_sides)


def play_one_round(chosen_main):
    """
    Play one round of Hazard.

    Args:
        chosen_main (int): a value between 5 and 9 inclusive.
    
    Returns (bool): True, if player wins the round and False, otherwise.
    """

    chance = throw_dice()

    if chance == chosen_main:
        return True
    if chance == 2 or chance == 3:
        return False
    if chance == 11 or chance == 12:
        if chosen_main == 5 or chosen_main == 9:
            return False
        if chosen_main == 6 or chosen_main == 8:
            return chance == 12
        # chosen_main is 7
        return chance == 11

    roll = throw_dice()
    while roll != chance and roll != chosen_main:
        roll = throw_dice()

    return roll == chance


def simulate_caster(chosen_main):
    """
    Simulate rounds until the caster loses two rounds in a row.

    Args:
        chosen_main (int): a value between 5 and 9 inclusive.

    Returns (int): the number of rounds won
    """

    num_wins = 0
    consecutive_losses = 0

    while consecutive_losses < 2:
        if play_one_round(chosen_main):
            consecutive_losses = 0
            num_wins = num_wins + 1
        else:
            consecutive_losses = consecutive_losses + 1

    return num_wins


def print_win_rate_table(num_rounds):
    """
    Print a table with the win rates for the possible choices for main

    Args:
        num_rounds (int): the number of rounds to simulate

    Returns: None
    """

    for chosen_main in range(5, 10):
        num_wins = 0
        for _ in range(num_rounds):
            if play_one_round(chosen_main):
                num_wins = num_wins + 1
        print(chosen_main, num_wins/num_rounds)


if __name__ == "__main__":
    error_msg = "The number of rounds needs to be a positive integer. Goodbye."
    n = input("Number of rounds: ")
    try:
        num_rounds = int(n)
    except valueError:
        print(error_msg)
        sys.exit(1)

    if num_rounds > 0:
        print_win_rate_table(num_rounds)
    else:
        print(error_msg)
        sys.exit(1)        
