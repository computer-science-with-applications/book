import random

def get_largest_roll(num_dice):
    '''
    Roll a specifed number of dice and return the largest face value.

    Inputs:
      num_dice: the number of dice to roll

    Returns: the largestface value rolled.
    '''

    NUM_SIDES = 6

    # initialize largest with a value smaller than the smallest
    # possible roll.
    largest = 0
    for i in range(num_dice):
        roll = random.randint(1,NUM_SIDES)
        if roll > largest:
            largest = roll

    return largest

def play_round():
    '''
    Play a round of the game Going to Boston using three dice.

    Inputs: None

    Returns: the score earned by the player as an integer.
    '''

    score = get_largest_roll(3)
    score += get_largest_roll(2)
    score += get_largest_roll(1)
    return score

    
def play_going_to_boston(goal):
    '''
    Simulate one game of Going to Boston.

    Inputs:
      goal (int): threshold for a win.

    Returns: None
    '''

    player1 = 0
    player2 = 0

    while (player1 < goal) and (player2 < GOAL):
        player1 += play_round()
        if player1 >= goal:
            break
        player2 += play_round()

    if player1 > player2:
        print("player1 wins")
    else:
        print("player2 wins")


def play_round_attempt_0():
    NUM_SIDES = 6
    score = 0

    # roll 3 dice, choose largest
    die1 = random.randint(1,NUM_SIDES+1)
    die2 = random.randint(1,NUM_SIDES+1)
    die3 = random.randint(1,NUM_SIDES+1)
    if die1 > die2:
        largest = die1
    else:
        largest = die2
    if die3 > largest:
        largest = die3
    score += largest

    # roll 2 dice, choose largest
    die1 = random.randint(1,NUM_SIDES+1)
    die2 = random.randint(1,NUM_SIDES+1)
    if die1 > die2:
        largest = die1
    else:
        largest = die2
    score += largest

    # roll 1 die, "choose" largest
    largest = random.randint(1,NUM_SIDES+1)
    score += largest

    return score

def play_round_muly():
    score = get_largest_roll(3)
    score *= get_largest_roll(2)
    score *= get_largest_roll(1)

    return score

    
def play_round_add_combined(num_dice):
    NUM_SIDES = 6
    score = 0
    for i in range(num_dice,0,-1):
        largest = 0
        for i in range(num_dice):
            roll = random.randint(1,NUM_SIDES+1)
            if roll > largest:
                largest = roll
        score += largest

    return score

def play_round_add_or_mult(num_dice, do_add):
    if do_add:
        score = 0
    else:
        score = 1

    for i in range(num_dice,0,-1):
        largest_val = get_largest_roll(num_dice)
        if do_add:
            score += largest_val
        else:
            score *= largest_val
    return score
        
    
def play_round_mult(num_dice):
    score = 1
    for i in range(num_dice,0,-1):
        score *= get_largest_roll(num_dice)

    return score



def play_one_game(goal):
    player1 = 0
    player2 = 0

    while (player1 < goal) and (player2 < goal):
        player1 += play_round()
        if player1 >= goal:
            break
        player2 += play_round()

    return player1 > player2

def simulate_many_games(num_trials, goal):
    wins = 0
    for i in range(num_trials):
        if play_one_game(goal):
            wins = wins + 1
            
    print(wins/num_trials)

