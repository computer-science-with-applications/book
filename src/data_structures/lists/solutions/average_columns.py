def average_columns(matrix):
    """
    Compute the average of each row.

    Args:
        matrix (List[List[float]]): the data of interest

    Returns (List[float]]): a list with the average value in each column
    """
    N = len(matrix)
    assert N > 0
    
    M = len(matrix[0])
    assert M > 0

    result = []
    # iterate over the column index space
    for j in range(M):
        tot = 0
        # iterate over the range index space
        for i in range(N):
            tot = tot + matrix[i][j]
        result.append(tot / N)
    return result

def test_single_average_columns(m, expected):
    """
    Run a single test for average_columns

    Args:
       m (List[List[number]]): the matrix
       expected (List[float]): the expected result
    """
    epsilon = 0.00000001
    actual = average_columns(m)
    # Verify that the result has the right length
    assert len(expected) == len(actual)
    # Verify that all the elements are within epsilon of their
    # corresponding expected value.
    for i, _ in enumerate(actual):
        assert abs(actual[i] - expected[i]) < epsilon
    
def test_average_columns():
    # Check square matrix
    test_single_average_columns([[1.0, 2.0, 3.1],
                             [4.5, 5.0, 6.0],
                             [7.0, 8.3, 9.0]],
                            [4.166666666666667, 5.1000000000000005, 
                             6.033333333333334])
                             
    # Check a matrix with more rows than columns
    test_single_average_columns([[1.0, 2.0, 3.1],
                             [4.5, 5.0, 6.0],
                             [7.0, 8.3, 9.0],
                             [10.0, 11.0, 12.0]],
                            [5.625, 6.575, 7.525])
    
    # Check a matrix with more columns than rows.
    test_single_average_columns([[1.0, 2.0, 3.1],
                             [4.5, 5.0, 6.0]],
                            [2.75, 3.5, 4.55])
    

    # Check matrix with exactly one row with exactly one element
    test_single_average_columns([[1.0]], [1.0])      

if __name__ == "__main__":
    test_average_columns()

