#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import math

#upc checksum function

def checksum(upc):



    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    #upc needs to be a doc string
    #upc = str[0:11]
        # check type of input
        # raise TypeError if not string
    if upc != str():
        raise TypeError("Invalid Input")


        # check length of string
        # raise ValueError if not 12
    if len(upc) != 12:
        raise ValueError("Incorrect Length")


        # convert string to array
        # hint: use the list function


    #makes upc a list
    upc_list = list(upc)
    #upc_list = map(int, upc_list)
        # generate checksum using the first 11 digits provided
        # check against the the twelfth digit
            #1 Add odd number digits then multiplying by 3
            #2 Add step 1 result + total of even number digits
            #3 calculate step 2 result modulo 10
            #4 Subtract step 3 result from 10


    #upc_check = (10 - (((sum(upc[::2])*3) + sum(upc[1::2])) % 10))
    #upc_check line by line and put upc_odd and even in order to make split the sum of the odds and sum of the evens
    upc_odd = 0
    upc_even = 0
    for i in range(len(upc)):
        if i %2 == 0:
            upc_even += upc[i]
        else:
            upc_odd += upc[i]
        i += 1
    upc_odd = upc_odd * 3
    upc_subtract = upc_odd - upc_even
    upc_modulo = upc_subtract % 10
    upc_check = 10 - upc_modulo

        # return True if they are equal, False otherwise


    #checks if upc 12th number equals the checksum result
    #check if upc_check = upc_list
    if upc_check == upc_list[-1]:
        return True
    else:
        return False

