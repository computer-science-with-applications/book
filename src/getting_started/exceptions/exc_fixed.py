def divide(a, b):
    """ divide a by b """
    try:
        ret_val = a / b
    except ZeroDivisionError:
        # Send None back to the caller in the
        # hopes they can do something sensible
        # with it.
        ret_val = None
    return ret_val

def print_divisions(N):
    """ Print result of dividing N by integers less than N. """
    for i in range(1, N):
        d = divide(N, i)
        print(f"{N} / {i} = {d}")




