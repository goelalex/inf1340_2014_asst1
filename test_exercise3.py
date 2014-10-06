#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Rock") == 2

def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(ValueError):
        decide_rps("Paper", "Stone")
        decide_rps("Pap", "Roc")
        decide_rps("Scissors", "Papers")
        decide_rps("Sisors", "Paper")
    with pytest.raises(TypeError):
        decide_rps(1, 11)
    # other tests

test_checksum()
test_input()