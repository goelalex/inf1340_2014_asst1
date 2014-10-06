#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.
    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """
    letter_grade = ""
    list_grade = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]
    gpa = 0.0
    if type(grade) is str:
        # Check that if grade is one of the accepted values
        # Assign grade to letter_grade
        for count in range(0, len(list_grade)):
            if grade == list_grade[count]:
                letter_grade = grade
        # Check if grade is one of the accepted values
        # Print error and raise ValueError exception
        if not letter_grade:
            print("wrong letter")
            raise ValueError("Invalid value passed as parameter")
    elif type(grade) is int:
        # Check that grade is in the accepted range
        # Assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)
        # Check if the grade is in the accepted range,
        # Print error and raise ValueError exception
        if grade > 100 or grade < 0:
            print(grade)
            print("error")
            raise ValueError("Invalid value passed as parameter")
        # convert the numeric grade to a letter grade
        elif grade >= 90:
            letter_grade = "A+"
        elif grade >= 85:
            letter_grade = "A"
        elif grade >= 80:
            letter_grade = "A-"
        elif grade >= 77:
            letter_grade = "B+"
        elif grade >= 73:
            letter_grade = "B"
        elif grade >= 70:
            letter_grade = "B-"
        else:
            letter_grade = "FZ"
    # if grade is not string or integer raise a TypeError exception
    else:
        raise TypeError("Invalid type passed as parameter")
    # check letter_grade, and assign the value to gpa accordingly
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.0
    #return gpa value as function result
    return gpa

