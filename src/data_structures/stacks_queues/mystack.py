# CS121 A'15: Stacks
#
# Borja Sotomayor
# August 2015
#
# Module providing a simple API for working with stacks

def create():
    '''
    Create an empty stack.

    Returns: Empty stack
    '''

    return []

def is_empty(stack):
    '''
    Returns True if the stack contains no elements,
    and False otherwise.
    '''

    assert isinstance(stack, list)

    return len(stack) == 0

def push(stack, value):
    '''
    Push a value into the stack (i.e., add the value
    at the top of the stack)

    Returns: nothing
    '''

    assert isinstance(stack, list)

    stack.append(value)

def pop(stack):
    '''
    Pop the value at the top of the stack. Note that
    this not only returns the popped value, but it
    also removes it from the stack.

    Returns: The popped value
    '''

    assert isinstance(stack, list)

    return stack.pop()

def top(stack):
    '''
    Return the value at the top of the stack, *without*
    removing it from the stack.

    Returns: Value at the top of the stack
    '''

    assert isinstance(stack, list)

    return stack[-1]

def to_string(stack):
    '''
    Returns a string representation of the stack.
    '''

    assert isinstance(stack, list)

    s  = " TOP OF THE STACK\n"
    s += "-------------------\n"
    
    for v in reversed(stack):
        s += str(v).center(20) + "\n"

    s += "-------------------\n"
    s += "BOTTOM OF THE STACK\n"
    return s
    

# This part of the Python file only gets run if we run the file
# like this:
#
#     python3 stack.py
#
# If we just do "import stack" from another Python module, this
# code won't be run. When creating a module that defines an API,
# this "__main__" portion is a good place to write some basic 
# testing code (this is not a substitute for writing unit tests,
# just a convenient way of testing your code as you write it,
# without having to import it in a separate module).
if __name__ == "__main__":
    s1 = create()

    assert is_empty(s1)

    push(s1, 10)
    push(s1, 27)
    push(s1, 5)
    push(s1, 9)
    push(s1, 7)
    print(to_string(s1))

    assert not is_empty(s1)

    v = top(s1)
    assert v == 7
    assert top(s1) == 7

    v = pop(s1)
    assert v == 7
    assert top(s1) == 9
    
    print(to_string(s1))

    while not is_empty(s1):
        print(pop(s1))

    assert is_empty(s1)

        

