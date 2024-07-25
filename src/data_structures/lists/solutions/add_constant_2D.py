def add_constant_2D(m, c):
    """
    Given a matrix and a constant, add the constant to every element
    in the maxtrix.

    Args:
       m (List[List[int | float]]): the input matrix
       c ([int | float]): the constant

    Returns: None
    """
    for i, row in enumerate(m):
        for j, _ in enumerate(row):
            m[i][j] +=  c            

def test_add_constant_2D():
    # Check a square matrix
    m = [[1, 2], [3, 4]]
    add_constant_2D(m, 30)
    assert m == [[31, 32], [33, 34]]

    # Check a matrix with more rows than columns
    m = [[1, 2], [3, 4], [5, 6]]
    add_constant_2D(m, 20)
    assert m == [[21, 22], [23, 24], [25, 26]]

    # Check a matrix with more columns than rows
    m = [[1, 2, 3], [4, 5, 6]]
    add_constant_2D(m, 20)
    assert m == [[21, 22, 23], [24, 25, 26]]

    # Check a matrix with exactly one row and exactly one column
    m = [[10]]
    add_constant_2D(m, 10)
    assert m == [[20]]

if __name__ == "__main__":
    test_add_constant_2D()
