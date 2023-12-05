def divide(a, b):
    ''' divide a by b '''
    ret_val = a / b
    return ret_val

def print_divisions(N):
    ''' Print result of dividing N by integers less than N. '''
    for i in range(0, N):
        d = divide(N, i)
        print(N, "/", i, "=", d)




