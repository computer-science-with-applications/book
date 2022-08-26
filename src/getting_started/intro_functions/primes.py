def print_primes(N):
    for n in range(2, N+1):
        if is_prime(n):
            print(n)

def is_prime(n):
    encountered_divisor = False
    for i in range(2, n):
        if n % i == 0:
            encountered_divisor = True
            break
            
    return not encountered_divisor
