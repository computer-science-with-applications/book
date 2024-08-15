def compute_grade(midterm, final, hw_avg):
    """
    Given a student's midterm and final exam grades and their average
    homework score, compute the student's grade.

    Inputs:
        midterm (float): a score between 0-100
        final (float): a score between 0-100
        hw_avg (float): a score between 0-100

    Returns (str): the student's grade 
    """
    # Verify that the parameters have sensible values
    assert 0.0 <= midterm <= 100.0
    assert 0.0 <= final <= 100.0
    assert 0.0 <= hw_avg <= 100.0

    if final >= 90 and midterm >= 90 and hw_avg >= 90:
        return 'A'
    if final >= 80 and midterm >= 80 and hw_avg >= 80:
        return  'B'
    if final >= 70 and midterm >= 70 and hw_avg >= 70:
        return 'C' 
    if (final >= 50 and midterm >= 50 and 
        final >= (midterm+20) and hw_avg >= 90):
        return 'B'
    return 'F'

    
def test_compute_grade():
    """ Simple test code for compute grade """

    assert compute_grade(90.0, 90.0, 92.0) == "A"
    assert compute_grade(80.0, 85.5, 80.0) == "B"
    assert compute_grade(70.0, 70.0, 73.5) == "C"
    assert compute_grade(50.0, 70.0, 90.0) == "B"
    assert compute_grade(70.0, 50.0, 90.0) == "F"
    assert compute_grade(50.0, 70.0, 85.0) == "F"

test_compute_grade()
