def fun1(x, y, z):
    if x % y == z:
        return x + y + z
    else:
        return 1

def fun2(i,j):
    i = i + 2
    j = j + 3

def fun3(x, y, z=2):
    for i in range(4, x):
        for j in range(2, y):
            a = fun1(i, j, z)
            if a >= 10:
                fun2(i,j)
                return i + j
    return -1

print(f"fun(6, 4, 2): {fun3(6, 4, 2)}")


