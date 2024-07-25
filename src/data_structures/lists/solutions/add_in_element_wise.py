def add_in_element_wise(lst1, lst2):
    """
    Takes two lists of the same length and updates lst1 such that the
    ith element of lst1 will contain the sum of the original ith
    element of the lst1 and the ith element of lst2.

    Args:
        lst1 (List[number]): a list of values
        lst2 (List[number]): a list of values    

    Returns: None
    """
    assert len(lst1) == len(lst2)
    for i, _ in enumerate(lst1):
        lst1[i] += lst2[i]

def test_single_add_in_element_wise(lst1, lst2):
    """
    Run a single test for add_in_element_wise

    Args:
        lst1 (List[number]): first operand
        lst2 (List[number]): second operand
    """
    # Compute a new list with the expected value
    t = [lst1[i] + lst2[i] for i, _ in enumerate(lst1)]
    add_in_element_wise(lst1, lst2)
    assert lst1 == t             

def test_add_in_element_wise():
    # Check empty lists
    test_single_add_in_element_wise([], []),

    # Check single element lists
    test_single_add_in_element_wise([10], [20]),

    # Check multi-element lists
    test_single_add_in_element_wise([10, 20, 30], [40, 50, 60])


if __name__ == "__main__":
    test_add_in_element_wise()