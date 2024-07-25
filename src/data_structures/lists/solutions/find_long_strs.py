def find_long_strs(lst, threshold):
    """
    Given a list of strings, return a list of the strings that
    are at least threshold long.

    Args:
        lst (List[str]): a list of strings to consider
        threshold (int): the minimum length of a string to include

    Returns (List[str]): a list of the strings from lst that
      are at least threshold charaters long.
    """
    result = []
    for s in lst:
        if len(s) >= threshold:
            result.append(s)
    return result


def find_long_strs_1(lst, threshold):
    """
    Given a list of strings, return a list of the strings that
    are at least threshold long.

    Args:
        lst (List[str]): a list of strings to consider
        threshold (int): the minimum length of a string to include

    Returns (List[str]): a list of the strings from lst that
      are at least threshold charaters long.
    """
    return [s for s in lst if len(s) >= threshold]

def test_find_long_strs():

    # Check empty list
    assert find_long_strs([], 3) == []

    # Check list with only the empty string
    assert find_long_strs([""], 4) == []

    # Check one element list that is too short
    assert find_long_strs(["ab"], 4) == []
    
    # Check one element list that is the exact length of the threshold
    assert find_long_strs(["abcd"], 4) ==  ["abcd"]
                          
    # Check one element list that is the longer than the threshold
    assert find_long_strs(["abcdef"], 4) == ["abcdef"]

    # Check a multi-element list where everything should be in the result
    assert find_long_strs(["abc", "d", "efgh", ""], 0) == \
        ["abc", "d", "efgh", ""]

    # Check a multi-element list where only some of the strings should
    # be in the result    
    assert find_long_strs(["abc", "d", "efgh", ""], 3) == ["abc", "efgh"]

    # Check a multi-element list where none the strings should be in the result     
    assert find_long_strs(["abc", "d", "efgh", ""], 10) == []


def test_find_long_strs_both():
    test_cases = [
        ([], 3, []),
        ([""], 4, []),
        (["ab"], 4, []),
        (["abcd"], 4, ["abcd"]),
        (["abcdef"], 4, ["abcdef"]),
        (["abc", "d", "efgh", ""], 0, ["abc", "d", "efgh", ""]),
        (["abc", "d", "efgh", ""], 3, ["abc", "efgh"]),
        (["abc", "d", "efgh", ""], 10, [])
        ]

    for lst, threshold, expected in test_cases:
        assert find_long_strs(lst, threshold) == expected
        assert find_long_strs_1(lst, threshold) == expected    

if __name__ == "__main__":
    test_find_long_strs()
    test_find_long_strs_both()        