import random

def flip_coins(n, prob_heads=0.5, seed=None, debug_level=0):
    """
    Flip a weighted coin n times and report the number that come up
    heads.

    Args:
        n (int): number of times to flip the coin
        prob_heads (float): probability that the coin comes up heads
            (default: 0.5)
        seed (int | None): the seed for the random number generator
            (default: None)
        debug_level (int): controls the amount of information printed
            about the computation

    Returns (int): number of flips that came up heads.
    """
    assert 0 <= debug_level <= 2

    if debug_level >= 1:
        msg = (f"Debug {debug_level}: " + 
               f"flip_coins(n={n}, prob_heads{prob_heads}, " +
               f"seed={seed}, debug_level={debug_level})")
        print(msg)
              
              
    random.seed(seed)

    num_heads = 0
    
    for i in range(n):
        flip = random.uniform(0.0, 1.0)
        if flip < prob_heads:
            num_heads = num_heads + 1
        if debug_level == 2:
            msg = (f"Debug {debug_level}: flip: {flip}\t" +
                   f"num_heads: {num_heads}")
            print(msg)
    
    return num_heads

# Sample calls
print(f"Result: {flip_coins(5, seed=5000)}\n")
print(f"Result: {flip_coins(5, seed=5000, debug_level=1)}\n")
print(f"Result: {flip_coins(5, seed=5000, debug_level=2)}\n")
print(f"Result: {flip_coins(5, seed=5000, debug_level=2)}\n")




