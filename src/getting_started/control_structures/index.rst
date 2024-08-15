.. _chapter-control:

Control Flow Statements
=======================

In the previous chapter, we saw that a program is essentially a collection of 
instructions to a computer. We saw two specific instructions: assignment
statements, which assign a value to a variable, and the ``print`` function, which prints a value on the screen. For example:

.. python-run::
   :formatting: separate

   n = 7
   print("n is", n)
   n = 10
   print("n is now", n)

The "instructions" in a program are called *statements*. 
The above program has four statements: two assignment statements and two 
function call statements (remember that ``print`` is something called a 
"function"; we will explain this construct in more detail in the next 
chapter).  


You might notice that these calls to ``print`` look different than the calls
you have seen thus far. Here, we pass two comma-separated values of different
types to the function. In general, 
you can pass multiple values with different types to ``print``, 
and the function will print each of them separated by spaces. 

.. info-note::

   Notice that we used a different format for showing code above. Instead of
   showing the execution of the program line by line in the interpreter,
   we showed all of the code followed by all of its output. 
   In fact, if you saved the above code in a file named ``statements.py`` 
   and ran ``python statements.py``
   from the terminal, you would see the output shown above. 

   Of course, you can still run the above code in the interpreter. We are 
   showing you the code and the output in a different way because,   
   as we move on to more complex pieces of code, this format will be more 
   readable than the interpreter format (which can get a bit cluttered 
   with the ``>>>`` prompt for every statement). 
   However, we will still be using
   the interpreter format for small pieces of code.   
   

These statements are run in sequence (i.e., one after the other).
Sometimes, though, we want the program to run a statement based
on the outcome of a previous statement, or we may want to repeat a
block of statements multiple times. To support this, most programming
languages include *control flow statements*. In this chapter, we will
focus on three types of control flow statements:

-  **Conditional statements**, also known as "if statements" or "if-then-else statements",
   allow us to run a piece of code only if a given condition
   (expressed as a boolean expression) is true, and optionally allow us to run
   an alternate piece of code if the condition is false. For example,
   given a variable ``x`` containing an integer, we may want to perform
   a different action when ``x`` is positive than when ``x`` is zero or negative 
   (we could express this condition using the boolean expression ``x > 0``).
-  **Sequence-based loops**, also known as "for loops", allow
   us to repeat a piece of code based on a sequence of values. For example,
   given a list of numbers, we may want to determine, for each number, whether
   the number is prime. So, we want to "repeat" the code for testing primality
   for each number in the list.
-  **Condition-based loops**, also known as "while loops", allow
   us to repeat a piece of code based on whether a boolean expression is true.
   For example, when performing a simulation, we may want to continue running
   the simulation until some stopping condition is met.

.. 
   Precise definitions can be found at
   
   https://docs.python.org/3.4/reference/toplevel_components.html,
   https://docs.python.org/3.4/reference/simple_stmts.html
   https://docs.python.org/3.4/reference/compound_stmts.html.

In the next chapter, we will see additional statements that relate to 
*functions* and which also allow us to alter the control flow of our program.

Conditional Statements
----------------------

In the previous chapter, we learned that a boolean expression is an expression
that evaluates to either ``True`` or ``False``:

.. python-run::

    n = 5
    n > 0

A conditional statement allows the program to perform different actions
based on the value of a boolean expression. For example:

.. code:: python

   if n > 0:
       print(n, "is a positive number")

In the above code, the ``print`` statement will be run *only* if ``n``
is greater than zero. 

The conditional statement starts with a special keyword ``if``, which
is part of the syntax of the Python language. The keyword ``if`` is
followed by a boolean expression and a colon.  The next line contains
the first line of the the code to run *if* the boolean expression evaluates to 
``True``.  The spacing before ``print`` is important, and we’ll return to
this detail soon.

Let's try out this code in the interpreter. Make sure you type four spaces before 
the call to ``print``:
  
.. python-run::

   n = 5
   if n > 0:
       print(n, "is a positive number")

The ``if`` statement spans multiple lines and the interpreter won't
run the statement until you've finished writing it. After you've written
the ``if`` line, the interpreter will switch the prompt to ``...`` to
indicate that it is still expecting input as part of a multi-line statement.
After you write the ``print`` line, the interpreter will still show the
``...`` prompt because it isn't sure whether you're going to provide more lines
in the ``if`` statement. Pressing Enter on a blank line tells the interpreter that the code is ready to be run.

.. info-note::

   Remember that the ``...`` prompt is an artifact of the Python interpreter.
   If you were to write this code in a file, you would not include
   the ``...`` characters. In fact, try saving this code in an ``if.py``
   file:
   
   .. code:: python

      n = 5
      if n > 0:
          print(n, "is a positive number")
          
   And running ``python if.py`` from the terminal. The output should be:
   
   .. code-block:: none

      5 is a positive number


Now, try it with a negative value of ``n``:

.. python-run::

   n = -5
   if n > 0:
       print(n, "is a positive number")


Notice that, after running the ``if`` statement, the interpreter didn't produce
any output.  The value of ``n`` is not greater than zero and so, the 
``print`` statement was not executed.


In the above example, the ``if`` statement contained a single statement to 
execute conditionally. However, conditional statements can contain multiple statements to 
execute as well. For example:

.. python-run::
   :formatting: separate

   n = 5
   if n > 0:
       print(n, "is a positive number")
       n = -n        
       print("And now the number is negative:", n)
   
In this case, if the condition is true, then Python will run all of the 
statements under the ``if``. More specifically, the *block* of statements 
under the ``if``,  that is, all the statements at the same level of indentation
(i.e., with the same number of spaces before them),  will be run. For example, 
consider this other version of the code:

.. python-run::
   :formatting: separate

   n = 5
   if n > 0:
       print(n, "is a positive number")
       n = -n        
   print("And now the number is:", n)

And again with a negative number:

.. python-run::
   :formatting: separate

   n = -5
   if n > 0:
       print(n, "is a positive number")
       n = -n        
   print("And now the number is:", n)

Notice that the first ``print`` and the ``n = -n`` statement are run
only if the condition is true, but the second ``print`` is *always*
run. The second ``print`` is not part of the ``if``
statement but occurs *after* the ``if`` statement.

Python's syntax uses indentation to 
delimit blocks of code, typically with four spaces corresponding to one 
level of indentation. As with other syntactical elements, Python is very 
picky about this detail and incorrect indentation will produce
errors. For example, we'll see an error if we do not indent the code in an 
``if statement``:

.. python-run::
   :formatting: separate

   if (n % 2) == 1:
   print(n, "is odd")

Or if we use inconsistent indentation inside the same block of code:

.. python-run::
   :formatting: separate

   if (n % 2) == 1:
       print(n, "is odd")
        print("This concludes the odd branch.")        
        
For this first ``if`` example, we walked you through all the syntactical
elements of the statement but, as you get more comfortable with Python,
it is easier to learn about new elements of the language by getting
a more formal description of their syntax. In the case of the ``if``
statement, a formal description would look like this:

.. parsed-literal::

    **if** *<boolean expression>*:
        *<statements>*

We will use this convention often when describing new statements and other
aspects of Python. Words in **bold** represent keywords that are part of
the language itself, whereas anything delimited with ``<`` and ``>`` means
"substitute this for ..." (i.e., you do not write the ``<`` and ``>`` 
characters themselves). Additionally, remember that indentation matters, so 
the statement or statements that constitute  ``<statements>`` all have the same level of indentation.


So, now we can easily introduce a variant of the ``if`` statement in which we
specify an alternate block of statements to run if the condition is *false*:

.. parsed-literal::

    **if** *<boolean expression>*:
        *<statements>*
    **else**:
        *<statements>*

For example:

.. python-run::
   :formatting: separate

   n = 6
   if (n % 2) == 1:
       print(n, "is odd")
   else:
       print(n, "is even")

When written in this format, the block under the ``if`` is usually called
the *if branch*, and the block under the ``else`` is called the
*else branch*.

In this example, each block has a single statement but, as we saw
earlier, each block can have multiple statements:

.. python-run::
   :formatting: separate

   n = 5
   if (n % 2) == 1:
       print(n, "is odd")
       print("This concludes the odd branch.")
   else:
       print(n, "is even")
       print("This concludes the even branch.")


An ``if`` statement can also have multiple if branches (but only one ``else``, 
which is run only if none of the conditions are met). After the first ``if`` 
branch, subsequent branches start with the keyword ``elif`` (which stands for 
"else if"). For example:

.. parsed-literal::

    **if** *<boolean expression>*:
        *<statements>*
    **elif** *<boolean expression>*:
        *<statements>*
        
    ... 
       
    **else**:
        *<statements>*

For example:

.. python-run::
   :formatting: separate

   n = 17
   if n < 0:
       print(n, "is negative")
   elif n > 0:
       print(n, "is positive")
   else:
       print(n, "is zero")
       

When we have multiple branches, as soon as Python finds a true boolean 
condition, it will evaluate that branch and ignore all others. Python first 
evaluates the ``if`` branch's condition, and moves to subsequent 
``elif`` branches only if no prior condition is true. If no branch is true, Python will run the code in the ``else`` branch. 

An important note: for any ``if`` statement, *at most one branch will be run*, even if the conditions in multiple branches are true. For example:

.. python-run::
   :formatting: separate

   n = 17
   if n < 0:
       print(n, "is negative")
   elif n > 0:
       print(n, "is positive")
   elif n % 2 == 1:
       print(n, "is odd")
   elif n % 2 == 0:
       print(n, "is even")
       
In the above example, there are two conditions that are true when
``n`` is 17: ``n > 0`` and ``n % 2 == 1``. Python, however, will only
run the code for the *first* branch with a true condition (in this
case, ``n > 0``). In general, it is good practice to make the
conditions in an ``if`` statement mutually exclusive (i.e., at most
one of them can be true).


You should also take care to distinguish between an ``if`` statement
with multiple branches and multiple ``if`` statements. For example,
the code below is *not* equivalent to the code above:

.. python-run::
   :formatting: separate
 
   n = 17
   if n < 0:
       print(n, "is negative")
   if n > 0:
       print(n, "is positive")
   if n % 2 == 1:
       print(n, "is odd")
   if n % 2 == 0:
       print(n, "is even")
       
The code above has four *separate* ``if`` statements (often referred
to as *parallel* if statements), while the previous example had a
*single* ``if`` statement with four branches. Since we have four
separate statements, each conditional statement is evaluated and
Python will run the block of code for any true conditional (in this
case, the second and third ``if`` statements).

.. admonition:: A Common Pitfall

    Using parallel ``if`` statements when you need a single ``if``
    statement can lead to bugs that can be very hard to find.  For
    example,

    .. python-run::
       :formatting: separate

       n = 7
       if n > 0:
          print(n, "is positive")
          n = -n
       elif n < 0:
          print(n, "is negative")

    will yield a very different result than:    

    .. python-run::
       :formatting: separate              

       n = 7
       if n > 0:
          print(n, "is positive")
          n = -n

       if n < 0:
          print(n, "is negative")

    Why? In the first example, the first branch of the conditional is
    true and so the second branch is never tested.  In the second
    example, the second conditional is a *separate* statement.  Its
    test *will* be evaluated and since, the value of ``n`` changes
    during the execution of the first conditional the result of that
    test will be ``True`` and its statement will be executed.

.. tip:: Handling multiple conditions


   If you have a bug in code that has a conditional statement with
   multiple conditions, a good first step is to verify that the
   conditions (i.e. the boolean expressions) are mutually exclusive.
   If not, ask whether your application requires overlapping
   conditions.  If not, rewrite the conditions to make them mutually
   exclusive.  If so, check that the order you have chosen for the
   conditions makes sense for the application.  Also, make sure that
   you test each of the possible conditions.  Finally, verify that you
   have not used parallel if statements when a single if statement
   with multiple conditions is required.

   In general, it is a good practice to try out your code with values
   that will trigger the different conditions in a conditional
   statement.


Practice Problems
~~~~~~~~~~~~~~~~~

**Problem 1**

Assume you have an integer variable named ``year`` that holds a a year
represented as a positive integer.  Write a block of code that prints
the year and either ``"is leap year"`` or ``"is not leap year"``.

To gain practice with conditionals, we recommend using conditional
statements instead of logical operators (that is, ``and``, ``or``,
``not``, etc) in your solution.

Before you try to solve this problem, try to come up with some sample
values for year and the expected results.

**Problem 2**

An instructor would like you to write block of code to determine a student's grade based the following rules: the student's grade is a(n):

- A if the student's midterm, final, and hw are all at least 90 
- B if the student's midterm, final, and hw are all at least 80 
- C if the student's midterm, final, and hw are all at least 70 
- B if the student's hw is at least 90, their midterm and final are both at least 50 and their final is at least 20 points higher than their midterm.  Otherwise the student should receive an F.  

Your code should set a variable named ``grade`` to the letter grade
the student earned based on the following three floating point
variables:

- ``hw``, which holds a student's homework average,
- ``midterm``, which holds a student's midterm exam score, and
- ``final``, which holds a student's final exam score.

What would make good sample values for ``hw``, ``midterm``, and ``final``?


``for`` Loops
-------------

*Loops* provide a mechanism for repeating work in a program.
Loops are often used when we need to process a set of values and perform
the same action for each. 
For example, given a list of prices, we may want to compute
the tax on each price as well as keep a running total
of all the taxes paid. To do this task, we will use a ``for`` loop
(in the next section, we will see a different type of loop,
the ``while`` loop, that operates differently).

``for`` loops have the following syntax:

.. parsed-literal::

    **for** *<variable>* in *<sequence>*:
        *<statements>*
        
For example:        
        
.. python-run::
   :formatting: separate

   for p in [10, 25, 5, 70, 10]:
       print("The price is", p)


Notice that the loop repeated the ``print`` statement five times, once for
each value in a sequence of values. In each repetition, or *iteration*, of the 
loop, the variable ``p`` is set to the value of a specific element in the
provided sequence of values, starting with the first and advancing
through the provided sequence. Once all of the elements have been
processed, the loop ends.

The sequence in the above ``for`` loop (``[10, 25, 5, 70, 10]``) is
called a *list*. We will take a deeper look at lists and other types of sequences in 
Chapter :ref:`chapter-lists`, but for now, will 
only use them in ``for`` loops. Lists are values and can be assigned to variables so 
instead of including the list of values directly in the ``for`` loop, 
we could first store it in a variable:

.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]

   for p in prices:
       print("The price is", p)

While in this case, we are specifying the value of ``prices`` directly
in the program, you could imagine these prices being read from a
file, or being scanned at the checkout counter of a store.

Like ``if`` statements, we can include multiple statements in the loop:

.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]

   for p in prices:
       tax = 0.10 * p
       total = p + tax
       print("The price (with tax) is", total)
       
The block of statements contained in a loop is usually called the *body* of the loop.

Our loop example uses a list with five values as the sequence and the
loop iterate five times and prints one line of output for each value.
If we used a list with ten values for the sequence, the loop would
iterate ten times, once per value.  If the list has zero values, which
known as the empty list and is written as ``[]``, then the loop will
iterate zero times.

.. python-run::
   :formatting: separate

   prices = []

   print("Before the loop")
   for p in prices:
       tax = 0.10 * p
       total = p + tax
       print("The price (with tax) is", total)
   print("After the loop")

Notice that the calls to ``print`` before and after the loop, which
are not controlled by the loop, are executed and generate output.  The
call to ``print`` in the body of the loop, in contrast, is never
executed and thus generates no output, because the loop iterates zero
times.

.. tip:: Testing loops

   A good rule of thumb for testing loops: try the loop with a list
   that has zero values, a list that has exactly one value, and a list
   that has many values.


Practice Problems
~~~~~~~~~~~~~~~~~

**Problem 3**

Given a list of integers named ``lst``, compute a variable ``total``
that contains the sum of the absolute values of the elements (that is,
the values) in the list. (e.g. the list ``[-1, 2, 1]`` would set
``total`` to ``4``).  Use the built-in function ``abs`` to compute the
absolute value of a number.  Here is are some example uses of ``abs``:

.. python-run::

   x0 = 5
   abs(x0)
   x1 = -5
   abs(x1)

Before you write a solution, make a list of a few sample test cases
and the corresponding expected results.

**Problem 4**

Given a list of booleans named ``lst``, write code to set a variable
``contains_false`` to ``True`` if the list contains the value
``False`` and to ``False`` otherwise.

Before you write a solution, make a list of a few sample test cases
and the corresponding expected results.


Nested statements
~~~~~~~~~~~~~~~~~

Suppose we wanted to compute the total tax on all the prices.
We could accomplish this task with the following loop:
       
.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]

   total_tax = 0

   for p in prices:
       tax = 0.10 * p
       total_tax = total_tax + tax

   print("The total tax is", total_tax)
   
Notice that we used an additional variable, ``total_tax`` to add up the values
of the tax. This kind of variable is usually referred to as an *accumulator*
variable because it is used to add up (or accumulate) a set of values.

Now, suppose that prices with a value less than 15 are not taxed. This means
that, when computing the total tax, we should only add up the taxes of the
prices that meet the following condition: ``p >= 15``.

So far, the body of an ``if`` statement or a ``for`` loop has been a sequence
of assignments or ``print`` statements (the only two other statements we know).
It is certainly possible, however, for the body of a ``for`` loop to include
``if`` statements or even other ``for`` loops.      

For example:

.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]

   total_tax = 0

   for p in prices:
       if p >= 15:
           tax = 0.10 * p
           total_tax = total_tax + tax
       else:
           print("Skipping price", p)

   print("The total tax is", total_tax)

Notice the two levels of indentation: one level for the body of the loop, and
another for the ``if`` and ``else`` branches. To be clear, we could have
other statements at the same level of indentation as the ``if`` statement:

.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]

   total_tax = 0

   for p in prices:
       print("Processing price", p)
       if p >= 15:
           print("This price is taxable.")
           tax = 0.10 * p
           total_tax = total_tax + tax
       else:
           print("This price is not taxable.")
       print("---")

   print("The total tax is", total_tax)
   

Suppose there were three tax rates (5%, 10%, and 15%) and we wanted to
find the total value of the tax under each tax rate for each of the
prices. If we only had one price to worry about, we could use this
single loop to compute the different taxes:

.. python-run::
   :formatting: separate
   
   p = 10
   tax_rates = [0.05, 0.10, 0.15]
   
   print("Price", p)
   for tr in tax_rates:
       tax = tr * p
       print("Taxed at", tr, "=", tax)

If we had multiple prices to worry about, however, we would use a *nested* 
``for`` loop. We can combine both of the single loop examples by *nesting* the 
loop over the prices inside of the loop over tax rates to find the total tax 
for different tax rates.

.. python-run::
   :formatting: separate
   
   prices = [10, 25, 5, 70, 10]
   tax_rates = [0.05, 0.10, 0.15]
   
   for tr in tax_rates:
       total_tax = 0
       for p in prices:
           if p >= 15:
	       tax = tr * p
               total_tax = total_tax + tax
       print("Taxed at", tr, "the total tax is", total_tax)

Notice that we replaced the fixed tax rate (``0.10``) from the
original loop over the prices with the outer loop variable (``tr``).
Let's walk through this computation. For each iteration of the outer
loop:

* the variable ``total_tax`` is set to zero, then 

* the inner loop iterates through all the prices, checks whether each price (``p``) is taxable, and if so, updates the total tax using the current value of ``tr``, and finally

* the print statement outputs the current tax rate (that is, the value of ``tr``) and the computed total tax.


When you use nested loops, it is very important to think carefully
about where to initialize variables.  As a thought experiment,
consider what would happen if we initialized ``total_tax`` to zero
*before* (rather than in) the body of the outer loop.

.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]
   tax_rates = [0.05, 0.10, 0.15]
   total_tax = 0

   for tr in tax_rates:
       for p in prices:
           if p	 >= 15:
               tax = tr * p
               total_tax = total_tax + tax
       print("Taxed at", tr, "the total tax is", total_tax)

Notice that rather than restarting at zero for each new tax rate, the
total tax from the previous iteration of the outer loop carries
over. As a result, the answers are wrong.

Do keep in mind that the right answer is context dependent.  If
instead of representing different possible tax rates for a given
taxing entity (such as, a city), the rates instead represented the tax
rates for different tax domains, say the city, county, and state.  If
your goal was to compute the total tax paid for all the prices across
all the taxing domains, then it would make sense to initialize
``total`` before the loop nest.  In this use case, you would likely
move the ``print`` statement out of the loops altogether as well.


.. tip:: Nested loops and initialization

   If you have a bug in code that uses nested loops, verify that you
   are initializing *all* the variables used in the loop in the right
   place for your specific application.  



Practice Problems
~~~~~~~~~~~~~~~~~

**Problem 5**

Rewrite your solution to Problem 3 to use a conditional rather than a call to ``abs``.

**Problem 6**




Iterating over ranges of integer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common way to use ``for`` loops is to do something with all the
integers in a given *range*. Let's say we wanted to print out
which numbers between 1 and 10 are odd and even. We could do
it with this simple loop, which also features a nested ``if``
statement:

.. python-run::
   :formatting: separate

   nums = [1,2,3,4,5,6,7,8,9,10]
   for n in nums:
       if (n % 2) == 1:
           print(n, "is odd")
       else:
           print(n, "is even")

What if we wanted to do this computation with the numbers between 1 and 100?
While we could manually write out all those numbers, there is a better
way of doing this task: we can use Python's built-in ``range`` function:

.. python-run::
   :formatting: separate

   for n in range(1, 11):
       if (n % 2) == 1:
           print(n, "is odd")
       else:
           print(n, "is even")

We specify two numbers for ``range``: a lower bound and an upper
bound.  The lower bound is inclusive, but the upper bound is not; i.e., ``range`` will allow
you to iterate through every integer starting at the lower bound and
up to but not including the upper bound.  To change this loop to do
our computation on the numbers between 1 and 100, we would simply
change the upper bound in the call to ``range`` from 11 to 101 (*i.e.*,
``range(1, 101)``).

.. admonition:: A Common Pitfall

   You should think very carefully about the appropriate bounds when
   using ``range``.  In particular, make sure you don't make an 
   "off-by-one" error,
   where you set a bound to be too low or too high by one. This type of
   mistake is very common and can be difficult to track down.


Example: Primality testing
~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's move on to a slightly more involved example: testing whether
a number is prime. While there are very elaborate methods for
testing primality, a naive way of testing whether a number :math:`n`
is prime is to divide that number by every integer between 2 and :math:`n-1`.
If any such integer evenly divides :math:`n`, then :math:`n` is *not* prime.

Assume that we have a variable ``n`` containing the number we are testing.
We could use a ``for`` loop that uses ``range`` to iterate over every integer
between 2 and :math:`n-1`. Inside the loop, we would check whether
each of integer evenly divides ``n`` using the modulus
operator (if the remainder of dividing ``n`` by another integer is zero,
then that number can't be prime). 

Let's take a first stab at this problem
by setting up the loop, but not solving the problem entirely: 

.. python-run::
   :formatting: separate

   n = 81
   print("Testing number", n)
   for i in range(2, n):
       if n % i == 0:
           print(i, "divides", n)
   print("Testing done")

This code simply prints out the divisors of ``n``. Now let's try
it with a prime number:

.. python-run::
   :formatting: separate

   n = 83
   print("Testing number", n)
   for i in range(2, n):
       if n % i == 0:
           print(i, "divides", n)
   print("Testing done")

Since 83 is a prime number and doesn't have any divisors (other than 1 and itself),
the program doesn't print any divisors. So, it looks like our code is on the right
track, even if it doesn't give us a clean "yes" or "no" answer to whether ``n``
is prime or not. 

Solving a simple version of a complex problem is common practice in
programming. Avoid the temptation to solve an entire problem at once,
instead try solving simpler versions of the problem first to make sure
you are on the right track.  For example, the code above reassures us
that we're checking divisibility correctly.

So, how do we modify this code to check whether a number is prime?
Well, if n has even a single divisor, it will not be prime. So, all we
need to do is keep track of whether we have encountered a divisor or
not. While we could do this with an integer (by keeping track of how
many divisors we have encountered, and then checking whether the
number is zero or not), we can get away with using only a boolean
variable, since all we care about is whether we have encountered a
divisor or not. We initialize this variable to ``False``, since we haven’t
encountered any divisors yet at the start of the program.

.. python-run::
   :formatting: separate

   encountered_divisor = False
   n = 83
   for i in range(2, n):
       if n % i == 0:
           encountered_divisor = True
           
   if encountered_divisor:
       print(n, "is NOT prime")
   else:
       print(n, "is prime")

Notice that the value of ``encountered_divisor`` will not change once
it is set to ``True``.  What would happen if we added an ``else``
clause that set the value of ``encounter_divisor`` to ``False`` when
``n`` is not evenly divisible by ``i``?  We'd have a bug: our code
would declare all numbers to be prime.

Finally, as an additional example of nesting one loop inside another,
suppose we want to print whether each integer in a given range is prime or not. 
We could simply nest the primality testing
code we wrote above inside another ``for`` loop that
uses ``range`` to iterate over a sequence of integers, each of which
we will test for primality:

.. python-run::
   :formatting: separate

   for n in range(2,32):
       encountered_divisor = False
       for i in range(2, n):
           if n % i == 0:
               encountered_divisor = True
               
       if encountered_divisor:
           print(n, "is NOT prime")
       else:
           print(n, "is prime")


The ``break`` statement
~~~~~~~~~~~~~~~~~~~~~~~

The primality testing algorithm we just saw is a correct algorithm:
for all values of ``n`` (where :math:`n \geqslant 1`), the algorithm
will correctly determine whether ``n`` is prime or not. However,
it is nonetheless a *terrible* algorithm.

Why? Suppose you wanted to test whether :math:`2^{61}` is prime. It is
clearly not prime (it is divisible by 2), but the algorithm we
presented would nonetheless waste a lot of time iterating over all
numbers from 2 to :math:`2^{61}`, even though we would know ``n``
isn't prime the moment we divided it by 2.  To make the cost more
concrete, if we can perform 15,000 iterations of the loop in 1
microsecond, then determining whether :math:`2^{61}` is prime using
the code above would take nearly five years.

We need to tweak our algorithm so that we can "bail out" of the
``for`` loop as soon as we've found our answer.  We can use a
``break`` statement, which immediately exits the loop, to do this:

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

Notice how all we had to do was add a single ``break`` statement in
the case when we find a divisor.  Making this simple change reduces
the time to determine that :math:`2^{61}` is not prime to under a
microsecond.

Even so, this algorithm is *still* not particularly great. For example, :math:`2^{61}-1`
happens to be prime and, if we used the above algorithm to test this number,
we would still end up performing :math:`2^{61}-1` divisions (about two quintillions, or :math:`2\cdot 10^{18}`). 

So, adding the ``break`` statement only allowed us to optimize certain cases
(which might be fine if we expect to run our algorithm only with small integers).

Don't forget that, as we discussed in Chapter :ref:`chapter-introduction`, 
computational thinking includes thinking about the *complexity* of 
computational solutions. This small example highlights that you 
shouldn't settle for an algorithm simply because it produces the correct 
answer. Instead, you should also ask yourself whether the algorithm
is sufficiently efficient for your purposes.

Sometimes, this process is as simple as asking yourself
how your algorithm will perform in a couple representative cases. For example, 
the performance of this algorithm with a composite (not prime) number is 
probably fine, but the performance
with very large prime numbers will be very bad. Other times, more elaborate
analysis is required. We will be revisiting the notion of complexity several
more times throughout this book.

Before we move on, let's change our nested loop example to use
``break`` and see what happens:

.. python-run::
   :formatting: separate

   for n in range(2,32):
       encountered_divisor = False
       for i in range(2, n):
           if n % i == 0:
               encountered_divisor = True
	       print("Breaking:", i, "evenly divides", n)
	       break

       if encountered_divisor:
           print(n, "is NOT prime")
       else:
           print(n, "is prime")

Upon encountering a ``break``, Python exits the innermost enclosing
loop. We added a ``print`` statement to highlight this behavior.  As
you can see from the output, upon finding a value of ``i`` that evenly
divides the current value of ``n``, Python prints a message with the
values of ``i`` and ``n`` and moves on to the conditional that follows
the inner loop.

Keep in mind that ``break`` statements are always used in a loop
guarded by a conditional statement.  A loop with an unguarded
``break`` statement will execute at most once.  This loop, for
example,

.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]

   for p in prices:
       print("The value of p is:", p)
       break
     		
executes outputs exactly one line.  If list of prices happens to be
empty, then the loop would not generate any output, which explains why
we wrote that a loop with an unguarded break would execute "at most"
once.


Practice Problems
~~~~~~~~~~~~~~~~~

**Problem 6**

Rewrite your solution to Problem 4 to stop the loop looking at values
once you find the first ``False`` in the list.


``continue`` statement
~~~~~~~~~~~~~~~~~~~~~~

Python will immediately exit a loop when it encounters a ``break``
statement.  Sometimes, you just want to stop the current iteration and
move on to the next one.  To illustrate this concept, we will rewrite
an earlier example using ``continue``:

.. python-run::
   :formatting: separate

   prices = [10, 25, 5, 70, 10]

   total_tax = 0

   for p in prices:
       if p < 15:
           print("Skipping price", p)
	   continue
       tax = 0.10 * p
       total_tax = total_tax + tax

   print("The total tax is", total_tax)

In this version, we flipped the test to be ``p < 15`` (rather than ``p
>= 15``), added a use of ``continue`` after the call to ``print`` in the
conditional, and reduced the indentation for the rest of the loop
body.

While ``continue`` should be used sparingly as it can lead to
confusing code, it can help improve readability when you have a
complex deeply-nested piece of code that needs to be executed in some
situations and not others.  Writing this code:

.. parsed-literal::
   
   for <variable> in <sequence>:
       if not <simple test>:
           <complex, deeply nested code>

this way:

.. parsed-literal::

   for <variable> in <sequence>:
       if <simple test>:
           continue
       <complex, deeply nested code>
	   
may yield code that is easier to understand.  And so, while our
example above is correct, we would not normally choose to write code
that simple using ``continue``.

As with ``break``, it does not make sense to use ``continue`` without
a corresponding conditional to guard its execution as the code
following an unguarded ``continue`` would never be executed.


``while`` loops
---------------

``while`` loops are a more general type of loop that, instead of repeating an action *for* each 
element in a sequence, will repeat an action *while* a condition is true. 
The condition is expressed using a boolean expression, which allows us
to write much more complex loops than ``for`` loops.

The syntax for ``while`` loops is the following:

.. parsed-literal::

    **while** *<boolean expression>*:
        *<statements>*

Python starts executing a ``while`` loop by evaluating the boolean expression 
and, if it is true, running the block of statements (otherwise, the ``while`` 
loop is skipped entirely).
After the statements are run, the boolean expression is evaluated *again*, and
if it remains true, the statements are run again. This process is repeated 
until the boolean expression becomes false.        
        
For example, this ``while`` loop will add up all of the integers between 1 and ``N``:      

.. python-run::
   :formatting: separate

   N = 10
   i = 1
   sum = 0
   
   while i <= N:
       sum = sum + i
       i = i + 1
       
   print(sum)

We use a ``sum`` variable to store the sum of all the integers, and initialize
it to 0. Then, we use a variable ``i`` to represent the integer we are adding
to the sum. We initialize it to one and, in each iteration of the loop, we add
``i`` to the sum, and increment ``i`` by one. As long as ``i`` is less than ``N``,
the loop will keep adding ``i`` to ``sum``. 

Unlike a ``for`` loop, a ``while`` loop does not require a
sequence of values. Instead, we *must* keep track of and update 
the integer we add in each iteration of the loop 
(stored in variable ``i``). 

This difference is often the source of a common programming
error: forgetting to include code to increment ``i`` (that is, the
statement: ``i = i + 1``). Without this statement, the loop
becomes an *infinite loop*: the``while`` condition (``i <= N``) 
will never become false because the value of
``i`` will always be one (and thus will
never become greater than ``N``). When this happens, your program (or
the Python interpreter) will appear stuck. In most computer
environments, you can force your program to exit by pressing the
"Control" key and the "C" key (known as "Control-C") at the same time.
You may have to type "Control-C" a few times to get Python's attention.

In fact, precisely because of this issue, the above piece of code should be
implemented using a ``for`` loop, which is less error prone:

.. python-run::
   :formatting: separate

   N = 10
   sum = 0
   
   for i in range(N+1):
       sum = sum + i
       
   print(sum)
       
Notice that we cannot possibly fall into an infinite loop with this 
implementation, because the ``for`` loop
will *only* iterate over the specified range of values.

So when should we use a ``for`` loop instead of a ``while`` loop?
As a rule of thumb, any time you need to iterate over a sequence of
values, using a ``for`` loop is typically the best option. 
Although a ``while`` loop can get the job done, it
can be more error-prone.

There are, however, certain algorithms where the loop cannot naturally be
stated as iterating over a sequence of values, so we need the more
general mechanism provided by a boolean expression. We will
see one such example in the next section.


Practice Problems
~~~~~~~~~~~~~~~~~

**Problem 7**

Using only arithmetic and relational operators, conditional
statements, and a while loop: determine the nearest power of 2 that is
greater than or equal to a value ``N``.  You may assume that ``N >
0``.

What would make good test cases for this computation?

**Problem 8**

Using only arithmetic and relational operators, conditional
statements, and a while loop: determine the nearest power of 2 that is
less than or equal to a value ``N``.  You may assume that ``N > 0``.

What would make good test cases for this computation?


Putting it all together
-----------------------

In this section we are going to work through a slightly longer example
that combines conditionals and loops and involves non-trivial logic.

A few years ago Gil Kalai posed a question on his blog `Combinatorics
and more
<https://gilkalai.wordpress.com/2017/09/07/tyi-30-expected-number-of-dice-throws/>`__:


   You throw a dice until you get 6. What is the expected number of
   throws (including the throw giving 6) conditioned on the event that
   all throws gave even numbers.

The answer, somewhat paradoxically, is 1.5.  As noted by `Dan Jacob
Wallace
<https://gilkalai.wordpress.com/2017/09/08/elchanan-mossels-amazing-dice-paradox-answers-to-tyi-30/>`__,
the question can be answered using some probability theory and
pre-calculus, but it can also be answered by simulating a simple game
many times and averaging the number of throws per game.

In the game, we will roll one fair six-sided die over and over again
and count the number of rolls.  Since the problem is conditioned on
all the throws being even numbers, we will stop a given game and
declare it to be invalid as soon as we roll an odd number.  For valid
games, we will keep rolling the die until we hit a six.

Before we can translate this informal description into code, we need
to find a way to simulate rolling a die.  We can use a function,
``randint`` from Python's built-in ``random`` library for this
purpose.  Given a lower bound and an upper bound, the function chooses
a value uniformly at random between the lower bound and upper bound
inclusive (that is, including both end points).  Since we are working
with a six-sided die, we will call ``random.randint(1, 6)`` repeatedly
to get a randomly-chosen stream of values that range between ``1`` and
``6`` inclusive.

.. note::

   ``random.randint`` is a *function*, which we will be discussing in
   more detail in the next chapter. For now, all you need to so is that,
   like the ``print`` function, this function will
   perform a task for us and, in this case, it will be choosing a
   number randomly between ``1`` and ``6``. In chapter :ref:`chapter-organization-basics`
   we will also discuss Python's built-in libraries, like ``random``
   in more detail.

To simulate the game, we will need to roll the die over and over again
until one of two conditions is met: either (1) a six is rolled, which
ends the (valid) game or (2) an odd number is rolled, which signals
that the game is invalid and should end.  ``while`` loops are designed for
exactly this type of computation: we want to execute a piece of code
repeatedly while some conditions holds.  Here's one--quite direct--way
to translate this description into code:

.. code:: python

   # Simulate a new game
   is_valid_game = True
   # first roll
   roll = random.randint(1, 6)
   game_num_rolls = 1
   while roll != 6:
       if roll % 2 == 1:
           # stop: hit an odd number making the game invalid 
	   is_valid_game = False
	   break
       # subsequent rolls
       roll = random.randint(1, 6)
       game_num_rolls = game_num_rolls + 1

At the end of the game, the variable ``game_num_rolls`` will hold the
number of times the die was thrown in the game and the variable
``is_valid_game`` will tell us whether the game was valid.

Here is another less direct, but easier-to-read version:

.. code:: python

   # first roll
   roll = random.randint(1, 6)
   game_num_rolls = 1
   while roll == 2 or roll == 4:
       # subsequent rolls
       roll = random.randint(1, 6)
       game_num_rolls = game_num_rolls + 1
   is_valid_game = (roll == 6)

In this version, we keep rolling the die until we hit something other
than a ``2`` or a ``4`` (i.e., a ``1``, ``3``, ``5``, or ``6``). We
mark the game as valid only if the last roll, the one that caused the
game to stop, was a ``6``.

These two versions illustrate a common phenomenon: there is often more
than one way to implement a task and thinking about it in a slightly
different way may yield simpler code.

Let's move on to simulating our game many times and computing the
answer.  We can run multiple games or trials by wrapping a for-loop
around the code for simulating a game.  Our goal is to compute the
average number of rolls per valid game.  To do so, we will track the
number of valid games using the variable ``num_valid_games`` and the
total number of rolls made in *valid* games using the variable
``total_rolls_valid_games``.

Here's code that for the full task:

.. code:: python

   num_trials = 1000
   num_valid_games = 0
   total_rolls_valid_games = 0
   
   for _ in range(num_trials):
       # run a new game
       # first roll
       roll = random.randint(1, 6)
       game_num_rolls = 1
       while roll == 2 or roll == 4:
           # subsequent rolls
          roll = random.randint(1, 6)
          game_num_rolls = game_num_rolls + 1
       if roll == 6:
           # the game was valid
	   num_valid_games = num_valid_games + 1
	   total_rolls_valid_games = total_rolls_valid_games + game_num_rolls
	   
   if num_valid_games > 0:	   
       ans = total_rolls_valid_games/num_valid_games
       print("Average number of rolls in valid games:", ans)
   else:
       print("No valid games.  Try again.")


The value of the loop variable for the outer ``for`` loop is not needed in the
computation and so, we followed Python convention and named it ``_``
(underscore).

Note that we dropped the name ``is_valid_game`` and simply used the
expression ``roll == 6`` as the test for a conditional that ensures
that ``num_valid_games`` and ``total_rolls_valid_games`` are updated
only for valid games.

Finally, let's review our decisions about where to initialize the
variables used in the computation. The variables ``num_valid_games``
and ``total_rolls_valid_games`` are initialized before the outer loop
because they are used to accumulate values across the whole
computation.  In contrast, ``roll`` and ``game_num_rolls`` are
re-initialized for every iteration of the outer loop, because they
need to be reset to their initial values for each new game.


	   
Practice Problem Solutions
--------------------------

**Problem 1**:

Here are some sample values for ``year`` and the expected output::

    2024 is a leap year
    2000 is a leap year
    1900 is not a leap year
    2027 is not a leap year

Here is one approach to using conditional statements and relational
operators, but not logical ``and`` or logical ``or`` to determine
whether a year ``year`` with a positive integer represents a leap
year:

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 16-24

Here is an alternative way to write this code:

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 39-47

And here is a **incorrect** approach:

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 60-69

This code produces the right answer for three of the four sample
years.  Which years will be tagged correctly and which year will be
tagged incorrectly?  Why?


**Problem 2**

Here are some possible test cases as the expected value for ``grade``:

.. list-table:: Sample test cases
   :widths: 50 50 50 20
   :header-rows: 1

   * - Midterm
     - Final
     - Homework
     - Grade
   * - 90.0
     - 90.0
     - 92.0
     - A
   * - 80.0
     - 85.5
     - 80.0
     - B
   * - 70.0
     - 70.0
     - 73.5
     - C
   * - 50.0
     - 70.0
     - 90.0
     - B
   * - 70.0
     - 50.0
     - 90.0
     - F
   * - 50.0
     - 70.0
     - 85.0
     - F

Here is a block of code that sets the variable ``grade`` to the grade
a student earned using their homework (``hw``), final (``final``), and
midterm (``midterm``) scores:

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 106-115



**Problem 3**

.. list-table:: Sample test cases
   :widths: 50 20
   :header-rows: 1

   * - ``lst``
     - ``total``
   * - ``[]``
     - 0
   * - ``[5]``
     - 5
   * - ``[-5]``
     - 5
   * - ``[10, -10, 10, -10, 3, 0]``
     - 43

Here is a block of code that computes the sum of the absolute values in ``lst``:

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 144-147

**Problem 4**

Here are some sample test cases:

.. list-table:: Sample test cases
   :widths: 50 20
   :header-rows: 1

   * - ``lst``
     - ``total``
   * - ``[]``
     - ``False``
   * - ``[True]``
     - ``False``
   * - ``[False]``
     - ``True``
   * - ``[True, True, True, True, False]``
     - ``True``
   * - ``[False True, True, True, True, True]``
     - ``True``
   * - ``[True, False, False, True, False]``
     - ``True``
   * - ``[True, True, True, True]``
     - ``False``

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 197-202

Notice that this solution looks at every value in the list even though
we know the value of ``result`` won't change once it is set to
``True``.  We'll see a better way to write this code in Exercise 6.

**Problem 5**

Here is a version of the code that computes the sum of the absolute
values in a list using a conditional rather than a call to ``abs``.

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 161-166

	   
**Problem 6**

This code uses ``break`` to stop the loop upon finding the first
instance of ``False`` in the list.

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 235-240

**Problem 7**

Here are some sample tests:

.. list-table:: Sample test cases
   :widths: 20 20
   :header-rows: 1

   * - Value of ``N``
     - Expected value for ``nearest``
   * - 1
     - 1
   * - 2
     - 2
   * - 5
     - 8
   

And here is a solution:

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 278-280



**Problem 8**

Here are some test cases:

.. list-table:: Sample test cases
   :widths: 20 20
   :header-rows: 1

   * - Value of ``N``
     - Expected value for ``nearest``
   * - 1
     - 1
   * - 2
     - 2
   * - 23
     - 16



And here is a solution:

.. literalinclude:: practice_problem_solutions.py
   :language: python
   :lines: 296-298
