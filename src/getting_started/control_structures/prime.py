def is_prime_no_break(n):
    encountered_divisor = False
    for i in range(2, n):
        if n % i == 0:
            encountered_divisor = True
               
    return encountered_divisor


def is_prime_with_break(n):
    encountered_divisor = False
    for i in range(2, n):
        if n % i == 0:
            encountered_divisor = True
            break
               
    return encountered_divisor
