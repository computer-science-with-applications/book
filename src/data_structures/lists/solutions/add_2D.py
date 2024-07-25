def add_2D(m1, m2):
    """
    Given two matrices with the same shape, construct a new matrix
    with the element-wise sum of the inputs.

    Args:
        m1 (List[List[int | float]): one matrix
        m2 (List[List[int | float]): another matrix    

    Returns [List[List[int | float]]: a matrix, represented as a list of lists,
        with the element-wise sum of of the inputs.

    """
    # Verify that m1 and m2 have the same shape.
    assert len(m1) == len(m2)
    # all is a built-in function if all the values in the list are True
    assert all([len(m1[i]) == len(m2[i]) for i, _ in enumerate(m1)])

    new_m = []
    for i, row1 in enumerate(m1):
        new_row = []
        for j, _ in enumerate(row1):
            new_row.append(m1[i][j] + m2[i][j])
        new_m.append(new_row)
    return new_m

def test_add_2D():
    # Test a square matrix
    m1 = [[1, 2], [4, 5]]
    m2 = [[10, 20], [40, 50]]
    expected = [[11, 22], [44, 55]]
    assert add_2D(m1, m2) == expected

    # Test a matrix with more columns than rows
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[10, 20, 30], [40, 50, 60]]
    expected = [[11, 22, 33], [44, 55, 66]]
    assert add_2D(m1, m2) == expected
                   
    # Test a matrix with more rows than columns
    m1 = [[1, 2], [3, 4], [5, 6]]
    m2 = [[10, 20], [30, 40], [50, 60]]
    expected = [[11, 22], [33, 44], [55, 66]]
    assert add_2D(m1, m2) == expected

    # Test a matrix with a single row with a single column
    assert add_2D([[10]], [[20]]) == [[30]]

if __name__ == "__main__":
   test_add_2D() 
    