import math
import numpy as np


def compute_feature_mean(data, j):
    """
    Compute the mean of feature (column) j

    Inputs:
      data (list of lists of floats)

    Returns (float): mean of feature j
    """
    N = len(data)
    total = 0
    for i in range(N):
        total += data[i][j]
    return total/N


def compute_feature_stdev(data, j):
    """
    Compute the standard deviation of feature (column) j

    Inputs:
        data (list of lists of floats)

    Returns (float): standard deviation of feature j
    """

    N = len(data)
    mu = compute_feature_mean(data, j)
    total = 0
    for i in range(N):
        total = total + (data[i][j] - mu)**2
    return math.sqrt(1/N*total)

def standardize_matrix(data):
    assert len(data) > 0

    N = len(data)
    M = len(data[0])

    # initialize the result w/ 
    # NxM matrix of zeros.
    rv = []
    for i in range(N):
        rv.append([0]*M)
        
    # for each feature
    for j in range(M):
        mu = compute_feature_mean(data, j)
        sigma = compute_feature_stdev(data, j)

        # standardized feature
        for i in range(N):
            rv[i][j] = (data[i][j] - mu)/sigma

    return rv

def standardize_matrix_alt(data):
    assert len(data) > 0

    N = len(data)
    M = len(data[0])
       
    # initialize the result w/ 
    # NxM matrix of zeros.
    rv = []
    for i in range(N):
        rv.append([0]*M)
   
    # for each feature
    for j in range(M):
        # compute feature mean
        mu = sum([data[i][j] for i in range(N)])/N

	# compute adjusted vector
        adj_vec = [data[i][j]-mu for i in range(N)]

        # compute feature standard deviation
        sigma = math.sqrt(1/N*sum([adj_vec[i]**2 for i in range(N)]))

        # standardized the values
        for i in range(N):
            rv[i][j] = adj_vec[i]/sigma

    return rv



def standardize_vector_numpy_basic(avec):
    """
    Standardize a vector to have mean zero and standard deviation of 1.

    Inputs:
        vec: array of floats

    Returns: array of floats
    """

    N = len(avec)
    assert N > 0

    mean = avec.sum()/N
    std = math.sqrt(1/N*((avec-mean)**2).sum())

    return (avec - mean)/std

def standardize_vector_numpy(avec):
    """
    Standardize a vector to have mean zero and standard deviation of 1.

    Inputs:
        vec: array of floats

    Returns: array of floats
    """

    assert len(avec) > 0
    return (avec - avec.mean())/avec.std()


    
def normalize_vector(vec):
    """
    Compute a vector that points in the same direction as vec and has unit length.
    """

    vec_min = min(vec)
    vec_max = max(vec)
    rng = vec_max-vec_min

    rv = []
    for val in vec:
        rv.append((val-vec_min)/rng)

    return rv


def normalize_vector_alt(vec):
    """
    Compute a vector that points in the same direction as vec and has unit length.
    """

    vec_min = min(vec)
    vec_max = max(vec)
    rng = vec_max-vec_min
    return [(val-vec_min)/rng for val in vec]


def normalize_vector_numpy(vec):    
    vec_min = min(vec)
    vec_max = max(vec)
    rng = vec_max-vec_min
    return vec-vec_min/rng


def standardize_matrix(data):
    assert len(data) > 0

    N = len(data)
    M = len(data[0])

    # initialize the result w/ 
    # NxM matrix of zeros.
    rv = []
    for i in range(N):
        rv.append([0]*M)

    # for each feature
    for j in range(M):
        # compute the mean
        mu = sum([data[i][j] for i in range(N)])/N

        # compute the standard deviation
        sigma = math.sqrt(1/N*sum([(data[i][j]-mu)**2 for i in range(N)]))

        # standardized the values
        for i in range(N):
            rv[i][j] = (data[i][j]-mu)/sigma

    return rv


def standardize_matrix_alt(data):
    assert len(data) > 0

    N = len(data)
    M = len(data[0])

    # initialize the result w/ 
    # NxM matrix of zeros.
    rv = []
    for i in range(N):
        rv.append([0]*M)

    for j in range(M):
        # compute feature mean
        total = 0
        for i in range(N):
            total += data[i][j]
        mu = total/N

        # feature standard deviation
        total = 0
        adj_feature = []
        for i in range(N):
            adj_feature.append(data[i][j] - mu)
            total = total + adj_feature[i]**2
        sigma = math.sqrt(1/N*total)

        # standardized feature
        for i in range(N):
            rv[i][j] = adj_feature[i]/sigma

    return rv


def standard_matrix_numpy(data):
    assert len(data) > 0

    (N, M) = data.shape

    # initialize the result w/ 
    # NxM matrix of zeros.
    rv = np.zeros((N, M))

    # for each feature
    for j in range(M):
        mu = data[:,j].sum()/N
        sigma = math.sqrt(1/N*((data[:,j] - mu) ** 2).sum())
        rv[:, j] = (data[:,j]-mu)/sigma


    return rv

def standardize_vector(vec):
    """
    Standardize a vector to have mean 0.0 and standard deviation
    1.0.

    Inputs:
    vec: numpy array of floats
    
    Returns: numpy array of floats
    """

    mu = vec.mean()
    sigma = vec.std()
    return (vec-mu)/sigma


def standardize_features(data):
    """
    Standardize the features (columns) in data to have mean 0.0
    and standard deviation 1.0.
    
    Inputs:
    data: list of list of floats
    
    Returns: list of list of floats
    """

    (N, M) = data.shape
    
    # initialize the result w/ NxM matrix of zeros.
    rv = np.zeros((N, M))

    # for each feature
    for j in range(M):
        rv[:, j] = standardize_vector(data[:,j])

    return rv

