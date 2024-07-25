def average_rows(matrix):
    """
    Compute the average of each row.

    Args:
        matrix (List[List[float]]): the data of interest

    Returns (List[float]]): a list with the average value in each row
    """
    assert len(matrix) > 0
    assert len(matrix[0]) > 0
    
    result = []
    for row in matrix:
        result.append(sum(row) / len(row))
    return result

def test_single_average_rows(m, expected):
    """
    Run a single test for average_rows

    Args:
       m (List[List[number]]): the matrix
       expected (List[float]): the expected result
    """
    epsilon = 0.00000001
    actual = average_rows(m)
    # Verify that the result has the right length
    assert len(expected) == len(actual)
    # Verify that all the elements are within epsilon of their
    # corresponding expected value.
    for i, _ in enumerate(actual):
        assert abs(actual[i] - expected[i]) < epsilon
    
def test_average_rows():
    # Check square matrix
    test_single_average_rows([[1.0, 2.0, 3.1],
                             [4.5, 5.0, 6.0],
                             [7.0, 8.3, 9.0]],
                            [2.033333333333333, 5.166666666666667, 
                             8.1])
    
    # Check a matrix with more rows than columns
    test_single_average_rows([[1.0, 2.0, 3.1],
                             [4.5, 5.0, 6.0],
                             [7.0, 8.3, 9.0],
                             [10.0, 11.0, 12.0]],
                            [2.033333333333333, 5.166666666666667,
                             8.1, 11.0])
    
    # Check a matrix with more columns than rows.
    test_single_average_rows([[1.0, 2.0, 3.1],
                             [4.5, 5.0, 6.0]],
                            [2.033333333333333, 5.166666666666667])
    

    # Check matrix with exactly one row with exactly one element
    test_single_average_rows([[1.0]], [1.0])      

if __name__ == "__main__":
    test_average_rows()

