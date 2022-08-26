def is_prime_no_break(n):
    encountered_divisor = False
    i = 2
    while i < n:
        if n % i == 0:
            encountered_divisor = True
               
    return encountered_divisor


def is_prime_with_break(n):
    encountered_divisor = False
    i = 2
    while i < n:
        if n % i == 0:
            encountered_divisor = True
            break
        i = i + 1
               
    return encountered_divisor
