Recursion
=========

As we have seen throughout the book, there are many cases where we must repeat 
operations and can do so with a ``for`` or ``while`` loop.
This form of repetition is formally known as *iteration* and involves
defining a loop condition and a block of statements to be repeated
as long as that condition is true. Each repetition of the block of
statements is called an *iteration* and an algorithm that uses
this style of repetition is called an *iterative algorithm*.

In this chapter, we will discuss a different way of expressing
repetition: *recursion*. Recursion
is equally expressive as iteration, meaning that anything we
can do with iteration can also be done with recursion (and vice versa).
There are some algorithms, however, where a recursive solution
will require less code and will result in cleaner and more intuitive code 
than the equivalent iterative solution.
In this chapter, we will introduce recursion and work through several problems that
lend themselves naturally to a recursive solution.


Factorials
----------

Let's look at the factorial operation:

.. math::

   4! = 4\cdot 3 \cdot 2 \cdot 1 = 24

One of the formal definitions of factorial is:

.. math::

   n!=\prod_{k=1}^n k \!

We can implement this definition using a ``for`` loop:

.. python-run::
   :formatting: separate

   def factorial(n):
       '''  Compute n! iteratively '''

       rv = 1
       for k in range(1, n+1):
           rv = rv * k
       return rv

.. python-run::

   factorial(4)
   factorial(5)

Factorials can also be defined as follows:

.. math::

   n!=\left\{
               \begin{array}{ll}
                 1 & \textrm{if n=1}\\
                 n\cdot(n-1)! & \textrm{if n>1}
               \end{array}
             \right.

This is a *recursive definition*. Notice how there
is no reference to loops or to repetition. Instead, factorials are
defined in terms of themselves. At first, this approach may seem odd. Imagine
finding a definition in the dictionary that looked like this:

   **Recursion**: See *recursion*.
   
You would keep coming back to the definition of "recursion" infinitely!

However, the recursive definition of factorial works because it is
divided into two cases:

- *The base case*: In this case, the value of the factorial can be obtained immediately and trivially. In the case where :math:`n=1`, the value of the factorial is known immediately and without further computation: it is simply 1.
- *The recursive case*: In this case, we define the factorial in terms of itself. For factorials, we can define :math:`n!` as :math:`n` times :math:`(n-1)!`

So, if we were computing :math:`4!`, we would start in the recursive case,
which tells us that:

.. math::

   4! = 4\cdot 3!
   
To evaluate this formula, we need to find the value of :math:`3!` which,
again, involves the recursive case:

.. math::

   3! = 3\cdot 2!

Similarly for :math:`2!`:

.. math::

   2! = 2\cdot 1!
   
But, when we get to :math:`1!`, we know that :math:`1!=1`, so we can plug :math:`1` into the above formula, and we get:

.. math::

   2! = 2\cdot 1 = 2
   
Now that we know the value of  :math:`2!`, we can plug that
into this formula:

.. math::

   3! = 3\cdot 2!
   
And we get:

.. math::

   3! = 3\cdot 2 = 6
   
And, finally, now that we know the value of :math:`3!`,
plug it into the formula for :math:`4!`:

.. math::

   4! = 4\cdot 3!
   
And we get:
   
.. math::
 
   4! = 4\cdot 6 = 24

Notice that
the recursive case must be defined so that it
gets us closer to the base case when we use it; otherwise,
we would fall into infinite recursion.

We can implement our recursive definition of factorial 
in Python like this:

.. python-run::
   :formatting: separate

   def factorial_r(n):
       '''  Compute n! recursively '''

       if n == 1:
          return 1
       elif n > 1:
          return n * factorial_r(n-1)

.. python-run::

   factorial_r(4)
   factorial_r(5)

Notice that our function ``factorial_r`` calls itself.
We refer to such functions as *recursive functions*, and we refer
to the point where the function calls itself as a *recursive call*.
While the concept of recursion can be easy to understand at a high
level (think, for example, of how easily we defined factorials
recursively), writing recursive functions and understanding what
happens during a recursive call often stumps beginning programmers.

So, we are going to spend some time dissecting exactly what happens
in a recursive function. After that, we will work through several
examples of recursive algorithms that will help us to understand
how to design recursive functions, as well as when to use a recursive
algorithm instead of an iterative solution.


The anatomy of a recursive function call
----------------------------------------

To show what happens in the ``factorial_r`` function,
we have prepared a more verbose version that will do the 
same thing as the function shown earlier, but will print messages
to help us understand exactly what's going on. Don't worry if
you don't understand how we're formatting the output (especially
how we indent the messages, which requires using an extra parameter). 
Focus instead on following what happens during each recursive call.

.. todo::

   Question: do we want to add a verbose flag to this version to make it
   consistent with the rest of the functions in this chapter?

   What is the best way to fix the fact that some of the lines are too
   long?  Should we construct a string and then print it?

.. python-run::
   :formatting: separate
      
   def factorial_r(n, indent=""):
       '''  
       Compute n! recursively and print information about the
       computation along the way.

       Inputs:
         n (int): operand
         indent (string): spaces to use as a prefix when printing.

       Returns (int): n!
       '''  

       if n == 1:
          print(indent + "factorial_r(1) -- BASE CASE -- The value of 1! is 1")
          print()
          return 1
       elif n > 1:
          print(indent + "factorial_r({}) -- START OF RECURSIVE CASE".format(n))
          print(indent + "                  The value of {}! is {}*{}!".format(n, n, n-1))
          print(indent + "                  I need to find out the value of {}!".format(n-1))
          print()
          x = factorial_r(n-1, indent=indent+"    ")
          print(indent + "factorial_r({}) -- END OF RECURSIVE CASE".format(n))
          print(indent + "                  I now know that {}! is {}".format(n-1, x))
          print(indent + "                  Which means that {}! = {}*{}".format(n, n, x))
          print()
          return n * x

.. python-run::

   factorial_r(4)
   
Notice how, whenever we run into a recursive case, we put that function call
on "hold" while we go deeper into the recursion rabbit hole until we 
get to a base case and can start "wrapping up" all of the recursive cases that
we put on hold. Examining the function call stack (see :ref:`call-stack` in chapter :ref:`chapter-functions`) 
can help explain what happens
during a call to a recursive function. This process is a fairly low-level aspect of 
how recursive calls work, and so you can skip this discussion for now if you want. However,
if you're the kind of person who understands concepts better if you know
exactly what happens under the hood, read on. 

When a call is made to ``factorial_r(4)``, the following entry is added to
the function call stack. For simplicity, we will omit the ``indent`` parameter,
which is used purely for formatting purposes.

+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 4                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+

When the function reaches the recursive call (``factorial_r(n-1)``), it will need
to make a call to ``factorial_r(3)`` before it can set a value for ``x``. So,
we add an entry for ``factorial_r(3)``:

+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 4                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 3                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+

Recall that our stacks grow down the page, so we added the frame for
the call ``factorial_r(3)`` beneath the frame for the call
``factorial_4``.

This process is repeated for every recursive call, until we reach the
recursive call that triggers the base case:

+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 4                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 3                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 2                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 1                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+

At this point, we have a function call stack that is holding
information for all the calls from ``factorial_r(4)`` to
``factorial_r(1)``. When we reach the base case, the recursion starts
to *unwind* because we have reached a point where ``factorial_r`` can
return a value without having to make any more recursive calls. The
last entry in the function call stack will return 1:

+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 1                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: 1           |
+-------------------------------+

The function call represented by the previous entry in the function
call stack can now assign a value to variable ``x`` because it has
finished evaluating the function call ``factorial_r(1)``, so the
function call stack will look like this:

+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 4                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 3                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 2                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: 1                    |
|                               |
| **Return value**: 2           |
+-------------------------------+

Remember that once a function call ends, its entry is removed (or popped) from the
function call stack, so we no longer have an entry for ``factorial_r(1)``.

Now, the function call to ``factorial_r(2)`` will be able to return the value
``2`` (i.e., ``n`` multiplied by ``x``), which will become the value for ``x``
in ``factorial_r(3)``:

+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 4                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: *undefined*          |
|                               |
| **Return value**: None        |
+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 3                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: 2                    |
|                               |
| **Return value**: 6           |
+-------------------------------+

We repeat this process one final time, to obtain the return value of ``factorial_r(4)``:

+-------------------------------+
| **Function**: ``factorial_r`` |
|                               |
| **Parameters**:               |
|                               |
| * ``n``: 4                    |
|                               |
| **Variables**:                |
|                               |
| * ``x``: 6                    |
|                               |
| **Return value**: 24          |
+-------------------------------+

Thinking about recursive calls in terms of their function call stack
reinforces the notion that a fresh set of parameters and local
variables is created for a *every* call to a function.  Keeping this
fact in mind can help avoid a common mistake: thinking that the
recursive call simply "jumps" back to the beginning of the
function. For example, in the ``factorial_r`` function:

.. python-run::
   :formatting: separate

   def factorial_r(n):
       '''  Compute n! recursively '''

       if n == 1:
          return 1
       elif n > 1:
          x = factorial_r(n-1)
          return n * x
         
When we reach the ``factorial_r(n-1)`` call, we do not 
change the value of ``n`` and "jump" back up to the beginning of
the function that is currently running. Instead, an entirely new
entry in the function call stack is created, with its own values for
``n`` and ``x``. If you find yourself struggling to understand how
a recursive function works, try working through the function
call stack step-by-step as we did above.


Recursion vs. iteration
-----------------------

At this point, we have seen that we can implement the factorial
function using iteration:

.. python-run::
   :formatting: separate

   def factorial(n):
       '''  Compute n! iteratively '''

       rv = 1
       for k in range(1, n+1):
           rv = rv * k
       return rv

And using recursion:

.. python-run::
   :formatting: separate

   def factorial_r(n):
       '''  Compute n! recursively '''

       if n == 1:
          return 1
       elif n > 1:
          return n * factorial_r(n-1)

In this simple example, the amount of code we write for both functions
is roughly the same, so why would we choose recursion over iteration? 
In general, there are a number of algorithms and data structures 
that lend themselves naturally to a recursive definition. 
In those cases, a recursive implementation will typically be simpler 
and more elegant than the equivalent iterative implementation. This 
will become more apparent as we see more recursive algorithms.

However, you should resist the urge to use recursion as just
another way of performing repetition in your code. While it is true that
recursion and iteration are equally expressive (every iterative
algorithm can be converted to a recursive one, and vice versa),
you will usually use recursion *only* when you are faced 
with problems that have an inherently recursive definition.

For example, let's say we want to create a list with all the numbers 
between a lower bound ``lb`` and ``ub`` (both inclusive). We can do this work very 
simply with iteration (for the sake of argument, let's assume
we cannot use the ``range`` function):

.. python-run::
   :formatting: separate

   def gen_nums(lb, ub):
       '''
       Generate a list of integers from a lower bound to an upper
       bound inclusive.

       Inputs:
         lb (int): lower bound
         ub (int): upper bound

       Returns (list of ints): list of integers from lb to ub
         inclusive 
       '''

       l = []
       i = lb
       while i <= ub:
          l.append(i)
          i += 1
         
       return l

.. python-run::

   gen_nums(1,5)
   
Although we can also write a recursive solution to this problem,
it is arguably not as easy to understand as the equivalent iterative solution:


.. python-run::
   :formatting: separate

   def gen_nums_r(lb, ub):
       '''
       Generate a list of integers from a lower bound to an upper
       bound inclusive.

       Inputs:
         lb (int): lower bound
         ub (int): upper bound

       Returns (list of ints): list of integers from lb to ub
         inclusive 
       '''

       if lb > ub:
          return []
       else:
          return [lb] + gen_nums_r(lb+1, ub)

.. python-run::

   gen_nums_r(1,5)

Notice that our base case is the case when the lower bound is greater
than the upper bound. In this case, the list can be obtained
trivially: it will simply be an empty list. In the recursive case, we
create a list whose first element is the lower bound and the
rest of the list (from ``lb+1`` to ``ub``) is obtained recursively
(we're guaranteed to reach the base case eventually because we
increment ``lb`` by one in each call and get closer to ``ub`` with
each recursive call). As suggested earlier, you may want to work
through the function call stack for a simple example call, such as
``gen_nums_r(2,5)``, if you have trouble understanding how this
function works. 

Choosing between iteration and recursion can also be 
a question of taste. Most functional programming languages depend on recursion
to repeat operations and many of them do not include any iterative
constructs at all, so someone
who learned how to program using a functional programming language
may find the recursive version of ``gen_nums_r`` to be
more elegant and easier to understand.  Programmers who
have learned to program under the imperative paradigm (using loops
for repetition), however, tend to use recursion only when dealing with problems
that have an inherently recursive definition because it is easier
to translate the problem into code using that definition rather than trying
to figure out the equivalent iterative solution.

Permutations (or how to think recursively)
------------------------------------------

*Generating permutations* is a good example of a problem that has a
simple recursive definition: given :math:`n` elements, the
permutations of those elements are all possible ways of arranging
those elements.

For example, these are all of the possible permutations of (1,2,3):

::

    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1

And these are all of the possible permutations of (1,2,3,4):

::

    1 2 3 4
    1 2 4 3
    1 3 2 4
    1 3 4 2
    1 4 2 3
    1 4 3 2

    2 1 3 4
    2 1 4 3
    2 3 1 4
    2 3 4 1
    2 4 1 3
    2 4 3 1

    3 1 2 4
    3 1 4 2
    3 2 1 4
    3 2 4 1
    3 4 1 2
    3 4 2 1

    4 1 2 3
    4 1 3 2
    4 2 1 3
    4 2 3 1
    4 3 1 2
    4 3 2 1

Look closely at both sets of permutations. In particular, 
look at all the permutations of (1,2,3,4) that start with 4:

::

    4 1 2 3
    4 1 3 2
    4 2 1 3
    4 2 3 1
    4 3 1 2
    4 3 2 1

These permutations are generated by taking all of the permutations
of (1,2,3) and adding 4 as the first element. In fact,
the permutations of (1,2,3,4) are:

-  All permutations of (2,3,4) with 1 as the first element;
-  All permutations of (1,3,4) with 2 as the first element;
-  All permutations of (1,2,4) with 3 as the first element; plus
-  All permutations of (1,2,3) with 4 as the first element.

And the permutations of (1,2,3) are:

-  All permutations of (2,3) with 1 as the first element;
-  All permutations of (1,3) with 2 as the first element; plus
-  All permutations of (1,2) with 3 as the first element.

And so on.

Intuitively, it looks like permutations are defined recursively,
because we can define permutations of :math:`n` elements in
terms of permutations of :math:`n-1` elements. To write a 
recursive solution, we will generally take
the following three steps.

**Step #1: Determine the input(s) and output(s) to the function.**
This step may seem obvious given that we do this work any time we
write a function, but when solving a recursive problem, it is
especially important to make these decisions first.

In this case, the input to our function will be a list
of elements we want to generate permutations on. The output,
or return value, will be a list of permutations, with
each permutation being a list of elements. For example,
if we call the function with the following list:

::

    [1, 2, 3]
    
We would expect it to return the following:

::

     [[1, 2, 3],
      [1, 3, 2],
      [2, 1, 3],
      [2, 3, 1],
      [3, 1, 2],
      [3, 2, 1]]

The reason we need to figure the types out first is because we need to
ensure that both our base case and our recursive case expect the same
type of inputs and return the same type of outputs.

**Step #2: Determine the base case(s) for the function.**
We need to think about the case (or cases) where solving
the problem is trivial. With permutations, this case
is when we're asked to produce all the permutations
of one element. In this case, there is only one such
permutation: the permutation with that element.

So, we can start writing our ``permutations_r`` function
as follows:

.. python-run::
   :formatting: separate

   def permutations_r(p):
       '''
       Compute all the permutations of the values in p.

       Inputs:
         p (list): list of values to permute

       Returns (list of lists): permutations of p
       '''

       if len(p) == 1:
           # Base case
           return p
       else:
           # TODO: Recursive case
           return []
            
However, the above code for the base case is not correct!
Let's try calling the function in such a way that we hit
the base case immediately:

.. python-run::

   permutations_r([1])
   
The function returns ``[1]``, but we decided that the return
value of our function would be a *list* of permutations (and
``[1]`` represents a single permutation). What we really
want to get from the function is ``[ [1] ]``. So we re-write
the function as follows:           
       
.. python-run::
   :formatting: separate

   def permutations_r(p):
       '''
       Compute all the permutations of the values in p.

       Inputs:
         p (list): list of values to permute

       Returns (list of lists): permutations of p
       '''

       if len(p) == 1:
           # Base case
           return [ p ]
       else:
           # TODO: Recursive case
           return []       

.. python-run::

   permutations_r([1])

This is a common way to mess up the base case.  While it may make
intuitive sense for the function to return ``[1]`` in the trivial case
because we only have one permutation, we must make sure that the
code uses inputs and outputs consistently. Otherwise, the recursive
case will not work.

Make sure that your function works correctly for the base case before 
moving onto the next step. Test it
informally using the Python interpreter on inputs that will
immediately hit the base case and make sure the return value is
consistent with your desired type of output. Paying careful
attention to the input and output types will save you a fair amount of
trouble and debugging time farther down the road. 
       
             
**Step #3: Determine the recursive case(s) for the function.** This step
can be tricky because thinking recursively doesn't
come naturally to many people. We suggest taking the following
approach: if you are writing a function that takes some input
:math:`x`, write a solution that assumes that calls to that
function with a *smaller value* for :math:`x` will "just work".

For example, let's go back to the factorial function:

.. python-run::
   :formatting: separate

   def factorial_r(n):
       '''  Compute n! recursively '''

       if n == 1:
          return 1
       elif n > 1:
          return n * factorial_r(n-1)

After designing our base case, we wrote a recursive case that
assumes that the call to ``factorial_r(n-1)`` will "just work".
If we actually write out the entire sequence of function calls
and the function call stack we can understand *how* this works,
but when starting to write a recursive solution ,
it is better to not go down the rabbit hole of trying 
to trace every recursive call all the way down to the base case.

Instead, we implement the recursive case *under the assumption* that
recursive calls will "just work" as long as the parameters we pass to
the recursive call move us closer to the base case.  This
is certainly true in the case of factorial: for any positive value of
``n``, calling the function with ``n-1`` gets us closer to the base
case of ``n == 1``.

So, what is the recursive case for permutations? Our function
is called with a list of elements we want to generate permutations
on, and our base case is reached whenever that list contains
a single element. So, if the function is called like this::

   permutations_r([1,2,3,4])
   
We can *assume* that the following calls will "just work"::   

   permutations_r([2,3,4])
   permutations_r([1,3,4])
   permutations_r([1,2,4])
   permutations_r([1,2,3])
   
Or, more generally, if the function is called with a list
of size ``n``, we should implement our recursive case
*under the assumption* that recursive calls with a list
of size ``n-1`` will work. Notice how this approach will eventually
get us to the base case of calling the function with a list
of size ``n == 1``.   

Now, remember the example permutations we showed above. We
remarked that the permutations of (1,2,3,4) are simply:

-  All permutations of (2,3,4) with 1 as the first element;
-  All permutations of (1,3,4) with 2 as the first element;
-  All permutations of (1,2,4) with 3 as the first element; plus
-  All permutations of (1,2,3) with 4 as the first element

So, let's implement this logic under the assumption that
the recursive calls (with those smaller lists)
will return the correct permutations. First of all,
we said our function will return a list of permutations,
so let's start there:

.. python-run::
   :formatting: separate

   def permutations_r(p):
       '''
       Compute all the permutations of the values in p.

       Inputs:
         p (list): list of values to permute

       Returns (list of lists): permutations of p
       '''

       if len(p) == 1:
           # Base case
           return [ p ]
       else:
           # Recursive case
           rv = []
           
           # rv will contain the list of permutations
           
           return rv

Then, for each element of ``p``, we want to obtain the permutations
resulting from removing that element.

.. python-run::
   :formatting: separate

   def permutations_r(p):
       '''
       Compute all the permutations of the values in p.

       Inputs:
         p (list): list of values to permute

       Returns (list of lists): permutations of p
       '''

       if len(p) == 1:
           # Base case
           return [ p ]
       else:
           # Recursive case
           rv = []
           
           for x in p:
              p_minus_x = [v for v in p if v != x]
              perms_without_x = permutations_r(p_minus_x)
           
           return rv

``p_minus_x`` is simply a copy of the list ``p`` but with ``x``
removed from it. Next, we make the recursive call with that list.
If ``p`` is ``[1,2,3,4]`` and ``x`` is ``4``, then this recursive
call would return the following list::

     [[1, 2, 3],
      [1, 3, 2],
      [2, 1, 3],
      [2, 3, 1],
      [3, 1, 2],
      [3, 2, 1]]

Remember: avoid the urge to go down the rabbit hole of understanding
exactly what happens in this recursive call! For now, we take the approach
of writing the code under the assumption that the recursive call
will return exactly what we expect (according to how we specified
the inputs and outputs of our function).

However, our function is not yet finished. You should also resist
the urge to try and test it as soon as you've written the recursive call.
We said our function has to return a list of permutations, so we need
to take the permutations returned by the recursive call, add ``x``
to each permutation, and then add it to our ``rv`` list. For example,
in the specific case where ``p`` is ``[1,2,3,4]`` and ``x`` is ``4``,
we want to add the following permutations to ``rv``::

     [[4, 1, 2, 3],
      [4, 1, 3, 2],
      [4, 2, 1, 3],
      [4, 2, 3, 1],
      [4, 3, 1, 2],
      [4, 3, 2, 1]]

So we add a loop that iterates over the permutations returned by the
recursive call.  For each permutation, we construct a new list
containing ``x`` and the values from permutation and add it to the
list we are going to return:

.. python-run::
   :formatting: separate

   def permutations_r(p):
       '''
       Compute all the permutations of the values in p.

       Inputs:
         p (list): list of values to permute

       Returns (list of lists): permutations of p
       '''

       if len(p) == 1:
           # Base case
           return [ p ]
       else:
           # Recursive case
           rv = []
           
           for x in p:
              p_minus_x = [v for v in p if v!=x]
              perms_without_x = permutations_r(p_minus_x)
              for perm in perms_without_x:
                  pl = [x] + perm
                  rv.append(pl)
           return rv
           
At this point, our function is finished:        

.. python-run::

   permutations_r([1])
   permutations_r([1,2,3])
   
.. admonition:: Recursion and Induction

   If you're familiar with inductive proofs, they can also
   provide a good framework to think about recursion. When
   doing an inductive proof, we prove a statement for
   one or more base cases (such as :math:`n=0` and :math:`n=1`)
   and once we've done that, we take the *inductive step*:
   assuming the statement holds for :math:`n`, prove
   it holds for :math:`n+1`.
   
   Thinking recursively is similar to doing an inductive proof:
   once we've implemented the base case, we then implement 
   the recursive case under the assumption that a recursive
   call (with parameters that get us closer to the base
   case) will work.

Like we did for the factorial function, here is a version of the
permutations function that prints out messages explaining what happens
at each recursive call.  We encourage you to play around with it so
you can understand what happens when you make recursive calls.  This
function has several extra parameters: ``n``, which is the desired
number of elements in each permutation, ``verbose``, which controls
the printing of information about the computation, and ``level``,
which is used internally by the function to track the depth of the
recursion for printing purposes.  Notice that the code handles the
fact that there might be more than one element in ``p`` when ``n ==
1``.


.. python-run::
   :formatting: separate

   def permutations(p, n, verbose=False, level=0):
       '''
       Compute all the permutations of length n of the values in p.

       Inputs:
         p (list): list of values to permute
         n (int): desired size of the permutations
         verbose (boolean): indicates whether information about the
           computation should be printed (default: False)
         level (int): depth of the recursion (default: 0)

       Returns (list of lists): permutations of length n of values in p
       '''

       assert len(p) >= n

       if verbose: print(("    " * level) + "permutations({}, {})".format(p, n))
       if n == 1:
           rv = [[x] for x in p]
           if verbose: print(("    " * level) + "result: {}".format(rv))
           return rv
       elif len(p) == 1:
           if verbose: print(("    " * level) + "result: {}".format([p]))
           return [p]
       else:
           rv = []
           for x in p:
               if verbose: print(("    " * level) + "{} with...".format(x))
               rem = [v for v in p if v != x]
               for perms in permutations(rem, n-1, verbose, level+1):
                   rv.append([x] + perms)
           if verbose: print(("    " * level) + "result: {}".format(rv))
           if verbose: print()
           return rv
   
.. python-run::
   
   ps = permutations([1,2,3], 3, verbose=True)


.. todo::

   Show an iterative solution for comparison?

..
   The Towers of Hanoi
   -------------------
   
   If enough time: explain Towers of Hanoi. I have an actual physical
   "Towers of Hanoi" game that makes it easy to visually explain the game;
   I'm not sure the Towers of Hanoi are easy to explain just with code (may
   seem too abstract). If you'd like to borrow the Towers of Hanoi (and I
   am not using it that day) just let me know.
   
   .. code:: python
   
       # Solution to the Towers of Hanoi puzzle.
       #
       # In the Towers of Hanoi, we always have three pegs A, B, C:
       #
       #    |   |   |
       #    |   |   |
       #  __|___|___|__
       #    A   B   C
       #
       # Each of these pegs will take on a specific role:
       # the peg where the rings are (the "source peg"), 
       # the peg where the rings have to be moved (the 
       # "destination peg") and the "extra peg". These
       # roles are not fixed: in each recursive call,
       # the roles of each peg will change.
       #
       # Credit: This solution is inspired by https://gist.github.com/mos3abof/5232156
       
       
       # solve_hanoi_r is the recursive function. It takes the following parameters:
       #
       # N - The number of rings to move
       # pegs - The state of the pegs, represented by a dictionary mapping peg names (e.g., "A", "B", "C")
       #        to a list of rings in that peg (with the first element of the list being the bottom-most ring
       #        and the last element of the list being the top-most ring). Rings are represented as integers
       #        where 1 is the smallest ring and N is the largest.
       # source_peg, destination_peg, extra_peg: The names of the source peg, destination peg, and
       #        the extra peg(must be a peg in the "egs" dictionary)
       #
       # It does not return anything, but it does modify "pegs" in place and it prints
       # out the moves that have to be made.
       def solve_hanoi_r(N, pegs, source_peg, destination_peg, extra_peg):
           # BASE CASE: If N is 1, then we trivially move
           # the ring from the source peg to the destination peg
           # without having to use the extra peg at all:
           if N == 1:
               # Remove top-most ring from source peg
               ring = pegs[source_peg].pop()
               # Place it on destination peg
               pegs[destination_peg].append(ring)        
               print("Move ring {} from {} to {}".format(ring, source_peg, destination_peg))
               print()
               print_pegs(pegs)
               print()        
           else:
               # RECURSIVE CASES:
               #
               # Notice how, in these recursive calls, the roles of the pegs
               # for N-1 will be different than the roles for N.
               #
               # Move N-1 rings from the source peg to the extra peg,
               # using the destination peg as the extra peg.
               solve_hanoi_r(N-1, pegs, source_peg = source_peg,
                                        destination_peg = extra_peg, # i.e., in N-1, we use the current extra peg as the destination peg
                                        extra_peg = destination_peg) # i.e., in N-1, we use the current destination peg as the extra peg
               # Move 1 ring from the source peg to the destination peg
               solve_hanoi_r(1, pegs, source_peg = source_peg,
                                      destination_peg = destination_peg,
                                      extra_peg = extra_peg)
               # Move the previously moved N-1 rings from the extra peg,
               # to the destination peg, using the source peg as the extra peg.
               solve_hanoi_r(N-1, pegs, source_peg = extra_peg,
                                        destination_peg = destination_peg,
                                        extra_peg = source_peg)
       
               
       def print_pegs(pegs):
           for p in sorted(pegs):
               print("{}: {}".format(p, " ".join([str(x) for x in pegs[p]])))
       
               
       # Call solve_hanoi_r with the pegs starting at peg "A" and
       # going to peg "C".
       def solve_hanoi(N):
           pegs = {"A": list(range(N,0,-1)), "B": [], "C": []}
           print_pegs(pegs)
           print()
           solve_hanoi_r(N, pegs, "A", "C", "B")
   
   .. code:: python
   
       solve_hanoi(3)
   
   
   .. parsed-literal::
   
       A: 3 2 1
       B: 
       C: 
       
       Move ring 1 from A to C
       
       A: 3 2
       B: 
       C: 1
       
       Move ring 2 from A to B
       
       A: 3
       B: 2
       C: 1
       
       Move ring 1 from C to B
       
       A: 3
       B: 2 1
       C: 
       
       Move ring 3 from A to C
       
       A: 
       B: 2 1
       C: 3
       
       Move ring 1 from B to A
       
       A: 1
       B: 2
       C: 3
       
       Move ring 2 from B to C
       
       A: 1
       B: 
       C: 3 2
       
       Move ring 1 from A to C
       
       A: 
       B: 
       C: 3 2 1
       
   
   
   .. code:: python
   
       # Solution to the Towers of Hanoi puzzle.
       #
       # "N" is the number of rings, and "left" indicates
       # whether the rings should move left (True) or
       # right (False). We assume the pegs "wrap around"
       # so, if we label the pegs as A, B, and C:
       #
       #    |   |   |
       #    |   |   |
       #  __|___|___|__
       #    A   B   C
       #
       # If a ring is in peg A, and the direction of movement
       # is left, then the ring has to be moved to peg C.
       #
       # The function prints out what rings have to be moved
       # and in what direction, with 1 being the smallest ring
       # and N being the largest one.
       def moves(N, left):
           # BASE CASE: If we have to move zero rings, we're done
           if N == 0:
               return
       
           # RECURSIVE CASE: Move the N-1 rings on top of ring N
           # in the opposite direction. 
           moves(N-1, not left);
       
           # Now that the N-1 rings have been moved, move ring N
           # (note: we're just printing the actions to take, we
           # don't actually "move" anything in a data structure)
           if left:
               print("{} left".format(N))
           else:
               print("{} right".format(N))
       
           # Put the N-1 rings we moved previously back on top
           # of ring N
           moves(N-1, not left)
   
   .. code:: python
   
       moves(3, left=True)
   
   
   .. parsed-literal::
   
       1 left
       2 right
       1 left
       3 left
       1 left
       2 right
       1 left


Binary Search
-------------

Now that we've started to learn how to think recursively, we'll
work through another example to highlight how a recursive
algorithm can have multiple base cases and multiple recursive
cases. This algorithm can
be written very intuitively and elegantly using recursion,
while the equivalent iterative solution is, arguably, not
as intuitive.

Let's say we have the following sorted list of integers:

.. python-run::
   :formatting: separate

   lst = [1, 3, 4, 9, 12, 13, 20, 25, 27, 31, 42, 43, 50, 51]

How can we determine whether a given value exists in the list?  We
could loop through the list (or use the ``in`` operator). This method
is called a *linear* search. This algorithm is very simple, but its
complexity is :math:`O(n)`. For example: what if we want to check
whether 51 is in the list? We have to iterate through the whole list
before we get there.

However, we can exploit the fact that the numbers in the list are
sorted. We can start by accessing the middle element of the list,
and then constrain the rest of our search to either the
first half or the second half of the list. Then, once we
know which half to focus on, we can do the same thing again: choose the
middle element of that sub-list, and focus our search on the first or the 
second half of *that* sub-list. And so on and so forth until we either find the value or run out of elements to check.

For example, let's say we want to find whether 12 is contained in the list.
This list has 14 elements in it, so the index of its middle element
will be 14 divided by 2: 7. The first thing we do is check whether 
that position contains 12 (if it does, then we're done). It, however,
contains 25, which tells us that we can constrain our search 
to the sublist containing all the elements before 25:

.. python-run::
   :formatting: separate

   lst2 = [1, 3, 4, 9, 12, 13, 20]
   
Now, we repeat this process. The middle element of this list is 9. We
now know that we should constrain our search to all the elements that
come after 9 in ``lst2``:

.. python-run::
   :formatting: separate

   lst3 = [12, 13, 20]

Now, the middle element is 13, so we only need to look at the elements before
that element:

.. python-run::
   :formatting: separate

   lst4 = [12]
   
The middle element of this list is 12, the value we're looking for,
so we are done and the algorithm will return that 12 *is* contained in
the list.

Now let's see what happens when we look for a value that *doesn't*
exist in the list: 17. The first steps are similar to the ones above:

.. python-run::
   :formatting: separate
   
   lst = [1, 3, 4, 9, 12, 13, 20, 25, 27, 31, 42, 43, 50, 51]
   # Middle element is 25, we look at elements before it
   lst2 = [1, 3, 4, 9, 12, 13, 20]
   # Middle element is 9, we look at elements after it
   lst3 = [12, 13, 20]
   
Now, the middle element is 13, so now we need to look at the elements
after it:

.. python-run::
   :formatting: separate

   lst4 = [20]
   
At this point, we could realize that the list contains a single element,
and that this element is not the one we're looking for but, to be consistent
with how we've done the other steps, we're going to look at the list of
elements before the middle element, which will simply be the empty list:

.. python-run::
   :formatting: separate

   lst5 = []
   
Notice that this feels like a recursive solution: we keep doing a
search on progressively smaller lists until we reach a trivial case.

This algorithm is called *binary search*: we progressively divide the
search space in half until we find the element we're seeking (or
realize it doesn't exist in the list). Unlike linear search, 
which has a complexity of :math:`O(n)`, the complexity
of binary search is :math:`O(\log_2 n)` because we split the search space 
in half with each step.

Binary search is also an example of an
algorithm with two base cases and two recursive cases. We will follow
the same steps we followed in the permutations example to
flesh out the exact algorithm.

**Step #1: Determine the input(s) and output(s) to the function.**
The input to our function is going to be a list ``lst`` and a
value ``x``. We want to determine whether ``x`` is contained
in ``lst``, so it will be enough to return a boolean value
(``True`` or ``False``). It would not be hard to modify
the algorithm to return the *index* of ``x`` in ``lst``,
but we will stick with returning a boolean value for simplicity.

**Step #2: Determine the base case(s) for the function.** In the examples 
we worked through above, we identified *two* base cases:

#. If ``lst`` is the empty list, then we return ``False``.
#. If the middle element of ``lst`` is ``x``, then we return ``True``.


We can write this in code like this:

.. python-run::
   :formatting: separate

   def binary_search(lst, x):
       '''
       Does x occur in lst?

       Inputs:
         lst (list of ints): sorted list of values
         x (int): value to find

       Returns (boolean): return True if x occurs in lst, and False
         otherwise.
       '''

       if len(lst) == 0:
           return False
       else:
           middle = len(lst)//2
   
           if lst[middle] == x:
               return True
           else:
               # TODO: Recursive cases
               pass


**Step #3: Determine the recursive case(s) for the function.**
If we do not hit one of the base cases, we need to do
a binary search on a sublist of ``lst``. If ``x`` is less than
the middle element of ``lst``, then we search the sublist
containing all the elements to the left of ``lst`` (i.e., ``lst[:middle]``).
If ``x`` is greater than the middle element of ``lst``, then we
search the sublist containing all the elements to the right
of ``lst`` (i.e., ``lst[middle+1:]``).

As with the permutations example, we make the recursive call under
the assumption that it will "just work" as long as we pass values
that get us progressively closer to the base cases (which we do
by passing progressively smaller lists in each recursive call).

Our code with the recursive cases will look like this:

.. python-run::
   :formatting: separate

   def binary_search(lst, x):
       '''
       Does x occur in lst?

       Inputs:
         lst (list of ints): sorted list of values
         x (int): value to find

       Returns (boolean): return True if x occurs in lst, and False
         otherwise.
       '''

       if len(lst) == 0:
           return False
       else:
           middle = len(lst)//2
   
           if lst[middle] == x:
               return True
           elif lst[middle] > x:
               return binary_search(lst[0:middle], x)
           elif lst[middle] < x:
               return binary_search(lst[middle+1:], x)
               
.. admonition:: A common pitfall

   A common pitfall when writing recursive functions is to make
   the recursive call correctly, but then not do anything with the
   return value of that recursive call. A common mistake
   when writing the above code would be to write the recursive
   cases like this::
   
      elif lst[middle] > x:
         binary_search(lst[0:middle], x)
      elif lst[middle] < x:
         binary_search(lst[middle+1:], x)
         
   The recursive calls are correct, but we are not using 
   their return value. In the permutations example,
   we took the permutations returned by the recursive call to
   create more permutations, and then returned those permutations.
   Here, we directly return whatever the recursive call returns.
                  

If we run this function, we can see it behaves as expected:


.. python-run::

   lst = [1, 3, 4, 9, 12, 13, 20, 25, 27, 31, 42, 43, 50, 51]
   binary_search(lst, 12)
   binary_search(lst, 25)   
   binary_search(lst, 9)   
   binary_search(lst, 17)
   binary_search(lst, -10)
   binary_search(lst, 100)
   
Earlier we said that the complexity of binary search is :math:`O(\log_2 n)`,
but that is actually not true of the implementation we have provided
above. The reason is subtle: We slice the list in each recursive
call, and slicing makes a copy of the slice, so we're using 
more space and time than necessary.  These are things we need to be 
mindful of when writing code: no operation comes for free, and even 
seemingly trivial operations have costs that can add up.

In fact, if we use IPython to test the runtime of our algorithm,
we'll see it actually take *longer* than a linear search!

.. code:: python

   In [1]: import random

   In [2]: large_list = list(range(1000000))
   
   In [3]: %timeit large_list.index(random.randint(0,1000000-1))
   100 loops, best of 3: 4.01 ms per loop
   
   In [4]: %timeit binary_search(large_list, random.randint(0,1000000-1))
   100 loops, best of 3: 7.69 ms per loop

We can solve this problem by making sure that we pass the complete
list in each recursive call (remember: this approach will pass a *reference*
to the list, not a copy, so we don't incur the cost of making copies of the list)
and adding two parameters, ``lb`` and ``ub``, that specify the lower and upper
bound of the sublist we will be searching within (``lb`` inclusive, ``ub`` exclusive).
We've also added a ``verbose`` parameter to print messages that can help us
see how the recursion unfolds.

So, our function becomes this:

.. python-run::
   :formatting: separate

   def binary_search_r(lst, x, lb, ub, verbose):
       '''

       Does x occur in lst between the indexes lb (inclusive) and ub
       (exclusive)?

       Inputs:
         lst (list of ints): sorted list of values
         x (int): value to find
         lb (int): lower bound (inclusive)
         ub (int): upper bound (exclusive)
         verbose (boolean): indicates whether information about the
           computation should be printed

       Returns (boolean): return True if x occurs in lst, and False
         otherwise.
       '''

       if verbose:
           print("binary_search_r(lst, {}, {}, {})".format(x, lb, ub))
            
       if (lb >= ub):          
           # out of values to consider in the list
           return False
       else:
           middle = (lb + ub)//2
   
           if verbose: print("    middle = {}".format(middle))
   
           if (lst[middle] == x):
               return True
           elif (lst[middle] > x):
               return binary_search_r(lst, x, lb, middle, verbose)
           elif (lst[middle] < x):
               return binary_search_r(lst, x, middle+1, ub, verbose)
    
Notice how some of the operations have been re-written in terms of ``lb`` and ``ub``.
For example, the first base case now checks whether the lower bound is greater than
or equal to the upper bound (which would be equivalent to searching on an empty
list). As written, this function would require passing ``0`` as the lower bound
and ``len(lst)`` as the upper bound any time we wanted to search through the
entire list. In such cases, we can write a *wrapper* function to make the 
initial call to the function:
    
.. python-run::
   :formatting: separate    
    
   def binary_search_alt(lst, x, verbose = False):
       '''
       Does x occur in lst?

       Inputs:
         lst (list of ints): sorted list of values
         x (int): value to find
         verbose (boolean): indicates whether information about the
           computation should be printed (default: False)

       Returns (boolean): return True if x occurs in lst, and False
         otherwise.
       '''

       return binary_search_r(lst, x, 0, len(lst), verbose)

Let's give the function a try:

.. python-run::

   lst = [1, 3, 4, 9, 12, 13, 20, 25, 27, 31, 42, 43, 50, 51]
   binary_search_alt(lst, 12, verbose=True)
   binary_search_alt(lst, 17, verbose=True)

.. admonition:: A common pitfall

   In the above implementation, the values of ``lst``, ``x``, and
   ``verbose`` are the same in all recursive calls, and we modify only
   one of ``lb`` or ``ub`` in each recursive call. While this may seem
   inefficient, the cost of passing these values as parameters is
   negligible compared to the rest of the algorithm. Resist
   the urge to make parameters like ``lst``, ``x``, and ``verbose`` 
   global variables simply because their values will be the same in all
   the recursive calls.
   
   
   
Now, if we test the performance of this version, we'll see that we do get a notable
running time improvement compared to linear search:


.. code:: python

   In [1]: %timeit large_list.index(random.randint(0,1000000-1))
   100 loops, best of 3: 3.73 ms per loop
   
   In [2]: %timeit binary_search_alt(large_list, random.randint(0,1000000-1))
   100000 loops, best of 3: 5.58 µs per loop

Finally, let's look at the iterative version of binary search:

.. python-run::
   :formatting: separate

   def binary_search_iter(lst, x):
       '''
       Does x occur in lst?

       Inputs:
         lst (list of ints): sorted list of values
         x (int): value to find

       Returns (boolean): return True if x occurs in lst, and False
         otherwise.
       '''

       lb = 0
       ub = len(lst)
   
       while lb < ub:
           middle = (lb + ub)//2
           
           if (lst[middle] == x):
               return True
           elif (lst[middle] > x):
               ub = middle
           elif (lst[middle] < x):
               lb = middle + 1            

       return False
       
We can see that it works as expected:

.. python-run::

   lst = [1, 3, 4, 9, 12, 13, 20, 25, 27, 31, 42, 43, 50, 51]
   binary_search_iter(lst, 12)
   binary_search_iter(lst, 25)   
   binary_search_iter(lst, 9)   
   binary_search_iter(lst, 17)
   binary_search_iter(lst, -10)
   binary_search_iter(lst, 100)       
       
The amount of code is not substantially different from that of the recursive
solution but it is arguably not as intuitive as the recursive solution. Because
binary search is defined recursively, its recursive implementation more closely
mirrors its actual definition. With iteration, we are simply taking the recursive
implementation and shoehorning it into a while loop. In this case, we only
required a single while loop but more complex recursive algorithms cannot
be restated iteratively as easily.   

..
   Merge sort
   ----------
   
   Suppose you have two sorted lists:
   
   .. code:: python
   
       l1 = [0, 1, 5, 6]
       l2 = [2, 3, 4, 9, 10]
   
   It is relatively simple to take those two lists and *merge* them into a
   single sorted list:
   
   .. code:: python
   
       def merge(l1, l2):
           i1 = 0  # Index into l1
           i2 = 0  # Index into l2
           
           merged = []  
           for k in range(len(l1) + len(l2)):
               if i1 == len(l1):
                   # We've processed all the elements in l1,
                   # all that's left is to append the remaining
                   # elements in l2
                   merged.append(l2[i2])
                   i2 += 1
               elif i2 == len(l2):
                   # Same as above, but viceversa
                   merged.append(l1[i1])
                   i1 += 1
               elif l1[i1] < l2[i2]:
                   # l1 has the smaller element, and
                   # thus the next element for the merged list
                   merged.append(l1[i1])
                   i1 += 1
               else:
                   # Same as above, but viceversa
                   # When items are equal, we arbitrarily take
                   # them from l2 (it would work the same if we
                   # took them from l1)
                   merged.append(l2[i2])
                   i2 += 1
           
           return merged
   
   Work through this step by step:
   
   .. code:: python
   
       merge(l1, l2)
   
   
   
   
   .. parsed-literal::
   
       [0, 1, 2, 3, 4, 5, 6, 9, 10]
   
   
   
   Now let's say we wanted to sort an unsorted list:
   
   .. code:: python
   
       l = [5, 1, 6, 0, 10, 3, 2, 9, 4]
   
   Let's split it into two halves:
   
   .. code:: python
   
       l1 = [5, 1, 6, 0]
       l2 = [10, 3, 2, 9, 4]
   
   If we could sort these sublists, we could sort the whole list just by
   merging them together. It turns out there is a very simple and elegant
   recursive algorithm for this called mergesort:
   
   .. code:: python
   
       def mergesort(l):
           if 0 <= len(l) <= 1:
               # BASE CASE: If the list is empty or only
               # has one element, it is already sorted
               return l
           else:
               # RECURSIVE CASE
               middle = len(l) // 2
               
               bottom = mergesort(l[0:middle])
               top = mergesort(l[middle:])
               merged = merge(bottom, top)
               
               return merged
   
   Work through this example step by step:
   
   .. code:: python
   
       mergesort(l)
   
   
   
   
   .. parsed-literal::
   
       [0, 1, 2, 3, 4, 5, 6, 9, 10]
   
   
   
   BSB NOTE: Below is a version of mergesort that uses list indices instead
   of slicing. However, it's actually not much more efficient than the
   slicing version because merge() still has to use an auxiliary array, so
   the space requirements are still :math:`O(n)`. In fact, doing in-place
   mergesort (with less than O(n) auxiliary space) is non-trivial
   (https://en.wikipedia.org/wiki/Merge\_sort#Variants). I've done
   comparisons of both, and the one with list indices is slightly better,
   but by a very small amount (~3%). i.e., the difference is not as stark
   as in binary search (where you go from using :math:`O(n)` space to using
   :math:`O(1)` space).
   
   .. code:: python
   
       def mergesort_alt(l, verbose=False):
           mergesort_r(l, 0, len(l), verbose)
       
       
       # This function performs a mergesort on positions [low, high) of a list.
       # Unlike the previous implementation, this function doesn't return anything
       # because it modifies the list in place.
       def mergesort_r(l, low, high, verbose, prefix=""):
           if verbose:
               print(prefix + "mergesort_r(l, {}, {})".format(low, high))
       
           if high-low <= 1:
               # BASE CASE: The size of the range [low, high) is 0 or 1
               # which means there is nothing to sort in that range
               if verbose:
                   print(prefix + "Nothing to sort")
           else:
               # RECURSIVE CASE
               
               middle = (low + high) // 2
       
               if verbose:
                   print(prefix + "sublist: {}".format(l[low:high]))
                   print(prefix + "middle: l[{}] = {}".format(middle, l[middle]))
                   prefix += "    "
       
               # Sort bottom half
               mergesort_r(l, low,      middle, verbose, prefix)
               # Sort top half
               mergesort_r(l, middle,   high, verbose, prefix)   
               # Merge two halves together
               merge_alt(l, low, high)              
       
               
       # Merges range [low, high) of a list. Note that this is 
       # *not* a general purpose merging function. If the
       # middle element of the range is:
       #
       #   middle = (low + high) // 2
       #
       # This function assumes that there are two sorted ranges:
       # one in [low, middle) and one in [middle, high].
       # This function will also modify the original list
       # (it doesn't return a new list)
       def merge_alt(l, low, high):
           N = high - low
           middle = (low + high) // 2
       
           merged = []
       
           i = low;                    # Bottom half index
           j = middle;                 # Top half index
           for k in range(N):
               if (i == middle):           # Bottom half is finished
                   merged.append(l[j])
                   j += 1
               elif (j == high):           # Top half is finished
                   merged.append(l[i])
                   i += 1
               elif (l[j] < l[i]):         # Bottom half has larger element
                   merged.append(l[j])
                   j += 1
               else:                       # Top half has larger element
                   merged.append(l[i])
                   i += 1
           
           # We copy the merged list into the original range
           for k in range(N):
               l[low+k] = merged[k]
   
   .. code:: python
   
       l = [5, 1, 6, 0, 10, 3, 2, 9, 4]
       mergesort_alt(l, verbose=True)
   
   
   .. parsed-literal::
   
       mergesort_r(l, 0, 9)
       sublist: [5, 1, 6, 0, 10, 3, 2, 9, 4]
       middle: l[4] = 10
           mergesort_r(l, 0, 4)
           sublist: [5, 1, 6, 0]
           middle: l[2] = 6
               mergesort_r(l, 0, 2)
               sublist: [5, 1]
               middle: l[1] = 1
                   mergesort_r(l, 0, 1)
                   Nothing to sort
                   mergesort_r(l, 1, 2)
                   Nothing to sort
               mergesort_r(l, 2, 4)
               sublist: [6, 0]
               middle: l[3] = 0
                   mergesort_r(l, 2, 3)
                   Nothing to sort
                   mergesort_r(l, 3, 4)
                   Nothing to sort
           mergesort_r(l, 4, 9)
           sublist: [10, 3, 2, 9, 4]
           middle: l[6] = 2
               mergesort_r(l, 4, 6)
               sublist: [10, 3]
               middle: l[5] = 3
                   mergesort_r(l, 4, 5)
                   Nothing to sort
                   mergesort_r(l, 5, 6)
                   Nothing to sort
               mergesort_r(l, 6, 9)
               sublist: [2, 9, 4]
               middle: l[7] = 9
                   mergesort_r(l, 6, 7)
                   Nothing to sort
                   mergesort_r(l, 7, 9)
                   sublist: [9, 4]
                   middle: l[8] = 4
                       mergesort_r(l, 7, 8)
                       Nothing to sort
                       mergesort_r(l, 8, 9)
                       Nothing to sort
   
   
   .. code:: python
   
       l
   
   
   
   
   .. parsed-literal::
   
       [0, 1, 2, 3, 4, 5, 6, 9, 10]
   
   
   
   .. code:: python
   
       random_numbers = [random.randint(0,1000000) for x in range(1000)]
   
   .. code:: python
   
       %timeit mergesort(random_numbers)
   
   
   .. parsed-literal::
   
       100 loops, best of 3: 2.49 ms per loop
   
   
   .. code:: python
   
       %timeit mergesort_alt(random_numbers)
   
   
   .. parsed-literal::
   
       100 loops, best of 3: 2.42 ms per loop
   
