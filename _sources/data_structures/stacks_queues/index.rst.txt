Implementing a Data Structure: Stacks and Queues
================================================

Up to this point, we have been using data types (integers, strings,
etc.)  and data structures (lists and dictionaries) that are part of
Python. While there is plenty we can do with them, sometimes we will
need to implement our own custom data structures. In this chapter, we
will present two new data structures: stacks and queues. While Python
actually already provides implementations of these data structures, we
will implement our own versions from scratch, so we can understand the
process involved in implementing a data structure. As we'll see, a key
aspect of this process is thinking about the *interface* of our data
structure, or how other programmers (not us) will interact with that
data structure.


Interfaces and APIs
-------------------

When we interact with lists and dictionaries in Python, we are blissfully
unaware of all their internal details. For example, take this simple
dictionary code:


.. python-run::

   d = {}
   d["A"] = 4.0
   "A" in d
   
In this code, we can think about the dictionary in fairly high-level terms: it contains
a collection of mappings between keys and values, and the code above adds one
such mapping and also queries whether a given mapping exists or not.

However, dictionaries internally use a data structure called a *hash table*.
Adding even a single mapping to the hash table involves a series of potentially
complicated steps, with a number of scenarios the implementer must handle: what
if the key already exists in the hash table? What if it doesn't? What if the
hash table doesn't have enough memory allocated to add more keys?

Fortunately, all those details are abstracted away for us, because Python
allows us to interact with the dictionary using a simple *interface*. When
we add a new mapping in the dictionary, we don't have to think in terms of
how we must manipulate the internal hash table; we just do this:

.. python-run::
   :formatting: separate

   d["A"] = 4.0

As users of a data structure, we only need to concern ourselves with the 
interface of that data structure. A term you'll hear often is *API*, which stands 
for *Application Programming Interface*. An API is a more general term, that can 
refer to the interface of a data structure (e.g., "the dictionary API"), but also to 
any collection of functions or protocols that allow us to interact with a software 
library or system, while abstracting away all of its internal details.

For example, when we import Python's ``random`` module, we are gaining access
to a software library for working with random numbers.

.. python-run::

   import random
   random.randint(1,100)
   
The ``random`` module has a well-specified API, and we use that API to
interact with ``random``. In the above piece of code, we don't need to know
the exact mechanism by which ``random.randint`` generates a random number: 
we just need to know that we can call that function with a lower bound and 
an upper bound, and it will return a random number within those bounds.

APIs can also refer to interfaces that allow us to access certain
services via the Internet, and specifically in a way that we can easily
incorporate in a program. For example, imagine we wanted to find out
the top Twitter users who use hashtag ``#programming`` (or any given
hashtag). We could go to the Twitter website, enter the hashtag into
their search tag, and then copy-paste the results to a file. However,
this is not something a program can do easily. 

Instead, Twitter provides an API for programs to access their data
more conveniently. This API is protocol-focused: it specifies the
messages that a program can send to their web server over the Internet
to obtain certain data.  For example, we can write a program that will
send a message to the Twitter API asking for all the tweets that meet
certain conditions (like including a given hashtag), and it will
return a JSON-encoded list of those tweets, which we can then easily
process from a program.  A popular API of this form will often spawn
competing libraries that are easier to use by abstracting away the
details of the actual protocol.

So, when writing a complex program or system, you rarely have to
implement the entire program completely from scratch, and it is common
to use multiple APIs as building blocks. Even when writing simple
Python programs, we often ``import`` existing libraries like
``random`` (so we don't have to implement our own functions for
generating random numbers).

In this chapter, we will implement a stack data structure and a queue
data structure, and we will focus not just on their internal
implementation, but also on what interface (or API) we will provide
for those data structures. In particular, we will provide an interface that 
is function-based: we expect anyone who uses the data structure to interact 
with it through a series of functions that we will write. Later in the book, 
we will introduce *classes* and *objects*, which will allow us to provide
a different type of interface: an object-oriented interface.

..
   See if we can incorporate any of this text that was originally written
   in the Stacks section:
   
   When it
   comes to data types, there are two roles for programmers:
   
   -  The data type *developer*, who is aware of all the internal details
      of the data type.
   -  The data type *user*, not in the sense of end-user of an application,
      but in the sense of another programmer that is *using* that data
      type.
   
   Take into account that, up to this point, you have all been *users* of
   the Python data types (integers, lists, dictionaries, etc.). Notice how
   you have been able to use these data types without knowing the internal
   details of the data types (much less being able to manipulate the
   internal details of the data type). When you created a new dictionary,
   one was provided for you, and you were given a well-defined set of
   operations that you could use to interact with that dictionary. You are
   blissfully unaware of what happens under the hood and, more importantly,
   you can't use dictionaries except in the ways intended by the Python
   developers (e.g., you can't use a list as a key in a dictionary).
   
   This "public interface" to the data type (the set of operations and
   attributes that the data type developer wants the user to be able to
   access) is called the data types API (Application Programmer Interface).
   You will now switch roles to being a data type developer although, by
   necessity, you will also be using the data types you develop (but it's
   important that you understand that there is a "barrier" between the two
   roles, and that the data type users should only interact with the data
   type through the API provided by the data type developer).

Stacks
------

A stack is essentially a list of values, but with a more constrained set
of operations available on that list. Most notably, we can only access
and manipulate one element in the data structure: the last element that
was inserted into the stack (which, in stacks, is known as the *top* of 
the stack). 

A common way of representing a stack is (non-surprisingly) as values stacked
on top of each other. For example:

::

      TOP
      
    |  10 |
    |  56 |
    | 105 |
    |  42 |
    |  5  |
    -------

     BOTTOM

.. todo::

   Come up with pretty diagrams instead of ASCII art.

In the above stack, we can only interact with the value ``10``: we can
see its value, we can remove it from the stack, or we can stack
another value on top of it. However, we cannot interact with the other
values in the stack without first removing the values above them (unless,
for example, we remove value ``10``, and then ``56`` becomes the top
of the stack).

More specifically, these are all the operations we can do with a stack:

-  Creating an empty stack
-  *Pushing* a value into the stack. If a stack was empty, then the
   stack will contain just the pushed value. If the stack already had
   values, we "stack" the new value on the top of stack.
-  *Popping* a value from the stack. This operation takes the value at the top of
   the stack and removes it (we also get to see what that value is)
-  *Peeking* at the value at the top of the stack. This operation tells us what
   the value at the top of the stack is but unlike popping does not
   remove it from the stack.
-  Checking whether a stack is empty.

It may seem like we're unnecessarily limiting ourselves: why would
we want to use a data structure like this when we already have lists,
which allow us to do so much more? One reason is that there are many
algorithms that can implemented in a straightforward way if we
use a stack data structure (or, rather, if we write the algorithm
in terms of stack operations like pushing and popping). For example,
here are some applications that use stacks:

- Undo algorithms in a word processor.
- Expression evaluation in compilers and interpreters.
- Functional call evaluation, which is the origin of the :ref:`function call stack <call-stack>`.

Later on, we'll see that another reason why limiting ourselves
to a constrained set of operations can be beneficial from
and interface/API standpoint.

However, let's first see how we can implement a stack. Since a stack
is a sequence of values, we can use a list to implement one.
For example, the stack we showed above could be represented as:

.. python-run::
   :formatting: separate

   s = [ 5, 42, 105, 56, 10 ]

Since we only interact with the top of the stack, we will store the
elements in the stack from bottom to top (i.e., the top of the stack
will be the last element in the list). This way, we can "push"
onto the stack using the list's ``append`` method:

.. python-run::
   
   s
   s.append(37)
   s

And popping can be done simply by calling the appropriately named
``pop`` method:

.. python-run::

   s
   s.pop()
   s   

.. admonition:: The complexity of list operations

   Why do we choose to store the stack in a list from bottom to top,
   instead of from top to bottom? If we stored it from top to
   bottom, the stack would look like this:

   .. python-run::
      :formatting: separate

      s2 = [ 10, 56, 105, 42, 5 ]

   And we could push using the ``insert`` method:

   .. python-run::
   
      s2
      s2.insert(0, 37)
      s2   

   And pop using the ``pop`` method (but specifying that
   we want to pop the 0th element of the list):
   
   .. python-run::
   
      s2
      s2.pop(0)
      s2   
   
   The results are seemingly the same as the bottom-to-top
   implementation, but the performance of the operations is not.  In
   Python, appending to the end of the list and removing the last element
   in the list can be done very efficiently in :math:`O(1)` time.
      
   Inserting and removing at the start of a Python list, on the other
   hand, requires :math:`O(n)` time, because all the elements in the list
   need to be shifted forward or backward by one position.  This analysis
   is not universally true of all list data structures in all languages
   and, in fact, there are list implementations (including a ``deque``
   data structure included in Python's ``collections`` module) that
   allows insertion and removal of the first element in :math:`O(1)`
   time. These types of differences give us another reason why, depending
   on how we intend to use a data structure, we may need to be aware of
   the complexity of its operations.
      
   The complexity of many data structure operations in Python can be
   found here: https://wiki.python.org/moin/TimeComplexity
  
At this point, we know how to use a list in a stack-like manner,
but nothing is stopping us from performing non-stack operations 
on that list. For example, we can easily modify non-top entries
in the stack, which is not allowed in a stack:

.. python-run::

   s[2] = 37
   s

This observation leads us to the other reason why limiting ourselves to a
constrained set of operations can be beneficial: to ensure
that the data structure is manipulated only in acceptable
ways. 

For example, earlier we discussed how dictionaries
are implemented internally as hash tables, but we interact
with dictionaries only through a limited set of operations
provided by that data structure's interface or API. This API abstracts
away the internal details of how dictionaries work, making
our lives easier as programmers, but it also prevents us from
wreaking havoc on the data structure by directly manipulating
the internal hash table. Another way of seeing this is that
dictionaries only allow us to interact with them on their own terms:
the only way of manipulating them is through their API (which
the programmers who implemented dictionaries have control over).

So, when implementing our stack data structure, we want to make sure
that the programmer who uses that stack *cannot* manipulate it in 
non-stack ways (like modifying anything other than the top
element of the stack). For now, we will accomplish this by
defining an API as a collection of functions. Later on in the book,
we will see how to define this same API but using an object-oriented
approach.

So, we will need functions for the operations we described earlier.
Creating an empty stack is simple enough:

.. python-run::
   :formatting: separate

   def stack_create():
       return []

.. python-run::

   s = stack_create()

Notice how the function returns a list but, conceptually, it returns a
*stack*. The programmer who uses our stack doesn't need to know that ``s`` is actually
a list (even though in Python this is easy enough to find out). In fact,
a very important principle of API design is that it should be possible
for the data type developer to change the internal implementation
without affecting the users of our data type (who should be treating the
value returned by ``create`` as an *opaque type*). 

For example, let's go back to dictionaries again. When we create
a new dictionary (e.g., ``d = {}``) we are blissfully unaware that 
variable ``d`` actually refers to a hash table and, not just that,
if the Python developers decided to switch to a different internal
representation, we would keep using dictionaries the same way.

Pushing, popping, peeking, and checking emptiness are similarly
straightforward:

.. python-run::
   :formatting: separate

   def stack_push(stack, value):
       stack.append(value)
    
   def stack_pop(stack):
       return stack.pop()
    
   def stack_top(stack):
       return stack[-1]
    
   def stack_is_empty(stack):
       return len(stack) == 0

Finally, let's also add a function that creates a string representation of the
stack:

.. python-run::
   :formatting: separate

   def stack_to_string(stack):
       s  = " TOP OF THE STACK\n"
       s += "-------------------\n"
        
       for v in reversed(stack):
           s += str(v).center(20) + "\n"
    
       s += "-------------------\n"
       s += "BOTTOM OF THE STACK\n"
       return s

Now, we can work with stacks using only these functions:

.. python-run::

   s = stack_create()
   stack_push(s, 10)
   stack_push(s, 27)
   stack_push(s, 5)
   stack_push(s, 9)
   stack_push(s, 7)
   print(stack_to_string(s))
    
.. python-run::

   stack_pop(s)
   print(stack_to_string(s))
    
Of course, because ``stack_create`` returns a list (which we're conceptually
manipulating as a stack), nothing stops a user from doing this:

.. python-run::

   s
   s[2] = 37
   s

This lack of control over access to the underlying representation is one of the limitations of using a function-based API in Python: it is
still relatively easy to perform forbidden operations on the data structure.
When we discuss object orientation later in the book, we will see that the
object oriented paradigm allows us to define APIs in a way that more strongly
protects the internal data of a data structure.


.. todo::

   Change s to stk in the examples to avoid confusion between the s in the print code and the stack s.


..
    The Stock Span problem
    ----------------------

    .. todo::

       Do we want to include this? It's based on an example someone else wrote,
       (http://www.geeksforgeeks.org/the-stock-span-problem) but I'm guessing 
       this is a general enough problem that we could reuse it ourselves.
       
       Alternatively, we can think of a different problem to highlight the use
       of stacks.

    Given a list of prices :math:`P` for a stock, where each element
    :math:`P_i` corresponds to the price of the stock on day :math:`i`, the
    span :math:`S_i` is the number of *consecutive* days before and
    including :math:`i`, for which the price of the stock is less than or
    equal to :math:`P_i`.

    So let's say we have this list of prices:

    .. python-run::
       :formatting: separate

       p = [100, 80, 60, 70, 60, 75, 85]

    The values of S should be ``[1, 1, 1, 2, 1, 4, 6]``. Work through this
    on the blackboard.

    The stock span problem is an example of a problem that can be solved
    more efficiently with stacks. For now, let's look at a solution
    *without* stacks:

    .. python-run::
       :formatting: separate

       def compute_span(prices):
           s = []
            
           # Traverse the list of prices
           for i, price in enumerate(prices):
               # For each price, traverse all the previous prices,
               # incrementing S_i until we encounter a price that
               # is larger than the current price.
               s_i = 0
               for prev_price in prices[i::-1]:           
                   if prev_price > price:
                       break
                   else:
                       s_i += 1
                       
               s.append(s_i)
                       
           return s

    .. python-run::

       compute_span(p)


    What is wrong with this solution? It is :math:`O(n^2)`

    We can use stacks to produce a more efficient implementation.

    .. python-run::
       :formatting: separate

       # Stack-based implementation of the stock span problem.
       # Notice how we only use the stack functions when interacting
       # with the stack. We never access the values in the 'st' list
       # directly.
       def compute_span_stacks(prices):
           s = []
            
           # Create a stack
           st = stack_create()
           
           # Traverse the list of prices
           for i, price in enumerate(prices):
               
               # Pop elements from stack until we encounter a price that
               # is greater than the current price, or until the stack
               # is empty
               while not stack_is_empty(st):
                   prev_price = prices[stack_top(st)]
                   
                   if prev_price > price:
                       break
                   else:
                       stack_pop(st)
            
               if stack_is_empty(st):
                   # If the stack is empty, then the current price
                   # is greater than all the elements to the left of
                   # it (note: this is trivially true for the first
                   # price in the list)
                   s_i = i + 1
               else:
                   # Otherwise, the current price is only greater than the
                   # elements after the index at the top of the stack.
                   s_i = i - stack_top(st)
                      
               s.append(s_i)
                        
               # Push the index of this price into the stack
               stack_push(st, i)
                
           return s

    .. python-run::

       compute_span_stacks(p)

    The above algorithm is :math:`O(n)`.




Queues
------

Like stacks, queues represent a sequence of values, but with
a different set of allowed operations on that sequence of values.
In particular, the start of that sequence of values is known
as the *back* of the queue, and the end of the sequence is
known as the *front* of the queue. For example::

          ------------------
   BACK   10  56  105  42  5   FRONT
          ------------------

A queue is like the typical queue you encounter when waiting in line
for something: elements can only enter the queue through the back of
the queue and can only exit the queue through the front. More
specifically, the only allowed operations with a queue are:
          
-  Creating an empty queue
-  *Enqueueing* a value at the back of the queue
-  *Dequeueing* a value at the front of the queue
-  *Peeking* at the value at the front of the queue
-  Checking the size of queue, including whether it is empty

Assuming we only use these operations, no element in the queue
can "skip the line". If an element enters the queue at the back
of the queue, it will not leave the queue until enough elements
(in front of it) are dequeued, so it reached the front of the
queue itself.

Like stacks, we will use a list to implement our queue. With
stacks, using the end of the list as the top of the stack
was the best choice from a performance standpoint.  For queues,
we have to choose whether to use the start of the list as the back
and the end of the list as the front, or vice versa.

As it turns out, we can choose either option. If we make the end of
the list be the front of the queue, Enqueueing is :math:`O(n)`
(because we're inserting at the start of the list) but dequeuing is
:math:`O(1)` (because we're deleting at the end). If we make the end
of the list be the back of the queue, the complexities are swapped
(enqueueing is :math:`O(1)` and dequeuing is :math:`O(n)`).

Assuming that the number of enqueue/dequeue operations is roughly the
same (because in many applications, what gets enqueued eventually gets
dequeued), there's really no difference between using the start or end
of the list as the front (and vice versa for the back of the queue).
These are the kind of issues that data structure implementors have to deal
with, but which the programmers that use the data structures *should not care about* 
(except that, sometimes, the documentation will tell you the complexity of certain
operations).

So, our queue operations can be implemented with the following functions:

.. python-run::
   :formatting: separate

   def queue_create():
       return []
    
   def queue_is_empty(queue):
       return len(queue) == 0
    
   def queue_length(queue):
       return len(queue)
   
   def queue_enqueue(queue, value):
       queue.append(value)
    
   def queue_dequeue(queue):
       return queue.pop(0)
   
   def queue_front(queue):
       return queue[0]
    
   def queue_to_string(queue):
       s  = "FRONT OF THE QUEUE\n"
       s += "------------------\n"
       
       for v in queue:
           s += str(v).center(19) + "\n"
   
       s += "------------------\n"
       s += "BACK OF THE QUEUE \n"
       return s

And we can now work with queues by calling those functions:

.. python-run::

   q1 = queue_create()
   queue_enqueue(q1, 10)
   queue_enqueue(q1, 27)
   queue_enqueue(q1, 5)
   queue_enqueue(q1, 9)
   queue_enqueue(q1, 7)
   print(queue_to_string(q1))   

.. python-run::

   queue_front(q1)
   print(queue_to_string(q1))
   queue_dequeue(q1)
   print(queue_to_string(q1))
   
.. todo::

   Include a substantial queue example (like Stock Span for stacks)

