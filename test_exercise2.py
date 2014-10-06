#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("036000291452") is True
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("123456789012") is True
    assert checksum("124297385722") is True
    assert checksum("854336576384") is True
    assert checksum("717951000841") is False
    assert checksum("075678164120") is False
    assert checksum("568439479540") is False
    assert checksum("301248381248") is False
    assert checksum("562374673261") is False
    assert checksum("249572305686") is False
    # other tests


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)

    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")
        checksum("-12345678901")
        checksum("1234567s8901")
    # other tests

test_checksum()
test_input()
# add functions for any other tests