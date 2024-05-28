"""
Simple program for checking primes.
"""

from primes import is_prime
from mersenne import is_mersenne_prime_exponent, get_power_of_two_exponent

if __name__ == "__main__":
    n = input("Enter a number: ")

    n = int(n)

    if not is_prime(n):
        print(f"{n} is not a prime number.")
    else:
        p = get_power_of_two_exponent(n + 1)
        if p is not None:
            if is_mersenne_prime_exponent(n):
                print(f"{n} is a double Mersenne prime: both {n}")
                print(f"  and 2**{n} - 1 are both Mersenne primes.")
            else:
                print(f"{n} is a Mersenne prime ({n} == 2**{p} - 1.")
        else:
            if is_mersenne_prime_exponent(n):
                print(f"{n} is a prime number, but not a Mersenne prime")
                print(f"   (however, 2**{n} - 1 is a Mersenne prime).")
            else:
                print(f"{n} is a prime number, but not a Mersenne prime")
                print(f"  and neither is 2**{n} - 1.")
