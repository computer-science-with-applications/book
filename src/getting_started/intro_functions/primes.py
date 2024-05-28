def print_primes(lb, ub):
    """
    Print the primes between lb and ub inclusive.

    Args:
        lb (int): the lower bound of the range
        ub (int): the lower bound of the range

    Returns: None
    """
    for n in range(lb, ub + 1):
        if is_prime(n):
            print(n, "prime")
        else:
            print(n, "composite")

def is_prime(n):
    """
    Is n a prime number?

    Args:
        n (int): the value to check

    Returns (bool): True if n is prime and False otherwise.
    """

    encountered_divisor = False
    for i in range(2, n):
        if n % i == 0:
            encountered_divisor = True
            break
            
    return not encountered_divisor
