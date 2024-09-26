# Alternative implementation

def count_unique_states_per_company(complaints):
    """
    For each company, count the number of different states
    that had complaints.

    Args:
        complaints (List[Dict[str, str]) A list of complaints, where each 
            complaint is a dictionary

    Returns (Dict[str, int]]): a dictionary maps a company name to
      the number of different states that had a complaint for the
      company.  
    """
    # Built a intermediate data structure that maps company names
    # to a set of the states that had complaints about that company.
    # Build the result as you go.
    states_per_company = {}
    for complaint in complaints:
        c = complaint["Company"]
        if c not in states_per_company:
            states_per_company[c] = set()
        states_per_company[c].add(complaint["State"])

    # Build the final result
    return { company : len(states) for company, states in states_per_company.items()}


def test_count_unique_states_per_company():
    """ Simple tests for count_unique_states_per_company """

    # Empty list of complaints
    assert count_unique_states_per_company([]) == {}

    # List with one complaint
    c = complaint_list[0]
    assert count_unique_states_per_company([c]) == {c["Company"] : 1}

    
    # Test a list with multiple complaints
    longer_list = complaint_list
    assert count_unique_states_per_company(longer_list) == \
        {"Smith's Forge" : 1,
         'Acme Anvils' : 2}
