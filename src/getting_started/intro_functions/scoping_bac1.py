def fun1(i):
    i = i - 2
    return i

def fun2(i):
    return fun1(i) + fun1(i)

def fun3(i):
    return fun1(i * 2)

def fun4(i):
    i = fun3(i)
    return fun2(i)

print(f"fun4(6): {fun4(6)}")
