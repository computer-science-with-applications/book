def print_component(lst, print_first):
    """
    Given a list of tuples of length two (that is, 2-tuples or pairs)
    and a boolean, print the first element in each pair if the boolean
    is True and the second if the boolean is False.

    Inputs:
        lst [List[Any, Any]]: a list of pairs
        print_first [bool]: will be True, if the first value in the
          pair should be printed and False, if the second should be
          printed.
    """
    for fst, snd in lst:
        if print_first:
            print(fst)
        else:
            print(snd)

def test_single_print_component(lst, print_first, expected):
    """
    Run a single test case for print_component

    Args:
        lst (List[Tuple(Any, Any)]): the test list
        print_first (bool): the test value for print_first
        expected(str): a string with the expected values
    """
    print(f"print_component({lst}, {print_first}):")
    if expected is None:
        print(" Should not print any values")
    else:
        print(f"  should print {expected} (with one value per line)")
    print("Actual values printed:")
    print_component(lst, print_first)
    print()      

def test_print_component():
    # Check an empty list with True for print_first
    test_single_print_component([], True, None)

    # Check an empty list with False for print_first
    test_single_print_component([], False, None)

    # Check a list with a single tuple: print first element
    test_single_print_component([("a", 5)], True, "a")
    # Check a list with a single tuple: print second element
    test_single_print_component([("a", 5)], False, 5)

    # Check a list with multiple tuples: print first elements
    test_single_print_component([("a", 27), ("bcd", 25), ("z", 15)], True, 
                                "a, bcd, and z")
    # Check a list with multiple tuples: print second elements    
    test_single_print_component([("a", 27), ("bcd", 25), ("z", 15)], False, 
                                "27, 25, and 15")
    
if __name__ == "__main__":
    test_print_component()