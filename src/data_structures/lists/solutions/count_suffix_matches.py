def count_suffix_matches(words, suffix):
    """
    Count the number of words that end with a suffix.
    
    Inputs:
        words (List[str]): list of strings
        suffix (str): the suffix of interest.
        
    Return (int): the number of words in word that end with suffix. 
    """
    count = 0
    
    for word in words:
        if word.endswith(suffix):
            count += 1
            
    return count


def count_suffix_matches_1(words, suffix):
    """
    Count the number of words that end with a suffix.
    
    Inputs:
        words List[str]:  list of strings
        suffix [str]: a string
        
    Return [int]: the number of words in word that end with suffix. 
    """
    count = 0
    
    for word in words:
        if suffix == word[-len(suffix):]:
            count += 1
            
    return count 

def test_count_suffix_matches():
    """ Test code for count_suffix """
    test_cases = [
        # Check for multiple strings that match the suffix
        (["hello", "jello", "ham", "cello"], "ello", 3),

        # Check list of length one with a string that does not match the suffix
        (["hello"], "bye", 0),

        # Check list of length one with word that matches the suffix exactly
        (["hello"], "hello", 1),

        # Check list of length one where the string in the list is
        # a suffix of the suffix-to-be-counted.
        (["ello"], "hello", 0),

        # Check empty list
        ([], "hello", 0)
    ]
    for lst, suffix, expected in test_cases:
        assert count_suffix_matches(lst, suffix) == expected
