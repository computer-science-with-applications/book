import random

def flip_coins(n, prob_heads=0.5, seed=None):
    """
    Flip a weighted coin n times and report the number that come up
    heads.

    Args:
        n (int): number of times to flip the coin
        prob_heads (float): probability that the coin comes up heads
            (default: 0.5)
        seed (int | None): the seed for the random number generator
            (default: None)
        debug_level (int): 0 means do not print any extra information,
            1 means print the parameters, and 2 means print the
            parameters and the value of flip and num_heads for each
            coin flip.

    Returns (int): number of flips that came up heads.
    """

    random.seed(seed)

    num_heads = 0
    
    for i in range(n):
        flip = random.uniform(0.0, 1.0)
        if flip < prob_heads:
            num_heads = num_heads + 1
    
    return num_heads

# Sample calls
print(f"flip_coins(10): {flip_coins(10)}")
print(f"flip_coins(10, prob_heads=0.8): {flip_coins(10, prob_heads=0.8)}")
print(f"flip_coins(10, seed=5000): {flip_coins(10, seed=5000)}")
print(f"flip_coins(10, prob_heads=0.8, seed=5000): "
      f"{flip_coins(10, prob_heads=0.8, seed=5000)}")
print(f"flip_coins(10, 0.9, 5000): {flip_coins(10, 0.8, 5000)}")



