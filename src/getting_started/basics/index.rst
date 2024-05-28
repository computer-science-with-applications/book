.. _chapter-basics:

Programming Basics
==================

A computer program is, at its core, a collection of instructions that the
computer must perform. It could be as simple as telling the computer to
add two numbers or as complex as performing a complex simulation of
drug interactions. In this chapter, you will learn some
of the most basic instructions we can include in a program,
and you will run your first computer program. 

As you read through this chapter, it may seem like you won't be able to 
do much with these basic instructions. This is normal: the concepts
presented in this chapter lay the foundation for understanding more
complex concepts introduced in subsequent chapters.

In this book, we will be using the Python programming language and, more
specifically, Python 3. Python is a widely-used modern language with 
a fairly low overhead for getting started. Don't forget, however, that
the goal of this book isn't to teach you Python specifically; our
goal is to teach you how to think computationally and how to write
programs that provide a computational solution to a given problem.
Python just happens to be a very convenient language to get started
with, but many of the concepts and skills you will learn will
carry over to other languages.

Tools
-----

Before we get started, let's review the tools you'll need to follow
along as we introduce concepts.  Specifically, you'll need:

#. a shell and a terminal application,
#. a code or text editor, and
#. the Python 3 interpreter.

Both MacOS and Linux come with a terminal application pre-installed.
You may need to install one, however if you are running Windows.  The
program that runs within a terminal window and processes the commands
the you type is called a *shell*.  There are lots of shells---Bash,
ksh, PowerShell, etc.  For our purposes, it does not matter which one
you use as long as you know how to run basic commands and create
directories and move among them.

When you use the shell, you will type commands at the command-line
prompt.  We will use ``$`` as the shell command-line prompt in our
examples. You may see something different depending on exactly which
shell you are using.  The exact prompt does not matter, just remember
that you do not need to type the ``$`` when you enter a command.

Programmers often have *very* strong opinions about text editors.  One
of us is a long-time Emacs fan, the other uses graphical IDEs like
Visual Studio Code (VSCode) and PyCharm. We
currently recommend VSCode to our students. If you do not already have
a favorite text editor, try out a few and pick the one that works best
for *you* and then do your best to ignore all the comments coming from
your friends and colleagues about *their* favorite editor being the
one true editor.  Whichever editor you choose, you will need to be
able to create new files and edit existing files.

As for Python, depending on how your machine is configured you may
already have Python 3 or you may need to install it.  You can check
which, if any, version of Python you have installed by running the
following command at the command-line prompt in a terminal window::

   $ python --version
   Python 3.8.3

If the command fails with a ``command not found`` error, then you will
need to install Python 3.  If the output shows a version number
starting with 2 (e.g., ``Python 2.7``), try running ``python3``
instead of just ``python`` to make sure you run Python 3.  The version
numbers displayed may be different on your computer. Please make sure
you're running at least Python 3.4.

While we have chosen to recommend using an editor and a separate
interpreter, many programmers prefer to use integrated development
environments (IDE), such as PyCharm or Juypter notebooks.  You might
want to try one or more IDEs as well.  As long as you have a way to
edit code and run it, you will be in good shape,

If you choose to use different tools, please keep in mind that the
prompts and the format of output may be slightly different from our
examples below.


Your First Program
------------------

Traditionally, the first program you write is a simple program that instructs
the computer to print out the following message on the screen::
  
    Hello, world!
    
In Python, we can do this task with a single line of code:

.. code:: python

   print("Hello, world!")

Don't worry about the exact syntactical details just yet. However, do notice 
that the above line makes sense intuitively: we're telling the computer 
to *print* something 
on the screen: ``Hello, world!``

Not just that, that single line is the entirety of the program. In most programming
languages, a program is specified in plain text typically stored in one or more files.
So, if you create a text file called ``hello.py`` with that single line of code,
that file will contain your first program. 

Of course, now we have to *run* that program. In general, all
programming languages have some mechanism to take the contents of a
file containing a program and run the instructions contained in that
file. Because Python is an *interpreted* language, we have second way
of running the program: interactively entering Python code into an
*interpreter*.

These two ways of running code (storing it in a file or running it interactively
in an interpreter) are complementary. We will see how to do both in Python,
and then discuss when it makes sense to use one or the other. 

Using the Python interpreter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Python interpreter is a program that allows us to interactively run
Python code one line at a time. So, let's start the Python interpreter!
From the terminal, run the ``python`` command. You should see something like the following::

    Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
    [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

.. info-note::

   The exact date and version numbers shown when you start the
   interpreter will likely be different on your computer. As noted
   earlier, please make sure you're running at least Python 3.4.
   
The ``>>>`` symbol is called the *prompt*. If you write a line of Python code and press the Enter key,
the Python interpreter will run that single line of code, print any output resulting
from running that code, and will finally return to the prompt so you can write more
code. So, try typing in the "Hello, world!" program and then pressing "Enter". The
interpreter should look something like this::

   Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
   [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
   Type "help", "copyright", "credits" or "license" for more information.
   >>> print("Hello, world!")
   Hello, world!
   >>> 

Notice that, after the user pressed Enter, the Python interpreter *printed* ``Hello, world!``
before returning to the prompt. This is called the *output* of the program.

For the remainder of the book, whenever we want to show code that is intended to
be run in the Python interpreter, we will include the ``>>>`` prompt in the
code examples. However, this does *not* mean you have to type ``>>>`` yourself;
it is simply intended to distinguish between the code you type into the interpreter,
and the expected output of that code. For example:

.. python-run::

   print("Hello, world!")

Before we continue, it is worth noting that Python (and pretty much
all programming languages) are very picky when it comes to code syntax
(i.e., the required elements and form of a piece of code). For
example, code is usually case-sensitive, meaning that typing ``Print``
instead of ``print`` will result in an error:

.. python-run::

   Print("Hello, world!")

Every bit of syntax, even if it seems redundant, plays a role, so forgetting
to include quotation marks will similarly result in an error:

.. code:: 

   >>> print(Hello, world!)
     File "<stdin>", line 1
       print(Hello, world!)
                         ^
   SyntaxError: invalid syntax

If you type a piece of code into the interpreter and get an error back,
especially a ``SyntaxError``, double-check the code you typed to make
sure you included all of the necessary syntax and did not introduce any typos.

You'll encounter many errors as you learn to write code.  In a couple
of chapters, we'll explain how to interpret the information presented
in error messages in more detail.  For now, you can ignore most it;
just look at the last line to find out type of error occurred.

Running code from a file
~~~~~~~~~~~~~~~~~~~~~~~~

Instead of typing and running a program line by line in the
interpreter, we can also store that program in a file, typically named
with a ``.py`` extension, and tell Python to read the file and run the
program contained in it.  In fact, when we use the term "a Python
program" we typically refer to a ``.py`` file (or a collection of
``.py`` files; for now we'll work with just one) that contains a
sequence of Python instructions.

Let's write our "Hello World!" program using this approach: create a
blank text file called ``hello.py`` and edit it to contain this single
line:

.. code:: python

   print("Hello, world!")

To run this program, open a terminal and, in the same directory that
contains your ``hello.py`` file, run the following::

   $ python hello.py
       
This command should produce the following output::

   Hello, world!
   
And then immediately return to the terminal.

.. _chapter-basics-sec-interactive-vs-file:

Running code interactively vs. from a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have seen two ways of running Python code: by entering the code line by line
ourselves into the interpreter, and by saving the code in a text file 
and telling Python to run the contents of that file. 

Entering code into the interpreter line by line is very useful for trying
out small pieces of code. For example, let's say you wanted to experiment
with the "Hello, world!" code to see what happened if you included different
messages:

.. python-run::

   print("Hello, world!")
   print("Hello, reader!")
   print("Hello, interpreter!")
   
If we were running code from a file, we would have to open the ``hello.py`` file, edit it,
save it, and re-run ``python hello.py``. This process quickly becomes 
tedious, and using an interactive tool like the interpreter makes it much easier to experiment with
small pieces of code.

In fact, this type of tool is common in other interpreted programming 
languages, such as Ruby, JavaScript, R, and others. It is more formally 
called a REPL environment: Read-Evaluate-Print-Loop. The tool 
*reads* the code, *evaluates* it, *prints* any output it produces, 
and *loops* (i.e., allows you to start the process all over again by 
prompting you for more code).

By contrast, *compiled* programming languages like C, C++, Java, and
C# typically don't offer such an environment. In those languages, you
must write code in a file, and then run it from the file (or, more
precisely, code is first *compiled* into a binary format that the
computer can understand, and then it is actually run).

While the interpreter is a great tool, it is most 
useful for testing *small* pieces of code. Imagine that 
you had a complex program with hundreds or even thousands of lines of codes: 
typing it line by line into the interpreter *every time* you wanted to run it 
would be cumbersome. Instead, we store the program in a file 
(or several files) and run it from there. 

This reasoning, however, doesn't mean that all small programs are run
in the interpreter and all large programs are run from files. Instead,
the approaches are complementary. When writing a program, a common
workflow is to start writing the program in a file and to use the
interpreter to help you figure out specific pieces of code. In other
words, you may use the interpreter to work through tricky bits of
code, adding them to the text file only when they are correct. Later
in the book, we will see specific examples of this workflow.

Interpreters are also helpful for gaining familiarity with a new
*software library*. For example, Python itself includes a vast library
of code to handle common tasks (such as performing common math
operations and generating random numbers) and, while this code is very
well-documented, it usually pays off to familiarize yourself with it
in the interpreter before using it in programs.  Later in the book we
will see examples of how you can experiment with Python's standard
library in the interpreter, as well as other *third-party libraries*
(such as Pandas for data manipulation and Matplotlib for visualizing
data).

  

The Basics
----------

So far, the only "instruction" we've seen is ``print``, which allows
us to print some text on the screen (as we'll see later on, ``print``
is actually something called a "function" and ``print("Hello,
world!")`` is a "call" to that function). Of course, there is a lot
more you can do in Python. We'll see that there are instructions for
doing many things:

-  Simple arithmetic
-  Performing one action or another based on the result of a previous one
-  Repeating an action multiple times
-  And so on

For the remainder of this chapter we are going to focus on three fundamental
concepts found in nearly every programming language:

- Variables
- Types
- Expressions

As we said at the start of this chapter, there is little we'll be able
to do with these constructs alone, so don't worry if they seem a bit
abstract at first. In no time, you will find yourself using variables,
types, and expressions in all of your programs.


Variables
---------

A fundamental part of writing a computer program is keeping track of 
certain information throughout the lifetime of the program (i.e., while the
program is running). For example, 
if you were writing a simple program to compute the average of a 
series of measurements, you would need to
keep track of the running total of those measurements. This kind of 
information is stored in your computer's memory while a program is running. 

However, you will rarely (if ever) have to interact with your computer's memory
directly. Instead, most programming languages provide a convenient abstraction
for storing information: *variables*. A variable is a *symbolic name* 
representing a location in the computer's memory. You can store a 
specific *value*, such as a number or piece of text, in a variable and 
retrieve that value later on. 

In Python, you can *assign* a value to a variable like this::

    variable = value

The equals sign is called the *assignment operator*. It tells Python to
take the value on the right-hand side and assign it to the variable on
the left-hand side. The whole code fragment is called 
an *assignment statement*.

For example:

.. code:: python

   message = "Hello, world!"

In Python, it doesn't matter whether the ``message`` variable already 
existed or not. Whenever you perform an assignment on a previously-unseen 
variable, Python will choose a location in memory to store whatever value is 
assigned to that variable (in this case, the text ``"Hello, world!"``). 
You don't have to worry about the low-level details, as 
Python handles them under the hood.

Go ahead and try running the above assignment in the interpreter. You should 
see something like this:

.. python-run::
   :formatting: interpreter

   message = "Hello, world!"


After you press Enter, the interpreter will return straight to
the ``>>>`` prompt. Unlike the ``print`` function, an assignment does not 
produce any output. It simply alters the state of your computer.  
More specifically, this example stored the value ``"Hello, world!"`` in a 
location in the computer's memory
identified by the name ``message``. 

To print the value of a variable, we can use the ``print`` function:

.. python-run::

   print(message)
   
In fact, you can also just write the name of a variable in the
interpreter, and the interpreter will *evaluate* (or look up the value
of) the variable and print out its value:

.. python-run::

   message

You can ignore the quotation marks around ``Hello, world!`` in the 
above output;
we will revisit this detail later in this chapter.

Over the lifetime of a program, we can assign new values to variables
using the assignment operator. For example, notice that we assign a
sequence of new values to the ``message`` variable:
 
.. python-run::

   print(message)
   message = "Hello, reader!"
   print(message)
   message = "Hello, interpreter!"
   print(message)

Assigning a new value to an existing variable is often referred to as
*updating* the variable.


Types
-----

In the above example, the ``message`` variable contained a piece of text
(``"Hello, world!"``). However, variables can also contain other *types*
of data. Most programming languages (including Python) support at least 
three basic types:

-  **Numbers**: Numbers usually encompass both integer numbers and real numbers. 
-  **Strings**: Strings are how we refer to "text" in most programming
   languages (in the sense that text is a "string" of characters). We've
   actually already seen an example of a string: ``Hello, world!`` (the
   character ``H`` followed by the character ``e`` followed by the character ``l``, etc.).
-  **Booleans**: Booleans represent truth values (*True* or *False*).

Additionally, Python also supports a special "None" type, to indicate
the *absence* of a value.  In this section, we will describe the above
three types, as well as the special "None" type, in more detail.


In most programming languages, each variable in a program has a specific type 
associated with it. For example, ``message`` has a string type: it stores 
a string of characters. Notice, however, that we didn't need to tell 
Python "``message`` is a variable of type string". 
This is because Python is a *dynamically-typed* language: it can figure out the
type of a variable on-the-fly. In this case, the fact that we assigned a string
value (``"Hello, world!"``) to ``message`` was enough for Python to determine 
that ``message`` was a string variable. In addition, as we will see later in 
this chapter, the type of a variable can change dynamically during the 
lifetime of a program.

Other languages, like Java and C/C++, are
*statically-typed* and require the programmer to specify the type of
*every* variable. For example, in Java we would need to declare the
variable like this::

    String message = "Hello, world!";
    
In a statically-typed language, once the type of a variable is set, 
it remains the same for the remainder of the program's lifetime.



Integers
~~~~~~~~

An integer is a number without a fractional component. We can use the assignment
operator to assign an integer value to a variable:

.. python-run::

   a = 5
   b = -16
   
In the above code, ``5`` and ``-16`` are what we call *literal values*, in the sense
that ``5`` is *literally* the integer 5, while ``a`` is the *symbolic* name
of a variable. Note how we can also specify *negative* integers.

Right now, there is not much we can do with integers, other than print them:

.. python-run::

   print(a)
   print(b)

As we will see soon, we will also be able to perform common arithmetic operations
with integers.


Real numbers
~~~~~~~~~~~~

Similarly, we can also assign real numbers to variables:

.. python-run::

   x = 14.3

Computers, however, can only represent real numbers up to a finite
precision.  In other words, while there are infinitely many real
numbers between 0.0 and 1.0, computers can only represent a finite
subset of those numbers. Similarly, :math:`\pi` has infinitely many decimal
places (3.14159265359...) but a computer can only store a finite
number of them.

Computers store real numbers using an internal representation called 
*floating point*. In fact, these numbers are commonly referred to as
*floats* in programming languages. The floating point representation 
*approximates* the value
of the real number and may not always store its exact value. For example,
the number ``2.0`` could, in some cases, be represented internally as ``1.99999999999999``.

Integers, on the other hand, use an *exact* internal representation. 
The *range* of integers that can be represented is still finite, 
but the internal representation of an integer is always an exact value. 
For example, the integer ``2``, if stored in a variable, will always be 
exactly ``2`` (instead of an approximation
like ``1.99999999999999``).

The difference between an integer literal and a floating point literal is the presence
of a decimal point. If a decimal point is present in the number, it will be 
represented internally as a floating point value, even if the fractional 
part is zero. Otherwise, it will be represented
as an integer.

For example:

.. python-run::

    x = 15.0
    b = 15
    print(x)
    print(b)

Conceptually, ``x`` and ``b`` both store the name number (fifteen), but they 
have different types: ``x`` is a float and ``b`` is an integer. Python actually
has a built-in ``type`` function that will tell us the exact type of a variable:

.. python-run::

   print(x)
   type(x)
   print(b)
   type(b)


.. technical-details::

   Types are represented using classes in Python, which is why the
   output of the ``type`` function says ``<class 'float'>`` rather
   than ``<type 'float'>`` or simply ``'float'``.  We will introduce
   classes later in the book.

This function also allows us to see how Python is able to recognize
the type of a variable has changed dynamically based on the value it
stores:

.. python-run::

   c = 10
   type(c)
   c = 10.5
   type(c)

Notice how variable ``c`` first stored an integer, but then switched to being
a ``float`` variable once we assigned a float to it.

Strings
~~~~~~~

We have already seen one way to assign a string value to a variable:

.. python-run::

   message = "Hello, world!"
   
One thing to note, though, is that the value that is associated with the
variable does not include the quotation marks. The quotation marks are simply
used to delimit the start and end of the string literal. This is why the 
quotation marks are not included when we print a string variable:

.. python-run::

   print(message)
   
But are included when we supply the name of the variable to the
interpreter:

.. python-run::

   message

The result of evaluating the name ``message`` includes the quotation
marks to indicate that the value is a string.

You can also use single quotes to delimit the start and end of a string literal:


.. python-run::

   message2 = 'Hello, universe!'
   
When using single or double quotes, the string cannot span multiple lines. Instead,
you can use triple-quotes (either three single quotes or three double quotes) to specify
strings that span multiple lines:

.. python-run::

   message3 = """This message
   spans multiple
   lines"""
   print(message3)
   message4 = '''And
   this
   one
   does
   too!'''
   print(message4)

When a user is writing a piece of code that spans multiple lines, 
the interpreter
will use three periods ``...`` to indicate that it is expecting more code
before it can run anything. 

You might reasonably wonder why there are so many different ways to
delimit a string.  One answer is that having different methods makes it
easier to include quotation marks in your strings.  For example, I
might want to have a string to represent the sentence: ``He said,
"Hello world!"``.  I can represent this value in Python using single
quotes ``'He said, "Hello world"'``.  Because we are using single quotes
to delimit the string, the two occurrences of ``"`` inside the string
are treated as normal characters that have no special meaning.  In
other languages, we would need to use a special pair of characters ``\"``,
known as an escape sequence, to indicate that the inner quotes are
part of the value.

Finally, note that you must always use some type of quotes to delimit the start
and end of a string. If you don't, Python cannot distinguish between a 
string literal and a variable name. For example, try this: 

.. python-run::

   message5 = Hello
   
When Python interprets the above code, it will assume that ``Hello``
is a the name of a variable, not a string. And since we haven't
defined a ``Hello`` variable, we will get a ``NameError`` telling you
as much.


F-strings
~~~~~~~~~

In addition to regular strings, Python provides f-strings (or more
formally, formatted string literals) as a way to construct a string
from a combination of basic text and computed values.  An f-string is
a string that has a lower-case or upper-case ``f`` before the opening
quotation mark and can contain one or more expressions enclosed in
curly braces in addition to regular text.

Python converts an f-string into a regular string by evaluating each
expression in curly braces and then replacing it, including the
curly braces, with the resulting value.  Here is an example:

.. python-run::

   x = 5
   y = 6
   print(f'The value of x is {x} and the value of y is {y}.')

Notice that Python replaced ``{x}`` with ``5``, the value of the
variable ``x``, and ``{y}`` with ``6``, the value of variable ``{y}``.

The code in the curly braces can be more complex than just a variable
name.  In general, it can be an arbitrarily complex expression.  For
example:

.. python-run::

   x = 5
   y = 6
   print(f'The value of x * y is {x * y}.')

F-strings also allow users to specify how to format the result of
evaluating the expression. We'll discuss this aspect of f-strings
later in :ref:`string_formatting`.


Booleans
~~~~~~~~

Variables can also contain a *boolean* value. This value can be 
either ``True`` or ``False``:

.. python-run::

   a = True
   print(a)
   b = False
   print(b)
   
As we noted earlier, Python is case sensitive, which means that capital
letters in ``True`` and ``False`` are required.  Typing ``true`` into
the Python interpreter, yields an error

.. python-run::

   true   

because Python interprets ``true`` as the name of a non-existent
variable, rather than as a boolean value.

Right now, there's not much we can do with boolean variables or values, 
but we'll see soon that they'll come in handy.

The value ``None``
~~~~~~~~~~~~~~~~~~

Sometimes, we may want to define a variable but not assign any 
value to it just yet.
In some cases, we can simply assign a reasonable default value to a variable. For
example, if we're writing a program to process sales, we may need to apply
a discount in certain cases (e.g., a client who is part of a loyalty program).
This program could include a variable to store the total discount, and
we could simply initialize it to zero:

.. python-run::

   discount = 0.0
   
If it turns out no discounts are applicable, then the default value of zero works well.

In some cases, however, we need to distinguish *absent* values
explicitly. For example, suppose a survey includes an optional
question where a customer can specify the number of children in their
household (which could be used for demographic classification
purposes). A default value of zero wouldn't work in this case, because
we would need to distinguish between "the customer didn't provide a
value" and "the customer did provide a value, and it is zero". We
would need some way of indicating that a variable simply has no
value. In Python, we can use the special value ``None``:

.. python-run::

   num_children = None
   
Besides using ``None`` directly in our programs, we will also see that there are a number of Python
operations that will use ``None`` to indicate that the operation did not produce any value at all.

Not all programming languages have this kind of special value. In languages 
without the special value ``None``, a variable would be assigned 
an *impossible* value instead. For example, we could assign a value of ``-1`` to ``num_children`` 
because it is impossible for someone to have "negative one" children and thus 
that value would actually mean that "``num_children`` has no value". 
You may encounter this convention now and then but, 
in Python, you should remember to use ``None`` to indicate the absence 
of a value.

.. technical-details:: 

   Since we mentioned that every value has a type, you might be
   wondering about the type of ``None``.  It has the type
   ``NoneType``, which has exactly one value: ``None``.


Scalar types
~~~~~~~~~~~~

Atomic values, those of type ``int``, ``float``, ``bool``, and
``NoneType`` plus values from a couple of types--``complex`` and
``bytes`` --that we will not discuss, are often referred to as
*scalars*.  If you have experience with linear algebra, you might
recognize this term as referring to a value that has a magnitude but
no direction (as opposed to a vector which has both a magnitude and a
direction).  If you don't have experience with linear algebra, just
remember that the term scalar is used to mean a single value--like
``5``, ``5.0``, or ``True`` --that cannot be broken into smaller
components.


Expressions
-----------

Now that we've seen variables, some basic types, and their corresponding literals, we can
combine them together into *expressions*. An expression is a piece of Python code
that gets *evaluated* to produce a new value. For example, we can combine integer literals using simple arithmetic
operators to produce new integer values. For example:

.. python-run::

   2 + 2

Note that whenever you enter an expression in the Python interpreter,
the interpreter will evaluate the expression and then print out the
resulting value.
   
We can also assign the result of evaluating an expression to a variable:

.. python-run::

   a = 2 + 2
   print(a)
   
And we can use variables in expressions themselves. For example, we
can add an integer literal and an integer variable:

.. python-run::

   a = 10
   a + 5

Or we can add two integer variables:

.. python-run::

   a = 10
   b = 20
   a + b
   
We will focus on only two types of expressions for now: arithmetic expressions,
which produce integer or float values, and boolean expressions, which produce
a boolean value.

For arithmetic expressions, addition, subtraction, multiplication (``*``) 
and division (``/``) work pretty much like you would expect them to:

.. python-run::

   2 + 2
   10 - 3
   3 * 3
   10 / 3
   
Notice, however, that division will always produce a floating point number even when
its operands are integers, *even* if the divisor evenly divides the dividend:

.. python-run::

   9 / 3

We can verify this claim using the ``type`` function that we
introduced earlier as a way to determine the type of a variable.  When
this function is used with an expression, Python will first evaluate
the expression and *then* determine the type of the result.


.. python-run::

   type(9 / 3)


When an integer result is desirable, we can use *integer division*:

.. python-run::

   10 // 3
   type( 10 // 3)

While the previous example suggests that this operator, known as *floor division*, just throws
away the fractional part of the result, it actually rounds down towards negative infinity:

.. python-run::

   - 10 // 3
     
There is also a *modulus* operator that will produce the remainder of
dividing two integers:

.. python-run::

   10 % 3

And an exponentiation operator that will raise a value to a power:

.. python-run::

   2 ** 3
   
When an expression contains multiple operators, Python evaluates the
operations in a specific order based on their relative
*precedence*. Most notably, multiplication and division are always
performed before addition and subtraction, so the expression
``10 - 2 * 3`` is equivalent to :math:`10 - (2 \cdot 3)`:

.. python-run::

   10 - 2 * 3
   10 - (2 * 3)


In technical terms, we say that multiplication and division have
*higher* precedence than addition and subtraction or alternatively, we
could say that addition and subtraction have *lower* precedence than
multiplication and division.  We will describe Python's precedence
rules in more detail below after we have introduced a few more
operators.

If we want to force a different order of evaluation, we can use parentheses:

.. python-run::

   (10 - 2) * 3
   10 - (2 * 3)

All of the above operators are *binary* operators, meaning that they operate
on two operands (one on the left and one on the right). Python also has
*unary* operators that operate on a single operand. For example,
unary negation will take an expression that evaluates to a number, and will
produce its negative value:

.. python-run::

   - (3 - 5)
   - (10 / 3)
   - (10 / -3)

When an arithmetic expression involves both integers and floats, the
entire expression will yield a float, *even* if the float's fractional part is
zero:

.. python-run::

   1 + 3.2
   2 * 3.0


The expressions we have seen that operate on numbers all produce a numeric value, but we can 
also use *relational operators* on numbers. These include operators such as "greater than" (``>``), 
"greater than or equals" (``>=``), "less than" (``<``),
"less than or equals" (``<=``), "equals" (``==``), and "not equals" (``!=``) to compare two
values. The result of the comparison will be a boolean value: ``True`` or ``False``. For example:

.. python-run::

   10 > 5
   100 < 2
   7 >= 7
   42 <= 37
   5 == 5
   5 != 5
   10 == 6
   10 != 6

Either side of the relational operator can be a literal value, a variable, or 
*any* expression that produces a number. For example:

.. python-run::

   a = 5
   5 + 5 < a * 3
   
In the above expression, the left side of the ``<`` evaluates to 10,
and the right side evaluates to ``15``, meaning that the comparison
becomes ``10 < 15`` (which evaluates to ``True``).  We do not
need to enclose the expressions ``5 + 5`` and ``a * 3`` in parenthesis because relational operators have lower precedence than arithmetic operators. 
Whether or not to include them for clarity is largely a matter of personal preference.


The equality and inequality operators can also be used with the value
``None``:

.. python-run::

   num_children = None
   tax_rate = 15.0
   num_children == None
   tax_rate == None

Python also includes two operators, ``is`` and ``is not``, that are
similar, but not identical, to ``==`` and ``!=``:

.. python-run::

   a is 5
   a is not 10
   num_children is None
   tax_rate is None
   tax_rate is not None

The differences between ``==`` and ``is`` are very subtle and we will not 
concern ourselves with them here.
However, by convention, ``==`` and ``!=`` are used to compare integers, 
floats, strings, and booleans, while ``is`` and ``is not`` are used to 
check whether a value is ``None`` or not. Later in the book, we will see
that there are differences between these operators that become important when the operands have more complex Python data types, such as lists.

On top of all this, we can combine boolean expressions using *logical* operators, where
each side of the operator must evaluate to a boolean value. The ``and`` 
operator evaluates to ``True`` if both sides of the operator evaluate 
to ``True`` and evaluates to ``False`` otherwise:

.. python-run::

   a = 10
   b = -5
   a > 0 and b > 0
   
The above expression checks whether both ``a`` and ``b`` are positive
non-zero numbers. Since ``b`` is not, the whole expression evaluates
to ``False``.

The ``or`` operator evaluates to ``True`` if either or both sides of the operator evaluate to ``True``,
and evaluates to ``False`` only if both sides of the operator are ``False``. For example:

.. python-run::

   a = 10
   b = -5
   a > 0 or b > 0
    
The above expression evaluates to ``True`` if ``a`` is a positive non-zero 
number, if ``b`` is a positive non-zero number, or if both ``a`` and ``b`` are 
positive non-zero numbers. Since ``a`` is positive, the expression evaluates 
to ``True``.  This operation is known as *inclusive or*, because it "includes" 
as ``True`` the case where both operands are true.

Finally the ``not`` operator takes only a single operand on its right side and negates a boolean value. For example:

.. python-run::

   a = 10
   b = -5
   not (a > 0 and b > 0)
   
The above expression yields ``True`` when either ``a`` or ``b`` are negative or zero, but
``False`` if they are both positive and non-zero. In other words, it yields
the opposite of the expression that we saw earlier.

At this point, while you can probably relate to the need to compute
the value of an arithmetic expression, you may be wondering about the
purpose of boolean expressions. We will see in the next chapter that
boolean expression will be used to determine whether an action has to
be performed or not, or for how many times an action should be
repeated. For example, if you are writing a stock-trading application,
you might need a way to express that a given stock should be sold *if*
its price (stored in a variable called ``price``) reaches or exceeds a
certain target price (stored in a variable called ``target_price``).
The boolean expression that controls this action could look something
like this:

.. code:: python

   price >= target_price
   
We can combine different logical operations to describe complex rules.
For example, in the United States Senate, a bill can be brought to the
floor for debate in a few ways:

- all of the senators present in the chamber agree on a *motion to proceed*, also known as unanimous consent, or
- at least 60 senators vote in favor of a motion to proceed, or
- a quorum of at least 51 senators is present, a majority of the senators present vote in favor of a *motion to proceed*, and the bill either is not or cannot be filibustered (defined roughly as "talked to death"), or
- a quorum is present, half the senators present vote in favor of a *motion to proceed*, the bill either is not or cannot be  filibustered, and the Vice President is present and votes in favor of the motion to proceed.

Given variables for:

- the number of votes in favor of the motion to proceed (``num_yea``), 
- the number of votes against proceeding (``num_nay``), 
- a boolean that indicates whether the bill is being filibustered (``is_filibuster``), and
- a boolean that indicates whether the Vice President in present and votes "yea" (``is_vp_yea``).

and a couple of constants:

.. code:: python

   FILIBUSTER_LIMIT = 60
   QUORUM = 51

we can translate these rules into a boolean expression:

.. code:: python

     (num_yea >= FILIBUSTER_LIMIT) or \
     ((num_yea + num_nay > QUORUM) and \
      (not is_filibuster) and \
      ((num_yea > num_nay) or ((num_yea == num_nay) and is_vp_yea)))

This expression is long. To prevent the line of code from getting too
long to read easily, we split it across multiple lines using backward
slash (``\``) to indicate that the expression continues on the next
line.  Alternatively, we could have wrapped the whole expression in
parentheses:

.. code:: python

     ((num_yea >= FILIBUSTER_LIMIT) or 
      ((num_yea + num_nay > QUORUM) and 
       (not is_filibuster) and 
       ((num_yea > num_nay) or ((num_yea == num_nay) and is_vp_yea))))

We could have chosen to use the numbers 60 and 51 in the expression
directly, but it is better to give these types of values names rather
than have them appear as *magic numbers* in an expression.  It is
traditional to name *constants*, that is, variables whose values are
fixed and will not change during the lifetime of a program, using
capital letters.

You might notice that we did not include a special case for unanimous
consent.  We handle this case by setting ``num_yea`` equal to the
filibuster limit and ``num_nay`` to zero.  Alternatively, we could
introduce a new boolean variable, ``unanimous_consent`` for tracking
this situation and add a new clause to the expression:

.. code:: python

   (unanimous_consent or 
    (num_yea >= FILIBUSTER_LIMIT) or 
    ((num_yea + num_nay > QUORUM) and 
     (not is_filibuster) and 
     ((num_yea > num_nay) or ((num_yea == num_nay) and is_vp_yea))))


Notice that we wrote ``unanimous_consent`` rather than
``unanimous_consent == True`` for the new clause that we added to the
expression.  The latter form frequently appeals to new programmers,
but adding ``== True`` is redudant and should be avoided.  We'll come
back to the appropriate values for ``num_yea``, ``num_nay``, etc in
the case that the senators approve the motion to proceed by unanimous
consent shortly.

.. technical-details:: Operator precedence

   You might be asking yourself whether all the parentheses in the
   expression above necessary?  To answer that question we need to
   understand the relative precedence of the different operations used
   in the expression.  Here is a subset of Python's precedence rules
   taken from `Operator Precedence section
   <https://docs.python.org/3/reference/expressions.html>`_ of the
   Python Language Reference.

   +------------------------------------------------------------------+----------------------------+
   | Operator                                                         | Description                |
   +==================================================================+============================+
   | ``**``                                                           | exponentiation             |
   +------------------------------------------------------------------+----------------------------+
   | ``-x``, ``+x``                                                   | unary negation, unary plus |
   +------------------------------------------------------------------+----------------------------+
   | ``*``, ``/``, ``//``, ``%``                                      | multiplication, division,  |
   |                                                                  | floor division, remainder  |
   +------------------------------------------------------------------+----------------------------+
   | ``+``, ``-``                                                     | addition, subtraction      |
   +------------------------------------------------------------------+----------------------------+
   | ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``, ``is``, ``is not`` | relational, comparison,    |
   |                                	                              | and identity operations    |    
   +------------------------------------------------------------------+----------------------------+
   | ``not x``                                                        | logical negation           |
   +------------------------------------------------------------------+----------------------------+
   | ``and``                                                          | logical and                |
   +------------------------------------------------------------------+----------------------------+
   | ``or``                                                           | logical (inclusive) or     |   
   +------------------------------------------------------------------+----------------------------+

   Operators higher in the table have higher precedence than operators
   lower in the table.  For example, exponentiation has higher
   precedence than unary negation.  Operators in the same row have the
   same precedence and are evaluated left to right if they occur
   together.  For example, the expression ``2 / 3 * 4`` is equivalent
   to ``(2 / 3) * 4``.  Similarly, with the exception of
   exponentiation, multiple instances of the same operator are
   evaluated left to right, so the expression ``2 / 3 / 4`` is
   equivalent to ``(2 / 3) / 4``.  Exponentiation, in constrast, is
   evaluated right to left, so the expression ``2 ** 3 ** 4`` is
   equivalent to ``2 ** (3 ** 4)``.

   In addition to saying that one operator has higher precedence than
   another, programmers also use the phrase *binds more tightly* to
   mean that one operator has higher precedence than another. For
   example, multiplication binds more tightly than addition.

   Since arithmetic operations bind more tightly than relational
   operations, which in turn, bind more tightly than logical
   operations, we can write the expression for describing when a bill
   can be brought to the floor of the United States Senate for debate
   with many fewer parenthesis:

   .. code:: python

        num_yea >= FILIBUSTER_LIMIT or \
        num_yea + num_nay > QUORUM and \
        not is_filibuster and \
        (num_yea > num_nay or num_yea == num_nay and is_vp_yea)

   Only one set--those around the expression ``num_yea > num_nay or
   num_yea == num_nay and is_vp_yea``--is required to express the
   rules of the senate. As noted earlier, whether to include the rest
   of the parentheses or not is largely a matter personal preference.
   

As noted, the operands for nearly all binary operators evaluated left
to right.  Logical operators exploit this evaluation order to provide
a very useful feature: they *short circuit*, that is, if the value of
the left operand determines the result of the operation (``True`` for
``or``, ``False`` for ``and``), then the right operand is not
evaluated.  For example, given the expression:

.. code:: python

   (y != 0) and (x % y == 0)

the subexpression ``(x % y == 0)`` will not be evaluated if ``y`` has
the value zero.  Why?  Because if ``y`` is zero, then the result of
the ``and`` is guaranteed to be ``False``.  Conveniently, short circuiting
allows us to avoid dividing by zero in this case.

This property of ``and`` and ``or`` makes the order of the operands
important. This expression:

.. code:: python

   (x % y == 0) and (y != 0) 

will fail with a ``ZeroDivisionError`` error when ``y`` is zero,
because the left operand is evaluated first.

Now that we have discussed short circuiting, let's return to the
filibuster example:

.. code:: python

   (unanimous_consent or 
    (num_yea >= FILIBUSTER_LIMIT) or 
    ((num_yea + num_nay > QUORUM) and 
     (not is_filibuster) and 
     ((num_yea > num_nay) or ((num_yea == num_nay) and is_vp_yea))))

Python will stop evaluating this expression as soon as one of the
three ``or`` clauses evaluates to ``True``.  As a result, the values
of ``num_yea``, ``num_nay``, etc can be set to zero or to ``None`` or
not at all, for that matter, if ``unanimous_consent`` is true.


     

String expressions
~~~~~~~~~~~~~~~~~~

Strings also support many of the operations we just described.
Addition, for example, works with strings and results in the
concatenation, or joining, of those strings:

.. python-run::

   "abc" + "def"
   name = "Alice"
   "Hello, " + name

One thing to note: while you can mix integers and floats when using
the addition operator, mixing integers and strings generates a type
error:

.. python-run::

   tax = 15.0
   "Your tax rate is " + tax

We will describe a solution to this problem in the next section.

The equality and identity operations can also be used on strings:

.. python-run::

   name = "Alice"
   name == "Bob"
   name != "Bob"
   name == "Alice"
   name is "Alice"
   name is not "Bob"

.. common-pitfalls:: Mixing types with the equality operator

   While, as we noted, you cannot mix strings and numbers when using
   arithmetic operations, such as addition, you *can* mix types when
   using the ``==`` and ``!=`` operators, but be careful: they 
   check whether the two values have the same type. For example:

   .. python-run::

       5 == "Hello"

   Naturally, the result is ``False``: the number 5 is not the same as
   the string ``"Hello"``. However, evaluating this expression is also
   yields ``False``:

   .. python-run::

       10 == "10"

   When comparing two values of a different type, Python won't make
   any attempt to convert one to the other's type before making the
   comparison. Instead, the above expression returns ``False`` because
   an integer is not the same thing as a string, even if semantically
   they refer to the same thing.

The relational operations can also be used on strings:

.. python-run::

   "Alice" < "Bob"
   "Alex" > "Alice"

The relational operators use lexicographic ordering when used to
compare strings: the result of the operation is determined by
comparing the first two characters that differ.  In the first example,
the strings differ in the first character and "A" comes before "B" and
so, the result of evaluating ``"Alice" < "Bob"`` is ``True``.  In the
second example, the strings differ first at the third character and
since "e" does not come after "i", the result of evaluating the
expression is ``False``.

.. technical-details:: Character encoding and relational operators

   What does it mean for one character to "come before" another?
   Strings in Python are represented using a *character encoding*
   which associates each individual character (like ``A`` and ``B``)
   with an integer value.  You can actually see that integer value by
   using the built-in ``ord`` function:

   .. python-run::

      ord("A")
      ord("B")
      ord("ñ")
      ord("🤔")

   Notice how ``A`` has a lower numerical value than ``B``, so it is
   considered to come before ``B``. Also, notice how letters from
   other alphabets, such as ``ñ`` from the Spanish alphabet, and
   emojis are valid characters in Python. This is
   because the default character encoding in Python is Unicode, which
   supports a wide array of characters, including practically all
   non-English characters.

   If you are working with English language text (or, more specifically,
   with the 26-letter Roman alphabet), then in practice,
   you do not need to be concerned with this technical detail. When it
   comes to the relational operators and strings, you can assume they
   support the standard English dictionary ordering on strings. 
   
   If you are working with text that includes characters outside the 
   26-letter Roman alphabet, the ordering created by the Unicode encoding 
   may not always produce the expected result. For example, in Spanish, 
   the letter ``ñ`` comes after ``n`` and before ``o``, which means
   the word ``original`` must come after ``ñoño``. However:
   
   .. python-run::
   
      "original" > "ñoño"
      
   Ordering string can thus get a bit complicated in these cases, and
   often requires the use of external libraries, like `PyICU <https://gitlab.pyicu.org/main/pyicu>`__.

We have only described a small subset of the operations supported by
strings here.  We discuss lots more later in :ref:`chapter-lists`.


Casting
-------

There are times when we need to convert a value from one type to
another. For example, we might get a real number represented as a
string from a user interface and want to compute with that value as a
number. To do so, we first need to convert it from a string to a
floating point value. We convert or *cast* the string into a floating
point value using the ``float`` function:

.. python-run::

   approx_pi = "3.1415"
   x = float(approx_pi)
   x * 2

Or we might want to cast a float into a string (using ``str``) and
then combine it with another string:

.. python-run::

   approx_pi = 3.1415
   s = str(approx_pi) + " is an approximation to Pi" 
   print(s)


When we cast a float to an integer, we not only change the type, we
also change the value by throwing away the fractional part:

.. python-run::

   approx_pi = 3.1415
   int(approx_pi)

Note that throwing away the fractional part is equivalent to rounding
towards zero.  If the value is positive, as in the above example,
``int`` will round it down towards zero.  In contrast, if the value is
negative, ``int`` will round up towards zero:

.. python-run::

   neg_pi = -3.1415
   int(neg_pi)


Dynamic Typing Revisited
------------------------

Now that we've seen some basic types as well as expressions, we can
see some of the implications of dynamic typing in a bit more detail.
Like we said earlier, Python is dynamically-typed, which means it
infers the type of a variable when we assign a value to it. As we saw
earlier, we can see the exact type of a variable by writing
``type(v)`` (where ``v`` is a variable).

Notice that Python correctly infers that ``a`` should be an integer 
(or ``int``), that ``x`` should be a float, and that ``s`` should 
be a string (or ``str``) based on the values supplied on the right-hand side 
of the assignment statements:

.. python-run::

   a = 5
   type(a)
   x = 3.1415
   type(x)
   s = "foobar"
   type(s)
   
Not just that, we can assign a value of one type to a variable and,
later on, assign a value of a different type, and Python will
*dynamically* change the type of the variable. In contrast, a
statically-typed language would likely generate an error pointing out
that you're trying to assign a value of an incompatible type.

.. python-run::

   b = 5
   type(b)
   b = "Hello"
   type(b)


One consequence of this property is that an operation that succeeds
in one line, may not succeed a few lines later.  For example,

.. python-run::

   b = 5
   c = b + 7
   print(c)
   b = "hello"
   c = b + 7

The first time we evaluate the expression ``b + 7``, the evaluation
succeeds and yields the value ``12``.  The second time, however, the
evaluation fails, because ``b`` is now a string and we cannot add a string 
and an integer.

When working with a dynamically-typed language like Python, we must be
careful to use types consistently. Just because a variable can change
its type throughout the lifetime of a program doesn't mean it
should. As you take your first steps with Python, you should try to be
disciplined about choosing a type for a variable and then sticking
with it throughout the program.
   
Code Comments
-------------

Before we move on to the next chapter, there's one final element of Python 
syntax we need to discuss: code comments. When writing code in a Python file, you can include notes for the reader, known as *comments*, in your 
code using the hash character, and Python will ignore everything that appears
after the hash character:

.. code:: python

   # This is a comment
   a = 5
   
   # This is a comment that
   # spans multiple
   # lines
   b = 5
   
   c = a + b  # Comments can also appear at the end of lines
   

You will see comments in many of the examples we will provide, 
and it is good practice to use comments to document your code, 
especially when your code is not self-explanatory.


   
