import random 

def get_largest_roll(num_dice, num_sides=6):
    """
    Roll a specified number of dice and return the largest face
    value.

    Args:
        num_dice (int): the number of dice to roll
        num_sides (int): the number of sides in a single die (default: 6)

    Returns (int): the largest face value rolled
    """

    # initialize largest with a value smaller than the smallest
    # possible roll.
    largest = 0
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        largest = max(roll, largest)

    return largest
