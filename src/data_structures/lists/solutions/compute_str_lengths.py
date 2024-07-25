def compute_str_lengths(lst):
    """
    Given a list of strings, compute a list of the lengths of the strings.

    Inputs (List[str]): a list of strings

    Returns (List[int]): a list of the length of the strings
      in the input list.
    """
    result = []
    for s in lst:
        result.append(len(s))
    return result

# Alternative version that uses a list comprehension
def compute_str_lengths_1(lst):
    """
    Given a list of strings, compute a list of the lengths of the strings.

    Inputs (List[str]): a list of strings

    Returns (List[int]): a list of the length of the strings
      in the input list.
    """
    return [len(s) for s in lst]

def test_compute_str_lengths():
    """
    Simple test code for compute_str_lengths
    """

    # Check empty list
    assert compute_str_lengths([]) == []
    
    # Check a one element list
    assert compute_str_lengths(["xyzw"]) == [4]
    
    # Check a element list where the single element is the empty string. 
    assert compute_str_lengths([""]) ==  [0]

    # Check a multi-element list
    assert compute_str_lengths(["abc", "d", "efgh", ""]) == [3, 1, 4, 0]

def test_compute_str_lengths_both():
    test_cases = [
        ([], []),
        (["xyzw"], [4]),
        ([""], [0]),
        (["abc", "d", "efgh", ""], [3, 1, 4, 0])
    ]

    for lst, expected in test_cases:
        assert compute_str_lengths(lst) == expected
        assert compute_str_lengths_1(lst) == expected    

if __name__ == "__main__":
    test_compute_str_lengths()
    test_compute_str_lengths_both()