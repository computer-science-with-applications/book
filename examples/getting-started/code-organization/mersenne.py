"""
A collection of functions related to Mersenne primes.
"""

import math
import primes


def is_mersenne_prime_exponent(p):
    """
    Is p the exponent of a mersenne prime?  That is, is 2**p - 1 a prime number?
      This function assumes that p is prime.

    Args:
        p (int): the exponent to check

    Returns (bool): True if p is the exponent of a mersenne prime,
        False otherwise.
    """
    if p == 2:
        return True

    m = 2**p - 1

    # Check whether m is prime using the Lucas–Lehmer primality test
    # https://en.wikipedia.org/wiki/Lucas–Lehmer_primality_test
    s = 4
    for _ in range(p - 2):
        s = ((s * s) - 2) % m

    return s == 0


def get_power_of_two_exponent(n):
    """
    If n be expressed as 2**m, return m.  Otherwise
      return None.

    Args:
        n (int): the value to check

    Returns (int):
      - m if n == 2 ** m
      - None, otherwise.
    """
    # Can n be expressed as 2^m?
    m = math.log2(n)

    if m.is_integer() and 2**int(m) == n:
        return int(m)
    else:
        return None


def print_mersenne_primes(max_p):
    """
    Print the mersenne primes that have an exponent in the range from
      1 to max_p (non-inclusive).

    Args:
        max_p (int): the upper bound (non-inclusive) for the range of
          exponents to consider.
    """
    i = 1
    for p in range(max_p):
        if not primes.is_prime(p):
            continue
        if is_mersenne_prime_exponent(p):
            m = 2 ** p - 1
            print(f"M{i}: {m} = 2**{p} - 1")
            i += 1
