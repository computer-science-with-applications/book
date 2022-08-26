The pandas library
==================

`Pandas <http://pandas.pydata.org/>`_ is a data analysis toolkit for Python that makes it easy to
work with certain types of data, specially:

-  Tabular data (i.e., anything that can be expressed as labelled
   columns and rows)
-  Time series data
-  Matrix data
-  Statistical datasets

In this chapter, we will focus on tabular data and organize our discussion of this
library around an exploration of data from the 2015 New York City
Street Tree Survey, which is freely available from the New York City
open data portal (https://data.cityofnewyork.us).  This survey was
performed by the New York City Department of Parks and Recreation with
help from more than 2000 volunteers.  The goal of the survey is to
catalog the trees planted on the City right-of-way, typically the
space between the sidewalk and the curb, in the five boroughs of New
York.  We can use this data to answer questions such as:

#. How many different species are planted as street trees in New York?
#. What are the five most common street tree species in New York?
#. What is the most common street tree species in Brooklyn?
#. What percentage of the street trees in Queens are dead or in poor health?
#. How does street tree health differ by borough?

The survey data is stored in a CSV file that has 683,789 lines, one per
street tree. (Hereafter we will refer to trees rather than street
trees for simplicity.)  The census takers record many different
attributes for each tree, such as the common name of the species, the
location of the tree, etc.  Of these values, we will use the
following:

* ``boroname``: the name of the borough in which the tree resides;
* ``health``: an estimate of the health of the tree: one of good, fair, or poor;
*  ``latitude`` and ``longitude`` :  the location of the tree using geographical coordinates;
* ``spc_common``: the common, as opposed to Latin, name of the species;
* ``status``: the status of the tree: one of alive, dead, or stump;
* ``tree_id``: a unique identifier

Some fields are not populated for some trees. For example, the
``health`` field is not populated for dead trees and stumps and the
species field (``spc_common``) is not populated for stumps and most
dead trees.

Pandas supports a variety of data types.  We'll talk about
three---``DataFrame``, ``Series`` and ``Categorical``---in detail.  We
also talk about how filtering, which was introduced in our discussion
of Numpy, and grouping, a new concept, can be used to answer complex
questions with little code.  But before we get get started, we need to
import Pandas.  This step is traditionally done using the ``as``
option with ``import`` to introduce a short alias (``pd``) for the
library.

.. python-run::

   import pandas as pd



.. todo:: add a road map for the rest of the chapter.

DataFrames
----------

We'll start by loading the tree data into a data structure.  Data frames,
the main data structure in Pandas, were inspired by the data structure
of the same name in R and are designed to represent tabular data.  The
library function ``pd.read_csv`` takes the name of a CSV file and
loads it into a data frame.  Let's use this function to load the tree
data from a file named ``2015StreetTreesCensus_TREES.csv``:

.. python-run::

    trees = pd.read_csv("2015StreetTreesCensus_TREES.csv")

This file is available in our :ref:`example code <example-code>`,
in the ``working_with_data/pandas/`` directory. Please note that it is
provided as a ZIP file called ``tree-census-data.zip``, and you must un-zip
it before using it.

The variable ``trees`` now refers to a Pandas ``DataFrame``.  Let's
start by looking at some of the actual data.  We'll explain the
various ways to access data in detail later.  For now, just keep in
mind that the columns have names (for example, "Latitude",
"longitude", "spc_common", etc) and leverage the intuition you've built up
about indexing in other data structures.

Here, for example, are a few columns from the first ten rows of the
dataset:

.. python-run::

    trees10 = trees[:10]
    trees10[["Latitude", "longitude", "spc_common", "health", "boroname"]]

Notice that the result looks very much like a table in which both the
columns and the rows are labelled.  In this case, the column labels
came from the first row in the file and the rows are simply numbered
starting at zero.

Here's the full first row of the dataset with all 41 attributes:

.. python-run::
    
    trees.iloc[0]

and here are a few specific values from that row:

.. python-run::

    first_row = trees.iloc[0]
    first_row["Latitude"]
    first_row["longitude"]
    first_row["boroname"]

Notice that the latitude and longitude values are floats, while the
borough name is a string.  Conveniently, ``read_csv`` analyzes each
column and if possible, identifies the appropriate type for the data
stored in the column.  If this analysis cannot determine a more
specific type, the data will be represented using strings.

We can also extract data for a specific column:

.. python-run::
    
    trees10["boroname"]

and we can easily do useful things with the result, like count the number
of times each unique value occurs:

.. python-run::

    trees10["boroname"].value_counts()

Now that you have a some feel for the data, we'll move on to
discussing some useful attributes and methods provided by data frames.
The ``shape`` attribute yields the number of rows and columns in the
data frame:

.. python-run::

   trees.shape

The data frame has fewer rows (683,788) than lines in the file
(683,789), because the header row is used to construct the column
labels and does not appear as a regular row in the data frame.

We can use the ``columns`` attribute to examine the column labels:

.. python-run::

   trees.columns

We noted earlier that the rows, like columns, have labels.
Collectively, these values are known as the index.  As currently
constructed, the tree data set has an index that ranges from zero to
683,787.  Often, data sets have a meaningful value that can be used to
uniquely identify the rows.  The trees in our data set, for example,
have unique identifiers that can be used for this purpose.  Let's
re-load the data and specify the name of a column to use for the
index using the ``index_col`` parameter:

.. python-run::

    trees = pd.read_csv("2015StreetTreesCensus_TREES.csv",
                        index_col="tree_id")

Now that we have a meaningful index, we can use the ``index``
attribute to find the names of the rows:

.. python-run::

   trees.index

Now let's look at accessing values in the sample data frame in a more
systematic way.  We can extract the data for a specific row using
either the appropriate row label or the position of the row in the
data frame.  To index the data using the row label (``180683`` for the
row at position 0), we use the ``loc`` operator with square brackets.

.. python-run::

    trees.loc[180683]

To access the row using the row number, that is, its position in the
data frame, we use ``iloc`` operator and square brackets:

.. python-run::

   trees.iloc[0]

.. todo:: add citation for definition of series.

In both cases the result of evaluating the expression has type Pandas
``Series``:

.. python-run::

   type(trees.iloc[0])

A ``Series`` is defined as "a one-dimensional labeled array capable of
holding any data type (integers, strings, floating point numbers,
Python objects, etc.)."  Briefly, we can think of a ``Series`` as an
array and index it using integers, for example, ``trees.iloc[0][0]``
yields the first value in the first row ("08/27/2015").  We can also
think of it as a dictionary and index it using the labels.  We can,
for example, extract the exact same value using the expression
``trees.iloc[0]["created_at"]``.

As we saw earlier, we can use slicing to construct a new data frame
with a subset of the rows of an existing data frame.  For example,
this statement from above:

.. python-run::
   
   trees10 = trees[0:10]

constructs a data frame that contains the first ten rows (row 0
through row 9 inclusive) of the trees data set.  One thing to keep in
mind, the new data frame and the original data frame share the same
underlying data, which means that updating one, updates the other!

We can extract the values in a specific column as a series using
square brackets with the column name as the index:

.. python-run::

   trees10["spc_common"]

We can also use dot notation to access a column, if the corresponding
label conforms to the rules for Python identifiers and does not
conflict with the name of a ``DataFrame`` attribute or method:

.. python-run::

   trees10.spc_common

The tree dataset has many columns, most of which we will not be using
to answer the questions posed at the beginning of the chapter.  As we
saw above, we can extract the desired columns using a list as the
index:

.. python-run::

   cols_to_keep = ['spc_common', 'status', 'health', 'boroname', 'Latitude', 'longitude']
   trees_narrow = trees[cols_to_keep]
   trees_narrow.shape

This new data frame has the same number of rows and the same index as
the original data frame, but only six columns instead of the original
41.

If we know in advance that we will be using only a subset of the
columns, we can specify the names of the columns of interest to
``pd.read_csv`` and get the slimmer data frame to start.  Here's a
function that uses this approach to construct the desired data frame:

.. python-run::

    def get_tree_data(filename):
        '''
    	Read slim version of the tree data and clean up the labels.

    	Inputs:
    	    filename: name of the file with the tree data

    	Returns: DataFrame
        '''
        cols_to_keep = ['tree_id', 'spc_common', 'status', 'health', 'boroname', 
                        'Latitude', 'longitude']
        trees = pd.read_csv(filename, index_col="tree_id",
                            usecols=cols_to_keep)
        trees.rename(columns={"Latitude":"latitude"}, inplace=True)
    	return trees

    trees = get_tree_data("2015StreetTreesCensus_TREES.csv")

A few things to notice about this function: first, the index column,
``tree_id``, needs to be included in the value passed with the
``usecols`` parameter.  Second, we used the ``rename`` method to fix a
quirk with the tree data: "Latitude" is the only column name that
starts with a capital letter.  We fixed this problem by supplying a
dictionary that maps the old name of a label to a new name using the
``columns`` parameter.  Finally, by default, ``rename`` constructs a
new dataframe.  Calling it with the ``inplace`` parameter set to
``True``, causes frame updated in place, instead.

A note about missing values
---------------------------

As we noted when we described the tree data, some attributes are not
included for some entries.  The entries for stumps and dead trees, for
example, do not include values for the health of the tree.  We can see
the impact of this missing data in row 630, which contains information
about a dead tree in Queens:

.. python-run::

   trees.iloc[630]

Notice that both the ``health`` and the ``spc_common`` fields have the
value ``NaN``, which stands for "not a number."  This value is
inserted in place of missing values by default by ``pd.read_csv``.
We'll talk about how Pandas handles these values as we explore the
trees data set.

Series
------

Now that we have the data in a form suitable for computation, let's look at what is
required to answer the first two questions: "How many different
tree species are planted in New York?" and "What are the five most common
tree species in New York?"

One approach would be to write code to iterate over tree species in
the ``spc_common`` column, build a dictionary that maps these names to
counts, and then process the dictionary to extract the answers to our
questions:

.. python-run::

    counts = {}
    for kind in trees.spc_common:
        if pd.notnull(kind):
            counts[kind] = counts.get(kind, 0) + 1

    print("Number of unique street tree species:", len(counts.keys()))

    top_5 = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:5]
    for kind, val in top_5:
        print(kind)

Recall that the species is not specified for stumps and most dead
trees and that missing values are represented in the data frame with
the value ``NaN``.  We do not want to include these values in our
count and so we'll check for ``NaN`` using ``pd.notnull`` before we
update ``counts``.  The method ``pd.notnull`` can be used with a
single value or with a compound value, such as a list, series, or a
data frame. In this context, we are calling it with a single value and
it will return ``True`` if ``kind`` is not ``NaN`` and ``False``
otherwise.

This code works, but thus far all we have gained from using Pandas in
service to answering our question is the ability to extract and
iterate over a column from the data frame, which is not very exciting.
We can, in fact, answer these questions with very little code by using
some of the many attributes and methods provided by the ``Series``
data type.  Here for example, is code, to answer the first question
using the ``nunique`` method:

.. python-run::

   num_unique = trees.spc_common.nunique()
   print("Number of unique street tree species:", num_unique)

which returns the number of unique values in a series.  By default, it
does not include ``NaN`` in the count.  The ``unique`` method, which
returns a Numpy array with the unique values in the series, is also
useful.

We can also answer the second question with very little code.  we'll
use the ``value_counts`` method to construct a *new* series in which
the index labels are the different species that occurred in
``spc_common`` and the values count the number of times each species
occurred.  Conveniently, the values are ordered in descending order by
count, so the most frequent item is first and we can use slicing to
extract the top five:

.. python-run::

   vc = trees.spc_common.value_counts()
   vc[:5]

The resulting series is not quite what we want: the names of the
trees.  Fortunately, we can extract these names from the slices series
using the ``index`` attribute:

.. python-run::

   for kind in vc.index[:5]:
       print(kind)

In addition to the ``index`` attribute, the ``Series`` type includes
other useful attributes, such as ``size`` which holds the number of
elements in the series and ``values``, which yields an array with the
series' values.  This type also comes with a large number of useful methods.
We'll discuss a few of them here.

As we just saw, we can slice a series. We can also extract individual
elements using the ``loc`` and ``iloc`` operators with a value's index
and position respectively:

.. python-run::

   vc.loc["London planetree"]
   vc.iloc[0]

We can also drop the ``loc`` operator and just use square brackets
with the index:

.. python-run::

   vc["London planetree"]

Finally, if the index is a legal Python identifier and it does not
conflict with a ``Series`` attribute or method name, we can use the
dot notation.  "London planetree" does not qualify because of the
embedded space, but "mimosa" on the other hand, does:

.. python-run::

   vc.mimosa

The series ``describe`` method computes a new series that contains
summary information about the data and is very useful when you are
exploring a new dataset.  The result depends on the type of the values
stored in the series.  In the case of the common names of the tree
species, the values are strings and so, ``describe`` tells us the
number of entries (``count``), the number of unique values
(``unique``), the most common value (``top``), and its frequency
``freq``).

.. python-run::

   trees.spc_common.describe()

By default, all of these values are computed excluding ``NaN`` values.
This method provides an alternative way to answer our first question:

.. python-run::

   num_unique = trees.spc_common.describe()["unique"]
   print("Number of unique street tree species:", num_unique)

One thing to note about this code: we used the square bracket notation
to access the ``unique`` value from the result of ``describe``.  Could
we have used dot notation instead?  No, because even though ``unique``
is a legal Python identifier, it conflicts with the name of a series
method.

Given a series with numeric values ``describe`` computes the number of
values in the series, the mean of those values, their standard
deviation, and their quartiles.  Latitude and longitude are the only
values represented by floats in our sample dataset and it does not
really make sense to compute quartiles for these values.  So, we'll
construct a simple series with an index that ranges from zero to ten
to use an example using the ``pd.Series`` constructor and a list of
values:

.. python-run::

   sample_series = pd.Series([92, 74, 80, 60, 72, 90, 84, 74, 75, 70])
   sample_series
   sample_series.describe()

The ``describe`` method can also be applied to data frames.

As with NumPy arrays, operators are applied element-wise and
Numpy-style broadcasting is used to construct values of the same shape
prior to applying the operator.  For example, we could compute a
series with the percentage live trees, dead trees, and stumps using a
call to ``value_counts`` and a couple of operators:

.. python-run:: 
   
   trees.status.value_counts()/len(trees) * 100

.. todo:: what other methods should we include here?


Filtering
---------

Now let's move on to our third and fourth questions: "What is the most
common street tree species in Brooklyn?" and "What percentage of the
trees street in Queens are dead or in poor health?"

We could answer these questions by iterating over the data frame using
the ``iterrows`` method, which yields a tuple with the label and
corresponding value for each row in the data frame.  In the body of
the loop, we would identify the relevant rows, construct a dictionary,
and calculate the most frequent species as we go:

.. code:: python

    >>> top_kind = ""
    >>> top_count = 0
    >>> brooklyn_tree_counts = {}
    >>> for idx, tree in trees.iterrows():
    ...     if tree["boroname"] == "Brooklyn":
    ...         kind = tree["spc_common"]
    ...         if pd.notnull(kind):
    ...             brooklyn_tree_counts[kind] = brooklyn_tree_counts.get(kind, 0) + 1
    ...             if brooklyn_tree_counts[kind] > top_count:
    ...                 top_count = brooklyn_tree_counts[kind]
    ...                 top_kind = kind
    ... 
    >>> print("Most common tree in Brooklyn:", top_kind)
    Most common tree in Brooklyn: London planetree

Alternatively, we could leverage Pandas a bit more by constructing a
new data frame with the relevant rows and then using the ``Series``
``mode`` method to find the most frequent non-null value in the
``spc_common`` column:

.. code:: python

    >>> brooklyn_trees = []
    >>> for idx, tree in trees.iterrows():
    ...     if tree["boroname"] == "Brooklyn":
    ...         brooklyn_trees.append(tree)
    ... 
    >>> bt = pd.DataFrame(brooklyn_trees)
    >>> print("Most common tree in Brooklyn:", bt.spc_common.mode().iloc[0])
    Most common tree in Brooklyn: London planetree

The ``mode`` method returns returns a series of with the most frequent
value or, in the case of a tie, values

.. code:: python

    >>> bt.spc_common.mode()
    0    London planetree
    dtype: object

To find the name of the species that occurs most often, we'll extract
the first value from this series using ``iloc[0]`` Given a tie, we'll
just use the first one.

Unfortunately, both of these approaches are quite slow, because
iterating over a data frame one row at a time is an expensive
operation.  A better way to answer this question is to use filtering,
which is similar to filtering in Numpy.  Here's a statement that
computes the same data frame with entries for the trees in Brooklyn
much more efficiently:

.. python-run::

    in_brooklyn = trees.boroname == "Brooklyn"
    bt = trees[in_brooklyn]

The variable ``in_brooklyn`` refers to a series with boolean values,
one per tree, that are ``True`` for trees in Brooklyn and ``False``
otherwise.  If we use a series of booleans to index into a data frame,
the result will be a new data frame that includes the rows for which
the corresponding boolean is ``True``. 

Using this approach, we can compute the most common tree in Brooklyn
quite compactly and efficiently:

.. python-run::

    bt = trees[trees.boroname == "Brooklyn"]
    print("Most common tree in Brooklyn:", bt.spc_common.mode().iloc[0])

Notice that this version specifies the filter expression directly as
the index, rather than assigning an intermediate name to the series of
booleans.

We can combine multiple conditions using the element-wise and (``&``)
and element-wise or (``|``) operators.  For example, here's code that
constructs a data frame with the entries for trees in Queens that are
that are either dead or in poor health:

.. python-run::

   filter = (trees.boroname == "Queens") & \ 
              ((trees.status == "Dead") | (trees.health == "Poor"))
   bad_trees_queens = trees[filter]

Note that the parentheses are necessary because element-wise and
(``&``) has higher precedence than both equality (``==``) and
element-wise or (``|``).

To answer our question "What percentage of the trees street in Queens
are dead or in poor health?", we need both the number of trees in
Queens (excluding stumps) and the number of bad trees in Queens, so
we'll split the filtering into two pieces:

.. python-run::
 
   not_stump_in_queens = (trees.boroname == "Queens") & (trees.status != "Stump")
   trees_in_queens = trees[not_stump_in_queens]

   bad_tree_filter = (trees_in_queens.status == "Dead") | \
                         (trees_in_queens.health == "Poor")
   bad_trees_in_queens = trees_in_queens[bad_tree_filter]

   s = "Percentage of the trees street in Queens are dead or in poor health: {:.2f}%"
   print(s.format(len(bad_trees_in_queens)/len(trees_in_queens)*100))

The first two lines build a data frame for the trees in Queens
(excluding stumps), while the second and third lines filter this new data
frame further to find the dead trees and trees in poor health.

Grouping
--------

To answer our last question--- "How does tree health differ by
borough?"---we will compute a data frame similar to Table X, which has
one row per borough.  Specifically, it contains data for the
percentages of trees in the borough deemed to be in good, fair, or
poor health and for dead trees and stumps.

.. todo:: center the table...fix reference (Table X)

.. csv-table:: Stree Tree Health by Borough
   :header: "Borough", "Good", "Fair", "Poor", "Dead", "Stumps"
   :widths: 50,30,30,30,30,30
   :align: center

   Bronx,78.2%,12.8%,3.6%,3.0%,2.5%
   Brooklyn,78.0%,14.1%,3.6%,1.9%,2.4%
   Manhattan,72.4%,17.5%,5.5%,2.8%,1.8%
   Queens,77.4%,13.8%,3.8%,1.8%,3.2%
   Staten Island,78.5%,13.8%,4.0%,1.8%,1.9%


We'll work up to this task by answering some easier questions first:

#. How many entries does the data set have for each borough?
#. For each borough, how many entries are for live trees, dead trees, and stumps?
#. For each borough, what percentage of the trees are live, dead, or stumps?

To count the number of entries per borough, we could walk over the
individual rows and update a dictionary that maps boroughs to entry
counts.  But as we learned in the last section, iterating over the
rows individually is slow and is best to be avoided.  Another way to
compute this information would be to use filtering to create a data
frame for each borough and then compute its length.  Here's a function
that uses this approach:

.. python-run::

   def find_per_boro_count(trees):
       counts = []
       boros = sorted(trees.boroname.unique())
       for boro in boros:
           boro_df = trees[trees.boroname == boro]
           counts.append(len(boro_df))

       return pd.Series(counts, index=boros)

   find_per_boro_count(trees)

In each iteration of the loop, we identify the trees in a specific
borough, count them using ``len``, and then save the number on a list.
Once this list is constructed, we use it and the list of borough names
to create a series with the desired result.

The task of separating the rows of a data frame into groups based on
one or more fields and then doing some work on the individual groups
is very common and so, Pandas provides the ``groupby`` method to
simplify the process.  The groups can be specified in a variety of
ways.  We'll start with the most straightforward: using a column label
or a tuple of column labels.  This method returns a special
``DataFrameGroupBy`` object.  When we iterate over an object of this
type, we get a tuple that contains the name of the group and a data
frame that contains the rows that belong to the group.

Here's a version of ``find_per_boro_count`` that uses ``groupby`` on
the borough name rather than explicit filtering:

.. python-run::

   def find_per_boro_count(trees):
       counts = []
       boros = []
       for boro, boro_df in trees.groupby("boroname"):
           counts.append(len(boro_df))
           boros.append(boro)

       return pd.Series(counts, index=boros)

   find_per_boro_count(trees)

Other than the use of ``groupby``, the only difference between this
function and the previous one is that we construct the list of borough
names from the group names rather than applying ``unique`` to the
``boroname`` column.

This version runs faster than the previous version, but it turns out
there is an even better way to compute this result.  This particular task,
grouping by a field or fields and then counting the number of items in
each group, is so common that the ``DataFrameGroupBy`` class includes
a method, named ``size``, for this computation.  Using this method, we
can count the number of trees per borough in one line:

.. python-run::

   trees.groupby("boroname").size()

How do we build on this code to compute the number of live trees,
dead trees, and stumps for each borough?  Recall that this information
is available for each tree in the ``status`` field.  We can group the
data using this field along with the borough to get the information
we want:

.. python-run::

   status_per_boro = trees.groupby(["boroname", "status"]).size()
   status_per_boro

What might not be immediately clear from this output is that
``status_per_boro`` is a ``Series`` with a hierarchical index, not a
data frame.

.. python-run::

   status_per_boro.index

We can extract the information for a given borough as series using
square brackets and the name of the borough:

.. python-run::

   status_per_boro["Bronx"]

and we can extract a specific value, say, the number of live trees,
for a specific borough using either two sets of square brackets or one
set of square brackets and a tuple:

.. python-run::

   status_per_boro["Bronx"]["Alive"]

   status_per_boro["Bronx", "Alive"]

Our desired result is a data frame, not a series with a hierarchical
index, but before we convert the result to the right type, let's add
some code to calculate percentages rather than the counts:

.. python-run::

   pct_per_boro = status_per_boro/trees.groupby("boroname").size()*100
   pct_per_boro


Notice that while the numerator of the division operation is a series
with a hierarchical index, the denominator is a series with a flat
index.  Pandas uses Numpy-style broadcasting to convert the
denominator into something like this value:

.. parsed-literal::

   boroname       status
   Bronx          Alive       85203
                  Dead        85203
                  Stump       85203
   Brooklyn       Alive      177293
                  Dead       177293
                  Stump      177293
   Manhattan      Alive       65423
                  Dead        65423
                  Stump       65423
   Queens         Alive      250551
                  Dead       250551
                  Stump      250551
   Staten Island  Alive      105318
                  Dead       105318
                  Stump      105318
   dtype: float64

before performing the division.  Similarly, the value 100 is broadcast
into a series with the right shape before the multiplication is done.

We now have the right values in the wrong form. We need to convert the
series into a data frame with the borough names as the index and the
different values for status (``'Alive'``, ``'Dead'``, and ``'Stump'``)
as the column labels.  There are a couple of ways to accomplish this
task. For now, we'll describe the most straight-forward approach: use
the ``unstack`` method, which converts a series with a hierarchical
index into a data frame.  By default it uses the lowest level of the
hierarchy as the column labels in the new data frame and the remaining
levels of the hierarchical index as the index of the new data frame.
In our example, ``unstack`` will use the ``boroname`` as the data
frame index and the values of ``status`` as the column labels, which
is exactly what we want:

.. python-run::

   pct_per_boro.unstack()

We've walked through several steps to get to this point, let's put
them together before we move on:

.. python-run::

   counts_per_boro = trees.groupby("boroname").size()
   status_per_boro = trees.groupby(["boroname", "status"]).size()
   pct_per_boro = status_per_boro/counts_per_boro * 100.0
   pct_per_boro_df = pct_per_boro.unstack()
   pct_per_boro_df

We are now close to answering the question of how tree health differs
by borough.  The last step is to replace the ``Alive`` column in our
current result with three new columns--- ``Good``, ``Fair``, and
``Poor``---using information in the ``health`` column.

A common way to do this type of task is to compute and then process a
new column with the combined information---health for live trees and
status for dead trees and stumps.  We'll use the Pandas ``where``
method to compute the new column (``combined``) and then
add it to the ``trees`` data frame using an assignment statement.

.. python-run::

    trees["combined"] = trees.status.where(trees.status != "Alive", trees.health)

The ``where`` method will return a series with the same shape and
index as ``trees.status``.  A given entry in this series will hold the
same value as the corresponding entry in ``trees.status`` if the
corresponding entry has a value other than ``"Alive"`` and the
corresponding value from ``trees.health``, if not.  The ``where``
method uses the index to identify corresponding entries.  In this
example, every index value in ``trees.status`` appears in both the
condition and in what is known as the *other* argument
(``tree.health``, in our example).  When a given index is missing from
either the condition or from the other argument, ``where`` will insert
a ``NaN`` into the result.

Here's some sample data from the result:

.. python-run::

   trees[629:632]

Rows 629-631 happen to contain information about a live tree, a dead
tree, and a stump. Notice that the new ``combined`` column contains
the health of the first tree, which is live, but the status for the
other two, which are not.

Once we have completed our computation, we can drop the ``combined``
column from the data frame using ``drop`` with ``axis=1``.  Putting it
all together, we get this function, which computes a data frame with
information about how tree health differs by borough:

.. python-run::

    def tree_health_by_boro(trees):
        trees["combined"] = trees.status.where(trees.status != "Alive", 
                                               trees.health)
        num_per_boro = trees.groupby("boroname").size()
        combined_per_boro = trees.groupby(["boroname","combined"]).size()
        pct_per_boro = combined_per_boro/num_per_boro*100.0
	pct_per_boro_df = pct_per_boro.unstack()
        trees.drop("combined", axis=1)
        return pct_per_boro_df[["Good", "Fair", "Poor", "Dead", "Stump"]]

    tree_health_by_boro(trees)

By default, ``unstack`` will order the columns by value, which is not
ideal for our purposes.  Our function solves this problem by indexing
the result of ``unstack`` with a list of the columns in the preferred
order.

It seems a little silly to add a column and almost immediately remove
it.  And, in fact, we don't actually need to add the combined data to
the data frame to use it in a call ``groupby``.  In addition to
specifying the groups using one or more column names, we can also
specify the groups using one or more series.  We can even combine the
two approaches: use one or more column names and one or more series.

Let's look at what happens when we use a single series to specify the
groups:

.. python-run::

  combined_status = trees.status.where(trees.status != "Alive", 
                                       trees.health)
  trees.groupby(combined_status).size()

The groups are determined by the values ``combined_status``.  A row
from ``tree`` is included in a given group, if ``combined_status``
contains an entry with the same index and the associated value matches
the group's label.  For example, ``177922`` appears as an index value
in both ``trees`` and ``combined_status``:

.. python-run::

   combined_status.loc[177922]

   trees.loc[177922]

This tree will be in the ``'Stump'`` group, because that's the value
of tree ``177922`` in ``combined_status.loc``.  In contrast, tree
``180683`` will be in group ``'Fair'``, because that's its value in
``combined_status``:

.. python-run::

   combined_status.loc[180683]

   trees.loc[180683]

In this case, every index value in ``trees`` has a corresponding value
in the index for ``combined_status``.  If ``trees`` had contained an
index that did not occur in ``combined_status``, then the
corresponding row would not have appeared in any group.  Similarly, an
index that appeared in ``combined_status`` and not ``trees`` would not
have an impact on the result.  This process of matching up the indices
and discarding entries that do not have mates is known as an *inner
join*.

While this example used a single series, we can also use a list or
tuple of series to specify the groups.  In this case, a row from the
data frame is included in the result if its index occurs in all the
series in the list.  The row's group is determined by creating a tuple
using its index to extract the corresponding values from each of the
series.

We can also mix column names and series.  In this case, you can think
of the column name as a proxy for the column as a series.  That is,
``trees.groupby("boroname", "status")`` is the same as
``trees.groupby([trees.boroname, trees.status])``.

Using this approach, we can skip adding the "combined" field to
``trees`` and just use the series directly in the ``groupby``:

.. python-run::

    def tree_health_by_boro(trees):
        combined_status = trees.status.where(trees.status != "Alive", 
                                             trees.health)
        num_per_boro = trees.groupby("boroname").size()
        combined_per_boro = trees.groupby(["boroname",combined_status]).size()
        pct_per_boro = combined_per_boro/num_per_boro*100.0
	pct_per_boro_df = pct_per_boro.unstack()
        return pct_per_boro_df[["Good", "Fair", "Poor", "Dead", "Stump"]]

    tree_health_by_boro(trees)


Pivoting
--------

In the previous section, we used ``unstack`` to convert a series with
a hierarchical index into a data frame with a flat index.  In this
section, we'll look at another way to handle the same task using the
``pct_per_boro`` series:

.. python-run::

   pct_per_boro

As first step, we will convert the series into a data frame using
the series' ``to_frame`` method:
      
.. python-run::

   pct_per_boro_df = pct_per_boro.to_frame()            
   pct_per_boro_df

The resulting data frame retains the hierarchical index from the series
and has a single column with name ``0``.  Using ``reset_index``, we
can shift the hierarchical index values into columns and construct a
new range index:

.. python-run::

   pct_per_boro_df = pct_per_boro_df.reset_index()
   pct_per_boro_df

You'll notice that this data frame is long and thin as opposed to
short and wide, as is desired.  Before we convert the data frame into
the appropriate shape, let's rename the column labelled ``0`` into
something more descriptive:

.. python-run::

   pct_per_boro_df.rename(columns={0:"percentage"}, inplace=True)

Finally, we can use the data frame ``pivot`` method to convert a long
and thin data frame into a short and wide data frame.  This function
takes three parameters: a column name to use as the index for the new
data frame, a column to use to make the new data frames' column names,
and the column to use for filling the new data frame.  In our case,
we'll use the borough name as the index, the ``status`` column to
supply the column names, and the recently renamed ``percentage``
column to supply the values:

.. python-run::

   pct_per_boro_pvt = pct_per_boro_df.pivot("boroname", "status", "percentage")
   pct_per_boro_pvt


Because every borough has at least one tree of each status, values are
available for all the entries in pivot result.  If a combination is
not available, ``pivot`` fills in a ``NaN``.  We can see an example of
this by computing a pivot table for tree species per boro:

.. python-run::

    species_per_boro = trees.groupby(["spc_common", "boroname"]).size()
    species_per_boro_df = species_per_boro.to_frame().reset_index()
    species_per_boro_pvt = species_per_boro_df.pivot("spc_common", "boroname", 0)

and then by examining the resulting value for a species named Atlas
cedar:

.. python-run::

   species_per_boro_pvt.loc["Atlas cedar"]

Notice that the entry for ``Manhattan`` is ``NaN``.

In case  you are curious, here's the  code that we used  to identify a
tree to use as an example:

.. python-run::

   species_per_boro_pvt[species_per_boro_pvt.isnull().any(axis=1)]

Let's pull this expression apart.  The expression
``species_per_boro_pvt.isnull()`` yields a data frame of booleans with
the same shape as ``species_per_boro_pvt``, that is 132 (species) by 5
(boroughs).  A given entry is ``True`` if the corresponding entry in
``species_per_boro_pvt`` is ``NaN``.  We use a reduction to convert
this value into a series of booleans, where the ith entry is ``True``
if the ith row contains at least one ``True``.  Recall from our
discussion of reductions in the Numpy chapter, that we use an axis of
one when to apply the reduction function to the rows.  Also, recall
that ``any`` returns ``True`` if at least one value in the input is
``True``.  Putting this together: the expression
``species_per_boro_pvt.isnull().any(axis=1)`` yields a series of
booleans, one per tree type, that will be ``True`` if the
corresponding entry in ``species_per_boro_pvt`` contains a ``NaN``
for at least one borough.  Finally, we use this series as a filter to
the original pivot table to extract the desired entries.

While we'll admit that this code computes a somewhat esoteric
result---species that occur in some, but not all five boroughs---it is
impressive how little code is required to extract this information
from the data set.

As an aside, in this case, it makes sense to replace the null values
with zeros.  We can do this task easily using the ``fillna`` method:

.. python-run::

    species_per_boro_pvt.fillna(0, inplace=True)
    species_per_boro_pvt.loc["Atlas cedar"]

As in other cases, adding ``inplace=True`` as a parameter instructs
``fillna`` to make the changes in place rather construct a new data
frame.

Saving space with Categoricals
------------------------------

Our tree data set contains nearly 700,000 rows, so a natural question
to ask is: how large is the memory footprint?  We can answer this
question using the ``info`` method for data frames.  Like many Pandas
methods, ``info`` has a variety of options.  For our purposes, we'll
use the ``verbose=False`` option, which reduces the amount of
information generated by the method and ``memory_usage="deep"``
option, which tells ``info`` to include all the memory costs
associated with the data frame.  Before we run ``info``, we'll reload
the data from the file to clean up any extra columns left over from
our earlier computation:

.. python-run::

   trees = get_tree_data("2015StreetTreesCensus_TREES.csv")
   trees.info(verbose=False, memory_usage="deep")

The last line of the output tells us that our ``trees`` data frame
uses more than 180MB of space, which is non-trivial.  One way to
reduce this amount is to replace strings with categoricals, which are
more space efficient.  Categorical variables are used to represent
features that can take on a small number of values, such as, borough
names or the ``status`` and ``health`` fields of our tree data set.
Though we can represent these values as strings, it is more space
efficient to represent them using the Pandas ``Categorical`` class,
which uses small integers as the underlying representation. This
efficiency may not matter for a small dataset, but it can be
significant for a large dataset.

We can construct a categorical variable from the values in a series
using the ``astype`` method with ``"category"`` as the type.  Here's
some code that displays a slice with borough names for the first five
entries in the ``trees`` data frame, constructs a new series from the
``boroname`` field using a categorical variable, and then shows the
first five values of the new series:

.. python-run::

  trees.boroname[:5]
  boro_cat = trees.boroname.astype("category")
  boro_cat[:5]

Notice that the ``dtype`` has changed from ``object`` to ``category``
and that the category has five values ``Bronx``, ``Brooklyn``, etc.

Using this simple mechanism dramatically reduces the memory footprint
of the trees data.  Specifically, we can reduce the amount of memory
needed by a factor of 10 by converting the ``boroname``, ``health``,
``spc_common``, and ``status`` fields from strings to categoricals:

.. python-run::

   for col_name in ["boroname", "health", "spc_common", "status"]:
       trees[col_name] = trees[col_name].astype("category")

   trees.info(verbose=False, memory_usage="deep")

..
    This example no longer works and needs to be updated.
    See: https://stackoverflow.com/questions/37952128/pandas-astype-categories-not-working

    Unlike categorical variables in statistics, Pandas categorical
    variables can be used to represent features that have an inherent
    ordering.  For example, we might want to specify an ordering on the
    possible values for the health field (``Poor < Fair < Good``), which
    we can do by specifying extra parameters to the ``astype`` method.q

    .. python-run::

       trees = get_tree_data("2015StreetTreesCensus_TREES.csv")
       health_as_ordered_cat = trees.health.astype("category",
                                                   categories=["Poor", "Fair", "Good"],
                                                   ordered=True)
       health_as_ordered_cat[:5]


Another way to create a ``Categorical`` is to define a set of labelled
bins and use them along with the method ``pd.cut`` to construct a
categorical variable from a series with numeric values.  Our tree data
does not have a natural example for this type of categorical, so we'll
use ten sample diastolic blood pressure values as an example:

.. python-run::

   dbp_10 = pd.Series([92, 74, 80, 60, 72, 90, 84, 74, 75, 70])     

We might want to label values below 80 as "normal", values between 80
and 90 as pre-hypertension, and values at 90 or above as high.  To
define the bin boundaries, we specify an ordered list of values:

.. python-run::

   dbp_bins = [0.0, 80, 90, float("inf")]

The values are paired in sequence to create the bin boundaries : [0.0,
80], (80, 90], and (90, float("inf")].  By default, the right value in
each pair is not included in the bin.  Also, by default the first
interval does not include the smallest value.  Both of these defaults
can be changed using optional parameters named ``right`` and
``include_lowest`` respectively.  Somewhat counter-intuitively,
``right`` needs to be set to ``False``, if you want to include the
rightmost edge in the bin.

The bin labels are specified as a list:

.. python-run::

   dbp_labels = ["normal", "pre-hypertension", "high"]

The number of labels should match the numbers of bins, which means
this list is one shorter than the list of floats used to define the
bin boundaries.  

Give these bin boundaries and labels, we can create a categorical
variable from the sample diastolic blood pressures using ``pd.cut``:

.. python-run::

   pd.cut(dbp_10, dbp_bins, labels=dbp_labels, right=False)

As expected from the description above, patients 3, 4, 7-9 are
labelled as having "normal" diastolic blood pressure, patients 2 and 6
are labelled with "pre-hypertension" and patients 0 and 5 are labelled
has having high diastolic blood pressure.

Summary
-------

Pandas is very complex library and we have barely skimmed the surface
of its many useful features. We strongly encourage you to look at the
documentation to explore the wealth of options it provides.

.. todo:: missing topics: merge, transform, and apply. plotting.





