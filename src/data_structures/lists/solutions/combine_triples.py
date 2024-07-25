def combine_triples(lst):
    """
    Given a list of integer triples (3-tuples), compute a triple, where the ith
    element in the result is the sum of the ith element in the triples
    from the input list.

    Args:
        lst (List[Tuple(int, int, int)]): the list of triples

    Returns Tuple[int, int, int]: a triple where the ith element is the 
      sum of the ith elements from the input triples.
    """
    fst_tot = 0
    snd_tot = 0
    third_tot = 0
    for f, s, t in lst:
        fst_tot += f
        snd_tot += s
        third_tot += t
    return (fst_tot, snd_tot, third_tot)

def test_combine_triples():
    """
    Test code for combine triples
    """
    test_cases = [
        # Each test case has a list and the expected result
        # Check the empty list
        ([], (0, 0, 0)),

        # Check a one element list
        ([(1, 2, 3)], (1, 2, 3)),
        
        # Check a multi-element list
        ([(1, 2, 3), (4, 5, 6), (7, 8, 9)], (12, 15, 18))
        ]

    for lst, expected in test_cases:
        assert combine_triples(lst) == expected

if __name__ == "__main__":
    test_combine_triples()
