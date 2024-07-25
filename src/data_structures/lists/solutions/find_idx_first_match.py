def find_idx_first_match(lst1, lst2):
    """
    Find the first index where lst1 and lst2 have the same
    value. Return -1 if none of the indexes hold matching values.

    Args:
        lst1 (List[number]): one list
        lst2 (List[number]): another list

    Returns (int): the first index at which lst1 and lst2 have the
        same value or -1, if none of the indexes hold matching values.
    """
    assert len(lst1) == len(lst2)
    for idx, val1 in enumerate(lst1):
        if val1 == lst2[idx]:
            return idx

    return -1

# Alternative solution that uses enumerate
def find_idx_first_match_1(lst1, lst2):
    """
    Find the first index where lst1 and lst2 have the same
    value. Return -1 if none of the indexes hold matching values.

    Args:
        lst1 (List[number]): one list
        lst2 (List[number]): another list

    Returns (int): the first index at which lst1 and lst2 have the
        same value or -1, if none of the indexes hold matching values.
    """
    assert len(lst1) == len(lst2)
    for idx, _ in enumerate(lst1):
        if lst1[idx] == lst2[idx]:
            return idx

    return -1


# Alternative solution that works for lists that are
# not the same length.
def find_idx_first_match_2(lst1, lst2):
    """
    Find the first index where lst1 and lst2 have the same
    value. Return -1 if none of the indexes hold matching values.

    Args:
        lst1 (List[number]): one list
        lst2 (List[number]): another list

    Returns (int): the first index at which lst1 and lst2 have the
        same value or -1, if none of the indexes hold matching values.
    """
    for idx, _ in enumerate(lst1):
        if idx >= len(lst2):
            # lst1 is longer than lst2
            break

        if lst1[idx] == lst2[idx]:
            return idx

    return -1


def test_find_idx_first_match():
    # Check empty lists
    assert find_idx_first_match([], []) ==  -1
    
    # Check one element lists that match
    assert find_idx_first_match([10], [10]) == 0

    # Check one elements that do not match
    assert find_idx_first_match([10], [5]) ==  -1

    # Check multi-element list with a match in the middle
    assert find_idx_first_match([3, 4, 6, 7], [2, 3, 6, 7]) == 2
    
    # Check multi-element list with a match in the middle
    assert find_idx_first_match([3, 4, 6, 7], [2, 3, 5, 7]) == 3

    # Check multi-element list with no match
    assert find_idx_first_match([3, 4, 6, 7], [2, 3, 5, 8]) ==  -1

def test_find_idx_first_match_all_versions():
    test_cases = [
        ([], [], -1),
        ([10], [10], 0),
        ([10], [5], -1),
        ([3, 4, 6, 7], [2, 3, 6, 7], 2),
        ([3, 4, 6, 7], [2, 3, 5, 7], 3),
        ([3, 4, 6, 7], [2, 3, 5, 8], -1)    
    ]
    for lst1, lst2, expected in test_cases:
        assert find_idx_first_match(lst1, lst2) == expected
        assert find_idx_first_match_1(lst1, lst2) == expected        
        assert find_idx_first_match_2(lst1, lst2) == expected

    # check last version
    find_idx_first_match_2([10], []) == -1
    find_idx_first_match_2([], [10]) == -1

if __name__ == "__main__":
    test_find_idx_first_match()
    test_find_idx_first_match_all_versions()