.. _chapter-numpy:

NumPy
=====

NumPy is a Python library that supplies two major features. First, it 
provides better support for large multi-dimensional arrays. Second, it 
provides high-level mathematical functions that operate on them.

Unlike many other languages, Python doesn’t include a native type for
arrays or matrices. Instead, we could use lists, lists-of-lists,
lists-of-lists-of-lists, etc. Although these data structures can be
used to represent multi-dimensional arrays, working with them can get
pretty messy.  As an example, let's look at some data from the
National Institute of Diabetes and Digestive and Kidney
Diseases.  (The data is available at the `UCI Machine Learning
Repository
<http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes>`_)
During this study, information was collected for a group of patients
from the Pima Indian Tribe.  We can represent this data with a matrix
in which each row corresponds to the data collected for an individual
patient and each column corresponds to a specific feature (e.g.,
diastolic blood pressure) for all the patients. Here is subset of the
data that includes information for ten patients for four features
(plasma glucose level, diastolic blood pressure, triceps skin
foldthickness, and two-hour serum insulin):

.. parsed-literal::

    [[89.0, 66.0, 23.0, 94.0],
     [137.0, 40.0, 35.0, 168.0],
     [78.0, 50.0, 32.0, 88.0],
     [197.0, 70.0, 45.0, 543.0],
     [189.0, 60.0, 23.0, 846.0],
     [166.0, 72.0, 19.0, 175.0],
     [118.0, 84.0, 47.0, 230.0],
     [103.0, 30.0, 38.0, 83.0],
     [115.0, 70.0, 30.0, 96.0],
     [126.0, 88.0, 41.0, 235.0]]


.. todo:: add citation to the Pima Indians data set.  Is it OK to use this data as an example?  What is the right citation.

Before applying classification or prediction algorithms, statisticians
often standardize data such that each feature (or variable) in the
matrix for analysis has a mean of zero and standard deviation of
one. Let's consider this common pre-processing step.  Specifically,
the values in the standardized matrix, :math:`m^{\prime}` should be
computed using the following formulas:

.. math::

       \mu_{j} &= 1/N*\sum_{i=0}^{N-1} m_{i,j} \\
       \\
       \sigma_{j} &= \sqrt{1/N*\sum_{i=0}^{N-1} (m_{i,j}-\mu_{j})^2} \\
       \\
       m^{\prime}_{i,j} &=  (m_{i,j} - \mu_{j})/\sigma_j \\


where :math:`m_{i,j}` is the value of the jth feature for patient i,
:math:`\mu_{j}` is the mean of the jth feature, and :math:`\sigma_{j}` is
its standard deviation.

We can translate these formulas into code that uses for loops and
list indexing to process data that is represented as a list of lists:

.. python-run::
   :formatting: separate


   def compute_feature_mean(data, j):
       '''
       Compute the mean of feature (column) j
   
       Inputs:
         data (list of list of floats)

       Returns (float): mean of feature j
       '''

       N = len(data)
       total = 0
       for i in range(N):
           total += data[i][j]
       return total/N


   def compute_feature_stdev(data, j):
       '''
       Compute the standard deviation of feature (column) j
   
       Inputs:
         data (list of lists of floats)

       Returns (float): standard deviation of feature j
       '''

       N = len(data)
       mu = compute_feature_mean(data, j)
       total = 0
       for i in range(N):
           total = total + (data[i][j] - mu) ** 2
       return math.sqrt(1 / N * total)

   def standardize_features(data):
       '''
       Standardize features to have mean 0.0 and standard deviation
       1.0.

       Inputs:
         data (list of list of floats): data to be standardized
	   
       Returns (list of list of floats): standardized data
       '''

       N = len(data)
       M = len(data[0])

       # initialize the result w/ NxM list of lists of zeros.
       rv = []
       for i in range(N):
           rv.append([0] * M)
        
       # for each feature
       for j in range(M):
           mu = compute_feature_mean(data, j)
           sigma = compute_feature_stdev(data, j)

           # standardized feature
           for i in range(N):
               rv[i][j] = (data[i][j] - mu)/sigma

       return rv


While this code is straightforward, it is nowhere near as compact as
the mathematics and it is easy to get the indexing wrong.  Also, the
functions ``compute_feature_mean`` and ``compute_feature_stdev`` are
not as general as one might like.  For example, they are not
particularly useful for computing the mean of a list or the standard
deviation of a row in a list-of-lists.

We can use list comprehensions to make the helper functions more
compact, but the resulting code is still not as general as one would
like:

.. python-run::
   :formatting: separate

   def compute_feature_mean(data, j):
       '''
       Compute the mean of feature (column) j.
   
       Inputs:
         data (list of lists of floats)

       Returns (float): mean of feature j
       '''

       N = len(data)
       return sum([data[i][j] for i in range(N)]) / N

   def compute_feature_stdev(data, j):
       '''
       Compute the standard deviation of feature (column) j.
   
       Inputs:
         data (list of lists of floats)

       Returns (float): standard deviation of feature j
       '''

       N = len(data)
       mu = compute_feature_mean(data, j)
       return math.sqrt(1 / N * sum([(data[i][j] - mu) ** 2 for i in range(N)]))


List-of-lists do not provide an easy way to operate on a subset of the
elements of the data structure, such as the elements of a column, as a unit. 
Consequently, our functions are awkward and unwieldy. 
As you will see later in this chapter, NumPy's array data
structure supports operations that work on the elements of an array
collectively and allows programmers to apply these operations to
operands of different sizes and shapes. It also provides easy ways to
read and update sub-arrays.


Using these mechanisms, we can write code that is substantially more
compact and resembles the underlying mathematics. The function 
``standardize_features``, for example, can be written as:

.. python-run::
   :formatting: separate

   def standardize_features(data):
       '''
       Standardize features to have mean 0.0 and standard deviation
       1.0.

       Inputs:
         data (2D NumPy array of floats): data to be standardized

       Returns (2D NumPy array of floats): standardized data
       '''

       mu = data.mean(axis=0)
       sigma = data.std(axis=0)
       return (data - mu) / sigma

Although we do not expect you to grasp the details of this function
right now, you can see that this version is more compact. Once you
have finished this chapter, we hope that you will find this version easier to
understand and reproduce than the loops and lists version.


Importing NumPy
---------------

Before we can use NumPy, we need to import it.  Traditionally,
programmers use the ``as`` option with ``import`` to import NumPy and
assign it a short alias (``np``):

.. python-run::

   import numpy as np


Creating arrays
---------------

There are a variety of ways to create arrays.  The easiest is to call
the NumPy ``array`` method with a list as a parameter. We use
as many levels of list nesting as desired dimensions in the array.
Here's code, for example, that allocates sample arrays that have one
(``a1d``), two (``a2d``), and three (``a3d``) dimensions and shows
their values:

.. python-run::

    a1d = np.array([1,2,3])
    a1d
    
    a2d = np.array([ [1,2,3] , [4,5,6] ])
    a2d

    a3d = np.array([ [ [1,2,3] , [4,5,6] ] , [ [10,20,30] , [40,50,60] ] ])
    a3d

Unlike lists, all of the elements in an array must have the same type
and the size of an array is fixed once it has been created. These
limitations help enable operations on Numpy arrays to be
more efficient than similar list operations.

Arrays have several useful properties: we can determine the array's number of
dimensions using the ``ndim`` property and sizes of dimensions using the 
``shape`` property, which evaluates to a
tuple with one integer value per dimension:

.. python-run::

   print("a3d has", a3d.ndim, "dimensions")
   print("a3's shape is:", a3d.shape)

An array's ``size`` property yields the number of elements in the
array, or the product of its shape.

.. python-run::

   print("a3 has", a3d.size, "values")


We can construct arrays of all zeros or all ones using the NumPy
library routines ``zeros`` and ``ones``.  These methods will construct
a one-dimensional array of length ``N`` if called with an integer
argument, ``N``, or an N-dimensional array if called with a tuple of
integers of length ``N``.  Here are some examples:

.. python-run::

   np.zeros(10)

   np.zeros((2, 2))

   np.ones((3, 2, 2))

NumPy also includes a couple of routines, ``arange`` and
``linspace``, for constructing arrays that range over a set of
values.  Both functions are more versatile than Python’s ``range``
function.  The ``arange`` function creates arrays of values that range
from a lower bound up to but not including an upper bound in specified
increments.  The lower bound, upper bound, and increment can all be
floating point values.

.. python-run::

    np.arange(1, 3, 0.5)
    np.arange(3, 1, -0.5)

As with the ``range`` function, the lower bound is optional and
defaults to zero.  The increment is also optional and defaults to one.

.. python-run::

    np.arange(3)


The ``linspace`` function is similar, but takes the desired number of
values in the resulting array as an argument, instead of the interval
between values, and the upper bound is included in the result. For
example, if we wanted to create an array with seven equally-spaced
values between 0 and 100 (inclusive), we would just use the following:

.. python-run::

    np.linspace(0, 100, 7)

Finally, NumPy includes a function, ``loadtxt``, for loading data from
a file into an array.  This function takes the name of the file as a
required argument.  Programmers can also specify the data type of the
values, a number of header rows to skip (``skiprows``), the delimiter
that is used to separate values in a row (``delimiter``), etc.  We
can load the data shown above from a file named
``pima-indians-diabetes.csv`` into an array named ``data`` with this
call to the ``loadtxt`` function:

.. python-run::

    data = np.loadtxt("pima-indians-diabetes.csv", skiprows=1, delimiter=",")
    data


.. todo:: Do we want to use a reduced version of the dataset to match the list of lists example at the start of the chapter?


Array indexing and slicing
--------------------------

NumPy arrays support a variety of ways to access the stored data.  The
most familiar mechanism uses square brackets to index the array and
looks like list indexing:

.. python-run::

    a1d[2]

    a2d[1][2]

    a3d[1][1][2]

Experienced NumPy programmers, however, typically use an alternate
format that accepts tuples as indexes.  The first item in the tuple
specifies the row index, which is the first dimension, the second
item specifies the column index, which is the second dimension, and so on.
Our first example above does not change because ``a1d`` is one-dimensional.  
The latter two examples, however, would be written by an
experienced programmer as:

.. python-run::

    a2d[1, 2]

    a3d[1, 1, 2]


Like lists, array elements are mutable, and can be updated using an
array index on the left side of an assignment statement.  For example,
notice the change in the value of ``a1d`` shown before and after
the assignment statement in the following code:

.. python-run::

    a1d
    a1d[0] = 7
    a1d


Programmers can slice NumPy arrays using slicing notation familiar
from lists.  Let's look at some examples of slicing using a
one-dimensional array, named ``a``.

.. python-run::

    a = np.array([0,   1,   4,   9,  16,  25,  36,  49,  64,  81, 100, 121])

    a[1:7]
    a[3:10:2]
    a[:]
    a[10:3:-1]

Recall that the format for specifying a slice is: ``X:Y:Z``, where ``X``
specifies an inclusive lower bound, ``Y`` specifies an exclusive upper
bound, and ``Z`` specifies the increment.  If omitted, the
lower bound defaults to zero, the upper bound defaults to ``N``, where
``N`` is the size of a one-dimensional array and the size of the
corresponding dimension for a multi-dimensional array, and finally,
the increment defaults to one.  The second colon is typically omitted
when the desired increment is one.  Using a single colon (``:``) to
specify a slice combines these defaults and is equivalent to
specifying ``0:N:1`` as the slice.

Slicing one-dimensional arrays is not all that different from slicing
lists.  Things get more interesting when slicing multi-dimensional arrays.  Here are a few examples:

.. python-run::

    b = np.array([[0, 1, 4, 9],
                  [16, 25, 36, 49],
                  [64, 81, 100, 121],
                  [144, 169, 196, 225],
                  [256, 289, 324, 361],
                  [400, 441, 484, 529]])
    b[1:4, :3]
    b[:, 2]

The first example extracts the value of a 3x3 sub-array that consists of
the first three columns (written as ``0:3:1`` in long form or ``:3``,
using the defaults) from rows one, two, and three (``1:4:1`` or
``1:4``) of ``b``.  The second extracts all the values in column two
as a *one-dimensional* array.

Sub-arrays, like single elements, can be updated by specifying a slice
on the left side of an assignment statement and an array with the same
shape and type as the slice on the right side. (We'll see later that
the same-shape requirement can be relaxed in some cases.)

.. python-run::

   b[:, 2] = np.array([7, 7, 7, 7, 7, 7])
   b

This ability to extract and modify columns and, more generally,
sub-arrays, with ease explains, in part, the appeal of NumPy as a tool.
In many cases, NumPy will allow us to perform, in just one or two
lines of code, operations that would typically require using one or
more loops with lists.

To make this idea concrete, let's return to our standardization
example.  We can replace the list comprehension in our second
implementation of ``compute_feature_mean`` with a slice:


.. python-run::
   :formatting: separate

   def compute_feature_mean(data, j):
       '''
       Compute the mean of feature (column) j.
   
       Inputs:
         data (2D NumPy array of floats)

       Returns (float): mean of feature j
       '''

       N = data.shape[0]
       return sum(data[:, j]) / N


As you might expect, the built-in ``sum`` function returns the sum of  
elements when it is called on an array.


Operations on arrays
--------------------

NumPy supports a rich set of operations that behave quite differently 
than similar-looking operations on lists.  In particular,
many operations operate element-by-element rather than on the array as
a unit.  Let's use the array ``a2d`` defined earlier as an example:

.. python-run::

   a2d

If we multiply ``a2d`` by the integer ``2``, we get back a new array in
which element (i, j) has the value ``a2d[i, j] * 2``.

.. python-run::

   a2d * 2

The same operation on a list, in contrast, would perform repeated
concatenation:

.. python-run::

   l2 = [[1, 2, 3], [4, 5, 6]]
   l2 * 2


Here are a few more examples:

.. python-run::

   a2d + 2
   a2d > 2
   a2d == 2

Notice that the second and third examples yield results that have the
same shape as ``a2d``, but that the elements are booleans rather than
floats.  These operations will turn out to be very useful when we
discuss boolean indexing later in the chapter.

We can use these scalar operations plus slicing to rewrite our
``compute_feature_stdev`` function more compactly:

.. python-run::
   :formatting: separate

   def compute_feature_stdev(data, j):
       '''
       Compute the standard deviation of feature (column) j.
   
       Inputs:
         data (2D NumPy array of floats)

       Returns (float): standard deviation of feature j
       '''

       N = data.shape[0]
       mu = compute_feature_mean(data, j)
       return math.sqrt(1 / N * sum((data[:, j] - mu) ** 2))

This version of the function uses slicing to extract the feature as a
one-dimensional array. It then subtracts the mean (``mu``), which is a
float, from the values in this array and compute the squares of the
subtracted values.  In both operations, one operand is a
one-dimensional array and the other is a scalar (a float, in this
case).  The rest of the expression uses standard floating point
operations and the square root function from the ``math`` library.

In addition to these scalar operations, NumPy also supports operations
where both operands are arrays.  In the simplest case, both operands
have the same shape and the operation is performed element-by-element.

.. python-run::

   x = np.array([[10, 20, 30],
                 [40, 50, 60]])
   a2d + x
   a2d / x

Using these element-wise operations, we can rewrite our code to
standardize features more compactly:

.. python-run::
   :formatting: separate

   def standardize_features(data):
       '''
       Standardize features to have mean 0.0 and standard deviation
       1.0.

       Inputs:
       data (2D NumPy array of floats): data to be standardized
	   
       Returns (2D NumPy array of floats): standardized data
       '''

       N,M = data.shape

       mus = [compute_feature_mean(data, j) for j in range(M)]
       mu_vec = np.array(mus)
       sigmas = [compute_feature_stdev(data, j) for j in range(M)]
       sigma_vec = np.array(sigmas)

       # initialize the result w/ NxM list of lists of zeros.
       rv = np.zeros(data.shape)
        
       # for each row
       for i in range(N):
           rv[i] = (data[i] - mu_vec) / sigma_vec

       return rv

This version constructs arrays with the means and standard deviations
of features and then uses element-wise subtraction and division to
standardize the rows of the data.

.. admonition:: A common pitfall

   What do you think is the result of using the ``*`` operator?

   .. python-run::

      d = np.array([[1, 2], [3, 4]])
      e = np.array([[1, 0], [0, 1]])

      d
      e

      d * e

   It's element-wise multiplication, not matrix multiplication!  We
   need to use the ``dot`` method to compute a matrix product. 

   .. python-run::

       np.dot(d, e)

NumPy also supports a large number of mathematical functions, such as
``np.sin``, that are applied element-wise:

.. python-run::

    f = np.array([[1, -1], [np.pi, -np.pi]])
    f

    np.cos(f)


Reshaping arrays
----------------

Before we discuss more complex operations on arrays, we must introduce the
notion of reshaping an array.  We can change an array's shape using
the ``reshape`` method:

.. python-run::

    a = np.arange(12)
    a
    ra = a.reshape(3, 4)
    ra

Be aware that the original array and the reshaped
array share the same underlying data.  This design has two
consequences. First, the size (i.e., the number of elements) of the
original array and the size of the reshaped array must be the same.
So, this expression:

.. parsed-literal::

    np.linspace(0, 100, 10).reshape(2, 5)

which creates a one-dimensional array with 10 elements and then
resizes it into a two-dimensional array that spreads these ten values
over two rows with five values each, is acceptable. On the other hand, 
this expression:

.. parsed-literal::

    np.linspace(0, 100, 7).reshape(2, 5)

which tries to reshape an array with seven elements into one with ten
elements, is not.

Second, if you reshape an array, updating either the original or the reshaped array updates both arrays!  Notice in this code, for example, that both ``a`` and ``ra`` change as a result of the update to ``a[0]``:

.. python-run::

   a[0] = 7
   a
   ra


Reductions
----------

Reduction methods allow us to “reduce” an array to a single value. For
example, we might want to compute the mean of all of the values, the
standard deviation of all of the values, etc. Given an array ``b``, for
example:

.. python-run::

   b = (np.arange(24) ** 2).reshape(6, 4)
   b

we can compute the mean and standard deviation using the ``mean``
and ``std`` methods:

.. python-run::

   print("The mean of b is:", b.mean())
   print("The standard deviation of b is:", b.std())

These operations can also be applied along different dimensions to
yield an array of values.  For example, we might want to compute the
means of the rows or the standard deviations of the values in each
column.  Such tasks can be accomplished by specifying an axis as an
optional argument to the reduction method. For example, to compute row means, 
we could use the expression:

.. python-run::

   b.mean(axis=1)

and to compute the standard deviations of the columns, we could use
the expression:

.. python-run::

   b.std(axis=0)

If you are like us, your immediate reaction to these expressions is,
"wait a minute, why are you specifying axis 1 to get the mean of
the rows instead of axis 0?" 

An axis specifies a family of arrays
over which to compute some desired value.  Let's think about the two-dimensional 
case first and use ``b`` as an example.  If the axis is
``0`` , the family will have four values: ``b[:, 0]``, ``b[:, 1]``,
``b[:, 2]``, and ``b[:, 3]``.  The family is constructed by slicing
``b`` using a colon in the axis dimension and each of
the possible index values in the non-axis dimension.

.. python-run::

   col_means = np.array([b[:, 0].mean(),
                         b[:, 1].mean(),    
                         b[:, 2].mean(),    
                         b[:, 3].mean()])

   b.mean(axis=0) == col_means

If the axis is ``1``, the family is constructed by slicing ``b`` with a
colon for dimension one, which picks up all the columns in a row, and
each of the possible row indices for non-axis or row dimension.

.. python-run::

   row_means = np.array([b[0, :].mean(),
                         b[1, :].mean(),    
                         b[2, :].mean(),    
                         b[3, :].mean(),
                         b[4, :].mean(),
                         b[5, :].mean()])

   b.mean(axis=1) == row_means

In general, if an array  `D`  has :math:`N` dimensions and shape
:math:`(d_0, ..., d_{i-1}, d_i, d_{i+1}, ..., d_{N-1})`, the result of
a reduction along axis :math:`i` will have :math:`N-1`
dimensions and shape :math:`(d_0, ..., d_{i-1}, d_{i+1}, ...,d_{N-1})`.
The value at index :math:`(j_0, ..., j_{i-1}, j_{i+1}, ..., j_{N-1})` will be the result of applying the reduction operation to the slice :math:`D[j_0, ..., j_{i-1}, :, j_{i+1}, ..., j_{N-1}]`.

To make this concrete, let's reshape ``b`` into a three-dimensional array and take the sum
along axis one:

.. python-run::
   
   b2 = b.reshape((3, 2, 4))
   b2
   b2.sum(axis=1)


As expected, the resulting array has shape :math:`(3, 4)`
and the resulting value at index ``(1, 2)``, for example, is the
sum of slice ``b2[1, :, 2]``.

.. python-run::

   b2[1, :, 2]
   sum(b2[1, :, 2])

Returning to our example, we can replace the code to compute the mean
and standard deviation arrays with reductions along axis 0:

.. python-run::
   :formatting: separate

   def standardize_features(data):
       '''
       Standardize features to have mean 0.0 and standard deviation
       1.0.

       Inputs:
         data (2D NumPy array of floats): data to be standardized

       Returns (2D NumPy array of floats): standardized data
       '''

       N,M = data.shape

       mu_vec = data.mean(axis=0)
       sigma_vec = data.std(axis=0)

       # initialize the result w/ NxM list of lists of zeros.
       rv = np.zeros(data.shape)
        
       # for each row
       for i in range(N):
           rv[i] = (data[i] - mu_vec) / sigma_vec

       return rv


Fancy indexing
--------------

NumPy supports fancier ways of indexing that are more powerful than
those provided for regular Python lists.  The simplest of these
mechanisms allows us to specify the desired indexes with a list:

.. python-run::

    a = np.arange(100, 112)
    a
    a[ [1, 3, 6] ]


In this case, the result is a one-dimensional array with three values:
``a[1]``, ``a[3]``, and ``a[6]``.

If we use a multi-dimensional array as the index, the values at the
specified indices in the data array are returned in an array of the same shape
as the index array.

.. python-run::

    a[ np.array([ [1,3] , [10, 7] ]) ]


Indexing with an array of booleans yields a *flattened*, that is,
one-dimensional, array.  A value from the data array is included in
the result if the corresponding value in the index array has the value
``True``.

.. python-run::

    c = np.array([100, 200, 300])
    c[np.array([True, False, True])]

This indexing method is most useful in combination with relational
operators:

.. python-run::

    b = (np.arange(24) ** 2).reshape(6, 4)
    b
    b > 100
    b[b > 100]

When we use this mechanism with assignments, the elements specified by
the filter are updated.  For example, here's a statement that sets all
elements in ``b`` greater than 100 to zero:

.. python-run::

    b[b > 100] = 0
    b

Filters can be combined using the element-wise and (``&``), or
(``|``), and xor (exclusive or) operations (``^``).  Here, for example, is a
statement that replaces the odd values greater than 100 with zeros in
``b``:

.. python-run::

    b = (np.arange(24) ** 2).reshape(6, 4)
    b[(b > 100) & (b % 2 == 1)] = 0
    b


If we put all of the above together, we can do some pretty elaborate
computations with arrays/matrices in just a few lines.  For example,
we might want to filter out all outliers in ``b`` that are more than
one standard deviation away from the mean:

.. python-run::

    b = (np.arange(24) ** 2).reshape(6, 4)
    b2 = b - b.mean()
    b[abs(b2 / b2.std()) < 1]


Advanced topics
---------------

This section covers advanced topics: broadcasting, the linear algebra
library, and matrices.  You can safely skip this part on your first
read.  Understanding broadcasting is helpful, but it is a complex
topic that may be easier to grasp after you've had some experience with
arrays.


Broadcasting
~~~~~~~~~~~~

In the previous section, we described operations with one array and
one scalar operand and operations on two arrays of the same shape.  In
this section, we will discuss the process of broadcasting, which makes
it possible to perform operations on arrays that have compatible but
not identical shapes.  In these cases, NumPy *logically* constructs
intermediate values that have the same shape using *broadcasting* before
performing the element-by-element operations.  For the sake of efficiency,
NumPy does not actually construct these intermediate values in memory,
but we'll describe the process as if it does because it makes
broadcasting easier to understand.

We'll start our explanation by describing the broadcasting process
using a pair of arrays that have the same number of dimensions and
then discuss what to do when the arrays do not have the same
number of dimensions.  

Assume we have two arrays, :math:`D` and :math:`E`, with shapes
:math:`(d_0, d_1, ..., d_{N-1})` and :math:`(e_0, e_1, ..., e_{N-1})`
respectively.  The arrays are *compatible* if :math:`d_i = e_i`,
:math:`d_i = 1`, or :math:`e_i = 1` for :math:`0 \leq i < N`.  That
is, two arrays are compatible if, for every dimension, the arrays
either have the same size along that dimension or one of them has size
one for that dimension.

Let's make this more concrete by looking at the compatibility of a few
different combinations of sample arrays.

.. python-run::

   a2by3 = np.array([[1, 2, 3], 
                     [4, 5, 6]])
   a2by3.shape

   a1by3 = np.array([[4, 5, 6]])
   a1by3.shape

   a3by3 = np.array([[4,  5,  6], 
                     [7,  8,  9],
                     [10, 11, 12]])
   a3by3.shape

   a2by1 = np.array([[1], 
                     [2]])
   a2by1.shape

The arrays ``a2by3`` and ``a1by3`` are compatible because ``a1by3`` has
size one for the first dimension and ``a2by3`` and ``a1by3`` both have
the same size (``3``) in the second dimension.  Similar reasoning
explains that ``a1by3`` and ``a2by1`` are also compatible.
The arrays ``a2by3`` and ``a3by3``, in contrast, are not compatible
because they have different sizes for the first dimension and those
sizes are both greater than one.  As a result, the expression
``a2by3 + a3by3`` will fail when evaluated.

.. python-run::

   a2by3 + a3by3

The next step is to determine the shape of the arrays created by
broadcasting, which is computed as a function of the shapes the
underlying arrays: :math:`(max(d_0, e_0), max(d_1, e_1), ...,
max(d_{N-1}, e_{N-1}))`.  Returning to our examples, the broadcast
shape for ``a2by3 + a1by3`` is :math:`(max(2, 1), max(3, 3))` or
:math:`(2,3)`.  Similarly, the broadcast shape for ``a1by3 + a2by1`` will
be :math:`(max(1, 2), max(3, 1))` or :math:`(2,3)`.

To create an array of the correct shape, broadcasting replicates
values along the dimensions where the size of the original array is
one and the size of broadcast value is greater than one.  Once this
process is complete, NumPy can perform element-by-element operations
on the intermediate arrays to produce a result.

Let's return to our example of ``a2by3 + a1by3``.  We know that the arrays are
compatible and that the broadcast shape is :math:`(2, 3)`.  The array
``a2by3`` already has the right shape. The array ``a1by3``, on the other
hand, needs to be stretch from :math:`(1,3)` to :math:`(2,3)`, which
is accomplished by replicating along the row dimension (that is,
dimension 0):

.. parsed-literal::

    array([[4, 5, 6],
           [4, 5, 6]])

Once this intermediate value is computed, NumPy can add it to ``a2by3`` to
get a final result of:

.. python-run::

   a2by3 + a1by3

In this case, only one of the operands needed to be stretched to
construct an intermediate value of the right shape. In other cases,
both arrays need to be stretched.  For example, as noted above
``a1by3 + a2by1`` will yield a value with a shape of :math:`(2,3)`, which
requires NumPy to stretch ``a1by3`` from :math:`(1,3)` to :math:`(2,3)`
as in the previous example, and to stretch ``a2by1`` from :math:`(2, 1)`
to :math:`(2,3)`.  In the latter case, the values are replicated along
column because ``a2by1`` has size one in the second dimension:

.. parsed-literal::

   array([[1, 1, 1],
          [2, 2, 2]])

Once both values are stretched, NumPy can construct the final result
for ``a1by3 + a2by1``:

.. python-run::

   a1by3 + a2by1

Now, let's consider what happens when one of the arrays has fewer
dimensions than the other.  Since it does not matter for this
computation which is smaller, let's say that :math:`E` is smaller and
has shape :math:`(e_0, e_1, ..., e_M)` where :math:`M < N`.  To start
the broadcasting process, NumPy reshapes ``E`` into an array with
``N`` dimensions.  The shape of that array is constructed by
prepending :math:`N-M` ones to the original shape of ``E``: :math:`(1,
..., 1, e_0, e_1, ..., e_M)`.  You can think of this transformation as
being equivalent to wrapping one extra pair of square brackets around
the list passed to ``np.array`` for each added dimension.  Once the
array with fewer dimensions has been reshaped, the broadcasting
process can proceed as described above.

At the beginning of the previous section, we explained that NumPy
supports operations with one array operand and one scalar operand.  We
can explain now that these operations are supported through
broadcasting.  A scalar can be thought of as a one dimension array of
size 1.  For example, consider what happens when we compute ``a2by3 +
2``, which is equivalent to ``a2by3 + np.array([2])``.  Since
``a2by3`` has shape :math:`(2,3)` and ``np.array([2])`` has shape
:math:`(1,)`, NumPy will logically reshape ``np.array([2])`` into
``np.array([[2]])``, which has a shape of :math:`(1,1)`, as a first
step.  It will then determine that the broadcast shape for ``a2by3 +
2`` is :math:`(2,3)` and will replicate ``np.array([[2]])`` along both
dimensions to create an intermediate value of the right shape:

.. parsed-literal::

   array([[2, 2, 2],
          [2, 2, 2]])

Finally, it will add ``a2by3`` to this intermediate value to yield:

.. parsed-literal::

   array([[3, 4, 5],
          [6, 7, 8]])


Let's put all of these
ideas together and look at what happens when we add ``a1by3 + a7`` where ``a7``
is defined as:

.. python-run::

   a1by3by1 = np.array([[[1],
                         [2],
                         [3]]])
   a1by3by1.shape


Because ``a1by3`` and ``a1by3by1`` do not have the same number of dimensions,
the first step will be for NumPy to logically construct a new array
from ``a1by3`` that has the value:

.. parsed-literal::

   array([ [ [ 4, 5, 6 ] ] ])

This value, which has the shape: :math:`(1, 1, 3)`, has the same number
of dimensions as ``a1by3by1``.  NumPy will then determine that the broadcast
shape of ``a1by3 + a1by3by1`` is :math:`(1, 3, 3)` and it will construct intermediate
results of the form:

.. parsed-literal::

   array([[[ 4.,  5.,  6.],
           [ 4.,  5.,  6.],
           [ 4.,  5.,  6.]]])

and

.. parsed-literal::

    array([[[ 1.,  1.,  1.],
            [ 2.,  2.,  2.],
            [ 3.,  3.,  3.]]])


and finally combine them to yield a result of:

.. parsed-literal::

    array([[[5, 6, 7],
            [6, 7, 8],
            [7, 8, 9]]])


With NumPy, an assignment is legal as long as the array on the right side can be 
broadcast to the same shape as the array or sub-array on the left side. This 
allows us to relax the requirement for arrays on either side
of an assignment to have the same shape. For example:

.. python-run::
 
    b = (np.arange(24) ** 2).reshape(6, 4)
    b[:, 0:2] = np.array([10, 20])
    b
   
The slice referenced on the left side of the assignment statement has
shape :math:`(6, 2)`, while the array on the right-side has shape
:math:`(2, )`.  To complete the assignment, NumPy broadcasts
``np.array([10, 20])`` into:

.. parsed-literal::

   array([[10, 20], 
          [10, 20], 
          [10, 20], 
          [10, 20], 
          [10, 20], 
          [10, 20]])

which has the expected shape of :math:`(6, 2)`, and then performs the
update.



Example: Standardizing features, revisited
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We now have all the pieces necessary to understand the NumPy solution
to the task of standardizing features that we presented at the start
of the chapter.

.. python-run::
   :formatting: separate

   def standardize_features(data):
       '''
       Standardize features to have mean 0.0 and standard deviation
       1.0.

       Inputs:
         data (2D NumPy array of floats): data to be standardized

       Returns (2D NumPy array of floats): standardized data
       '''

       mu_vec = data.mean(axis=0)
       sigma_vec = data.std(axis=0)
       return (data - mu_vec) / sigma_vec


We discussed the first couple of lines, which use reductions to
compute the means and standard deviations of the features, above.  Only the
last line is new.  The expression ``(data - mu_vec)``
yields an array with shape ``(N, M)``.  Notice that we do not need a
loop to do this computation.  Instead, we rely on NumPy's
broadcasting mechanism to convert ``mu`` from a vector of length ``M``
into an ``N`` by ``M`` array and use element-wise subtraction to do the computation. 
In the new array, the jth column holds ``N``
copies of the mean of the jth feature.  Broadcasting also converts
``sigma_vec`` from ``1`` by ``M`` array into an ``N`` by ``M`` array,
and allows us to do element-wise division to compute the desired
``N`` by ``M`` array.


Linear algebra
~~~~~~~~~~~~~~

NumPy includes a linear algebra library (``numpy.linalg``), which
is traditionally imported with the alias ``la``:

.. python-run::

    import numpy.linalg as la

This library includes functions for performing a few different
decompositions (``cholesky``, ``qr``, and ``svd``), computing
eigenvalues, eigenvectors, norms, and other values (e.g., ``det``,
``norm``, ``matrix_rank``), and determining the inverse of a
matrix.

As an example, let's use a few of these methods to solve the following
system of equations:

.. raw:: latex

   \begin{align} 1\cdot x_0 + 3\cdot x_1 & = 11 \\ 2\cdot x_0 + 8\cdot x_1 & = 28 \end{align}

We can represent this system of equations using two arrays. We can
write them mathematically as:

.. raw:: latex

   \begin{equation*} \mathbf{X} = \left( \begin{matrix} 1 & 3 \\ 2 & 8\end{matrix} \right) \;\;\;\; \mathbf{Y} = \left( \begin{matrix} 11 \\ 28\end{matrix} \right) \end{equation*}

and construct them using NumPy as follows:

.. python-run::

    X = np.array([ [1,3] , [2, 8] ])
    Y = np.array([ [11], [28] ])

One way to solve this system is to compute by the dot product of the
inverse of ``X`` and ``Y``:

.. python-run::

    iX = la.inv(X)
    iX

    solution = np.dot(iX, Y)
    solution

Another is to use the ``linalg.solve`` function.

.. python-run::

    solution = la.solve(X, Y)
    solution


In this case, both methods have similar performance.  In general,
``la.solve()`` is preferred because it will exploit properties of
``X``, such as symmetry, to increase efficiency, when appropriate.


NumPy's matrix type
~~~~~~~~~~~~~~~~~~~

NumPy also has a matrix type that is useful because some of the
operators "make more sense" with matrices. e.g., \* will do matrix
multiplication, not element-wise multiplication:

.. python-run::

    d = np.matrix([[1, 2], [3, 4]])
    e = np.matrix([[1, 0], [0, 1]])

    d * e

However, most NumPy developers recommend using the more general array
type (anything you can do with a matrix, you can do with an array;
e.g., matrix multiplication is just the ``dot`` method).  The converse
is not true: matrices are always two-dimensional.

.. todo:: which, if any, of these examples used below were taken from other sources?  The NumPy tutorial, for example.

