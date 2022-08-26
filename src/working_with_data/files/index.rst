Working with Files
==================

A very common programming pattern proceeds as follows:

#. Read the contents of one or more files from disk and load the data into one or more data structures.
#. Manipulate the data in some way.
#. (Optional) Write the resulting data back to disk.

Programmers often connect multiple programs written using this pattern
into data-processing pipelines.

In this chapter, we'll discuss how to work with several different file
formats.  We'll start with the most basic mechanisms and work our way
up to higher-level tools and more complex formats.

Basic file I/O 
--------------

Reading file input and writing file output is often referred to as
I/O, or input/output.  We'll start our discussion of basic file I/O
with a simple example: load the contents of the text file
``instructor-email.txt`` into a sorted list.  Here are the contents of
the file:

::

    amr@cs.uchicago.edu
    borja@cs.uchicago.edu
    yanjingl@cs.uchicago.edu
    mwachs@cs.uchicago.edu
    dupont@cs.uchicago.edu

and here's the desired result::

    ["amr@cs.uchicago.edu",
     "borja@cs.uchicago.edu",
     "dupont@cs.uchicago.edu",
     "mwachs@cs.uchicago.edu",
     "yanjingl@cs.uchicago.edu"]

To access the contents of a file, we first need to open it using the
built-in function ``open``:

.. python-run::

    f = open("instructor-email.txt")

The ``open`` function returns a data structure, known as a *file
pointer*, that we can use to work with the contents of the file.  It is
common to use the word *file* to refer to both a file on disk and a file
pointer.

Once we have a file pointer, we can perform a number of
operations on it.  In a sense, text files are simply very long strings
that are stored on disk.  So, for example, we can read the entire
contents of the file into a string in a single operation using the
``read`` method:

.. python-run::

    s = f.read()
    s

The characters ``\n`` are what is known as an *escape sequence*, which
in this case encodes the newline character. Notice that if we print
the value of ``email_address``, all of the occurrences of the ``\n``
escape sequence are converted into newlines as expected:

.. python-run::

   print(s)

We can convert the string into a list of email addresses using the
string ``split`` method, which, by default, breaks the string into
tokens using white space (that is, spaces, tabs, newlines, etc.) as a
the delimiter.

.. python-run::

   s.split()

Finally, we can call the built-in function ``sorted`` to to get the
desired result: a sorted list of email addresses:

.. python-run::

   email_addresses = sorted(s.split())

When reading from a file, the operating system keeps track of the most recent
position it has read. In this case, the file pointer has already
reached the end-of-file (or EOF). So, if we call ``read`` again, we
don't get the contents of the file, we get an empty string instead:

.. python-run::

    data = f.read()
    data


Once we're done working with a file, we need to close the file pointer:

.. python-run::

    f.close()

Following the close, you can no longer use that file pointer to access
the file. (You'd have to reopen the file to use it again.) It is
important to close files to free the associated resources and, as
we'll see later on when writing to files, to ensure that all of your
updates to the file are written to disk.

It is easy to forget to close a file, so it is common to use a
``with`` statement, which guarantees that the file will be closed no
matter what happens in the body of the statement.

.. python-run::

    with open("instructor-email.txt") as f:
        s = f.read()
        email_addresses = sorted(s.split())
    print(email_addresses)

The ``with`` statement introduces a new name, in this case, ``f``,
that refers to the file pointer returned by the call to ``open``.  At
the end of the ``with`` block, file ``f`` is closed automatically.

Instead of reading the file in one chunk, we can also read it line by
line.  One approach is to use a for loop that iterates over a text
file line by line.  For example, here's some code that reads and
prints each line in the ``instructor-email.txt`` file:

.. python-run::

    with open("instructor-email.txt") as f:
        for line in f:
            print(line)

This result may look a bit funny to you.  Why the extra empty line?
Each line from the file includes a newline at the end, and
``print`` adds a newline as well.  We can see the actual representation
of the string using the built-in ``repr`` function:

.. python-run::

    with open("instructor-email.txt") as f:
        for line in f:
            print(repr(line))

When reading lines from a file, we can use the ``strip`` method from the
string library to remove leading and trailing whitespace:

.. python-run::

    with open("instructor-email.txt") as f:
        for line in f:
            print(line.strip())


To accomplish our goal of creating a sorted list of email addresses,
we can combine a familiar pattern for constructing lists with a use of
``with`` and a call to the list ``sort`` method.

.. python-run::

    email_addresses = []
    with open("instructor-email.txt") as f:
        for line in f:
            email = line.strip()
            email_addresses.append(email)

    email_addresses.sort()


Writing data to a file
----------------------

To write to a file, we must open the file in write mode (note the use of
``"w"`` as a second parameter to ``open`` to specify that we're opening
the file in write mode):

.. python-run::
   :formatting: separate

   open("names2.txt", "w")

It is very
important to understand that when you open an existing file in write
mode, *all* of its existing contents will be wiped away! If you open a
file that doesn't already exist in write mode, a new file will be
created.  

Once we have a writable file pointer, we can append a string to the file using
``write``.  For example, after we run this code:

.. python-run::
   :formatting: separate

   with open("names.txt", "w") as f:
       f.write("Anne Rogers\n")
       f.write("Borja Sotomayor\n")
       f.write("Yanjing Li\n")
       f.write("Matthew Wachs\n")
       f.write("Todd Dupont\n")

The file ``names.txt`` will contain:

.. parsed-literal::

   Anne Rogers
   Borja Sotomayor
   Yanjing Li
   Matthew Wachs
   Todd Dupont

We could also use the ``print`` method to generate this output, which
has the advantage that it will add the newline automatically.  The
``file`` keyword parameter allow us to specify a file pointer as the
destination of call to ``print``.


.. python-run::

    with open("names2.txt", "w") as f:
        print("Anne Rogers", file=f)
        print("Borja Sotomayor", file=f)
        print("Yanjing Li", file=f)
        print("Matthew Wachs", file=f)
        print("Todd Dupont", file=f)        

Internally, writes to files are often stored in a buffer
and then written out to disk in batches.  When you close a file, you flush any
buffered data to disk.  If you do not close your file, the data
from the last few writes you do may remain in the buffer and thus
may not get written back to disk.

Let's put these pieces together to write a function that transforms a file
with a list of email addresses into a new file with the domain name
(that is, ``@cs.uchicago.edu``) stripped off.

.. python-run::

    def strip_domain(input_filename, output_filename):
        '''

        Strip the domain names off the email address from the input
        file and write the resulting usernames to the output file.

        Inputs:
	  input_filename: (string) name of a file with email addresses
	  output_filename: (string) name for the output file.
        '''

        # Load data into a data structure (a list of strings)
        email_addresses = []
        with open(input_filename) as f:
            for line in f:
                email = line.strip()
                email_addresses.append(email)
            
        # Transform the data
        usernames = []
        for email in email_addresses:
            username, domain = email.split("@")
            usernames.append(username)
        
        # Write the data
        with open(output_filename, "w") as f:
            for username in usernames:
                print(username, file=f)

In this case, the operation is simple enough that we could've produced
the usernames during the input loop or during the output loop, but in
general, it's good to separate input, transformation, and output into
separate steps.

Python's basic file I/O functionality is sufficient for working with
simple files, but sometimes we need work with more complex data
files. In the next few sections, we'll introduce a few existing data
formats and libraries that it make it easy to work with them.  In
general, it is better to use an existing format and its associated
libraries, if you can, than to invent your own ad hoc format.

CSV
---

The acronym CSV stands for Comma Separated Values. CSV files contain
values separated by commas (and sometimes by other delimiters) and are
typically used to represent tabular data, that is, any data that can
be organized into rows, each with the same columns (or *fields*).

Here are the contents of a CSV file named ``instructors.csv``:

::

    id,lname,fname,email
    amr,Rogers,Anne,amr@cs.uchicago.edu
    borja,Sotomayor,Borja,borja@cs.uchicago.edu
    yanjingl,Li,Yanjing,yanjingl@cs.uchicago.edu
    mwachs,Wachs,Matthew,mwachs@cs.uchicago.edu
    dupont,Dupont,Todd,dupont@cs.uchicago.edu

The first line is the header row; it includes the names of the
columns/fields (``id``, ``lname``, ``fname``, and ``email``). The
remaining lines contain the data.

With what we've seen so far, we could just use the existing file
functions to read this file and generate some simple output:

.. python-run::

    with open("instructors.csv") as f:
        header = f.readline() # Skip the header row
        
        for row in f:
            fields = row.strip().split(",")
            
            id = fields[0]
            last_name = fields[1]
            first_name = fields[2]
            email = fields[3]
            
            print("{} {}'s e-mail is {}".format(first_name, last_name, email))

We could similarly use the existing file functions to write a CSV file.

This process, however, can be very error-prone, and it doesn't account
for a number of peculiarities in the CSV file format e.g., what if a
column holds a string value with a comma in it? Such a value would be
represented in double-quotes, like ``"Hello, world!"``, but the above
code would fail.  To make this concrete, let's look at what, would
happen if we added this line to the file:

.. parsed-literal::

   spade,"Spade, Jr",Sam,spade@cs.uchicago.edu

We'd get:

::

   Jr" "Spade's e-mail is Sam

as the output for this line, because the ``split`` method is not
designed to handle commas embedded in quoted sub-strings.

Fortunately, Python includes a ``csv`` module that allows us to work
with CSV files more naturally.

.. python-run::

    import csv

The ``DictReader`` class allows us to iterate over the rows in a CSV
file, and access each field in a row via a dictionary (with the same
field names specified in the header row or using the optional
``fieldnames`` parameter).

.. python-run::

    with open("instructors.csv") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print("{} {}'s e-mail is {}".format(row["fname"], row["lname"], row["email"]))

We can use a similar class, ``DictWriter``, to write CSV file.

.. python-run::
   :formatting: separate

   fieldnames = ["id", "lname", "fname", "email"]
   
   with open("instructors-122.csv", "w") as f:
       writer = csv.DictWriter(f, fieldnames=fieldnames)
       writer.writeheader()
       
       row = {"id": "amr",
              "lname": "Rogers",
              "fname": "Anne",
              "email": "amr@cs.uchicago.edu"}

       writer.writerow(row)

       row = {"id": "mwachs",
              "lname":"Wachs",
              "fname": "Matthew",
              "email": "mwachs@cs.uchicago.edu"}
      
       writer.writerow(row)


The ``csv`` module also has ``reader`` and ``writer`` classes that use
lists to represent rows rather than dictionaries. This allows us to
interact with the fields positionally instead of by name.

JSON
----

JSON (JavaScript Object Notation) is a *lightweight* data-interchange
format that web services commonly use.  It is also used as a
data storage format.  JSON supports a few different types:

-  Object: looks like a python dictionary with string-value pairs (string:value) separated by commas,
-  Array: empty list or list of values,
-  Value: string, number, object, array, true, false, null

Note the nesting of object and array in the definition of value.

An application might receive a string in JSON format from another
application, like a web service, or as a file.  Python has a ``json``
module for handling JSON data in either form.  We'll start by looking
at the functions that operate on strings, but first, we need to import
the library.

.. python-run::

    import json

The ``dumps`` function takes a Python data structure and encodes it in
JSON format:

.. python-run::

    l = ['baz', None, 1.0, 2]
    json.dumps(l)

Notice that the result is a string representation of the data, with
some minor differences from Python (e.g., "null" instead of "None")

JSON allows for nested data structures and, so, the
``dumps`` function handles them as well:

.. python-run::

    data = [ 'foo', {'bar': l} ]
    json.dumps(data)

The ``loads`` function takes a string containing data encoded
in JSON format and decodes it, yielding the corresponding Python data
structures:

.. python-run::

   json.loads("42")

.. python-run::

   json.loads("[1,2,3]")

.. python-run::

   json.loads('["foo", {"bar": ["baz", null, 1.0, 2]}]')

The ``load`` and ``dump`` functions perform analogous operations, but
on files.  The ``dump`` function takes two arguments---an appropriate
data structure and a file pointer---and writes a JSON encoding of the
data structure to the file.  Here's a sample call:

.. python-run::

   with open("saved_data.json", "w") as f:
      json.dump(data, f)

that yields a file named ``saved_data.json`` with contents of:

.. parsed-literal:: 

   ["foo", {"bar": ["baz", null, 1.0, 2]}]

For a large and complex data structure, the standard encoding can be 
hard to read. You can use the optional ``indent`` parameter, which
allows you to specify the number of spaces to indent for each level of
nesting, and the ``sort_keys`` parameter to generate output that is
easier to read.  This code, for example,

.. python-run::

   with open("saved_data.json", "w") as f:
      json.dump(data, f, indent=4, sort_keys=True)

yields a version of ``saved_data.json`` with the following contents:

.. parsed-literal::

   [
       "foo",
       {
           "bar": [
               "baz",
               null,
               1.0,
               2
           ]
       }
   ]   


The ``load`` function takes a file pointer, reads the data from the
file, and returns the decoded data structure:

.. python-run::

   saved_data = None
   with open("saved_data.json") as f:
       saved_data = json.load(f)
   saved_data


YAML
----

YAML (YAML Ain't Markup Language) is, like JSON, a lightweight data
format that is intended to be both machine-readable and
human-readable.  It uses indentation rather than braces and brackets
to represent nesting.  We won't describe this format in detail, other
than to point out that these files are easy to read and to process
automatically.

YAML is often used for configuration files, as well as files that
need to be processed by a program, but also need to be readable
by a non-technical user. For example, the following ``rubric.yml`` file could
be used to provide the results of grading a programming assignment:

.. parsed-literal::

    Points:
        Tests:
            Points Possible: 50
            Points Obtained: 45

        Implementing foo():
            Points Possible: 20
            Points Obtained: 10

        Implementing bar():
            Points Possible: 20
            Points Obtained: 20

        Code Style:
            Points Possible: 10
            Points Obtained: 7.5

    Penalties:
        Code comments are written in Old English: -5

    Bonuses:
        Worked alone: 10

    Total Points: 87.5 / 100

    Comments: >
        Well done!

As with any library, we need to import the ``yaml`` library before we
can use it:

.. python-run::

    import yaml

We can load a YAML file using ``yaml.load`` with a file pointer:

.. python-run::

    with open("rubric.yml") as f:
        rubric = yaml.load(f)


The result will be a dictionary:

.. python-run::

   rubric

Notice that the nesting of the dictionary reflects the nesting of the
indentation above.



