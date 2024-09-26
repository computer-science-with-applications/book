complaint_list = [
    {'Company': "Smith's Forge",
     'Date received': '07/29/2013',
     'Complaint ID': '468882',
     'Issue': 'Managing the loan or lease',
     'Product': 'Consumer Loan',
     'Consumer complaint narrative': '',
     'Company response to consumer': 'Closed with explanation',
     'State': 'VA'},

    {'Company': 'Acme Anvils',
     'Date received': '08/23/2013',
     'Complaint ID': '567783',
     'Issue': 'Not heavy enough',
     'Product': 'Anvil',
     'Consumer complaint narrative': '',
     'Company response to consumer': 'Closed without explanation',
     'State': 'IL'},
    
    {'Company': 'Acme Anvils',
     'Date received': '09/17/2013',
     'Complaint ID': '779986',
     'Issue': 'too heavy enough',
     'Product': 'Anvil',
     'Consumer complaint narrative': '',
     'Company response to consumer': 'Closed with explanation',
     'State': 'VA'}]

def count_complaints_about(complaints, company_name):
    """
    Count complaints about the specified company

    Args:
        complaints (List[Dict[str, str]) A list of complaints, where each 
            complaint is a dictionary
        company_name [str]: The company name to count complaints for

    Returns [int]: count of complaints
    """
    count = 0
    for c in complaints:
        if c["Company"] == company_name:
            count = count + 1
    return count


def test_count_complaints_about():
    """ Simple tests for count_complaints_about """

    # Test the empty list
    assert count_complaints_about([], "Smith's Forge") == 0

    # Test one element lists using a complaint about Wells Fargo.
    assert count_complaints_about([complaint_list[0]], "Smith's Forge") == 1
    assert count_complaints_about([complaint_list[0]], 'Acme Anvils') == 0

    # Test a list with multiple complaints
    longer_list = complaint_list + [complaint_list[0]] * 2
    assert count_complaints_about(longer_list, "Smith's Forge") == 3
    assert count_complaints_about(longer_list, 'Acme Anvils') == 2
    assert count_complaints_about(longer_list, 'Acme Sweaters') == 0
    

def count_complaints_by_state(complaints):
    """
    Compute the number of complaints for each state.

    Args:
         complaints (List[Dict[str, str]]): A list of complaints, where each 
            complaint is a dictionary

    Returns: (Dict[str, int]): a dictionary that maps the name of a state to
      the number of complaints from that state.
    """
    d = {}
    for c in complaints:
        state = c["State"]
        if state in d:
            d[state] = d[state] + 1
        else:
            d[state] = 1
    return d


def test_count_complaints_by_state():
    """ Simple tests for count_complaints_by_state """

    # Test the empty list
    assert count_complaints_by_state([]) == {}

    # Test one element lists using a complaint from VA
    assert count_complaints_by_state([complaint_list[0]]) == {'VA': 1}

    # Test a list with multiple complaints
    longer_list = complaint_list + [complaint_list[0]] * 2
    assert count_complaints_by_state(longer_list) == {'VA' : 4, 'IL' : 1}

    
def organize_complaints_by_company(complaints):
    """
    Create a dictionary that maps the name of a company to a list of the
    complaint dictionaries that concern that company.

    Args:
        complaints (List[Dict[str, str]) A list of complaints, where each 
            complaint is a dictionary

    Returns: (Dict[str, List[Dict[str, str]]]): a dictionary that names the name
      of a company to a list of complaints for that company.
    """
    d = {}
    for complaint in complaints:
        c = complaint["Company"]
        if c not in d:
            d[c] = []
        # we are guaranteed that c will be in d at this
        # point and that d[c] will be a list.
        d[c].append(complaint)
    return d


def test_organize_complaints_by_company():
    """ Simple tests for organize_complaints_by_company """

    # Empty list of complaints
    assert organize_complaints_by_company([]) == {}

    # List with one complaint
    c = complaint_list[0]
    assert organize_complaints_by_company([c]) == {c["Company"] : [c]}

    
    # Test a list with multiple complaints
    longer_list = complaint_list
    assert organize_complaints_by_company(longer_list) == \
        {"Smith's Forge" : [complaint_list[0]],
         'Acme Anvils' : complaint_list[1:]}



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
    

if __name__ == "__main__":
    test_count_complaints_about()
    test_count_complaints_by_state()
    test_organize_complaints_by_company()
    test_count_unique_states_per_company()    

    
