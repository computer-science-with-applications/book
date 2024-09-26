complaint_list = [
    {'Company': 'Wells Fargo & Company',
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
    '''
    Count complaints about the specified company

    Inputs:
        complaints (List[Dict[str, str]) A list of complaints, where each 
            complaint is a dictionary
        company_name [str]: The company name to count complaints for

    Returns [int]: count of complaints
    '''
    count = 0
    for c in complaints:
        if c["Company"] == company_name:
            count = count + 1
    return count


def test_count_complaints_about():
    # Test the empty list
    assert count_complaints_about([], 'Wells Fargo & Company') == 0

    # Test one element lists using a complaint about Wells Fargo.
    assert count_complaints_about([complaint_list[0]], 'Wells Fargo & Company') == 1
    assert count_complaints_about([complaint_list[0]], 'Acme Anvils') == 0

    # Test a list with multiple complaints
    longer_list = complaint_list + [complaint_list[0]] * 2
    assert count_complaints_about(longer_list, 'Wells Fargo & Company') == 3
    assert count_complaints_about(longer_list, 'Acme Anvils') == 2
    assert count_complaints_about(longer_list, 'Acme Sweaters') == 0
    

def count_complaints_by_state(complaints):
    '''
    Compute the number of complaints for each state.

    Inputs:
         complaints (List[Dict[str, str]]): A list of complaints, where each 
            complaint is a dictionary

    Returns: (Dict[str, int]): a dictionary that maps the name of a state to
      the number of complaints from that state.
    '''
    d = {}
    for c in complaints:
        state = c["State"]
        if state in d:
            d[state] = d[state] + 1
        else:
            d[state] = 1
    return d


def test_count_complaints_by_state():
    # Test the empty list
    assert count_complaints_by_state([]) == {}

    # Test one element lists using a complaint from VA
    assert count_complaints_by_state([complaint_list[0]]) == {'VA': 1}

    # Test a list with multiple complaints
    longer_list = complaint_list + [complaint_list[0]] * 2
    assert count_complaints_by_state(longer_list) == {'VA' : 4, 'IL' : 1}

if __name__ == "__main__":
    test_count_complaints_about()
    test_count_complaints_by_state()
