.. _chapter-organization-basics:

Basics of Code Organization
===========================

Back in :ref:`chapter-basics`, we wrote our first program:

.. code:: python

   print("Hello, world!")

And saw that we could run it directly in the Python interpreter, like this:

.. python-run::

   print("Hello, world!")

Or by placing the code in a file called ``hello.py``, and running that file
from the terminal:

.. code:: shell

   $ python hello.py
   Hello, world!

In the previous chapter, we also saw that it is possible to write function
definitions in a Python file, such as the ``primes.py`` file that contained
our ``is_prime`` function, and them "import" the contents of that file
into the interpreter:

.. python-run::

   import primes
   primes.is_prime(4)
   primes.is_prime(7)

So, it seems that Python files can serve two purposes: I can
*run* a Python file, which may produce some result (like printing ``Hello, world!``) or
I can *import* a Python file, which allows me to use functions that are defined inside
that file. In this chapter, we will expand on this distinction (running vs. importing)
by introducing the notion of Python *modules*, and providing an introduction to
how to organize Python code in a program.

.. todo::

   When the part on software development is written, reference it and mention that
   we'll discuss code organization in a lot more detail there.


Python modules
--------------

A Python module is, quite simply, a file containing Python code. The ``hello.py`` file
mentioned above is a Python module, as is the ``primes.py`` file from the previous
chapter. However, as we saw earlier, we used each of these files in very different ways:
we "ran" the ``hello.py`` file, but we ``import``-ed the ``primes.py`` file. To
explore this distinction, we'll start by elaborating on what it means to "import" a module.
To do this, we will use two
modules which you can find in our :ref:`example code <example-code>`: ``getting-started/code-organization/primes.py``
and ``getting-started/code-organization/mersenne.py`` In Python, modules are usually referred
to without the ``.py`` extension, so we will refer to these as the "``primes`` modules" and the
"``mersenne`` module".

If you look at the ``primes`` module, you'll see it contains two functions, ``print_primes``
and ``is_prime``:

.. code:: python

   def print_primes(max_n):
       # ...

   def is_prime(n):
       # ...

The actual implementation of these functions won't be relevant to our discussion of modules,
as we'll be focusing on how these functions are *called* across modules, and not on how they
work internally. So, we won't be digging into their implementation, but we nonetheless
encourage you to take a quick look at the implementation of the ``is_prime`` function:
it is a bit more complex than the one we saw in the previous chapter, because
we need a faster algorithm for this chapter's example, and it provides several examples
of using conditional and looping statements in a non-trivial way.

As we've seen previously, we can use the ``import`` statement to access the contents of
the ``primes`` module from the interpreter:

.. python-run::

   import primes
   primes.is_prime(4)
   primes.is_prime(7)

The ``import`` statement also allows us to import only specific functions from a module,
like this:

.. python-run::

   from primes import is_prime
   is_prime(17)
   is_prime(42)

.. todo::

    .. common-pitfalls:: "import" vs "from X import Y" vs "from X import *"

       TODO

We can actually also import modules from *other* modules as well. In particular, the ``mersenne``
module provides a number of functions related to *Mersenne primes*, or prime numbers of the
form :math:`2^p-1`, where :math:`p` is itself a prime number. One of these functions
needs to call the ``is_prime`` function, located in the ``primes`` module, so we will
need to import the ``primes`` module from the ``mersenne`` module, which looks something
like this:

.. code:: python

    import primes

    def is_mersenne_prime(p):
        # ...

    def is_power_of_two(n):
        # ...

    def print_mersenne_primes(max_p):
        # ...

As with the ``primes`` module, the exact implementation of these functions won't be relevant to
our discussion, but notice how the ``print_mersenne_primes`` function uses the ``is_prime``
function from the ``primes`` module:

.. code:: python

    if not primes.is_prime(p):

We are able to use this function because we included the ``import primes`` statement at the top
of the ``mersenne`` module.

Now, let's try using a function from the ``mersenne`` module
from the interpreter. Before doing so, exit the interpreter and start it again,
so we can make sure the previous ``import primes`` statement we ran from
the interpreter isn't affecting this next example.

.. python-run::

   import mersenne
   mersenne.print_mersenne_primes(100)

Notice how we are able to call the ``print_mersenne_primes`` function in the ``mersenne`` module,
which internally requires using the ``is_prime`` function, located in a different module.
However, we are not required to run ``import primes`` ourselves in the interpreter,
because it is already being imported from inside the ``mersenne`` module.


Running vs importing a module
-----------------------------

So far, we've seen that Python modules can be imported from the interpreter and from
other modules, but modules can also be *run* from the command-line. To better understand
this distinction, we will use an ``arithmetic`` module which you can find in the
``getting-started/code-organization/`` directory of the examples. You'll see that there
are three versions of this module: ``arithmetic``, ``arithmetic_nomain``, and ``arithmetic_main``.

We'll start by looking at the ``arithmetic`` module, which contains two very simple functions:

.. literalinclude:: arithmetic.py
   :language: python

As expected, we can import this module and use it from the interpreter:

.. python-run::

   import arithmetic
   arithmetic.add(2, 10)
   arithmetic.multiply(2, 10)

But what happens if we *run* this module from the command-line?

.. code:: shell

   $ python3 arithmetic.py
   $

Nothing happens: Python returns immediately. The reason for this is
that Python ran through all the code in the ``arithmetic.py`` file, and only encounters
function definitions. Python internally makes a note that these functions have been defined,
but there are no statements in the file that would make Python do something, like
print a message or call the functions.

So, let's take a look at this slightly modified version, ``arithmetic_nomain``:

.. literalinclude:: arithmetic_nomain.py
   :language: python

This version includes some statements after the function definitions. If we run
this module we'll see the following:

.. code:: shell

   $ python3 arithmetic_nomain.py
   add(2, 10) =  12
   multiply(2, 10) = 20
   $

.. todo::

   Figure out a way to automatically generate the output above.

What's happening here is that Python runs through the code, makes a note of that functions
``add`` and ``multiply`` have been defined, and then encounters code that calls those functions
and prints something, and runs that code as well.

This may seem like a convenient way to define a few functions, and then include some basic
code to informally test those functions, but there is a snag: that code will also run
when we import the module, resulting in this:

.. python-run::

   import arithmetic_nomain
   arithmetic_nomain.add(2, 10)
   arithmetic_nomain.multiply(2, 10)

.. todo::

   When the testing chapter is written, refer to how there are better ways of testing
   your code.

The reason for this is that importing a module also causes Python to run through
all the code in the corresponding Python file, which is why we are then able
to use the functions defined in that module. However, we may want to be selective
about what code is run exactly and, in particular, we may want to separate out
the code that should only run when the module is run from the command line.
We can do this by placing the code in a *main block*.
We can see what this looks like in the ``arithmetic_main`` module:

.. literalinclude:: arithmetic_main.py
   :language: python

When we run it, the code under ``if __name__ == "__main__":`` runs as expected:

.. code:: shell

   $ python3 arithmetic_main.py
   add(2, 10) =  12
   multiply(2, 10) = 20
   $

But that code *won't* be run if we import the module:

.. python-run::

   import arithmetic_main
   arithmetic_main.add(2, 10)
   arithmetic_main.multiply(2, 10)

All that said, this doesn't mean that every Python module has to have a main block.
In the next section, we will elaborate on what a computer program is, and how
Python programs often span multiple modules (where typically only one module
will have a main block).


.. todo::

    .. common-pitfalls:: Running a module when importing is more appropriate

       TODO. Is this only an issue when using IPython?

.. common-pitfalls:: Reloading modules

   When you import a module from the interpreter, Python will import the current
   version of that module, and won't track changes in that module. This means
   that, if you make a change to the module, that change won't automatically
   propagate to the interpreter. For example, try doing the following:

    .. python-run::

       import arithmetic
       arithmetic_main.add(2, 10)

   Now, try modifying the ``arithmetic.py`` file modify the ``add`` function
   to look like this:

    .. code:: python

       def add(x, y):
           return x + y + 1

   Let's also add the following function:

    .. code:: python

       def subtract(x, y):
           return x - y

   If you try to use the ``add`` function, you'll see it still behaves according
   to the original (correct) version. Python will also tell you it can't find
   a ``subtract`` function:

    .. python-run::

       arithmetic_main.add(2, 10)
       arithmetic_main.subtract(100, 10)

   Interestingly, importing the module again won't actually resolve the situation:

    .. python-run::

       import arithmetic
       arithmetic_main.add(2, 10)
       arithmetic_main.subtract(100, 10)

   You need to explicitly reload the module using Python's built-in ``importlib`` module:

    .. code:: python

        >>> import importlib
        >>> importlib.reload(arithmetic)
        <module 'arithmetic' from 'arithmetic.py'>
        >>> arithmetic.add(2, 10)
        13
        >>> arithmetic.subtract(100, 10)
        90



Computer programs revisited
---------------------------

In :ref:`chapter-basics`, we said that "a computer program is, at its
core, a collection of instructions that the computer must perform". We now have a better
sense of what these instructions look like: ``if`` statements, ``for`` and ``while`` loops,
assignments, function definitions, function calls, etc. And, as we've seen a few times
already, the vessel for these instructions is text file with a name ending in ``.py``, i.e.,
a Python module.

However, this doesn't mean that a program is composed of exactly one module. While simple
programs can often be implemented in one module, it is very common for programs to span
multiple modules. To see an example of this, take a look at the  ``prime-checker`` module
in the ``getting-started/code-organization/`` examples directory. This is a module
with a main block that asks the user to enter a number, and will then print out
some information about whether the number is prime or not, and whether it is a Mersenne
prime or not:

.. python-run:: prime-checker.py
   :formatting: separate

Here are some sample runs of this program:

.. code:: shell

    $ python3 prime-checker.py
    Enter a number: 16
    16 is not a prime number.

.. code:: shell

    $ python3 prime-checker.py
    Enter a number: 23
    23 is a prime number, but not a Mersenne prime (and neither is 2^23-1).

.. code:: shell

    $ python3 prime-checker.py
    Enter a number: 61
    61 is a prime number, but not a Mersenne prime (however, 2^61-1 is a Mersenne prime).

.. code:: shell

    $ python3 prime-checker.py
    Enter a number: 127
    127 is a double Mersenne prime: both 127 and 2^127-1 are Mersenne primes.

However, all the logic involved in testing each number's primality
is contained in two other modules: ``primes`` and ``mersenne``. Our program, thus,
spans three modules: ``prime-checker``, ``primes``, and ``mersenne``.

This is a further example of *decomposition*: while we could have placed all the
code in a single module, dividing it into distinct modules, each with a related
set of functions, makes the code more manageable. It also improves the reusability
of our code: if we wanted to write a different program that involves checking a
number's primality, all we need to do is import our ``primes`` module.

All that said, this doesn't mean that "a collection of modules" is a program.
A program is specifically something that is *executable*, which is the technical term for
"something I can run" (in the manner we've described above, as opposed to
just importing a module). In a Python program, this often means that at least
one of the modules must include a ``__main__`` block.

On the other hand, when we have a collection of modules that provides some useful functionality,
but which is not executable, that is what we would call a *software library*, or simply a *library*.
For example, we could distribute the ``primes`` and ``mersenne`` modules as a "prime number library".
Neither of these modules has a ``__main__`` block and that is totally fine: these
modules are not meant to be run but, rather, to be imported by other modules.

While we may not develop that many libraries ourselves, we will almost certainly
*use* existing libraries in our code. In particular, Python itself includes a vast collection of
modules, called the Python Standard Library, that we can use in our code and
which we describe next.

The Python Standard Library
---------------------------

When you install Python on your computer, you are not only getting a Python interpreter,
but also access to a huge collection of modules that is already included with Python.
This is known as the Python Standard Library, or PSL, and it provides all
sorts of functionality that can come in handy when writing our code. It's hard to overstate
how large and useful this library is: it includes modules for most common tasks you can
imagine, such as string processing, math functions, file and directory access, network utilities,
and much, much more. You can see the full content of the PSL here: https://docs.python.org/3/library/

We have actually already used two of the modules included with the PSL: the ``random`` module
and the ``math`` module. Now that we know what modules are, we can better understand what is
happening when we do this:

    .. python-run::

       import random
       random.randint(1,100)

Based on what we saw earlier this chapter, it would seem that running ``import random`` requires
that there be a ``random.py`` file in the same directory as our code. Python *will* look for
a ``random.py`` file in the same directory as our code first but, if it does not find it,
it will check whether the PSL includes such a module (which it does). So, somewhere
in the official Python code, there is a ``random.py`` file containing a bunch of functions
related to random number generation, including a ``randint`` function (the actual ``random.py``
is actually a bit more complicated, and involves classes and objects, which we have not yet
seen).

.. technical-details:: Where exactly is the PSL?

   When you install any piece of software, some of that software will usually be installed
   in a "system directory", separate from the directories were you (a regular user) keep your own files.
   Without going to deep into how operating systems organize their filesystems, it is
   enough to know that the location of these system directories is well-known by applications
   running in your computer, including the Python interpreter.

   This means that the Python interpreter knows to search through
   those system directories if we ask it to import a module (and that module can't be found
   in the same directory as our code). For example, this is where you would find the
   ``random.py`` in most operating systems:

   - Windows: ``C:\Program Files\Python 3.8\lib\random.py``
   - MacOS: ``/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/random.py``
   - Linux: ``/usr/lib/python3.8/random.py``
