# Prompt asked students to write leap year code without logical operators

def is_leap_year_v1(year):
    """
    Print the year an an indication of whether the year is a leap year.

    Input:
        year [int]: the year in question
    """
    assert isinstance(year, int)
    assert year > 0, "Year must be positive" 

    # equivalent to:
    #   ((year % 400 == 0) or
    #    ((year % 4 == 0) and (year % 100 != 0)))
    if year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 4 == 0:
        if year % 100 != 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a leap year")        

def is_leap_year_v2(year):
    """
    Print the year an an indication of whether the year is a leap year.

    Input:
        year [int]: the year in question
    """
    assert isinstance(year, int)
    assert year > 0, "Year must be positive" 

    # equivalent to:
    #   ((year % 4 == 0) and 
    #    ((year % 100 != 0) or (year % 400 == 0)))
    if year % 4 == 0:
        if year % 100 != 0:
            print(f"{year} is a leap year")
        elif year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a leap year")                


def is_leap_year_wrong(year):
    """
    Print the year an an indication of whether the year is a leap year.

    Input:
        year [int]: the year in question
    """
    assert isinstance(year, int)
    assert year > 0, "Year must be positive" 

    # This code is incorrect.
    if year % 4 == 0:
        if year % 100 != 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")            
    elif year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

def test_leap_year():
    for year in [2024, 2000, 1900, 2027]:
        is_leap_year_v1(year)
        is_leap_year_v2(year)
        is_leap_year_wrong(year)
        print()


def get_grade(midterm, final, hw):
    """
    You are helping an instructor develop a grading tool for assigning final
    scores. This requires a function to generates a score based on a
    midterm, final, and hw score.

    The following scores and conditions are:
        - A if the midterm, final, and hw are all at least 90+
        - B if the midterm, final, and hw are all at least 80+
        - C if the midterm, final, and hw are all at least 70+
        - B if the hw is at least 90+, midterm and final are both at least 50+
        and the final is 20 points or more higher than the midterm
    Otherwise the student should receive an F

    Inputs:
        midterm[int]: a score between 0-100
        final[int]: a score between 0-100
        hw[int]: a score between 0-100

    Returns [str]: where the options are 'A', 'B', 'C', or 'F'. Case sensitive.
    """

    # Verify that the parameters have sensible values
    assert midterm >= 0
    assert final >= 0
    assert hw >= 0

    if final >= 90 and midterm >= 90 and hw >= 90:
        grade =  'A'
    elif final >= 80 and midterm >= 80 and hw >= 80:
        grade =  'B'
    elif final >= 70 and midterm >= 70 and hw >= 70:
        grade =  'C'
    elif final >= 50 and midterm >= 50 and hw >= 90 and final >= (midterm+20):
        grade =  'B'
    else:
        grade =  'F'
    return grade


def test_grade():
    print("Testing get_grade") 
    test_cases = [(90, 90, 90, "A"),
                  (80, 80, 80, "B"),
                  (70, 70, 70, "C"),
                  (50, 70, 90, "B"),
                  (70, 50, 90, "F"),
                  (70, 50, 85, "F")]

    for midterm, final, hw, expected in test_cases:
        grade = get_grade(midterm, final, hw)
        assert grade == expected


def abs_sum_v1(lst):
    """
    Compute the sum of the absolute value of the values in the
    list.

    Inputs:
        lst [List[int]]: the list of interest

    Returns [int]: sum of the absolute values of the elements of the
      lst.
    """
    total = 0
    for val in lst:
        total = total + abs(val)
    return total


def abs_sum_v2(lst):
    """
    Compute the sum of the absolute value of the values in the
    list.

    Inputs:
        lst [List[int]]: the list of interest

    Returns [int]: sum of the absolute values of the elements of the
      lst.
    """
    total = 0
    for val in lst:
        if val < 0:
            total = total - val
        else:
            total = total + val
    return total


def test_abs_sum():
    print("Testing abs sum")
    # Empty list
    assert abs_sum_v1([]) == 0
    assert abs_sum_v2([]) == 0    

    # one element lists
    assert abs_sum_v1([10]) == 10
    assert abs_sum_v1([-10]) == 10
    assert abs_sum_v2([10]) == 10
    assert abs_sum_v2([-10]) == 10    

    # multi-element list with negative values.
    assert abs_sum_v1([10, -10, 10, -10]) == 40
    assert abs_sum_v2([10, -10, 10, -10]) == 40    

    
def has_false_v1(lst):
    """
    Determine whether the lst contains False.

    Inputs:
       lst [List[bool]]: the list of interest

    Returns [bool]: True if False appears in the list and
      False otherwise
    """
    result = False
    for val in lst:
        # note the use of not rather than
        #   val == False.
        if not val:
            result = True
    return result


def has_false_v1(lst):
    """
    Determine whether the lst contains False.

    Inputs:
       lst [List[bool]]: the list of interest

    Returns [bool]: True if False appears in the list and
      False otherwise
    """
    result = False
    for val in lst:
        # note the use of not rather than
        #   val == False.
        if not val:
            result = True
    return result


def has_false_v2(lst):
    """
    Determine whether the lst contains False.

    Inputs:
       lst [List[bool]]: the list of interest

    Returns [bool]: True if False appears in the list and
      False otherwise
    """
    result = False
    for val in lst:
        if not val:
            result = True
            # we can stop as soon as we find a False
            break
    return result


def test_has_false():
    print("Testing has_false") 
    # Empty list
    # asserts that the result of the call should be False
    assert not has_false_v1([])
    assert not has_false_v2([])

    # One element list without False
    assert not has_false_v1([True])
    assert not has_false_v2([True])

    # One element list with False
    # asserts that the result of the call should be True
    assert has_false_v1([False])
    assert has_false_v2([False])
    
    # multi-element list with False
    assert has_false_v1([True, True, True, True, False])
    assert has_false_v2([True, True, True, True, False])

    # multi-element list without False
    assert not has_false_v1([True, True, True, True])
    assert not has_false_v2([True, True, True, True])


def find_nearest_power2_ge(n):
    """
    Find the nearest power of 2 greater than or equal to N
    
    Inputs:
      n (int): the value to check
    """
    assert n > 0

    nearest = 1
    while (nearest < n):
        nearest = nearest * 2
    return nearest

def test_nearest_power2_ge():
    print("Testing find_nearest_power2_ge")
    assert find_nearest_power2_ge(1) == 1
    assert find_nearest_power2_ge(2) == 2
    assert find_nearest_power2_ge(5) == 8

def find_nearest_power2_le(n):
    """
    Find the nearest power of 2 less or equal to N
    
    Inputs:
      n (int): the value to check
    """
    nearest = 1
    while (2*nearest <= n):
        nearest = nearest * 2

    return nearest

def test_nearest_power2_le():
    print("Testing find_nearest_power2_le")
    assert find_nearest_power2_le(1) == 1
    assert find_nearest_power2_le(2) == 2
    assert find_nearest_power2_le(23) == 16


if __name__ == "__main__":
    test_leap_year()
    test_grade()
    test_abs_sum()
    test_has_false()
    test_nearest_power2_ge()
    test_nearest_power2_le()    
