def print_matching_indexes(lst, val_to_match):
    """
    Prints the indexes that have a value that matches val_to_match.

    Args:
       lst (List[int]): the values to check
       val_to_match (int): the value of interest

    Returns: None
    """
    for i, val in enumerate(lst):
        if val == val_to_match:
            print(i)

def test_single_print_matching_indexes(lst, match_val, expected):
    """
    Run a single test for print_matching_indexes.

    Args:
        lst (List[int]): the test list
        match_val (int): the test value to match
        expected (List[int]): a list of the indexes that are expected
            to be printed or None, if none of the indexes are expected to match
    """
    print(f"print_matching_indexes({lst}, {match_val})")
    if len(expected) == 0:
        print(f"Expected: No indexes should be printed")
    else:
        print(f"Expected:")
        for idx in expected:
            print(idx)
    print("Actual:")
    print_matching_indexes(lst, match_val)
    print()    

def test_print_matching_indexes():
    """
    Test code for print_matching_indexes.  This code prints out the values 
    to expect from each test and then runs the test.
    """
    # Check a value that occurs more than once in the list
    test_single_print_matching_indexes([1, 3, 4, 1, 5, 7], 1, [0, 3])

    # Check a value that does not occur in the list
    test_single_print_matching_indexes([1, 3, 4, 1, 5, 7], 9, [])

    # Check the empty list
    test_single_print_matching_indexes([], 5, [])

    # Check a one-element list that matches
    test_single_print_matching_indexes([10], 10, [0])

    # Check a one-element list that does not match
    test_single_print_matching_indexes([10], 1, [])
    
    # Check a list where every value matches.
    test_single_print_matching_indexes([5, 5, 5, 5, 5], 5, [0, 1, 2, 3, 4])
         

if __name__ == "__main__":
    test_print_matching_indexes()        