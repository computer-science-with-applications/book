import sys

def divide(a, b):
    """ divide a by b """
    try:
        ret_val = a / b
    except ZeroDivisionError:
        # Send None back to the caller in the
        # hopes they can do something sensible
        # with it.
        ret_val = None
    except TypeError as e:
        # Fail: no way to move forward.
        print("Exception:", e)
        sys.exit(1)
    return ret_val



def print_divisions(N):
    """ Print result of dividing N by integers less than N. """
    for i in range(0, N):
        d = divide(N, i)
        print(f"{N} / {i} = {d}")




