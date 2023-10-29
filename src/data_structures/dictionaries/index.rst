.. _chapter-dictionaries:

Dictionaries and Sets
=====================

In the previous chapter, we saw that lists allow us to store multiple
values in a single data structure, but they do so in a very specific
way: the values are stored in a sequence. Python makes it very easy to
iterate over that sequence, as well as access items at specific
positions of the list.  This design makes lists a great data structure
for some use cases but not for others.

For example, suppose we were working with data on contributions to political
campaigns, with the following
information for each contribution:

- First name of contributor
- Last name of contributor
- ZIP Code where contributor lives
- Campaign that received the contribution
- Contribution amount

We could represent an individual contribution like this:

.. python-run::
   :formatting: separate

   c = ["John", "Doe", "60637", "Kang for President 2016", 27.50]
   
And a list of contributions like this:

.. python-run::
   :formatting: separate

   contributions = [
       ["John", "Doe", "60637", "Kang for President 2016", 27.50],
       ["Jane", "Doe", "60637", "Kodos for President 2016", 100.00],
       ["James", "Roe", "07974", "Kang for President 2016", 50.00]
       ]
               
Accessing the individual values inside this list requires using their
positions in the list, which can lead to code that is difficult to
read. For example, suppose we wanted to write a function that adds up
all the contributions made to a given campaign. The function would
look something like this:

.. python-run::
   :formatting: separate

   def total_contributions_candidate(contributions, campaign):
       '''
       Compute total contributions to a candidate's campaign

       Inputs:
         contributions (list of lists): one list per contribution
         campaign (string): the name of the campaign

       Returns (float): total amount contributed
       '''

       total = 0
       for contribution in contributions:
           if campaign == contribution[3]:
               total += contribution[4]
       return total
      
.. python-run::

   total_contributions_candidate(contributions, "Kang for President 2016")
   total_contributions_candidate(contributions, "Kodos for President 2016")
          
Using ``contribution[3]`` to access the name of the campaign and
``contribution[4]`` to access the contribution amount makes the code
hard to read. There are ways to make it a bit more readable, such as
defining variables to store the position of each value (e.g., we could
define ``CAMPAIGN_INDEX = 3`` and the access the campaign by writing
``contribution[CAMPAIGN_INDEX``]), but this approach is error-prone. We
could easily use the wrong value for the constant or the format of the data might
change over time.  In the latter case, we would need to check the
fields we are using carefully to ensure that we are still accessing
the correct positions.

For this application, it would be better to use a data structure
called a *dictionary*. Like lists, dictionaries can be used to
store multiple values, but do so by associating each value
with a unique *key* rather than with a position in a sequence.
This arrangement is similar to a physical dictionary: the words
are the "keys" and the definitions are the "values".

We could store an individual contribution in a dictionary like this:
 
.. python-run::
   :formatting: separate

   d = {"first_name": "John",
        "last_name": "Doe", 
        "zip_code": "60637", 
        "campaign": "Kang for President 2016", 
        "amount": 27.50}
        
Notice that we have a sequence of entries separated by commas where
each entry is a key-value pair separated by a colon. Instead of
accessing values by their positions in the data structure, we access
them by their keys.  For example, if we wanted to access the ZIP Code
of this contribution, we would use the key ``"zip_code"``:

.. python-run::

   d["zip_code"]
   
Because values are accessed by key rather than by position, dictionaries are also
referred to in other programming languages as "associative arrays" or "maps" 
(in the sense that they associate or map a key to a value).

In this example, all of the keys are strings. Although this design is
fairly common, it is not required. In fact, many different Python
types can be used for keys in a dictionary.  For now, we'll restrict
ourselves to types with values that cannot be changed
(i.e. *immutable* types), which includes strings, integers, booleans,
tuples of strings, etc.  We'll come back to the question of acceptable
types for dictionary keys briefly after we introduce Python classes.

While the types used for dictionary keys are restricted, the values
can have any type and different keys can have values with different
types.  Notice, for example, that not all of the keys in our example
have values with the same type: the value for ``"amount"`` is a float,
while the rest are strings.
   
Our list of contributions would now look like this:

.. python-run::
   :formatting: separate

   contributions = [
      {"first_name": "John",
       "last_name": "Doe", 
       "zip_code": "60637", 
       "campaign": "Kang for President 2016", 
       "amount": 27.50},
      {"first_name": "Jane",
       "last_name": "Doe", 
       "zip_code": "60637", 
       "campaign": "Kodos for President 2016", 
       "amount": 100.00},
      {"first_name": "James",
       "last_name": "Roe", 
       "zip_code": "07974", 
       "campaign": "Kang for President 2016", 
       "amount": 50.00}
   ]       
   
And our function to compute the total contributions now looks like
this:

.. python-run::
   :formatting: separate

   def total_contributions_candidate(contributions, campaign):
       '''
       Compute total contributions to a candidate's campaign

       Inputs:
         contributions (list of dictionaries): one dictionary per
           contribution
         campaign (string): the name of the campaign

       Returns (float): total amount contributed
       '''

       total = 0
       for contribution in contributions:
           if campaign == contribution["campaign"]:
               total += contribution["amount"]
       return total
      
.. python-run::

   total_contributions_candidate(contributions, "Kang for President 2016")
   total_contributions_candidate(contributions, "Kodos for President 2016")

The new function looks very similar to the original, but it is easier
to read and maintain.  

Dictionaries do more than simply provide convenient syntax for
accessing values by key instead of position.  As we’ll see later in
the chapter, dictionaries can also perform certain operations much
more efficiently than lists and allow us to implement certain
algorithms more elegantly.

It is very common to use a dictionary to represent a single "object"
(in this case, a single contribution to a campaign, with each
attribute of the contribution represented by a key in the dictionary),
especially when exchanging data between different systems. In fact,
later in the book, we will see a data format, JSON, that works well
with Python dictionaries and lists. Later on, we will also see how
*object-oriented programming* provides a third way of working with
"objects" in our programs.

.. admonition:: A possible pitfall: floats as keys

   Before we move on talking about useful dictionary operations, we'd
   like to stop and consider a simple example an example that may
   surprise you:

   .. python-run::
   
      d = {0.3: "found"}
      d.get(0.1 + 0.1 + 0.1, "not found")

   Using your understanding of real numbers, you might expect ``get``
   to return ``"found"``, the value associated with ``0.3``.  Using
   floats, however, ``0.1 + 0.1 + 0.1`` does not equal ``0.3`` and so,
   ``get`` does not find the key in the dictionary and returns the
   default value ``"not_found"``.

   So, while you technically use floats as keys for a dictionary, you
   should only do so when you are using values that can be represented
   exactly with a power of two or as the sum of powers of two.


Useful operations with dictionaries
-----------------------------------

Earlier, we saw that we can define a dictionary like this:

.. python-run::
   :formatting: separate

   d = {"first_name": "John",
        "last_name": "Doe", 
        "zip_code": "60637", 
        "campaign": "Kang for President 2016", 
        "amount": 27.50}

And access individual values by their keys like this:

.. python-run::

   d["zip_code"]
   
Note that when we attempt to *access* values in the dictionary, specifying a key
that doesn't exist in the dictionary produces an error:

.. python-run::

   d["affiliation"]

In addition to the square-bracket notation, we can access a value
using the ``get`` method, which method returns ``None`` if the
dictionary does not contain the specified key.

.. python-run::

   st = d.get("first_name")
   print(st)
   st = d.get("affiliation")
   print(st)

The ``get`` method also takes an optional second parameter to specify a default value that
should be returned if the key doesn't exist in the dictionary:

.. python-run::

   d.get("affiliation", "Unknown")


We can check if a dictionary contains a given key using the ``in`` operator:   

.. python-run::

   "first_name" in d
   "affiliation" in d

.. todo::
  
   Should we add "not in" here as well?


Dictionaries are also mutable: we can update the value associated with
a key in a dictionary and add new key-value pairs.  We assign a new
value to a key like this:

.. python-run::

   d["zip_code"] = "94305"
   d["zip_code"]

and add a new key-value pair using the same syntax:

.. python-run::

   d["affiliation"] = "Kodosican"
   d

We can also create a dictionary by starting from an empty (or partial)
dictionary and assigning values:


.. python-run::
   :formatting: separate

   d = {}
   d["first_name"] = "John"
   d["last_name"] = "Doe" 
   d["zip_code"] = "60637" 
   d["campaign"] = "Kang for President 2016" 
   d["amount"] = 27.50
   d["affiliation"] = "Kodosican"

.. python-run::

   d

We can remove an entry in the dictionary using the ``del`` operator:

.. python-run::

   d
   del d["affiliation"]
   d





We can iterate over the keys in a dictionary using the dictionary's
``keys`` method:

.. python-run::

   for key in d.keys(): 
       print(key)

This operation is sufficiently common that Python provides a
shorthand: iterating over the dictionary itself is equivalent to
iterating over the keys.  That is, when you iterate over a dictionary,
the loop variable will iterate over the *keys* of the dictionary:

.. python-run::

   for key in d:
       print(key)

We can also iterate over the values using the dictionary's ``values``
method:

.. python-run::

   for value in d.values():
       print(value)

And, finally, we can iterate over both the keys and the values using
the dictionary's ``items`` method:

.. python-run::

   for key, value in d.items():
       print(key, value)

Notice that the keys and values are not printed in any particular
order. Most notably, the keys are not shown in the order in which they
were added to the dictionary, nor are they printed in alphabetical
order. This behavior is another big difference between
dictionaries and lists: lists store values in a specific order, and
iterating over a list will always yield those values in that
order. There is no such guarantee with dictionaries: if we iterate
over the contents of a dictionary, we cannot assume any specific order
and, in fact, that order can even change from one ``for`` loop to
another!


.. admonition:: A common pitfall: changing the set of keys in a dictionary as you iterate over it

   There is an algorithm that allows us to compute the *K* most
   frequently seen items in a stream of data. We are not going to
   present the whole algorithm here. Instead, we will focus on a
   specific task within that algorithm that is used to exclude keys
   that have not been seen recently: take a dictionary that maps
   strings to positive integers, decrement all the values by one and
   remove any key-value pair where the resulting value is zero.


   You might be tempted to write the following **incorrect** function to do this
   task:

   .. python-run::
      :formatting: separate

      def decr_and_remove(d): 
          ''' 
          Given a dictionary that maps keys to positive integers,
          decrement the values and remove any key-value pair in which
          the decremented value becomes zero

          Input:
             d (dictionary): maps keys to positive integers
          '''

          for key, value in d.items():
              d[key] = value - 1
              if d[key] == 0:
                  del d[key]

   This code is not valid because you *cannot* modify a data
   structure as you iterate over it!  Here's one alternative solution:

   .. python-run::
      :formatting: separate

      def decr_and_remove(d): 
          ''' 
          Given a dictionary that maps keys to positive integers,
          decrement the values and remove any key-value pair in which
          the decremented value becomes zero


          Input: 
             d (dictionary): maps keys to positive integers
          '''

          keys_to_remove = []
          for key, value in d.items():
              d[key] = value - 1
              if d[key] == 0:
                  keys_to_remove.append(key)

          for key in keys_to_remove:
              del d[key]

   Here's another that computes and returns a new dictionary with the
   desired keys rather than removing the keys from the input dictionary.


   .. python-run::
      :formatting: separate

      def decr_and_keep_pos(d):
          '''
          Given a dictionary that maps keys to positive integers,
          subtract one from each value and include in the result only
          those key-value pairs that still have positive values after
          the decrement.

          Input:
            d (dictionary): keys to positive integers

          Returns (dictionary): keys to positive integers
          '''

          rv = {}
          for key, value in d.items():
              if value > 1:
                  rv[key] = value - 1
          return rv


Other ways to construct dictionaries
------------------------------------

As we have seen, we can construct dictionaries using dictionary
literals or updating an empty dictionary with 
new key-value pairs.  We can also construct dictionaries use the
``dict`` function and dictionary comprehensions. 

The ``dict`` function allows us to construct a *new* dictionary from a
variety of different types of values including a list of key-value
pairs or another dictionary.  For example, here are three different
ways to construct the same dictionary: the first uses a dictionary
literal, the second uses a call to ``dict`` with a list of pairs, and
the third uses a call to ``dict`` with a dictionary as the argument.


.. python-run::
   :formatting: separate

   d = {"first_name": "John",
        "last_name": "Doe", 
        "zip_code": "60637", 
        "campaign": "Kang for President 2016", 
        "amount": 27.50}

   keys_and_data = [("first_name", "John"), 
                    ("last_name", "Doe"), 
                    ("zip_code", "60637"), 
                    ("campaign", "Kang for President 2016"),
                    ("amount", 27.50)]

   d_from_list = dict(keys_and_data)

   d_from_dict = dict(d)

Dictionary comprehensions are similar to list comprehensions.  In
place of one transformation expression, dictionary comprehensions require two: one
that yields a key and another that yields a value.  For example,
here's another way to construct our sample dictionary:

.. python-run::

  d = {key: value for key, value in keys_and_data}

This example uses very simple expressions for the key and the value,
but in general, you can use arbitrarily complex expressions for either.
You can also specify a boolean expression to use as a filter.  For
example, we could rewrite the ``decr_and_keep_pos`` function from the
previous section using a dictionary comprehension with a filter:

.. python-run::
   :formatting: separate

   def decr_and_keep_pos(d):
       '''
       Given a dictionary that maps keys to positive integers,
       subtract one from each value and include in the result only
       those key-value pairs that still have positive values after the
       decrement.

       Input:
         d (dictionary): maps keys to positive integers

       Returns (dictionary): maps keys to positive integers
       '''

       return {key: value - 1 for key, value in d.items() if value > 1}

A key-value pair from the input dictionary will be used in the
construction of the result only if the original value is greater than
one.



Accumulating values with dictionaries
-------------------------------------

Dictionaries are often used to accumulate a value based on a key.  For example,
earlier we computed the total number of contributions for a specific
campaign.  What if we wanted to compute the total contributions for
each campaign?  We could call our previous function over and over
again, once per campaign, but there is a better approach.  A
dictionary that maps a campaign's name to the total contributions to
that campaign is a perfect tool for this task.  We start with an
empty dictionary and add new entries as we encounter new campaigns:

.. python-run::
   :formatting: separate

   def total_contributions_by_campaign(contributions): 
       ''' 
       Compute total contributions by campaign

       Input:
         contributions (list of dictionaries): one dictionary per
           contribution

       Returns (dictionary): maps campaign names to floats
       '''

       rv = {}
       for contribution in contributions:
           campaign = contribution["campaign"]
           if campaign not in rv:
               rv[campaign] = 0
           rv[campaign] += contribution["amount"]
       return rv


Here's a sample run of this function:

.. python-run::

   total_contributions_by_campaign(contributions)

Notice that the result is a dictionary.

.. todo::

  Is it correct to say that "not in" is an operator?

This implementation uses the ``not in`` operator to identify campaigns
that are being seen for the first time.  An alternative is to use
``get`` with a default value of zero for previously unseen campaigns:

.. python-run::
   :formatting: separate

   def total_contributions_by_campaign(contributions):
       ''' 
       Compute total contributions by campaign

       Input:
         contributions (list of dictionaries): one dictionary per
           contribution

       Returns (dictionary): maps campaign names to floats
       '''

       rv = {}
       for contribution in contributions:
           campaign = contribution["campaign"]
           rv[campaign] = rv.get(campaign, 0) + contribution["amount"]
       return rv

Accumulating values in this way is very common.

Nested dictionaries
-------------------

Dictionaries can be nested, meaning that the value associated with a
key can itself be a dictionary. For example, we might have a
dictionary that maps each candidate to a dictionary that maps a ZIP
Code as a string to the total contributions to that candidate from
that ZIP Code. Here’s a version of this dictionary constructed using
the contributions listed above:

.. python-run::
   :formatting: separate

   contributions_by_cand_by_zipcode = {
       "Kodos for President 2016": {"60637": 100.00},
       "Kang for President 2016": {"07974": 50.00,
                                   "60637": 27.50}
   }

Note that we chose to represent ZIP Codes as strings, not integers, to
make sure ZIP Codes like 07974 don't lose their leading zero and
become 7974.

We can extract the the total amount of contributions from ``60637`` to
the ``Kang for President 2016`` campaign using this expression:

.. python-run::

   contributions_by_cand_by_zipcode["Kang for President 2016"]["60637"]

The first set of square brackets extracts the sub-dictionary
associated with ``"Kang for President 2016"`` in
``contributions_by_cand_by_zipcode``, while the second retrieves the
value associated with ``"60637"`` from that sub-dictionary.


The code to compute this dictionary is not that much more complex than
the code for accumulating total contributions by candidate.  

.. python-run::
   :formatting: separate

   def total_contributions_by_campaign_by_zip(contributions):
       ''' 
       Compute the total contributions from each ZIP Code for each
       campaign

       Input:
         contributions (list of dictionaries): one dictionary per
           contribution

       Returns (dictionary): maps a campaign name to a sub-dictionary
         that maps ZIP Codes (as strings) to floats
       '''

       rv = {}
       for contribution in contributions:
           campaign = contribution["campaign"]
           zipcode = contribution["zip_code"]
           if campaign not in rv:
               rv[campaign] = {}
           rv[campaign][zipcode] = rv[campaign].get(zipcode, 0) + contribution["amount"]
       return rv

For each contribution, we first ensure that the campaign is
initialized properly in the return value.  We then use the ``get``
method to retrieve the total for contributions seen thus far from this
zipcode for the campaign, which will be zero for the first
contribution from this zipcode.  Once we have that value , we can just
add in the amount of the current contribution and update the
dictionary.  Here's a sample run of the function:

.. python-run::

   total_contributions_by_campaign_by_zip(contributions)

Notice that, as expected, the result contains nested dictionaries.


Data structures and their complexity
------------------------------------

The complexity of a computational solution to a problem, and how well
that solution performs, depends not only on the algorithm we use, but
also on our choice of data structures for that solution. Now that you
know about two data structures, lists and dictionaries, it is
important to understand the implications of using one or the
other. This decision will not be just a matter of personal preference:
your choice of data structure can have a considerable impact on how
well (or how poorly) your code performs.

For example, our political contribution data only has postal ZIP Codes
for the contributions, but not full addresses. One thing we might want
to do is compute the total contributions in each state and, to do so,
we need some way to map ZIP Codes to states. For the purposes of this
example, let's assume we only care about three ZIP Codes: 60637 in
Illinois, 07974 in New Jersey, and 94043 in California.

We could represent this data easily enough with a dictionary:

.. python-run::
   :formatting: separate

   zip_codes_dict = {"60637": "IL", 
                     "07974": "NJ",
                     "94305": "CA"}

But we could also store this mapping from ZIP Codes to states in a list of tuples, where each
tuple represents a mapping from a ZIP Code to that ZIP Code's state:

.. python-run::
   :formatting: separate

   zip_codes_list = [("60637", "IL"), ("07974", "NJ"), ("94305", "CA")]
   
Of course, the actual list of all the ZIP Codes would be much larger, with
more than 40,000 entries. 

Given a ZIP Code, obtaining that ZIP Code's state would involve
iterating through the list until we find the tuple that contains the
mapping from that ZIP Code to the corresponding state. We can write a
simple function to perform this operation:

.. python-run::
   :formatting: separate

   def get_state_from_zip(zip_code, zip_codes_list):
       '''
       Find the state associated with a given ZIP Code

       Inputs:
         zip_code (string): a ZIP Code
         zip_codes_list (list): pairs of ZIP Codes and state abbreviations

       Returns (string): state abbreviation or None, if the ZIP Code
         does not appear in the list
       '''

       for zc, st in zip_codes_list:
           if zc == zip_code:
               return st

       return None

.. python-run::

   get_state_from_zip("60637", zip_codes_list)
   get_state_from_zip("90210", zip_codes_list)
       
Notice that, if there is no corresponding ZIP Code in our list, the
function simply returns ``None``.

So, at this point we have two solutions that, essentially, accomplish
the same task:

.. python-run::

   zip_codes_dict
   zip_codes_list
   zip_codes_dict.get("60637")
   get_state_from_zip("60637", zip_codes_list)
   zip_codes_dict.get("07974")
   get_state_from_zip("07974", zip_codes_list)
   zip_codes_dict.get("94305")
   get_state_from_zip("94305", zip_codes_list)
   zip_codes_dict.get("11111")
   get_state_from_zip("11111", zip_codes_list)

Finding a given ZIP Code's state in the list, however, takes an amount
of time that is proportional to the size of the list. If we had 40,000
ZIP Codes, and the ZIP Code we're looking for is at the end of the
list, we would have to traverse the entire list to find that
value. While it's true that sometimes we'll search for a value that
is towards the start of the list, the time to find a value will *on
average* be proportional to the number of elements in the list. If
we had 20,000,000 values in the list, the average time to find a value
would be larger than if we have 40,000 values in the list.

Dictionaries, on the other hand, 
are implemented internally using a data structure called a *hash
table* that is optimized to access key-value mappings
very quickly.  In fact, the amount of time it takes to access a
key-value mapping is *not* proportional to the size of the input (in
this case, the ZIP Codes).  So, finding a value in a dictionary with
40,000 values will (roughly) take the same time as finding it in a
dictionary with 20,000,000 values.

.. admonition:: Big-O notation

   The performance or *complexity* of an algorithm or, in this case, of an operation
   on a data structure, is typically specified using *big-O notation*. 
      
   While big-O notation has a formal definition, it is not
   essential to understand the concept.  In a
   nutshell, if :math:`n` is the size of the input to a problem (e.g.,
   in this example, :math:`n` would be the number of ZIP Codes), then
   saying that something runs in :math:`O(n^2)` means that its running
   time is *roughly proportional* to :math:`n^2` (i.e., as `n` gets
   bigger, the running time grows quadratically).  On the other hand,
   if an algorithm runs in :math:`O(\log n)`, its running time grows
   logarithmically.
   
   Big-O notation helps us compare the performance of algorithms
   or individual operations on data structures. If one data structure
   can perform an operation in :math:`O(n)` and another data structure can
   perform that same operation in :math:`O(n^2)`, we know that,
   on average, the first data structure performs that operation faster
   than the second data structure.
   
   However, there is no "golden data structure" that beats every other
   data structure in every possible operation.  In fact, when a data
   structure provides good performance in one operation, there will
   usually be a trade-off: other operations may be less efficient, or
   even not supported by the data structure. So, choosing the right
   data structure often involves asking yourself what operations you
   will be using the most, and whether each data structure can perform
   those operations efficiently.
   
   In this case, we are looking at just one operation: finding a value in a list
   versus finding a value (through its key) in a dictionary. If :math:`n` is the 
   number of values, this operation can be done on lists in :math:`O(n)`
   (the running time is *linearly* proportional to :math:`n`), while
   this operation can be done on dictionaries in :math:`O(1)`, meaning that the
   running time is *not* proportional to :math:`n` (this is often referred to as
   "constant time"; strictly speaking, this operation is done in something
   called "amortized constant time", but you don't need to concern yourself
   with this distinction).    So, in this case, a dictionary would be a better choice.
   
   However, you should not jump to the conclusion that we should now
   use dictionaries for everything. If we were evaluating a different
   operation, it could turn out that lists would be a better
   choice. We explore this proposition in more detail below.


We can observe this difference in performance empirically by running our code with
the full ZIP Code database. We will show you the result of doing this experiment but,
if you would like to follow along, you can use the following files provided in our
:ref:`example code <example-code>`: the ``data_structures/dictionaries/zipcodes.py`` module,
as well as the ZIP Code database, ``data_structures/dictionaries/us_postal_codes.csv``.
You will also need to use IPython, not the regular Python interpreter (make sure to run
it in the same directory that contains the ``zipcodes.py`` and ``us_postal_codes.csv`` files.

From the IPython interpreter, run the following:

.. code:: python

   In [1]: run zipcodes.py
   
This command will run the code in ``zipcodes.py``, which reads the ZIP
Code database and loads it into both a list (``zip_codes_list``) and a
dictionary (``zip_codes_dict``). It will also define the
``get_state_from_zip`` function we wrote earlier, as well as a
function called ``gen_random_zip`` that generates a random ZIP
Code. We can see that they work as expected:


.. code:: python

   In [2]: get_state_from_zip("60637", zip_codes_list)
   Out[2]: 'IL'
   
   In [3]: get_state_from_zip("90210", zip_codes_list)
   Out[3]: 'CA'
      
   In [4]: zip_codes_dict.get("60637")
   Out[4]: 'IL'
   
   In [5]: zip_codes_dict.get("90210")
   Out[5]: 'CA'

   In [6]: gen_random_zip()
   Out[6]: '48344'
   
   In [7]: gen_random_zip()
   Out[7]: '22219'

Note: You will very likely get different ZIP Codes when you call ``gen_random_zip``.

When you make these individual calls, they may seem to be returning
nearly instantaneously.  Unfortunately, testing code performance informally in the
interpreter obscures what will happen when you write a program that
involves calling a function thousands or even millions of times.

IPython includes a handy ``%timeit`` command that will allow us to see how a piece of code performs when
run many times. As it turns out, the dictionary version is nearly 200 times faster than the list-based
version!

.. code:: python

   In [8]: %timeit zip_codes_dict.get(gen_random_zip())
   100000 loops, best of 3: 4.9 µs per loop
   
   In [9]: %timeit get_state_from_zip(gen_random_zip(), zip_codes_list)
   1000 loops, best of 3: 955 µs per loop

Note: You will likely get different running times, but the order of magnitude between the two times
should be roughly the same.

.. todo::

   Do we want to explain the output of timeit in more detail?

Things get more interesting if we actually look at how these running times change depending
on the size of the dataset. Our ``zipcodes.py`` file also defines a ``small_zip_codes_list`` 
and a ``small_zip_codes_dict`` with just 500 ZIP Codes, and a ``medium_zip_codes_list`` 
and a ``medium_zip_codes_dict`` with just 2000 ZIP Codes. If we use the ``%timeit`` command
to time our list-based and dictionary-based implementations with these datasets, we get
the following times:

+--------------+------------+------------+------------+
|              | n = 5000   | n = 20000  | n =  43624 |
+==============+============+============+============+
| Lists        | 0.142 ms   | 0.493 ms   | 1.01 ms    |
+--------------+------------+------------+------------+
| Dictionaries | 0.00477 ms | 0.00478 ms | 0.0048 ms  |
+--------------+------------+------------+------------+

So, not only are dictionaries faster than lists in an absolute sense, their performance is independent
of the size of the input. On the other hand, notice that as the dataset grows the list-based
implementation takes more and more time.

This result occurs because, as we saw earlier, finding the mapping
from a ZIP Code to a state in a list takes :math:`O(n)` time, while
finding a mapping in a dictionary takes :math:`O(1)` time.  If
:math:`n` is the number of ZIP Codes in our dataset, then the running
time of a :math:`O(n)` solution will increase (roughly) linearly as
our dataset gets bigger, while the running time of a :math:`O(1)`
operation will remain (roughly) constant.

So, based on all this, it sounds like we should just use dictionaries everywhere instead
of lists, right? Not so fast! As we mentioned earlier, there is no such thing as a
"golden data structure" that performs every possible operation in an optimal fashion.
There is, however, "the right data structure for this job" and, if "this job" is
finding a mapping between a key and a value, then dictionaries are definitely the
right data structure.

There are other operations, however, for which dictionaries are not so great. Most notably,
as we saw earlier, dictionaries are *unordered* data structures, which means that iterating
over a dictionary is not guaranteed to yield the keys in any particular order (and that
order can even change from one ``for`` loop to another). On top of that, even if we don't
care about the order in which the values are processed, a ``for`` loop over a dictionary
will usually be slower than a ``for`` loop over a list containing the same values.
So, if the order of the data matters, or if we are going to process it in sequence often,
then using a list will probably be a better choice. 


.. info-note::

   Why did we use random ZIP Codes instead of just testing the code with a fixed ZIP Code?
   If we used a fixed ZIP Code, the results could be skewed depending on where that ZIP Code is
   located in the list. For example, if we used 00210 (the first ZIP Code in the list),
   our list implementation would always find that ZIP Code very quickly (because it doesn't
   have to iterate through the rest of the list), making it look like the list version
   is just as good as the dictionary version:
   
   .. code:: python
   
      In [10]: %timeit zip_codes_dict.get("00210")
      The slowest run took 21.25 times longer than the fastest. This could mean that an intermediate result is being cached 
      10000000 loops, best of 3: 63.3 ns per loop
      
      In [11]: %timeit get_state_from_zip("00210", zip_codes_list)
      The slowest run took 17.80 times longer than the fastest. This could mean that an intermediate result is being cached 
      10000000 loops, best of 3: 127 ns per loop

   In this case, the dictionary version is only two times faster than the list version. Notice
   that we also get a message about "an intermediate result being cached". This phrase refers to the
   fact that computers are usually smart about detecting when a location in memory is being
   accessed frequently, and making sure it is "cached" in higher-speed memory in the computer's
   processor (instead of having to go to the computer's main memory, which is slower). Testing
   our implementation with the same inputs over and over again could show performance
   gains that are due to this caching mechanism, not the efficiency of the data structure itself. 
   


Sets
----

.. todo:: 

  Do we want to use mathematical definitions for the set operations instead of or in addition to the prose definitions?

Dictionaries are great for associating values to unique keys, but sometimes
we may simply want to have a collection of unique keys that we can access
as efficiently as a dictionary, but without associating a value with each key.
To do this, we can simply use a *set* data structure, which allows us
to store an unordered collection of distinct elements.

Typical set operations include:

- *membership* (:math:`e \in S`): which tests whether a given element, :math:`e`, appears in the set :math:`S`,

- *subset* (:math:`S \subseteq T`): which tests whether every element in :math:`S` also appears as an element in :math:`T`.

- *union* (:math:`S \cup T`): which yields a new set that contains the elements :math:`e` where :math:`e \in S` and/or :math:`e \in T`,

- *intersection* (:math:`S \cap T`): which yields a new set that contains the elements :math:`e` where :math:`e \in S` *and* :math:`e \in T`, and

- *difference* (:math:`S - T`): which yields a new set that contains the elements :math:`e` where :math:`e \in S` and :math:`e \notin T`.

Sets are sufficiently useful that Python provides a built-in ``set``
data structure.  

We can define a set literal by surrounding the initial elements of the
set with curly braces or using the built-in ``set`` function with a
sequence (list, string, etc.) as the parameter:

.. python-run::

   zipcodes = {"60637", "07974"}
   zipcodes

   zipcodes = set(["60637", "07974"])
   zipcodes

   vowels = set("aeiou")
   vowels

To construct an empty set, we use the ``set`` function:

.. python-run::

   empty_set = set()

We cannot use curly braces to create an empty set, because Python
interprets ``{}`` as an empty dictionary.

We can determine the number of elements in a set using the ``len``
function:

.. python-run::

   len(empty_set)
   len(zipcodes)
   len(vowels)

and we can test for set membership using the ``in`` operator:

.. python-run::

   "14850" in zipcodes
   "60637" in zipcodes

.. todo::

   Do we want to add an example using not in?

We can determine whether one set is a subset of another set using the
``issubset`` method.  Specifically, a call of the form
``S.issubset(T)`` tests whether the set ``S`` is a subset of the set
``T``.  For example:

.. python-run::

  {"07974"}.issubset(zipcodes)

  {"60637", "14850"}.issubset(zipcodes)


Sets are mutable: we can add and remove elements.  We can add elements
to a set using the ``add`` method:

.. python-run::

   zipcodes.add("14850")
   zipcodes.add("60637")
   zipcodes

The second example illustrates an important point about sets: adding
an element that is already a member of the set has no effect.

We can take elements out of a set using either the ``remove`` method
or the ``discard`` method.  The ``remove`` method removes a value from
a set, if it is a member, and throws a ``KeyError`` exception if it is
not.  The ``discard`` method, in contrast, removes the value if it is
a member of the set and does nothing if the value is not a member of
the set.

.. python-run::

   zipcodes.remove("60637")
   zipcodes.remove("60615")
   zipcodes

   zipcodes.discard("14850")
   zipcodes.discard("60615")
   zipcodes

Using the ``add`` method and ``len`` function, we can easily write
a function to determine how many different ZIP Codes had at least one
contribution.

.. python-run::
   :formatting: separate

   def compute_num_zipcodes(contributions):
       '''
       Compute the number of zipcodes with at least one contribution

       Inputs:
         contributions (list of dictionaries): one dictionary per
           contribution

       Returns (int): the number of zipcodes with at least one
         contribution.
       '''

       zipcodes_seen = set()
       for contribution in contributions:
           zipcodes_seen.add(contribution["zip_code"])
       return len(zipcodes_seen)

.. python-run::

   compute_num_zipcodes(contributions)

Alternatively, we can use set comprehensions, which are like
dictionary comprehensions with only keys, to do the same
computation:


.. python-run::
   :formatting: separate

   def compute_num_zipcodes(contributions):
       '''
       Compute the number of zipcodes with at least one contribution

       Inputs:
         contributions (list of dictionaries): one dictionary per
           contribution

       Returns (int): the number of zipcodes with at least one
         contribution
       '''

       zipcodes_seen = {c["zip_code"] for c in contributions}
       return len(zipcodes_seen)

.. python-run::

   compute_num_zipcodes(contributions)


Sets come with a variety of useful operations. We can compute a *new*
set that is the union of two sets using the ``|`` operator or the
``union`` method, the intersection of two sets using the ``&``
operator or the ``intersection`` method, and the difference of two
sets using the ``-`` operator or the ``difference`` method:

.. python-run::

   zipcodes = {"60637", "07974"}

   zipcodes | {"60637", "60615"}

   zipcodes.union({"60637", "60615"})

   zipcodes & {"60637", "60615"}

   zipcodes.intersection({"60637", "60615"})

   zipcodes - {"60637", "60615"}

   zipcodes.difference({"60637", "60615"})

Finally, since sets are collections, we can iterate over the
elements in a set:

.. python-run::

   for zc in zipcodes:
        print(zc)

As with dictionaries, sets are unordered and so the elements will be
printed in an arbitrary order.









..
    Counting k-mers
    ---------------

    A common operation in computational genomics is finding the number of
    occurrences of different k-mers in a DNA sequence, or the number of
    all possible substrings of length :math:`k` in a given sequence (this
    is similar to counting n-grams in computational linguistics). For
    example, the following sequence:

    ::

        AAGAGT

    contains the following 2-mers: - ``AA`` - ``AG`` (twice) - ``GA`` -
    ``GT``

    and the following 3-mers: - ``AAG`` - ``AGA`` - ``GAG`` - ``AGT``

    How could we solve this problem using only lists and strings?  We
    would need to generate all possible substrings of length :math:`k`
    (using only the DNA bases: ``A``, ``C``, ``T``, and ``G``), and then
    count how many times each combination appeared in a given DNA
    sequence.

    Let's start with a function to generate all possible DNA k-mers.

    .. python-run::
       :formatting: separate

       def generate_dna_kmers(k):
           '''
           Compute a list of all possible substrings of length k using
           only characters A, C, T, and G

           Inputs:
             k (int): size of substrings

           Returns (list of strings): list of all possible mers of
             length k

           '''
           bases = ["A", "C", "T", "G"]
        
           last = bases
           current = []
           for i in range(k-1):
               for b in bases:
                   for l in last:
                       current.append(l+b)
               last = current
               current= []
           return last

    .. python-run::

       generate_dna_kmers(1)

    .. python-run::

       generate_dna_kmers(2)


    .. python-run::

       generate_dna_kmers(3)


    Now, we need an additional function that, given a single substring, will
    count the number of (potentially overlapping) occurrences of that
    substring in a DNA sequence.

    .. literalinclude:: dnafile.py
       :pyobject: count_mer

    .. code:: python

        count_mer("GGG", "AGGGCGGG")




    .. parsed-literal::

        2


    Finally, we just need a function that, given a sequence and :math:`k`
    will use the previous two functions to count the number of occurrences
    of every possible k-mer in the sequence.

    .. literalinclude:: dnafile.py
       :pyobject: kmer_count


    .. parsed-literal::

        [('AA', 1), ('GA', 1), ('GT', 1), ('AG', 2)]


    .. code:: python

        kmer_count(3, "AAGAGT")


    .. parsed-literal::

        [('AGA', 1), ('AGT', 1), ('AAG', 1), ('GAG', 1)]


    .. code:: python

        seq1 = "AAGGCCTT"
        seq2 = "AAAGGGCCCTTT"
        seq3 = "ACTGTGCAAACCTTGGGGTTCCAA"
        seq4 = "AAGGAAGGCGCGCCGGAAAGAG"
        seq5 = "GGGGAGGG"

    .. code:: python

        kmer_count(1, seq4)


    .. parsed-literal::

        [('A', 8), ('C', 4), ('G', 10)]



    .. code:: python

        kmer_count(2, seq4)




    .. parsed-literal::

        [('AA', 4), ('GA', 3), ('CC', 1), ('GC', 3), ('AG', 4), ('CG', 3), ('GG', 3)]



    .. code:: python

        kmer_count(3, seq4)




    .. parsed-literal::

        [('AAA', 1),
         ('GAA', 2),
         ('AGA', 1),
         ('GGA', 2),
         ('GCC', 1),
         ('CGC', 2),
         ('GGC', 1),
         ('AAG', 3),
         ('GAG', 1),
         ('CCG', 1),
         ('GCG', 2),
         ('AGG', 2),
         ('CGG', 1)]



    Ask: This algorithm is correct but it is very inefficient. Why?

    First of all, we generate all possible k-mers (:math:`4^k`), even though
    they may not all appear in the sequence.

    Then, in ``count_mer`` we iterate over a sequence of length :math:`n`
    and check every substring of length :math:`k` to see if it matches the
    provided ``mer``. This requires :math:`n\cdot k` operations.

    Finally, in ``kmer_count`` we call ``count_mer`` :math:`4^k` times (the
    number of possible k-mers). So, we have to perform a total of
    :math:`n\cdot k \cdot 4^k` operations. As :math:`k` grows, the number of
    operations grows exponentially!

    This is terrible performance: any time you find yourself writing an
    algorithm where the number of "steps" grows exponentially with the size
    of the input, you probably need to look for a better solution (caveat:
    there are some types of problems where it is unknown whether there are
    solutions better than exponential)

    .. code:: python

        from dnafile import read
        
        seq_drosofila = read("drosofila-small.txt")

    .. code:: python

        len(seq_drosofila)




    .. parsed-literal::

        951900



    .. code:: python

        kmer_count(1, seq_drosofila)




    .. parsed-literal::

        [('A', 278920), ('C', 196552), ('T', 277040), ('G', 199388)]



    .. code:: python

        kmer_count(2, seq_drosofila)




    .. parsed-literal::

        [('AA', 96382),
         ('CA', 61129),
         ('TA', 66451),
         ('GA', 54957),
         ('AC', 52022),
         ('CC', 41883),
         ('TC', 54715),
         ('GC', 47932),
         ('AT', 75767),
         ('CT', 54085),
         ('TT', 94270),
         ('GT', 52918),
         ('AG', 54749),
         ('CG', 39455),
         ('TG', 61603),
         ('GG', 43581)]



    .. code:: python

        %time kmers = kmer_count(1, seq_drosofila)


    .. parsed-literal::

        CPU times: user 304 ms, sys: 4.01 ms, total: 308 ms
        Wall time: 308 ms


    .. code:: python

        %time kmers = kmer_count(2, seq_drosofila)


    .. parsed-literal::

        CPU times: user 1.4 s, sys: 0 ns, total: 1.4 s
        Wall time: 1.39 s


    .. code:: python

        %time kmers = kmer_count(3, seq_drosofila)


    .. parsed-literal::

        CPU times: user 5.51 s, sys: 0 ns, total: 5.51 s
        Wall time: 5.5 s


    .. code:: python

        %time kmers = kmer_count(4, seq_drosofila)


    .. parsed-literal::

        CPU times: user 22 s, sys: 0 ns, total: 22 s
        Wall time: 21.9 s


    Notice how the time with :math:`k` is roughly 4 times greater than the
    time with :math:`k-1`


    How can we improve on the k-mer counting algorithm using dictionaries?

    Instead of generating all possible k-mers and counting how many times 
    each appears in the sequence, we can make a single pass through the sequence
    and maintain a dictionary of k-mers. This dictionary is initially empty
    but, when we find a k-mer we add a (kmer, 1) entry in the dictionary
    (and, if we encounter that k-mer again, we increment the value of that
    entry).

    .. literalinclude:: dnafile.py
       :pyobject: kmer_count_better



    .. code:: python

        seq4




    .. parsed-literal::

        'AAGGAAGGCGCGCCGGAAAGAG'



    .. code:: python

        seq4[3:3+4]




    .. parsed-literal::

        'GAAG'



    .. code:: python

        kmer_count_better(1, seq4)




    .. parsed-literal::

        [('C', 4), ('A', 8), ('G', 10)]



    .. code:: python

        kmer_count_better(2, seq4)




    .. parsed-literal::

        [('GC', 3), ('AA', 4), ('GA', 3), ('CC', 1), ('AG', 4), ('GG', 3), ('CG', 3)]



    .. code:: python

        kmer_count_better(3, seq4)




    .. parsed-literal::

        [('GGA', 2),
         ('AGA', 1),
         ('CGC', 2),
         ('GCG', 2),
         ('GAG', 1),
         ('GGC', 1),
         ('GCC', 1),
         ('AGG', 2),
         ('GAA', 2),
         ('AAG', 3),
         ('CCG', 1),
         ('AAA', 1),
         ('CGG', 1)]



    Note: we use %timeit instead of %time because the running times are
    going to be pretty small. %timeit automatically runs the statement
    multiple times and takes an average.

    .. code:: python

        %timeit kmers = kmer_count_better(1, seq_drosofila)


    .. parsed-literal::

        10 loops, best of 3: 141 ms per loop


    .. code:: python

        %timeit kmers = kmer_count_better(2, seq_drosofila)


    .. parsed-literal::

        10 loops, best of 3: 182 ms per loop


    .. code:: python

        %timeit kmers = kmer_count_better(3, seq_drosofila)


    .. parsed-literal::

        10 loops, best of 3: 187 ms per loop


    .. code:: python

        %timeit kmers = kmer_count_better(4, seq_drosofila)


    .. parsed-literal::

        1 loops, best of 3: 188 ms per loop


    The running time is essentially the same regardless of :math:`k`! Why?
    Accessing/updating a dictionary is done in amortized constant time, so
    the number of operations in this algorithm is proportional only to
    :math:`n` (the length of the sequence). Notice, however, that we're
    making a copy of the substring in each step, so it's actually
    proportional to :math:`n\cdot k` (this is still much much much better
    than :math:`n\cdot k \cdot 4^k`). So, you'll start to see (slightly)
    longer running times as :math:`k` increases.

    .. code:: python

        %timeit kmers = kmer_count_better(100, seq_drosofila)


    .. parsed-literal::

        1 loops, best of 3: 512 ms per loop


    .. code:: python

        %timeit kmers = kmer_count_better(500, seq_drosofila)


    .. parsed-literal::

        1 loops, best of 3: 661 ms per loop


    .. code:: python

        %timeit kmers = kmer_count_better(1000, seq_drosofila)


    .. parsed-literal::

        1 loops, best of 3: 955 ms per loop



