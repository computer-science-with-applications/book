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
stack trace.  Because we directly typed ``x = 42 / 0`` into
the interpreter, these lines don't provide a lot of information in
this case (it is immediately apparent that the error originated in the
code we just typed).  

The stack trace is much more useful when an exception is raised inside
a function, as it will tell us the exact line inside that function
where the exception was raised. Not just that, it will provide us with
the complete sequence of function calls that led to the exception.

For example, suppose we wanted to write a simple program that prints
the result of dividing an integer N by all the positive integers less
than N.

.. code:: python

   def divide(a, b):
       ''' divide a by b '''
       return a / b
    
   def print_divisions(N):
       ''' Print result of dividing N by integers less than N. '''
       for i in range(N):
           d = divide(N, i)
           print(N, "/", i, "=", d)

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

Notice how this stack trace is much more informative. In particular,
it tells us than an exception happened after the following sequence of
events:

* Python ran ``exc.print_divisions(12)`` in the interpreter (shown in the stack trace as as ``File "<stdin>", line 1,  in <module>``).
* During the call to ``print_divisions``, Python ran the line
  ``d = divide(N, i)``, located in line 8 in the file ``exc.py``.
* During the call to ``divide``, Python ran the line ``return a / b``,
  located in line 3 of ``exc.py``. This last entry in the stack
  trace produced a ``ZeroDivisionError`` exception.

Notice that this is simply a printed version of the function call
stack, which we covered in section :ref:`call-stack` of the previous
chapter.

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

If we make this change to ``exc.py`` and run ``exc.print_divisions(12)``
within the same session of the python interpreter, we'll get the exact
same error as before:

   >>> exc.print_divisions(12)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "exc.py", line 8, in print_divisions
       d = divide(N, i)
     File "exc.py", line 3, in divide
       return a / b
   ZeroDivisionError: division by zero

Wait, didn't we fix this problem?  Yes, but Python does not
automatically reload your code when you change it.  We can use the
``reload`` function from ``importlib`` to fix our problem::

   >>> import importlib
   >>> importlib.reload(exc)
   <module 'exc' from 'exc.py'>
   >>> exc.print_divisions(12)
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

So, when your code raises an exception, try not to fixate on the exact
line that raises the exception. While that line could be wrong, it is
just as likely that the actual origin of the exception is somewhere
else in your code.  The stack trace provides some hints as to where to
look for the error.  Systematically adding ``print`` statements that
highlight the value of crucial variables can help you isolate the
source of the error.

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
       ''' divide a by b '''
       try:
           ret_val = a / b
       except ZeroDivisionError:
           # Send None back to the caller to signal
	   # that a/b is not defined.
           ret_val = None
       return ret_val

If we replace the ``divide`` function with the above version, reload
the file, and call ``print_divisions``, we will see:

.. code:: python

   >>> importlib.reload(exc)
   <module 'exc' from 'exc.py'>
   >>> exc.print_divisions(12)
   12 / 1 = None
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
after the ``try`` and, if it raises an exception, run an alternate
piece of code, which can be found after the ``except``.  In this case,
the division in the first call to ``divide`` will trigger the
exception and the code in the ``except`` clause will be run and will
set ``ret_val`` to ``None``.  Once the code in the ``except`` clause
is finished, the ``return`` statement that follows the ``try``
statement will be executed and the value of ``ret_val`` will be
returned to ``print_divisions``, which, in turn, will simply print it
as the result of the division.  None of the subsequent calls to
``divide`` in the loop will raise the exception.  In these cases,
``ret_val`` will simply be set to the result of the division and
returned as expected.

The ``divide`` function as written now handles division by zero
without failing.  Notice, however, that it can still fail.  For
example, notice what happens if we pass it non-numeric arguments:

.. code:: python

   >>> exc.divide("abc", "a")
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

   def divide(a, b):
       try:
           ret_val = a / b
       except ZeroDivisionError:
           # Send None back to the caller to signal
	   # that a/b is not defined.
           ret_val = None
       except TypeError as err:
           # Fail: no way to move forward.
           print("Type error:, err)
	   sys.exit(1)
       return ret_val


Now when we call ``divide`` on strings, our error message is printed
and the execution ends on the call to ``sys.exit(1)``:

.. code:: python

   >>> exc.divide("abc", "a")
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
when there are any cleanup operations that need to be performed
(closing files, closing database connections, etc.) regardless of
whether the code succeeded or failed.  For example:

.. python-run::
   :formatting: separate

   def divide(a,b):
       ''' Divide a by b and catch exceptions'''

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
           print("divide() was called with {} and {}".format(a, b))

       return ret_val

.. python-run::

   divide(6, 2)
   divide(6, 0)
   divide(6, "foo")


Before we close this chapter, let's look at what happens when we catch
some exceptions close to the source, but leave others to be handled
higher up the call stack.  Specifically, we'll return to the example
from the start of the chapter.  We've modified ``divide`` to catch the
``TypeError``, but not ``ZeroDivisionError``.  Instead, we'll handle
that error in ``print_divisions``.

.. python-run::
   :formatting: separate

   def divide(a,b):
       ''' Divide a by b and catch exceptions'''
       try:
           ret_val = a / b
       except TypeError as err:
           print("Type error:", err)
	   sys.exit(1)

       return ret_val

   def print_divisions(N):
       ''' Print result of dividing N by integers less than N. '''
       for i in range(N):
           try:
               d = divide(N, i)
               print(N, "/", i, "=", d)
           except ZeroDivisionError:
	       print(N, "/", i, "is undefined")

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




