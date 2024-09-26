.. _chapter-exceptions:

Understanding Errors and Catching Exceptions
============================================

When Python detects something wrong in your code, it will *raise* an
*exception* to indicate that an error condition has occurred and it is
severe enough that Python can't continue running the rest of your
code.

A very simple example of an exception occurs when we try to divide a
number by zero:

.. code:: python

   >>> x = 42 / 0

Trying to run the above code will result in an error like this:

::

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

Let's start with the last line: it tells us the name of the exception
(``ZeroDivisionError``) and a description of why the exception was
raised (``division by zero``).

The error message contains a *stack trace* or a synopsis of the state of
the call stack when the error is detected.  

Specifically, in this example, the first two lines constitute the
stack trace.  Because we directly typed ``x = 42 / 0`` into the
interpreter, these lines don't provide a lot of information (it is
immediately apparent that the error originated in the code we just
typed).

The stack trace is much more useful when an exception is raised inside
a function, as it will tell us the exact line inside that function
where the exception was raised. Not just that, it will provide us with
the complete sequence of function calls that led to the exception.

For example, suppose we wanted to write a simple program that prints
the result of dividing an integer N by all the positive integers less
than N.

.. code:: python

   def divide(a, b):
       """ divide a by b """
       return a / b
    
   def print_divisions(N):
       """ Print result of dividing N by integers less than N. """
       for i in range(N):
           d = divide(N, i)
           print(f"{N} / {i} = {d}")

If we store this code in a file named ``exc.py``, import it into
python, and then call the ``print_divisions`` function, we'll see
something like this::

   >>> import exc
   >>> exc.print_divisions(12)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "exc.py", line 8, in print_divisions
       d = divide(N, i)
     File "exc.py", line 3, in divide
       return a / b
   ZeroDivisionError: division by zero

This stack trace is much more informative. In particular, it tells us
than an exception happened after the following sequence of events:

* Python ran ``exc.print_divisions(12)`` in the interpreter (shown in the stack trace as as ``File "<stdin>", line 1,  in <module>``).
* During the call to ``print_divisions``, Python ran the line
  ``d = divide(N, i)``, located in line 8 in the file ``exc.py``.
* During the call to ``divide``, Python ran the line ``return a / b``,
  located in line 3 of ``exc.py``. This last entry in the stack
  trace produced a ``ZeroDivisionError`` exception.

Notice that this trace is simply a printed version of the function
call stack, which we covered in section :ref:`call-stack` of the
chapter that introduced functions.

There is clearly something wrong in our code, and the exception's
stack trace can be very useful to figure out exactly what is wrong.
Frequently there is a difference between the line that raises the
exception, and the code where the error actually originates. For
example, in this case, they are not the same! While it is true that
the ``a / b`` statement is the point at which the division by zero
occurs, there is actually nothing wrong with that particular line or
the ``divide`` function itself.  As a result, we turn our attention to
the next entry in the call stack::

    File "exc.py", line 8, in print_divisions
       d = divide(N, i)

This line contains a hint at the source of the problem: ``i`` must
have taken on the value ``0`` at some point to have triggered the
``ZeroDivisionError`` error.  Where does the ``i`` get its value?
From the ``for`` loop in ``print_division``:

.. code:: python

   for i in range(N):

This ``for`` loop will iterate over the values 0, 1, 2, ... N-1; we
want to avoid the value zero, so the ``range`` should start at one:

.. code:: python

   for i in range(1, N):

Instead of changing ``exc.py``, we will copy the file to a new file
named ``exc_fixed.py`` and then fix the copy.  If we import the corrected
version and run ``exc_fixed.print_divisions(12)``, we will get:

.. code:: python

   >>> import exc_fixed
   >>> exc_fixed.print_divisions(12)
   12 / 1 = 12.0
   12 / 2 = 6.0
   12 / 3 = 4.0
   12 / 4 = 3.0
   12 / 5 = 2.4
   12 / 6 = 2.0
   12 / 7 = 1.7142857142857142
   12 / 8 = 1.5
   12 / 9 = 1.3333333333333333
   12 / 10 = 1.2
   12 / 11 = 1.0909090909090908

Now, we get the result we expect.  The loop starts at ``1`` and no
longer triggers the divide-by-zero exception.

Making mistakes is an important part of learning to program and, it is
a normal part of writing and debugging code even, for experience
programmers.  Learning to use the clues provided by an error message
to identify the source of a bug takes time and patience.  When your
code raises an exception, try not to get too frustrated and try not
fixate on the exact line that raises the exception.  Instead, start by
reading the last line of the error message to understand exactly which
exception was raised and then work your way through the stack trace,
starting with the line that raised the exception and working backwards
through the call chain.  Using the insight you gained from that
process to decide where to add print statements to highight the value
of crucial variables and to reason careully about the flow of control
will help lead you to the source of the problem.
   

Catching exceptions
-------------------

While exceptions can alert us to errors in our code, they can also be
*caught* and handled in a way that is consistent with the goals of the
application.  In the case of our ``divide`` function, we'll just
return ``None`` to indicate to the client that the value of ``a / b`` is
not defined when ``b`` is zero.

We can catch an exception with a ``try`` statement, also known as a
``try`` .. ``except`` block.  For example:

.. code:: python

   def divide(a, b):
       """ divide a by b """
       try:
           ret_val = a / b
       except ZeroDivisionError:
           # Send None back to the caller to signal
	   # that a / b is not defined.
           ret_val = None
       return ret_val

We will store this version of ``divide`` along with the original code
for ``print_divisions`` (shown below) in a file named ``exc_try.py``:

.. code:: python

     def print_divisions(N):
       """ Print result of dividing N by integers less than N. """
       for i in range(N):
           d = divide(N, i)
           print(f"{N} / {i} = {d}")

If we run this new version, we will get:

.. code:: python

   >>> import exc_try
   >>> exc_try.print_divisions(12)
   12 / 0 = None
   12 / 1 = 12.0
   12 / 2 = 6.0
   12 / 3 = 4.0
   12 / 4 = 3.0
   12 / 5 = 2.4
   12 / 6 = 2.0
   12 / 7 = 1.7142857142857142
   12 / 8 = 1.5
   12 / 9 = 1.3333333333333333
   12 / 10 = 1.2
   12 / 11 = 1.0909090909090908

A ``try`` statement allows us to "try" a piece of code, which we write
after the ``try:`` and, if it raises an exception, run an alternate
piece of code, which can be found after the ``except:``.  In this case,
the division in the first call to ``divide`` will trigger the
exception and the code in the ``except`` clause will be run and will
set ``ret_val`` to ``None``.  Once the code in the ``except`` clause
is finished, the ``return`` statement that follows the ``try``
statement will be executed.  The value of ``ret_val`` will be
returned to ``print_divisions``, which, in turn, will simply print it
as the result of the division.  None of the subsequent calls to
``divide`` in the loop will raise the exception.  In these cases,
``ret_val`` will simply be set to the result of the division and
returned as expected.

The ``divide`` function as written now handles division by zero
without failing.  Notice, however, that it can still fail.  For
example, notice what happens if we pass it non-numeric arguments:

.. code:: python

   >>> exc_try.divide("abc", "a")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "exc.py", line 4, in divide
       return a / b
   TypeError: unsupported operand type(s) for /: 'str' and 'str'

This usage raises a different type of exception, a ``TypeError``.  Our
``try`` statement catches the ``ZeroDivisionError`` exception, but not
the ``TypeError`` exception.  As a result, our program
stops, and the stack trace message shown above is printed,

Fortunately, we can catch multiple types of exceptions in the same
``try`` statement:

.. code:: python

   import sys
   def divide(a, b):
       try:
           ret_val = a / b
       except ZeroDivisionError:
           # Send None back to the caller to signal
	   # that a/b is not defined.
           ret_val = None
       except TypeError as err:
           # Fail: no way to move forward.
           print("Type error:", err)
	   sys.exit(1)
       return ret_val


Now when we call ``divide`` on strings, our error message is printed
and the execution ends on the call to ``sys.exit(1)``:

.. code:: python

   >>> exc_try.divide("abc", "a")
   Type error: unsupported operand type(s) for /: 'str' and 'str'

This example also illustrates another feature of exceptions: we can
use the keyword ``as`` to give a name to the exception that was
caught.  In this case, we use the name ``err`` and pass it to ``print``
along with the string ``"Type error:"``.  Using a mechanism that we'll
discuss in the chapter on :ref:`chapter-classes`, ``print`` extracts a
string that describes the exception that occurred from ``err`` and prints
it.

We might not know all of the possible exceptions that can be raised by
a given piece of code when we first write it or the set of possible
exceptions might change over time (say, because a function we use has
changed and can now raise a broader set of exceptions).  If we want to
make sure to deal with all possible types of exceptions, we can catch
the generic exception ``Exception``.  This exception is best used to
handle unexpected exceptions, as in:

.. python-run::

   import sys
   def divide(a, b):
       try:
           ret_val = a / b
       except ZeroDivisionError:
           # Send None back to the caller to signal
	   # that a/b is not defined.
           ret_val = None
       except TypeError as err:
           # Fail: no way to move forward.
           print("Type error:", err)
           sys.exit(1)
       except Exception as err:
           # Fail: no way to move forward.
           print("Unexpected error:", err)
           sys.exit(1)

       return ret_val

The last ``except`` clause will only be executed, if the code in the
``try`` block throws an exception other than ``ZeroDivisionError`` or
``TypeError``.  You might be tempted to use a generic ``Exception`` to
catch everything. Don't.  It is likely that your application will be
better served by handling different exceptions in different ways.

The ``try`` statement also has an optional ``finally`` clause that
gets run whether an exception is raised or not. This clause is useful
when there are cleanup operations that need to be performed
(closing files, closing database connections, etc.) regardless of
whether the code succeeded or failed.  For example:

.. python-run::
   :formatting: separate

   import sys
   def divide(a,b):
       """ Divide a by b and catch exceptions"""

       try:
           ret_val = a / b
       except ZeroDivisionError:
           ret_val = None
       except TypeError as err:
           print("Type error:", err)
           sys.exit(1)
       except Exception as err:
           print("Unexpected Error:", err)
           sys.exit(1)
       finally:
           print(f"divide() was called with {a} and {b}")

       return ret_val

.. python-run::

   divide(6, 2)
   divide(6, 0)


Before we close this chapter, let's look at what happens when we catch
some exceptions close to the source, but leave others to be handled
higher up the call stack.  Specifically, we'll return to the example
from the start of the chapter.  We've modified ``divide`` to catch the
``TypeError``, but not ``ZeroDivisionError``.  Instead, we'll handle
that error in ``print_divisions``.

.. python-run::
   :formatting: separate

   import sys
   def divide(a,b):
       """ Divide a by b and catch exceptions"""
       try:
           ret_val = a / b
       except TypeError as err:
           print("Type error:", err)
	   sys.exit(1)

       return ret_val

   def print_divisions(N):
       """ Print result of dividing N by integers less than N. """
       for i in range(N):
           try:
               d = divide(N, i)
               print(f"{N} / {i} = {d}")
           except ZeroDivisionError:
	       print(f"{N} / {i} is undefined")

   print_divisions(12)

In the first iteration of the loop in ``print_division``, ``i`` will
be zero, which will cause the division operation in ``divide`` to
raise an exception.  The ``try`` statement in ``divide`` catches type
errors, but not divide-by-zero errors.  So, Python will propagate the
error to call site in ``print_division`` to see if the call to
``divide`` is nested within a ``try`` statement that knows how to
handle divide-by-zero errors.  In this case it is, and so, the
exception is handled by the ``except`` clause in ``print_divisions``.
In general, an exception will be propagated up the call stack until it
is caught by an enclosing ``try`` statement or Python runs out of
functions on the stack.

We have only skimmed the surface of exceptions in this chapter.  You
now know enough to read error messages and handle simple exception
processing.  We'll return to the topic of exceptions later in the book
to look ways to catch related types of errors in one ``except`` clause
and how to define and raise your own exceptions.


Practice Problems
-----------------

The practice problems in this section refer to the following functions:

.. python-run::

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

	return "some_func does not raise an exception"

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
            result = f"Caught {err} in yet_another_func"
        return result

**Problem 1**

- What value(s) could you pass to ``some_func`` to cause it to raise a ``TypeError``,
- What value(s) could you pass to ``some_func`` to cause it to raise a ``ZeroDivisionError``,
- What value(s) could you pass to ``some_func`` to cause it to raise an ``AssertionError``, and
- What value(s) could you pass to ``some_func`` to cause it return a value rather than raise an exception?

**Problem 2**

- What value(s) could you pass to ``some_other_func`` that will cause it to return ``"some_func does not raise an exception"``,
- What value(s) could you pass to ``some_other_func`` that will cause it to return ``"Caught TypeError in some_other_func"``,  and
- What value(s) could you pass to ``some_other_func`` that will cause it to return ``"Caught ZeroDivisionError in some_other_func"``.

**Problem 3**

What is the result of evaluating ``some_other_func(5)``?

**Problem 4**

What is the result of evaluating the following calls:

- ``yet_another_func(0)``,
- ``yet_another_func(1)``,
- ``yet_another_func(5)``,
- ``yet_another_func(15)``?

  
Practice Problem Solutions
--------------------------

**Problem 1**

- Any call to ``some_func`` with a value less than zero (e.g.  ``some_func(-1)``) will raise a ``TypeError``.
- The ``some_func(0)`` will raise a ``ZeroDivisionError``.
- Any call with a value between one and nine (inclusive) (e.g. ``some_func(5)``) will raise an ``AssertionError``.
- Any call with a value greater than or equal to ten (e.g. ``some_func(20)``) will not raise an exception and will return the string ``'some_func does not raise an exception'``.

**Problem 2**


- Any call to ``some_other_func`` with a value greater than or equal to nine (e.g. ``some_other_func(9)`` return the string ``'some_func does not raise an exception'``.  The call to ``some_func`` in the body of the ``try`` block of ``some_other_func`` does not raise an exception and so, none of the exception handlers are executed and and ``some_other_func`` executes the final return statement.
  
- Any call with a value less than -1 (e.g. ``some_other_func(-2)``) will return ``'Caught TypeError in some_other_func'``.  The call to ``some_func`` in the ``try`` block will raise a ``TypeError``.  Since the error is not caught by ``some_func`` it is propagated to ``some_other_func`` where it is caught by the exception handler.  The exception handler returns the string.
  
-  The call ``some_other_func(-1)`` will return ``'Caught ZeroDivisionError in some_other_func'``. The call to ``some_func`` in the ``try`` block will raise a ``ZeroDivisionError``.  Since the error is not caught by ``some_func`` it is propagated to ``some_other_func`` where it is caught by the exception handler.  The exception handler returns the string.

**Problem 3**

.. python-run::

    some_other_func(5)

This function raises an exception because the call to ``some_func`` raises an ``AssertionError`` and neither ``some_func`` nor ``some_other_func`` catch that type of exception, so it is propagated to top-level.

**Problem 4**

Each call to ``yet_another_func`` calls ``some_other_func``, which in
turn calls ``some_func``.  Some of the calls to ``some_func`` raise
exceptions, others do not.


.. python-run::

    yet_another_func(0)

In this case, the call to ``some_func`` raises a ``TypeError``, which
caught and handled by the ``TypeError`` clause the ``try`` block in ``some_other_func``.  That
handler has a normal return statement, so the call to
``some_other_func`` finishes normally and the ``try`` block in ``yet_another_func`` finishes normally.

.. python-run::
   
    yet_another_func(1)

Similar to the previous example, the exception, ``ZeroDivisionError``, is handled by ``some_other_func``.

.. python-run::

    yet_another_func(5)

In this case, the call to ``some_func`` raises an ``AssertionError``.
That error is not caught in either ``some_func`` or
``some_other_func`` and so, it is propagated to the ``try`` block in
``yet_other_func``, where it is caught and handled by the
``Exception`` clause.


.. python-run::
   
    yet_another_func(15)

This call does not raise any exceptions.

   
