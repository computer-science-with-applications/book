import practice_problems

def count_complaints_by_state(complaints):
    '''
    Compute the number of complaints for each state.

    Args:
         complaints [List[Dict[str, str]]] A list of complaints, where each 
            complaint is a dictionary

    Returns: [Dict[str, int]]: a dictionary that maps the name of a state to
      the number of complaints from that state.
    '''
    d = {}
    for c in complaints:
        state = c["State"]
        d[state] = d.get(state, 0) + 1
    return d

def test_count_complaints_by_state():
    # Test the empty list
    assert count_complaints_by_state([]) == {}

    # Test one element lists using a complaint from VA
    assert count_complaints_by_state([practice_problems.complaint_list[0]]) == {'VA': 1}

    # Test a list with multiple complaints
    longer_list = practice_problems.complaint_list + [practice_problems.complaint_list[0]] * 2
    assert count_complaints_by_state(longer_list) == {'VA' : 4, 'IL' : 1}


if __name__ == "__main__":
    test_count_complaints_by_state()
    
