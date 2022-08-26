# CS121 A'15: Queues
#
# Borja Sotomayor
# August 2015
#
# Module providing a simple API for working with queues

def create():
    '''
    Create an empty queue.

    Returns: Empty queue
    '''

    return []

def is_empty(queue):
    '''
    Returns True if the queue contains no elements,
    and False otherwise.
    '''

    assert isinstance(queue, list)

    return len(queue) == 0

def length(queue):
    '''
    Returns the length of the queue
    '''

    assert isinstance(queue, list)

    return len(queue)

def enqueue(queue, value):
    '''
    Enqueue a value in the queue (i.e., add the value
    at the back of the queue)

    Returns: nothing
    '''

    assert isinstance(queue, list)

    queue.append(value)

def dequeue(queue):
    '''
    Dequeue a value from the queue (i.e., remove the
    element at the front of the queue, and remove it
    from the queue)

    Returns: The dequeued value
    '''

    assert isinstance(queue, list)

    return queue.pop(0)

def front(queue):
    '''
    Return the value at the front of the queue, *without*
    removing it from the queue.

    Returns: Value at the front of the queue
    '''

    assert isinstance(queue, list)

    return queue[0]

def to_string(queue):
    '''
    Returns a string representation of the queue.
    '''

    assert isinstance(queue, list)

    s  = "FRONT OF THE QUEUE\n"
    s += "------------------\n"
    
    for v in queue:
        s += str(v).center(19) + "\n"

    s += "------------------\n"
    s += "BACK OF THE QUEUE \n"
    return s
    

# This part of the Python file only gets run if we run the file
# like this:
#
#     python3 queue.py
#
# If we just do "import queue" from another Python module, this
# code won't be run. When creating a module that defines an API,
# this "__main__" portion is a good place to write some basic 
# testing code (this is not a substitute for writing unit tests,
# just a convenient way of testing your code as you write it,
# without having to import it in a separate module).
if __name__ == "__main__":
    q1 = create()

    assert is_empty(q1)
    assert length(q1) == 0

    enqueue(q1, 10)
    enqueue(q1, 27)
    enqueue(q1, 5)
    enqueue(q1, 9)
    enqueue(q1, 7)
    print(to_string(q1))

    assert not is_empty(q1)
    assert length(q1) == 5

    v = front(q1)
    assert v == 10
    assert front(q1) == 10

    v = dequeue(q1)
    assert v == 10
    assert front(q1) == 27
    
    print(to_string(q1))

    while not is_empty(q1):
        print(dequeue(q1))

    assert is_empty(q1)

        

