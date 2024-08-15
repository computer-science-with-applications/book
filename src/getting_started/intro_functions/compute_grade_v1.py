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
        grade =  'A'
    elif final >= 80 and midterm >= 80 and hw_avg >= 80:
        grade =  'B'
    elif final >= 70 and midterm >= 70 and hw_avg >= 70:
        grade =  'C'
    elif (final >= 50 and midterm >= 50 and 
          final >= (midterm+20) and hw_avg >= 90):
        grade =  'B'
    else:
        grade =  'F'
    return grade

    
