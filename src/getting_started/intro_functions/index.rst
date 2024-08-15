.. _chapter-functions:

Introduction to Functions
=========================

Up to this point, we have seen enough programming concepts to express
non-trivial algorithms, such as determining whether a
number is prime or not:

.. python-run::
   :formatting: separate

   encountered_divisor = False
   n = 83
   for i in range(2, n):
       if n % i == 0:
           encountered_divisor = True
           break
           
   if encountered_divisor:
       print(n, "is NOT prime")
   else:
       print(n, "is prime")

The input to that algorithm was a number (stored in variable ``n`` in
the code above) and the result was a simple "yes" or "no" answer, printed
in the final ``if`` statement. 

However, we can run into a couple of issues with this code:

* What if we wanted to re-run that program to test the primality of a different number?
  If we were using the interpreter, we would have to type in all the code again
  (changing the value of ``n`` as we go). If we had saved the code to a file,
  we would have to edit the file manually to change the value of ``n``. 
* What if we wanted to use the *result* of the algorithm in a different
  context? For example, we could be writing a more complex program that,
  at some point, performs a specific action depending on
  whether a number is prime (certain cryptography algorithms, for example,
  need to make this choice). We would have to
  re-write the primality testing code and change the final ``if``.
* What if we needed to use the primality testing code in multiple parts of our
  program? We would have to repeat the above code in multiple places,
  which can be very error-prone. For example, if we decided to update the
  algorithm, we would have to make sure to update every copy of it.
  
*Functions* address these issues. Functions allow
us to name a piece of code and re-use it multiple times with different inputs (in fact, some programming languages
refer to them as *subroutines* or *subprograms*).

This mechanism is called a function because, like a mathematical function, 
functions in Python take some input values,
called the *parameters*, and produce a new value,
called the *return value*:

.. figure:: function.png
   :alt: Function

   Function

We have already *seen* uses of functions in some of our examples, like
the function ``random.randint``, which returns a randomly generated integer:


.. python-run::

   import random
   n = random.randint(0, 1000)
   print("The value of n is", n)

When calling an existing function, you specify parameters in
parentheses, with each parameter separated by a
comma. ``random.randint`` takes two parameters: one to specify a lower
bound and one to specify an upper bound. The code in
``random.randint`` takes the value of those parameters, computes a
random number between them, and *returns* the random
number. In the above example, we assign the returned value to
variable ``n``.

We can also call a function to perform an action rather than to
compute a value.  The ``print`` function, which we have used
extensively, is an example of such a function.

.. python-run::

   print("Hello, world!")
   n = 5
   print("The value of n is", n)
   
The ``print`` function runs code necessary to print input parameters
on the screen.

All Python functions return some value.  Functions
like ``print`` that perform an action rather than compute
a value return the special value ``None``.

As we will explore, functions are an important
*abstraction* mechanism. They allow us to *encapsulate* a piece of code and
then reuse that code, without being concerned with how that piece of code
works (other than knowing its purpose, parameters, and return value). For example,
when we used ``random.randint``, we did not have to worry about the
exact algorithm used to produce a random number. We just incorporated
this functionality into our code, *abstracting* away the internal details
of ``random.randint``.

In this chapter, we will cover the basics of writing our own functions, and
also dig into some of the lower-level aspects of how functions work. As we will
point out then, you can safely skip those low-level details for now, but may want to revisit
them once you're more comfortable with functions, and definitely before we get to
the Functional Programming and Recursion chapters, where we explore more
advanced concepts involving functions.


Anatomy of a function
---------------------

To describe the basic elements of a Python function, we will start
with a very simple function that takes two integers and returns
the product of those two integers:

.. python-run::
   :formatting: separate

   def multiply(a, b):
       """
       Compute the product of two values.

       Args:
           a (numeric): first operand
	   b (numeric): second operand

       Returns (numeric): the product of the inputs
       """

       n = a * b
       return n

Let's break down the above code:

* The ``def`` keyword indicates that we are *def*-ining a function. It
  is followed by the name of the function (``multiply``).
* The name of the function is followed by the names of the *parameters*.
  These names appear in parentheses, with parameters separated by commas, and are followed by a colon. (The parenthesis are required, even if the function has no parameters.)
  The parameters are the *input* to the function. In this case, we are defining
  a function to multiply two numbers, so we must define two parameters
  (the numbers that will be multiplied).  Sometimes we refer to these names as the *formal parameters* 
  of the function to distinguish them from the actual values provided when the function is used.  The line(s) containing keyword ``def``, the function name, the parameters, and the colon are known as the *function header*.
* A docstring and the body of the function follow the colon,
  both indented one level from the function header.
* A *docstring* is a multi-line string (delimited by triple quotes,
  either ``'''`` or ``"""``) that contains at least a brief description of
  the purpose of the function, the expected inputs to the function, and
  the function's return value.  While docstrings are not 
  required by the syntax of the language, it is considered good
  style to include one for *every* non-trivial function that you write.
* The body of the function is a block of code that defines what the
  function will do. Notice that the code operates on the parameters. As
  we’ll see later on, the parameters will take on specific values when
  we actually run the function. At this point, we are just defining
  the function, so none of the code in the body of the function is run just yet;
  it is simply being associated with a function called ``multiply``.
* Notice that the body of the function contains a ``return`` statement. This statement is
  used to specify the return value of the function (in this case, ``n``, a variable
  that contains the product of parameters ``a`` and ``b``). The last line of
  the body of the function is typically a ``return`` statement but, as we'll see
  later on, this statement is not strictly required.

Try typing in the function into the interpreter:

.. python-run::

   def multiply(a, b):
       """
       Compute the product of two values.

       Args:
           a (numeric): first operand
	   b (numeric): second operand

       Returns (numeric): the product of the inputs
       """

       n = a * b
       return n

Once the ``multiply`` function is defined, we can call it
directly from the interpreter. To do so, we just write the name
of the function followed by the values of the parameters in parentheses,
with the parameters separated by commas:

.. python-run::

   multiply(3, 4)
   
This use of ``multiply`` is referred to as a *function call*, and the values passed to the 
function are referred to as either the *actual parameters* or the *arguments*.   
This call will run the code in the
``multiply`` function, initializing ``a`` with the value 3 and ``b`` with the value 4. More
specifically, remember that the body of the function was this code:

.. code:: python

   n = a * b
   return n

When the function is called with parameters 3 and 4, the function effectively executes this code:

.. code:: python

   a = 3
   b = 4
   n = a * b
   return n

And then the Python interpreter prints ``12``, the value returned by the
function called with parameters 3 and 4. 

Later on, we'll see that passing arguments to functions is more 
complicated, but for now, you can think of a function simply initializing formal 
parameters in the function body from the actual parameter values specified in the 
function call.

You can also include function calls in expressions:

.. python-run::

   2 + multiply(3, 4)
    
When Python evaluates the expression, it calls ``multiply`` with actual 
parameters 3 and 4 and uses the return value to compute the value of the 
expression.  In general,
you can use a function call in any place where its return value would
be appropriate. For example, the following code is valid because the ``print`` 
function can take an arbitrary number of 
arguments and both string and integer are acceptable argument types:
   
.. python-run::

   print("2 x 3 =", multiply(2, 3))

Of course, context matters. The following code is not valid because
the function call returns an integer and Python can't add strings and
integers:

.. python-run::

   "2 x 3 = " + multiply(2, 3)

Finally, parameter values can also be expressions, 
as long as the expression yields a value of the
expected type. For example:


.. python-run::

   x = 3
   y = 5
   multiply(x, y)
   multiply(x - 1, y + 1)
   

The actual parameter expressions are evaluated *before* the ``multiply`` function is
called. As a result, the first call to ``multiply`` uses 3 and 5 
(the values of ``x`` and ``y`` respectively) as parameters. The 
second call to ``multiply`` uses ``x - 1``, or 2, and ``y + 1``, or 6, 
as the initial values for ``a`` and ``b``. 

In fact, the parameters to a function can themselves be function
calls:

.. python-run::

   multiply(4, multiply(3, 2))
   
In this case, Python first evaluates the inner call to ``multiply`` (that is, ``multiply(3, 2)``) and,
then uses the call's value (``6``) as the second parameter
to ``multiply``. The outer call essentially becomes ``multiply(4, 6)``.   


.. admonition:: A Common Pitfall

   The distinction between a function that *prints* something and a
   function that *returns* something is important, but often misunderstood. 
   Our ``multiply`` function, for example,
   returns the product of its two arguments.

   Let's look a similar function that prints the result instead:

   .. python-run::
     :formatting: separate
   
     def print_multiply(a, b):
         """
	 Print the product of two values.

	 Args:
             a (numeric): first operand
    	     b (numeric): second operand

         Returns: None
         """

         n = a * b
         print(n)

   
   When we call this function:

   .. python-run::

      print_multiply(5, 2)
    
   It appears to return ``10``.  The Python interpreter displays
   integers returned from a function and integers printed using ``print``
   in the same way (other Python interpreters, like IPython,
   explicitly distinguish between the two). We can see this difference
   if we explicitly assign the return value to a variable and then
   print it:
   
   .. python-run::
   
      rv = multiply(5, 2)
      print("The return value is:", rv)
   
   .. python-run::
      
      rv = print_multiply(5, 2)
      print("The return value is:", rv)
      
   Notice that ``print_multiply`` still printed the value ``10``, but
   the return value of the function is the special value ``None``.

   Additionally, although it is valid to use the
   result of one call to ``multiply`` as an argument to another, it
   is not valid do use a call to ``print_multiply`` in the same way.

   .. python-run::
   
      multiply(5, multiply(2, 3))
   
   .. python-run::
      
      print_multiply(5, print_multiply(2, 3))

   
   In general, if you are writing a function that produces a value
   that you want to use elsewhere, make sure that you *return* that
   value. Printing it is not sufficient.


Encapsulating primality testing
-------------------------------

We can use a function to encapsulate our primality testing code,
allowing us to use it easily and in more places.  Our
function will take an integer as a parameter and return ``True`` if
the integer is prime and ``False`` if it is not.

.. python-run::
   :formatting: separate

   def is_prime(n):
       """
       Determines whether the input is prime.

       Args:
           n (int): value to be checked

       Returns (bool): True if the input is prime and False otherwise
       """

       encountered_divisor = False
       for i in range(2, n):
           if n % i == 0:
               encountered_divisor = True
               break
           
       return not encountered_divisor

Once we type this function into the interpreter, we can run it as many
times as we want.

.. python-run::

   is_prime(4)
   is_prime(17)
   is_prime(81)

This is a big improvement from the previous chapter, where
we either had to type the code in all over again or edit a file to
modify the value of the number we were testing and rerun the code.  

Instead of typing the function into the interpreter, 
you can create a file named ``primes.py``
that contains the above function, and then run the following in the
interpreter:

.. python-run::

   import primes
   
You will be able to call the function from the interpreter like this:

.. python-run::

   primes.is_prime(4)
   primes.is_prime(7)

Similarly, you can use ``import primes`` in another Python file to
get access to the function. In this context, we would refer to
``primes`` as a *module*. Python already includes many built-in
modules that provide access to a large collection of useful
functions.  For example, earlier in the chapter we used
Python's ``random`` module and, more specifically, the ``randint``
function contained in that module.

Before we move on to the next topic, let's fix a bug you might have
noticed in our implementation of ``is_prime``: it does not handle one
as an argument properly:

.. python-run::

   primes.is_prime(1)

We could fix this problem by using a more complex expression in the
return statement:

.. python-run::
   :formatting: separate

   def is_prime(n):
       """
       Determines whether the input is prime.

       Args:
           n (int): value to be checked

       Returns (bool): True if the input is prime and False otherwise 
       """

       encountered_divisor = False
       for i in range(2, n):
           if n % i == 0:
               encountered_divisor = True
               break
           
       return (n != 1) and (not encountered_divisor)

.. python-run::

   is_prime(1)
   is_prime(4)
   is_prime(7)

But as you will see in the next section, there is a better way to
resolve this problem.

Practice Problem
~~~~~~~~~~~~~~~~

**Problem 1** Write a function ``print_categories`` that takes two
integers, a lower bound and an upper bound on a range (inclusive), and
prints each number in the range with an indication of whether the
number is prime or composite (that is, not prime).  Here is a sample
use of this function:

.. code::

   >>> print_categories(2, 10)
   2 prime
   3 prime
   4 composite
   5 prime
   6 composite
   7 prime
   8 composite
   9 composite
   10 composite

Your solution should call ``is_prime``, rather than repeat the
primality testing code.


Return statements
-----------------

The functions we've seen so far have a single return statement at the
end of the function. A return statement can appear anywhere in the
function and can appear multiple times. For example:

.. python-run::
   :formatting: separate
   
   def absolute(x):
       """
       Compute the absolute value of a number.

       Args:
           n (numeric): operand

       Returns (numeric): the magnitude of the input
       """

       if x < 0:
           return -x
       else:
           return x

.. python-run::
   
   absolute(3)
   absolute(-3)

We can use multiple return statements to simplify the return statement
in our second version of the ``is_prime`` function.  Specifically, we
can modify the function to treat one as a special case, immediately
returning ``False`` when the function is called with ``1`` as the
parameter.


.. python-run::
   :formatting: separate
   
   def is_prime(n):
       """
       Determines whether the input is prime.

       Args:
           n (int): value to be checked

       Returns (bool): True if the input is prime and False otherwise
       """

       if n == 1:
           return False   
   
       encountered_divisor = False
       for i in range(2, n):
           if n % i == 0:
               encountered_divisor = True
               break
              
       return not encountered_divisor   
   
In fact, we can tweak the function further to avoid using the
``encountered_divisor`` variable altogether. If we find that ``n`` is divisible
by ``i``, then we can return ``False`` right away. If we make it
through the whole ``for`` loop, then ``n`` must be
prime:

.. python-run::
   :formatting: separate
   
   def is_prime(n):
       """
       Determines whether the input is prime.

       Args:
           n (int): value to be checked

       Returns (bool): True, if the input is prime and False otherwise
       """

       if n == 1:
           return False   
   
       for i in range(2, n):
           if n % i == 0:
               return False
              
       return True   

.. python-run::
   
   is_prime(1)
   is_prime(4)
   is_prime(7)


Python computes the return value and leaves
the function *immediately* upon encountering a ``return`` statement.
For example, when it executes the first call above (``is_prime(1)``),
Python encounters the ``return`` statement 
within the first conditional and exits the function before it reaches the loop.  
In contrast, in the second call (``is_prime(4)``), 
Python enters the loop and encounters the return statement during its first
iteration.  Python reaches the final return statement only 
during the third call (``is_prime(7)``).

.. tip::

   As with ``break`` and ``continue``, every ``return`` statement in a
   loop should be guarded by a conditional statement.  Because Python
   returns from the current function as soon as it encounters a
   ``return`` statement, a loop with an unguarded ``return`` will
   never execute more than one iteration (and possibly, a partial
   iteration at that).


Practice Problem
~~~~~~~~~~~~~~~~

**Problem 2**

Let's return to the problem of writing code to help an instructor
determine a student's grade.  The instructor has decided that a
student will earn a(n):

- A if the student's midterm, final, and hw are all at least 90 
- B if the student's midterm, final, and hw are all at least 80 
- C if the student's midterm, final, and hw are all at least 70 
- B if the student's hw is at least 90, their midterm and final are both at least 50 and their final is at least 20 points higher than their midterm.  Otherwise the student should receive an F.  

In the previous chapter, you wrote code to set a variable to the grade
a student earned given variables with the student's homework average
and their grades on the midterm and final exams.

For this problem, your task is to write a function, ``compute_grade``,
that takes those three values as floats and returns the student's
grade as a string.



Advantages of using functions
-----------------------------

Functions help us organize and abstract code.  
We'll look at simulating *Going to Boston*, a simple
game with dice, to help illustrate this point.  

*Going to Boston* is played with three dice by two or more players who alternate 
turns. When it is a player's turn,
they first roll all three dice and set aside the die with the largest face
value, then roll the remaining two dice and set aside
the largest one, and finally, roll the remaining die.  The sum of
the resulting face values is their score for the round.  The players
keep a running total of their scores until one reaches 500 and wins.

Reusability
~~~~~~~~~~~

Let's think about how to implement the code for a single round.  We
could write code that implements the rules directly:

.. python-run::
    :formatting: separate

    def play_round():
        """
        Play a round of the game Going to Boston using three dice.

        Args: none

        Returns (int): score earned
        """

        num_sides = 6
        score = 0

        # roll 3 dice, choose largest
        die1 = random.randint(1, num_sides)
        die2 = random.randint(1, num_sides)
        die3 = random.randint(1, num_sides)
	largest = max(die1, die2, die3)
        score += largest

        # roll 2 dice, choose largest
        die1 = random.randint(1, num_sides)
        die2 = random.randint(1, num_sides)
	largest = max(die1, die2)
        score += largest

        # roll 1 die, choose largest
        largest = random.randint(1, num_sides)
	score += largest

        return score

This code is not very elegant, but it does the job and we can call it
over and over again to play as many rounds as we want:

.. python-run::

   play_round()
   play_round()
   play_round()

Although this implementation works, it has repeated code, which is a
sign of a poor design.  We should
abstract and separate the repeated work into a
function.  At times, this task will be easy because your implementation will have
a block of code  repeated verbatim.  More commonly, 
you will have several blocks of similar but not identical code.  When faced with
the latter case, think carefully about how to abstract the
task into a function that can be used, with suitable parameters, in
place of original code.

In the function ``play_round``, for example, we have three variants of
code to roll dice and find the largest face value (keep in mind the
largest face value of a single die roll is the value of the single
die).  To abstract this task into a function, we will take the number
of dice as a parameter and replace the calls(s) to ``max`` with a
single call.

.. python-run::
    :formatting: separate   

    def get_largest_roll(num_dice):
        """
        Roll a specified number of dice and return the largest face
        value.
    
        Args:
            num_dice (int): the number of dice to roll

        Returns (int): the largest face value rolled
        """

        num_sides = 6

        # initialize largest with a value smaller than the smallest
        # possible roll.
        largest = 0
        for i in range(num_dice):
            roll = random.randint(1, num_sides)
            largest = max(roll, largest)

        return largest

Given this function, we can replace the similar
blocks of code with functions calls that have appropriate inputs:

.. literalinclude:: boston.py
    :pyobject: play_round

This version is easier to understand and yields a new function,
``get_largest_roll``, that may be useful in other contexts.

As an aside, we chose to implement the rules for playing a round of
Going to Boston with exactly three dice.  We
could have chosen to generalize it by taking the number of
dice as a parameter.  For example:

.. python-run::
    :formatting: separate   

    def play_round_generalized(num_dice):
        """
        Play a round of the game Going to Boston.

        Args:
            num_dice (int): the number of dice to use

        Returns (int): score earned
        """

        score = 0

	# run the loop from num_dice down to one to mimic the
        # orginal code that rolls # three dice, then two, and then
	# finally, just one.
        for nd in range(num_dice, 0, -1):
	    score += get_largest_roll(nd)
        return score

A good rule of thumb is to start with a simple version of a function
and generalize as you find new uses.

Composability
~~~~~~~~~~~~~

In addition to reducing repeated code, we also use functions as building
blocks for more complex pieces of code.  For example, we can use our
``play_round`` function to simulate a two-person version of Going to
Boston.

.. literalinclude:: boston.py
   :pyobject: play_going_to_boston


This function is more complex than a simple call to
``play_round``, so let's look at it carefully.  Notice that we
take the winning score as a parameter instead of hard-coding it
as 500. Next, notice that in the body of the loop, we play a round for
``player2`` only if ``player1`` does not reach the winning score.  
The loop ends when one player reaches the target score; we then print
the winner.

Since both of our implementations of ``play_round`` complete the same
task and have the same interface, we could use either with our
implementation ``play_go_to_boston``.  In fact, it is common to start
with a straightforward algorithm, like our very basic implementation
of ``play_round``, for a task and only come back to replace if it
becomes clear that an algorithm that is more efficient or easier to
test is needed.

In general, we want to design functions that allow the function's user 
to focus on the function's purpose and *interface* (the number 
and types of arguments the function expects and the 
type of the value the function returns), and to ignore the
details of the implementation. In this case,  
we didn't need to understand how rounds are played to design the loop; 
we only needed to know that ``play_round`` does not take any arguments
and returns the score for the round as an integer. 

A word about our design choices: the decision to make the winning score a
parameter seems like a good choice, because it makes our function more
general without adding substantial burden for the user.  
The decision to combine the code for running one game and printing the winner, on
the other hand, has fewer benefits.  Our implementation fulfills the
stated task but yields a function that is not
useful in other contexts.  For example, this function would not be useful
for answering the question of "is there a significant benefit to going
first?"  A better design would separate these tasks into
two functions:

.. python-run::
   :formatting: separate

   def play_one_game(goal):
       """
       Simulate one game of Going to Boston.

       Args:
           goal (int): threshold for a win

       Returns (bool): True if player1 wins and False, if player2 wins.
       """

       player1 = 0
       player2 = 0

       while (player1 < goal) and (player2 < goal):
           player1 += play_round()
           if player1 < goal:
               player2 += play_round()

       return player1 > player2


   def play_going_to_boston(goal):
       """
       Simulate one game of Going to Boston and print the winner.

       Args:
           goal (int): threshold for a win
       
       Returns: None
       """

       if play_one_game(goal):
           print("player1 wins")
       else:
           print("player2 wins")

This design allows us to simulate many games to see if the first
player has an advantage:

.. python-run::
   :formatting: separate

   def simulate_many_games(num_trials, goal):
       """
       Simulate num_trials games of Going to Boston and print the
       average number of wins for player 1.

       Args:
           num_trials (int): number of trial games to play
           goal (int): threshold for a win

       Returns: None
       """

       wins = 0
       for i in range(num_trials):
           if play_one_game(goal):
               wins = wins + 1
       print(wins/num_trials)

    
Simulating 10,000 trials with a goal of 500 shows that there is a big
advantage to going first: ``player1`` wins roughly 60% of the time.

.. python-run::

   simulate_many_games(10000, 500)   
   simulate_many_games(10000, 500)   
   simulate_many_games(10000, 500)   


Testability
~~~~~~~~~~~

Finally, functions make code easier to test. A
piece of code that fulfills a specific purpose (e.g., to determine whether a
number is prime or roll N dice and return the largest face value)
is far easier to test when it is encapsulated inside a
function.

As we saw with primality testing earlier, once our code is
encapsulated as a function, we can test it informally by running the
function by hand with parameters for which we know the correct return
value.  Of course, manually testing functions in the interpreter can
still be cumbersome. The process of testing code can be largely
automated using *unit test frameworks* that allow us to specify
a series of tests, and easily run all of them.

.. _chapter-functions-variable-scope:

Variable scope
--------------

In Python and other programming languages, variables have a
specific *scope*, meaning that they are only valid and can only be
used in a specific part of your code. This concept is especially
relevant for functions because any variables that are
defined within a function have *function scope*, meaning that they are
only valid within that function (i.e., within the *scope* of that
function).
    
Variables that are only valid in a specific scope, such as
the scope of a function, are commonly referred to as *local variables*
(as opposed to *global variables*, which we will discuss later).  A
function's formal parameters are local
variables because they are valid only within the scope of the function.

Calling a function alters the control flow of a program: when
Python reaches a function call, it "jumps" to the function, runs
through the statements in the function, and finally, returns to the point 
in the code where
the function was called.  Let's look more carefully at what happens
during a call to ``play_round``:

.. literalinclude:: boston.py
    :pyobject: play_round

The first statement in ``play_round`` introduces a new variable, named
``score`` and sets its initial value to the result of evaluating a
function call (``get_largest_roll(3)``).  To evaluate this call,
Python will:

- evaluate the argument (``3``),
- create the parameter ``num_dice`` and initialize it to the result of evaluating the argument (3),
- transfer control to the body of ``get_largest_roll``, 
- execute the first two statements, which create new variables named ``num_sides`` and ``largest``, and initialize them to 6 and 0, respectively,
- execute the loop, which itself introduces new variables, named ``i`` and ``roll``, that are updated for each iteration, 
- set the return value of the function call to be the value of ``largest``, 
- discard the variables it created during the function evaluation (e.g., ``num_dice`` and ``num_sides``), and
- transfer control back to the first statement of ``play_round``.

The variables ``num_sides``, ``largest``, ``i``, and ``roll`` are
valid only within ``get_largest_roll``.  We would get an error if we
tried to use one them or the parameter (``num_dice``) outside of
the context of this function.  For example, this code will fail,

.. python-run::

   score = get_largest_roll(3)
   print(largest)

Similarly, the variable ``score`` is visible inside ``play_round``,
but not within ``get_largest_roll.`` Any attempt to use ``score``
inside ``get_largest_roll`` would also fail.

The second and third statements in ``play_round`` also call
``get_largest_roll`` and update the variable ``score``.  Python will go
through exactly the same steps to evaluate the second call, including
creating *fresh* versions of the parameter (``num_dice``) and the rest
of the local variables (``num_sides``, ``largest``, ``i``, and
``roll``), initializing them appropriately, and eventually discarding
them when the function returns.  Finally, it will complete the same process all
over again to evaluate the third call.

In all, three distinct sets of the local variables for
``get_largest_roll`` will be created and discarded over the course of
a single execution of ``play_round``.


Parameters
----------

Understanding how parameters work is an important aspect of learning
how to design and write functions. So far, we have seen some fairly
simple parameters, but, as we'll see in this section, parameters
have several features and nuances that we need
to keep in mind when writing functions.

Call-by-value
~~~~~~~~~~~~~

As discussed above, expressions used as arguments for a function call are
evaluated *before* the function call, and their *values* are
used to initialize fresh copies of the formal parameters.  This type of
parameter passing is known as *call-by-value*.

Let's consider a trivial example to illustrate one impact of this
design.  Here's a function that updates the value of its formal
parameter and three functions that use it:

.. python-run::
   :formatting: separate

   def add_one(x):
       print("  The value of x at the start of add_one is", x)
       x = x + 1
       print("  The value of x at the end of add_one is", x)
       return x

   def f():
       y = 5
       print("The value of y before the the call to add_one is", y)
       z = add_one(y)
       print("The value returned by the call to add_one is", z)
       print("The value of y after the the call to add_one is", y)

   def g():
       y = 5
       print("The value of y before the the call to add_one is", y)
       z = add_one(5)
       print("The value returned by the call to add_one is", z)
       print("The value of y after the the call to add_one is", y)

   def h():
       x = 5
       print("The value of x before the the call to add_one is", x)
       z = add_one(x)
       print("The value returned by the call to add_one is", z)
       print("The value of x after the the call to add_one is", x)

(We omitted docstrings from the functions to save space.)

Here's what happens when we call function ``f``:

.. python-run::
 
    f()

As expected, we do not see any changes to ``y``.  When Python reached the
call to ``add_one`` in ``f``, it evaluated the expression (``y``)
and initialized a fresh copy of ``x``, the formal
parameter of ``add_one``, to the resulting value (``5``).  As the function
executed, the value of that copy of ``x`` was read, updated, and then
read again.  Once ``add_one`` returned to ``f``, the copy of ``x`` was
discarded.  

From the perspective of
the ``add_one`` function, there is no difference between the call in
function ``f`` and the call in function ``g``.

.. python-run::

   g()

We can even reuse the name ``x`` in place of the name ``y``, as seen in
function ``h``, and the values printed by our code will not change:

.. python-run::
   :formatting: separate

   h()

Why? Because the variable ``x`` defined in function ``h`` and the
formal parameter ``x`` in ``add_one`` are *different* variables that
just happen to have the same name.


Practice Problem
~~~~~~~~~~~~~~~~

**Problem 3** Given the following functions:

.. code::

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

What is the result of evaluating this call: ``fun4(6)``?

**Problem 4**  Given the following code:

.. code::

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

What is the result of evaluating ``fun3(6, 4, 2)``?
	

Default parameter values
~~~~~~~~~~~~~~~~~~~~~~~~

Suppose we wanted to write a function that simulates flipping a coin
``n`` times. The function itself would have a single parameter, ``n``,
and would return the number of coin flips that landed on heads.
The implementation of the function needs a ``for`` loop to perform
all of the coin flips and uses ``random.randint`` to randomly produce
either a 0 or a 1 (arbitrarily setting 0 to be heads and 1 to be tails):

.. python-run::
   :formatting: separate
   
   import random
   
   def flip_coins(n):
       """
       Flip a coin n times and report the number that comes up heads.

       Args:
           n (int): number of times to flip the coin

       Returns (int): number of flips that come up heads.  
       """

       num_heads = 0
       
       for i in range(n):
           flip = random.randint(0, 1)
           if flip == 0:
               num_heads = num_heads + 1
       
       return num_heads
       
.. python-run::

   flip_coins(100)
   

As expected, if we flip the coin a large number of times,
the number of flips that come out heads approaches 50%:
   
.. python-run::

   n = 100000  
   heads = flip_coins(n)
   print(heads/n)
       
Now, let's make this function more general. Right now,
it assumes we're flipping a fair coin (i.e., there is an equal
probability of getting heads or tails). If we wanted to simulate a weighted coin
with a different probability of getting heads, we could add an extra
parameter ``prob_heads`` to provide the probability of getting
heads (for a fair coin, this value would be ``0.5``):

.. code:: python

   def flip_coins(n, prob_heads):

Of course, we also have to change the implementation of the
function. We will now use a different function from the ``random``
module: the ``uniform(a,b)`` function.  This function returns a
randomly chosen *float* between ``a`` and ``b``. If we call the function with
parameters ``0.0`` and ``1.0``, we can simply use values less than
``prob_heads`` as indicating that the coin flip resulted in heads, and
values greater than or equal to ``prob_heads`` to indicate tails:

.. python-run::
   :formatting: separate

   def flip_coins(n, prob_heads):
       """
       Flip a weighted coin n times and report the number that come up
       heads.

       Args:
           n (int): number of times to flip the coin
           prob_heads (float): probability that the coin comes up heads

       Returns (int): number of flips that came up heads.
       """

       num_heads = 0
       
       for i in range(n):
           flip = random.uniform(0.0, 1.0)
           if flip < prob_heads:
               num_heads = num_heads + 1
       
       return num_heads

Like before, we can informally validate that the function seems to be working
correctly when we use large values of ``n``:

.. python-run::

   n = 100000
   heads = flip_coins(n, 0.7)
   print(heads/n)
   heads = flip_coins(n, 0.5)
   print(heads/n)
   
       
However, it's likely that we will want to call ``flip_coins`` to
simulate a fair coin most of the time. Fortunately, Python
allows us to specify a *default value* for parameters. To do this, we
write the parameter in the form of an assignment, with the default value
"assigned" to the parameter:

.. python-run::
   :formatting: separate

   def flip_coins(n, prob_heads=0.5):
       """
       Flip a weighted coin n times and report the number that come up
       heads.

       Args:
           n (int): number of times to flip the coin
           prob_heads (float): probability that the coin comes up heads
             (default: 0.5)

       Returns (int): number of flips that came up heads.
       """

       num_heads = 0
       
       for i in range(n):
           flip = random.uniform(0.0, 1.0)
           if flip < prob_heads:
               num_heads = num_heads + 1
       
       return num_heads

We can still call the function with the ``prob_heads`` parameter:

.. python-run::

   flip_coins(100000, 0.7)
   flip_coins(100000, 0.35)
   
But, if we omit the parameter, Python will use ``0.5`` by default:

.. python-run::

   flip_coins(100000)

When you specify a function's parameters, 
those without default values must come first, followed by
those with default values (if there are any). Notice, for example, that the following code fails:

.. python-run::
   :formatting: separate

   def flip_coins(prob_heads=0.5, n):
       """
       Flip a weighted coin n times and report the number that come up
       heads.

       Args:
           prob_heads (float): probability that the coin comes up heads
             (default: 0.5)
           n (int): number of times to flip the coin

       Returns (int): number of flips that came up heads.
       """

       num_heads = 0
       
       for i in range(n):
           flip = random.uniform(0.0, 1.0)
           if flip < prob_heads:
               num_heads = num_heads + 1
       
       return num_heads

Positional and keyword arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So far, whenever we have called a function, we have specified the arguments in that function call in the same order as they appear in the function’s list of parameters (with the ability to omit some of those parameters that have a default value).  These types of arguments are referred to as *positional arguments*,
because how they map to specific parameters depends on their *position*
in the list of arguments. For example:

.. python-run::

   flip_coins(100000, 0.7)

In this case, ``100000`` will be the value for the ``n`` parameter and
``0.7`` will be the value for the ``prob_heads`` parameter.

It is also possible to specify the exact parameter that we are passing
a value by using *keyword arguments*. This type of argument follows
the same syntax as an assignment; for example:

.. python-run::

   flip_coins(n=100000, prob_heads=0.7)

Notice that, because we explicitly provide a mapping from values to parameters,
the position of the arguments no longer matters:

.. python-run::

   flip_coins(prob_heads=0.7, n=100000)
   
Keyword arguments can make a function call easier to read, especially for 
functions that have many parameters. With keyword arguments, we do not need to 
remember the exact position of each parameter.

It is possible to use both positional arguments and keyword arguments,
although in that case the positional arguments must come first.

For example, this call works:

.. python-run::

   flip_coins(100000, prob_heads=0.7)
   
But this call doesn't:

.. python-run::

   flip_coins(prob_heads=0.7, 100000)


Practice Problem
~~~~~~~~~~~~~~~~

**Problem 5**

Test code is designed to help validate the behavior of a piece for
code for a given set of values.  How do we test computations that use
randomness given that the generated random values change each time we
run the computation?  One way to address this problem is to set the
seed used to by the random number generator to compute the sequence of
values it returns.  The seed is set by calling ``random.seed`` with an
integer value.  If ``random.seed`` is called with the value ``None``,
the value of the system clock time at the time of the call is used as
the seed.  This function is typically called once at the start of the
computation.

Here is a simple illustration of how the seed works:

.. python-run::

   random.seed(5000)
   random.uniform(0.0, 1.0)
   random.uniform(0.0, 1.0)
   random.uniform(0.0, 1.0)
   random.seed(5000)
   random.uniform(0.0, 1.0)
   random.uniform(0.0, 1.0)
   random.uniform(0.0, 1.0)

Notice that the second three calls to ``random.uniform`` generate the
exact same values as the first three calls.
   
Rewrite ``flip_coins`` to take a seed as a second optional parameter
and to include a call to ``random.seed``.  Make sure to update the
docstring to include the extra parameter.

Once you have writen your function, write function calls that provide:

- only a value for ``n``,
- a value for ``n`` and a value for ``prob_heads``,
- a value for ``n`` and a value for the seed  parameter, but not ``prob_heads``, and 
- values for all three parameters.

**Problem 6**

A common trick when debugging a complex function is to include a
parameter called ``debug_level`` that is used to specify how much
information the function should print out during the computation.
During regular use, the debug level might be set to zero, while during
active debugging, it might be set higher.

For example, if we were to add a debug level parameter to
``flip_coin`` from ``Problem 5``, we might have:


- ``0`` mean do not print any information about the computation,
- ``1`` mean print the values of the parameters passed to the function, and
- ``2`` mean print the parameters and the values of ``flip`` and ``num_heads`` for coin flip.

For example, the call ``flip_coins(5, 0.5, 5000, debug_level=0)``
would not print any extra information; the call ``flip_coins(5, 0.5, 5000, debug_level=1)``
would print something like:

::

   Debug 1: flip_coins(n=5, prob_heads0.5, seed=5000, debug_level=1)

the call ``flip_coins(5, 0.5, 5000, 1)`` would print something like:

::

   Debug 2: flip_coins(n=5, prob_heads0.5, seed=5000, debug_level=2)
   Debug 2: flip: 0.2330654737797524	num_heads: 1
   Debug 2: flip: 0.7830144643540888	num_heads: 1
   Debug 2: flip: 0.4553051301153339	num_heads: 2
   Debug 2: flip: 0.501694756752729	num_heads: 2
   Debug 2: flip: 0.8394352573499935	num_heads: 2

The return value for all three calls, which is not shown, would be
``2`` as expected from the debugging output.

Update your solution for ``Problem 5`` to take a ``debug_level``
parameter and to use it to decide what information to print
using above description.

The exact output you will see when you run your implementation will
depend on the exact format you use in the necessary print statements
and the version of the ``random`` library that you are using.


Dynamic typing revisited
~~~~~~~~~~~~~~~~~~~~~~~~

Let's return to our ``multiply`` function and revisit the impact of
dynamic typing.  In this case, we've defined a function that is
intended to work with numbers. One of the nice things about Python is
that, as defined, the function will also seamlessly work with floats as well as with the integers that we used in our initial examples:

.. python-run::

   multiply(2.5, 3.0)

It even works when one parameter is an integer and one is a string:

.. python-run::

   multiply("hello ", 3)

but it does not work for all combinations of types.  Because Python
does not verify the types of parameters when the code is loaded,
passing incompatible values can lead to errors at runtime:

.. python-run::

   multiply(3.0, "hello")

This behavior is both an advantage and a disadvantage of
dynamically-typed languages. It is an advantage because we can often
use the same code for different types of inputs.  It is a
disadvantage because we do not learn about these types of errors
until runtime and it is very discouraging to have a long-running
computation fail with a type error.  In a statically-typed
language, we would specify the types of the parameters. Doing so
can make the definition more rigid, but enables us to catch errors
more quickly.


Global variables
----------------

As mentioned earlier, variables defined in a function are known as *local*
variables.  Variables defined outside the context of a function are
known as *global* variables.

Let's say we have an application that needs to compute the maximum of
:math:`N` rolls of a die in some places and the sum of :math:`N`
rolls of a die in other places and that the number of sides in a die
is constant (that is, the value does not change once it is set).  To
avoid defining variables for this constant in multiple places in our
code, we could move the definition out of the functions altogether.

.. code:: python

    NUM_SIDES = 6

    def get_largest_roll(num_dice):
        """
        Roll a specified number of dice and return the largest face
        value.
    
        Args:
            num_dice (int): the number of dice to roll

        Returns (int): the largest face value rolled
        """

        # initialize largest with a value smaller than the smallest
        # possible roll.
        largest = 0
        for i in range(num_dice):
            roll = random.randint(1, NUM_SIDES)
            largest = max(roll, largest)

        return largest

    def sum_throw(num_dice):
        """
	Throw a specified number dice and sum up the resulting rolls.

        Args:
            num_dice (int): the number of dice to roll

        Returns (int): the sum of the face values rolled
	"""
   
        total = 0
        for i in range(num_dice):
            total = total + random.randint(1, NUM_SIDES)

        return largest
   

In this example, the variable ``NUM_SIDES`` is defined and then used
in both functions.  As an aside, it is common to use names with all
capital letters to signal that a variable is a constant (that is, its
value will not change once it is set).

This is an excellent use of a global variable.  We avoid repeated code
(i.e., multiple definitions of the same value) and, since the value
does not change, there is never any confusion about the variable's
current value.

.. common-pitfalls::

   It can be tempting to use global variables as a way to reduce the
   number of parameters that are passed to a function.  If, for
   example, let's say you found a new use for ``get_largest_roll``,
   but with an eight-sided die instead of a six-sided die.  You might
   be tempted to simply update the value of ``NUM_SIDES`` to ``8``
   before calling ``get_largest_roll``:

   .. python-run::

      NUM_SIDES = 8
      get_largest_roll(3)

   Don't. This design is bad.  If you forget to set ``NUM_SIDES`` back
   to ``6``, subsequent calls to ``get_largest_roll`` (especially
   those related to its orginal purpose) might be incorrect in
   a particularly pernicious way: the answer looks fine (e.g., a
   ``3`` is returned) even though the function is no longer modelling
   the desired behavior.

   The appropriate way to extend the use of ``get_largest_roll`` is to
   use an optional parameter to allow the user to provide information
   about the die in some cases and not others:

   .. code:: python

        NUM_SIDES = 6

        def get_largest_roll(num_dice, die_num_sides=NUM_SIDES):
            """
            Roll a specified number of dice and return the largest face
            value.
    
            Args:
                num_dice (int): the number of dice to roll
	        die_num_sides (int): the number of sides on a
		  die (default: 6)

            Returns (int): the largest face value rolled
            """

            # initialize largest with a value smaller than the smallest
            # possible roll.
            largest = 0
            for i in range(num_dice):
                roll = random.randint(1, die_num_sides)
                largest = max(roll, largest)

            return largest

   Using this implementation, the original uses of the function will
   work without change, while new uses can supply the number of sides
   for the die as needed.

   **To avoid writing code that is hard to understand and debug,
   beginning programmers should limit themselves to using global
   variables for constants.** Even more experienced programmers should
   use them with great caution.

When a global variable and a local variable have the same name, the
local variable *shadows* the global variable.  That is, the local variable
takes precedence.  Here is a simple example of this behavior:

.. python-run::

   c = 5

   def add_c(x, c):
       """ Add x and c """
       return x + c

   add_c(10, 20)

When the call to ``add_c`` is made, a fresh local variable ``c`` is
created with the initial value of ``20``.  This local shadows the
global ``c`` and is the variable used in the computation.

Here is a related example that illustrates another aspect of shadowing:

.. python-run::

   c = 5

   def add_10(x):
       """ Add 10 to x """
       c = 10
       return x + c

   add_10(10)
   c

When the call to ``add_10`` reaches the assignment to ``c`` it defines
a *local* variable named ``c``.  It does *not* change the value of the
global variable of the same name; the global ``c`` still has the value
``5`` after the call.

.. technical-details::

   It is possible to override Python's default behavior to update a
   global variable within a function by declaring that it is
   ``global`` *before* is it used in the function.  Here is a trivial
   use of this feature:

   .. python-run::

      c = 5

      def update_c(new_c):
          """ Update the value of the global variable c  """
	  
          global c
	  c = new_c

      c

      update_c(10)

      c

   Notice that in this function, the value of the global variable
   named ``c`` has changed after the call to ``update_c`` because
   Python was informed that it should use the global ``c`` before it
   reached the assignment statement in the function ``update_c``.  As
   a result, it it does not create and set a fresh local variable.
   Instead, it updates the global variable ``c``.

   **This mechanism should be used with great care as indiscriminate
   use of updates to global variables often yields code that is buggy
   and hard to understand.**


.. _call-stack:

The function call stack
-----------------------

Understanding what happens under the hood during a function call helps us 
understand scoping and many other 
nuances of functions. This section delves into some of the
lower-level details of how functions work. You can safely skip for now
it if you like, but you should revisit it once you become
more comfortable with functions.

Programs, including Python programs, 
usually have a location in memory called the *call stack* (usually
referred to as the *stack*) that keeps track of
function calls that are in progress. When a program begins to run, the call 
stack is empty because no functions have been called. Now, let's suppose we have
these three simple functions:


.. python-run::
   :formatting: separate

   def tax(p, rate):
       """
       Compute the tax for a given price.

       Args:
           p (float): price
	   rate (float): tax rate

       Returns (float): the computed tax
       """
       t = p * rate
       return t
    
   def taxed_price(price, rate):
       """
       Compute the price with tax.
       
       Args:
           price (float): price
           rate (float): tax rate

       Returns (float): price with tax
       """

       price = price + tax(price, rate)
       return price
       
   def main():
       """
       Compute and print the price 100 with tax.

       Args: none

       Returns: None
       """

       p = 100
       
       tp = taxed_price(p, 0.10)
       
       print("The taxed price of", p, "is", tp)

``taxed_price`` takes a price (``price``) and a tax rate (``rate``) and
computes the price with tax. ``tax`` takes the same parameters and
computes just the tax. The
``main`` function calls ``taxed_price`` and prints information about
the price with and without taxes.

.. todo::

   Include a note that talks about the convention of using main() functions, etc.

Now, let's say we call the ``main`` function:

.. code:: python

   main()

This call will add an entry to the call stack:

+---------------------------+
| **Function**: ``main``    |
|                           |
| **Parameters**: None      |
|                           |
| **Local Variables**: None |
|                           |
| **Return Value**: None    |
+---------------------------+

This entry, known as a *stack frame*, contains all of the information
about the function call. This diagram shows the state of the function
call at the moment it is called, so we do not yet have any local
variables, nor do we know what the return value will be. However, the
moment we run the statement ``p = 100``, the stack frame will be
modified:

+------------------------+
| **Function**: ``main`` |
|                        |
| **Parameters**: None   |
|                        |
| **Local Variables**:   |
|                        |
| * ``p``: 100           |
|                        |
| **Return Value**: None |
+------------------------+
 
Next, when we reach this line:

.. code:: python

   tp = taxed_price(p, 0.10)
   
A local variable, ``tp`` , will be created, but its value will remain
undefined until ``taxed_price`` returns a value. So, the frame for
``main`` on the call stack will now look like this:

+------------------------+
| **Function**: ``main`` |
|                        |
| **Parameters**: None   |
|                        |
| **Local Variables**:   |
|                        |
| * ``p``: 100           |
| * ``tp``: *undefined*  |
|                        |
| **Return Value**: None |
+------------------------+

Remember that, when we call a function, the code that is currently
running (in this case, the statement ``tp = taxed_price(p, 0.10)``)
is, in a sense, put on hold while the called function runs and returns
a value. Internally, an additional frame is added
to the call stack to reflect that a call to ``taxed_price`` has been made.  
By convention, we draw the new frame stacked below the existing frame:


+-------------------------------+
| **Function**: ``main``        |
|                               |
| **Parameters**: None          |
|                               |
| **Local Variables**:          |
|                               |
| * ``p``: 100                  |
| * ``tp``: *undefined*         |
|                               |
| **Return Value**: None        |
+-------------------------------+
| **Function**: ``taxed_price`` |
|                               |
| **Parameters**:               |
|                               |
| * ``price``: 100              |
| * ``rate``: 0.10              |
|                               |
| **Variables**: None           |
|                               |
| **Return Value**: None        |
+-------------------------------+

Notice that the call stack retains information about ``main``.  The
program needs to remember the state ``main`` was in before the call to
``taxed_price`` (such as the value of its local variables) so that it
can return to that exact same state when ``taxed_price`` returns.

Next, notice that the value of parameter ``price`` is set to 100 and the value of the parameter ``rate`` is set to 0.10.  Why?
Because we called ``taxed_price`` like this:

.. code:: python

   taxed_price(p, 0.10)
 
We can now see why passing a variable as a parameter to a function
doesn't modify that variable. The function receives
the *value* of the variable, not the variable itself. This means that changes made inside the function
won't change the variable itself. In this case, ``taxed_price`` receives
the value of ``p`` (100), but does not modify ``p`` itself.

Now, in ``taxed_price`` we will run the following statement:

.. code:: python

   price = price + tax(price, t)

Once again, we are calling a function. As a result, the execution of ``taxed_price``
is paused while we run the ``tax`` function, which adds another frame to the
call stack: 

+-------------------------------+
| **Function**: ``main``        |
|                               |
| **Parameters**: None          |
|                               |
| **Local Variables**:          |
|                               |
| * ``p``: 100                  |
| * ``tp``: *undefined*         |
|                               |
| **Return Value**: None        |
+-------------------------------+
| **Function**: ``taxed_price`` |
|                               |
| **Parameters**:               |
|                               |
| * ``price``: 100              |
| * ``rate``: 0.10              |
|                               |
| **Variables**: None           |
|                               |
| **Return Value**: None        |
+-------------------------------+
| **Function**: ``tax``         |
|                               |
| **Parameters**:               |
|                               |
| * ``p``: 100                  |
| * ``rate``: 0.10              |
|                               |
| **Variables**: None           |
|                               |
| **Return Value**: None        |
+-------------------------------+

The order of the functions in the stack diagram is important:
notice that ``tax`` appears under ``taxed_price`` (or is *stacked* below ``taxed_price``)
and ``taxed_price`` is below ``main``. This means that ``tax`` was called from ``taxed_price`` which,
in turn, was called from ``main``. In other words, the stack contains information 
about not only each function call, but also the order
in which those calls were made.

Now, let's get back to ``tax``. It has the following two statements:

.. code:: python

   t = p * rate
   return t

The first statement creates a new local variable ``t``, and the second specifies 
the function's return value and terminates the function. So, after 
``return t`` is run, the most recent frame of the call stack will look like this:

+-----------------------+
| **Function**: ``tax`` |
|                       |
| **Parameters**:       |
|                       |
| * ``p``: 100          |
| * ``rate``: 0.10      |
|                       |
| **Variables**:        |
|                       |
| * ``t``: 10           |
|                       |
| **Return Value**: 10  |
+-----------------------+

Once the *calling* function, ``taxed_price``, has retrieved the return value, 
this frame will be *removed* from the
stack. After ``tax`` returns,
and the ``price = price + tax(price, t)`` statement in ``taxed_price``
is run, the stack will look like this:

+-------------------------------+
| **Function**: ``main``        |
|                               |
| **Parameters**: None          |
|                               |
| **Local Variables**:          |
|                               |
| * ``p``: 100                  |
| * ``tp``: *undefined*         |
|                               |
| **Return Value**: None        |
+-------------------------------+
| **Function**: ``taxed_price`` |
|                               |
| **Parameters**:               |
|                               |
| * ``price``: 100              |
| * ``rate``: 0.10              |
|                               |
| **Variables**:                |
|                               |
| * ``price``: 110              |
|                               |
| **Return Value**: None        |
+-------------------------------+

All of the parameters and local variables in a function's
scope *disappear* as soon as the function returns. As we see above, 
the frame for ``tax`` is *gone*, along with all of the information associated with it,
including its local variables. In addition, calling ``tax`` again
will create a *fresh* frame for the call stack: the values of the
parameters and local variables from previous calls will not carry over into new calls.

Similarly, once we execute the statement ``return price`` in the function ``taxed_price``, its return value will be set to ``110``,
and Python will plug that return value into the statement ``tp = taxed_price(p, 0.10)``  in
``main`` (which effectively becomes ``tp = 110``). At this point, the call stack will look like this:

+------------------------+
| **Function**: ``main`` |
|                        |
| **Parameters**: None   |
|                        |
| **Local Variables**:   |
|                        |
| * ``p``: 100           |
| * ``tp``: 110          |
|                        |
| **Return value**: None |
+------------------------+

The ``main`` function will then call ``print``, which create a frame for
``print`` stacked below ``main``'s frame. After
``print`` returns, ``main`` itself doesn't return anything explicitly, which means the
return value of ``main`` will default to ``None``:

.. python-run::

   rv = main()
   print(rv)

Although all of the above may seem like a lot of under-the-hood details, 
there are a few important takeaways:

- Every time we call a function, the values of all of its parameters and local variables
  are stored in a freshly-created stack frame and only exist while the function is running.
  We cannot access variables or parameters from any other stack entry unless
  they were passed as parameters to the current function and, even then, we will
  only get their values.
- When a function returns, the values of its parameters and variables are discarded
  and they do not persist into future function calls. For example, if we called
  ``tax`` again, it would not "remember" that a previous call already set a value
  for its local variable ``t``.
  

Practice Problem Solutions
--------------------------

**Problem 1**:

Here is a solution that assumes that the functions ``is_prime`` and ``print_categories`` are in the same file.

.. code::

    def print_categories(lb, ub):
        """
        Print the primes between lb and ub inclusive.

        Args:
            lb (int): the lower bound of the range
            ub (int): the lower bound of the range

        Returns: None
        """
        for n in range(lb, ub + 1):
            if is_prime(n):
                print(n, "prime")
            else:
                print(n, "composite")


And here is one that assumes that ``is_prime`` and
``print_categories`` are in different files and that ``is_prime`` is
in a file named ``primes.py``.

.. code::

    import primes

    def print_categories(lb, ub):
        """
        Print the primes between lb and ub inclusive.

        Args:
            lb (int): the lower bound of the range
            ub (int): the lower bound of the range

        Returns: None
        """
        for n in range(lb, ub + 1):
            if primes.is_prime(n):
                print(n, "prime")
            else:
                print(n, "composite")



**Problem 2**

Here is a solution that uses a single return statement:

.. literalinclude:: compute_grade_v1.py
   :language: python
   :pyobject: compute_grade

And here is a solution that uses multiple return statements:

.. literalinclude:: compute_grade_v2.py
   :language: python
   :pyobject: compute_grade

Which do you find easier to understand?

Here is some basic test code for this function:

.. literalinclude:: compute_grade_v2.py
   :language: python
   :pyobject: test_compute_grade

This test function must either be in the same file as
``compute_grade`` or the that contains the test code must include an
import statement that imports the function by name.  For example, if
``compute_grade`` is in a file call ``instructor.py``, the inport
statement would have the form:

::

   from instructor import compute_grade


**Problem 3**:

.. python-run::

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

**Problem 4**

.. python-run::

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

    print(f"fun3(6, 4, 2): {fun3(6, 4, 2)}")


**Problem 5**

Here is ``flip_coin`` augmented to take the seed for the random number
generator as an optional parameter:


.. python-run::

   def flip_coins(n, prob_heads=0.5, seed=None):
    """
    Flip a weighted coin n times and report the number that come up
    heads.

    Args:
        n (int): number of times to flip the coin
        prob_heads (float): probability that the coin comes up heads
            (default: 0.5)
        seed (int | None): the seed for the random number generator
            (default: None)


    Returns (int): number of flips that came up heads.
    """

    random.seed(seed)

    num_heads = 0
    
    for i in range(n):
        flip = random.uniform(0.0, 1.0)
        if flip < prob_heads:
            num_heads = num_heads + 1
    
    return num_heads
    
Here are some sample uses of this function:

.. python-run::

   flip_coins(5)
   
   flip_coins(5, prob_heads=0.8)

   flip_coins(5, seed=5000)

   flip_coins(5, prob_heads=0.8, seed=5000)

   flip_coins(5, 0.8, 5000)


Depending on which version of the Python ``random`` library you are
running, you may get different results.


**Problem 6**

Here is the implement of ``flip_coin`` from Problem 5 augmented to take the debug level as parameter:

.. literalinclude:: flip_v2.py
   :language: python
   :pyobject: flip_coins


The escape sequence ``\t``, used in the coin flip print statement, corresponds to a tab character.

..
    Global Variables
    ----------------

    Suppose we had a list of numbers:

    .. python-run::

       nums = [9.9, 10.0, 7.6, 6.6, 12.0, 7.8, 11.0, 7.3, 7.4, 9.2]

    And we wanted to create a new list with the normalized value of these numbers.
    This requires computing the mean (:math:`\mu`) and standard deviation (:math:`\sigma`)
    of the numbers, and then creating a new list where, for each number :math:`x`, the
    normalized value :math:`x'` is the following:

    .. math::

       x' = \frac{x - \mu}{\sigma}

    If we did this in the interpreter, we could do the following:

    .. python-run::

       import math
       mean = sum(nums) / len(nums)
       sqdiffs = [ (x - mean)**2 for x in nums]
       stdev = math.sqrt( sum(sqdiffs) / len(nums) )
       norm = [ (x - mean) / stdev for x in nums]
       mean
       stdev
       norm

    Now, let's say we wanted to take this code and make some functions we could
    reuse later on. We may be tempted to write something like this:

    .. python-run::
       :formatting: separate

       def get_mean():
           return sum(nums) / len(nums)

       def get_stdev():
           mean = get_mean()
           sqdiffs = [ (x - mean)**2 for x in nums]
           stdev = math.sqrt( sum(sqdiffs) / len(nums) )
           return stdev

       def get_normalized():
           return [ (x - mean) / stdev for x in nums]

    And then we could compute the normalized numbers as follows:

    .. python-run::
       :formatting: separate

       nums = [9.9, 10.0, 7.6, 6.6, 12.0, 7.8, 11.0, 7.3, 7.4, 9.2]
       mean = get_mean()
       stdev = get_stdev()
       norm = get_normalized()

       print(norm)

    This will actually work, because ``nums``, ``mean``, and ``stdev`` are *global variables*,
    or variables defined in the *global scope*. Any variable that is defined outside
    a function is a global variable, and thus can be accessed by any function. So,
    when ``get_normalized`` refers to ``mean`` and ``stdev``, it is simply referring
    to the variables that were created outside the function.

    .. todo::

       If we end up discussing modules and packages in any details, we will have to add
       some nuance to this definition.

    However, using global variables, although technically allowed, is typically frowned upon.
    The main reason is that it makes code harder to understand and read. For example,
    all three functions above operate on a list of numbers, but none of the functions have
    any parameters, so we have to read the entire code to realize that they are operating
    on a ``nums`` list defined elsewhere.

    Using global variables also makes code harder to maintain. For example, ``get_normalized``
    requires that the global variables be named specifically ``nums``, ``mean``, and ``stdev``.
    Any other names will prevent ``get_normalized`` from working, breaking our code.

    It is also easy to make silly mistakes that can be hard to debug. For example,
    suppose we implemented ``get_normalized`` like this:

    .. python-run::
       :formatting: separate

       def get_normalized():
           nums = [ (x - mean) / stdev for x in nums]

    It would seem that this function is simply modifying the global ``nums``
    variable (instead of returning a new value).
    However, ``get_normalized`` doesn't actually modify the global ``nums``
    variable; instead, it creates a new *local* variable with the same name
    (which, as we saw earlier, disappears as soon as the function returns).
    This causes this seemingly confusing error message:

    .. python-run::

       get_normalized()

    Basically, we've confused Python because we've written a function
    with a local variable ``nums``, but we use a list comprehension
    that iterates over that local variable ``nums``, but that local
    variable doesn't have a value yet! (hence ``local variable 'nums' referenced before assignment``).

    The main takeaway from all this is actually very simple:

    *Don't use global variables inside functions!*

    Note that using global variables is fine as long as you only
    use them in the global scope. For example, the following code
    has a global variable ``lst``:

    .. python-run::
       :formatting: separate

       lst = ["a", "b", "c"]

       def print_list(l):
           for s in l:
               print(s)

       print_list(lst)

    However, we only use that variable in the global scope. When
    we need to use that variable in a function, we explicitly
    pass it as a parameter to the function.

    Of course, storing data in the global scope and accessing it
    directly from functions, without having to worry about
    parameters, may sound like a clever shortcut, but it will
    usually cause issues in the long run. The use of global variables
    is, in fact, a bit of a contentious issue between programmers and,
    while it's true that more expert programmer can sometimes use
    global variables in legitimately effective ways, beginner programmers
    almost always run into all sorts of problems when using them. So, to be clear:

    **DON'T USE GLOBAL VARIABLES IN YOUR FUNCTIONS!**

    Whenever you implement a function, make sure that all of the inputs to
    a function (i.e., all the information it operates on) is received via its parameters.
    Similarly, the results of a function should be returned via its return value
    (although we'll see next that functions that modify lists operate a bit differently).

    There is, however, one generally accepted exception to this rule:
    it is ok for a function to reference global variables that store *constant* values
    (i.e., values that would never change during the execution of the
    program, like the value of :math:`\pi` or :math:`e`). For example,
    if we write a function to compute the area of a circle, we
    could implement it like this:

    .. python-run::
       :formatting: separate

       PI = 3.141592653589793

       def area(r):
           return PI * r * r

    .. python-run::
       :formatting: separate

       area(2.0)

    So, let's rewrite the ``get_mean``, ``get_stdev`` and
    ``get_normalized`` functions so they don't rely on any global variables:

    .. python-run::
       :formatting: separate

       def get_mean(nums):
           return sum(nums) / len(nums)

       def get_stdev(nums):
           mean = get_mean(nums)
           sqdiffs = [ (x - mean)**2 for x in nums]
           stdev = math.sqrt( sum(sqdiffs) / len(nums) )
           return stdev

       def get_normalized(nums):
           mean = get_mean(nums)
           stdev = get_stdev(nums)
           return [ (x - mean) / stdev for x in nums]

    Notice how they all operate on the ``nums`` list, but this list is
    passed as a parameter to all of them. ``get_normalized`` also
    computes the mean and standard deviation, instead of depending on
    those values being computed in the global scope.

    Now, the code that calls ``get_normalized`` looks like this:

    .. python-run::
       :formatting: separate

       nums = [9.9, 10.0, 7.6, 6.6, 12.0, 7.8, 11.0, 7.3, 7.4, 9.2]
       norm = get_normalized(nums)
       print(norm)

       
