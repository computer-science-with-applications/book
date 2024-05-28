"""
This file contains a version of play_one_round that does not follow
standard Python conventions.
"""

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
    elif (chance == 2) or (chance == 3):
        return False
    elif (chance == 11) or (chance == 12):
        if (chosen_main == 5) or (chosen_main == 9):
            return False
        elif (chosen_main == 6) or (chosen_main == 8):
            return (chance == 12)
        else:
            # chosen_main is 7
            return (chance == 11)
    else:
        roll = throw_dice()
        while (roll != chance) and (roll != chosen_main):
            roll = throw_dice()

        return (roll == chance)
