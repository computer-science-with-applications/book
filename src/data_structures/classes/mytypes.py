import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
    
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Line(object):
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

    @classmethod
    def from_slope_intercept(cls, slope, y_intercept):
        p0 = Point(0, y_intercept)
        p1 = Point(1, slope + y_intercept)
        return cls(p0, p1)

    def is_vertical(self):
        return self.p0.x == self.p1.x

    def get_slope(self):
        if self.is_vertical():
            return float('inf')
        else:
            return (self.p1.y - self.p0.y) / (self.p1.x - self.p0.x)
        
    def get_y_intercept(self):
        if self.is_vertical():
            if self.p0.x == 0:
                return 0.0
            else:
                return float('NaN')
        else:
            return self.p0.y - self.get_slope()*self.p0.x

    def __repr__(self):
        if self.is_vertical():
            return "x = {}".format(self.p0.x)
        else:
            return "y = {}*x + {}".format(self.get_slope(), self.get_y_intercept())


class Queue(object):

    def __init__(self, max_capacity = None):
        '''
        Initialize a queue.
    
        If max_capacity is None, then the queue
        has no maximum capacity.
        '''
        self.__queue = []
        self.__max_capacity = max_capacity

    @property
    def max_capacity(self):
        ''' Getter for max_capacity '''
        return self.__max_capacity

    @property
    def length(self):
        '''
        Returns the length of the queue
        '''
        return len(self.__queue)

    @property
    def front(self):
        '''
        Return the value at the front of the queue, *without*
        removing it from the queue.

        Returns: Value at the front of the queue
        '''

        return self.__queue[0]

    def is_empty(self):
        '''
        Returns True if the queue contains no elements,
        and False otherwise.
        '''
        return len(self.__queue) == 0


    def enqueue(self, value):
        '''
        Enqueue a value in the queue (i.e., add the value
        at the back of the queue).

        Returns: True if the value was enqueue; False if
        it wasn't enqueued because the queue has reached
        its maximum capacity.
        '''
        
        if self.max_capacity is not None and self.length == self.max_capacity:
            return False
        else:
            self.__queue.append(value)
            return True

    def dequeue(self):
        '''
        Dequeue a value from the queue (i.e., remove the
        element at the front of the queue, and remove it
        from the queue)

        Returns: The dequeued value
        '''

        return self.__queue.pop(0)

    def __repr__(self):
        '''
        Returns a string representation of the queue.
        '''
        s = ""

        for v in reversed(self.__queue):
            s += " --> " + str(v)

        s += " -->"

        return s


if __name__ == "__main__":
    # y = 5x + 7
    p = Point(0, 7)
    q = Point(1, 12)
    l = Line(p, q)
    print(l)
    print()

    # x = 2
    p = Point(2, 1)
    q = Point(2, 2)
    l = Line(p, q)
    print(l)
    print("Slope:", l.get_slope())
    print("Y-intercept:", l.get_y_intercept())
    print()

    # x = 0
    p = Point(0, 1)
    q = Point(0, 2)
    l = Line(p, q)
    print(l)
    print("Slope:", l.get_slope())
    print("Y-intercept:", l.get_y_intercept())
    print()

    l = Line.from_slope_intercept(slope = 5, y_intercept = 7)
    print(l)


