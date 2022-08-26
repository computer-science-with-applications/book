import random

def throw_dice():
    '''
    Throw a pair of six-sided dice

    Returns (int): the sum of the dice
    '''
    NUM_SIDES = 6
    val = random.randint(1,NUM_SIDES) + random.randint(1,NUM_SIDES)
    return val


def play_one_round(chosen_main):
    '''
    Play one round of Hazard.

    Inputs:
        chosen_main (int): a value between 5 and 9 inclusive.
    
    Returns (boolean): True, if player wins the round and False, otherwise.
    '''

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

    roll = throw_dice()
    while not ((roll == chance) or (roll == chosen_main)):
        roll = throw_dice()

    return (roll == chance)


def simulate_caster(chosen_main):
    '''
    Simulate rounds until the caster loses two rounds in a row.

    Inputs:
        chosen_main (int): a value between 5 and 9 inclusive.

    Returns (int): the number of rounds won
    '''

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
    '''
    Print a table with the win rates for the possible choices for main

    Inputs:
        num_rounds (int): the number of rounds to simulate
    '''

    for chosen_main in range(5, 10):
        num_wins = 0
        for i in range(num_rounds):
            if play_one_round(chosen_main):
                num_wins = num_wins + 1
        print(chosen_main, num_wins/num_rounds)


####### I don't think we want to use these functions in the example. ########
def estimate_num_rounds(num_trials, chosen_main):
    total_num_rounds = 0
    total_wins = 0
    for t in range(num_trials):
        (rounds, wins) = simulate_caster(chosen_main)
        total_num_rounds = total_num_rounds + rounds
        total_wins = total_wins + wins

    return total_num_rounds/num_trials, total_num_rounds-total_wins

def gen_num_rounds_tab(num_trials):
    for chosen_main in range(5, 10):
        print(chosen_main, estimate_num_rounds(num_trials, chosen_main))


'''
if __name__ == "__main__":
    print(estimate_num_rounds(100, 4))
'''    
        
        
