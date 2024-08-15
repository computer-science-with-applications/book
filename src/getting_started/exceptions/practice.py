def some_func(x):
    """ Docstring left out on purpose """
    if x < 0:
        # Will raise a TypeError if x is not a string.
        return str(x) + x
    elif x == 0:
        # Will raise a ZeroDivisionError
        return str(10 / x)
    elif x < 10:
        # Will raise an AssertionError
        assert False
    return  "some_func does not raise an exception"

def some_other_func(x):
    """ Docstring left out on purpose """
    try:
        result = some_func(x + 1)
    except TypeError:
        return "Caught TypeError in some_other_func"
    except ZeroDivisionError:
        return "Caught ZeroDivisionError in some_other_func"
    return result        

def yet_another_func(x):
    """ Docstring left out on purpose """
    try:
        result = some_other_func(x - 2)
    except TypeError:
        return "Caught TypeError in yet_another_func"
    except ZeroDivisionError:
        return "Caught ZeroDivisionError in yet_another_func"
    except Exception as err:
        return f"Caught {type(err)} in yet_another_func"
    return result
