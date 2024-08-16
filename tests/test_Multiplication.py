import pytest
from Multiplication_app.Multiplication import Multiplication

def tests_multiply_two_numbers():
    multiplier = Multiplication() # Instantiate the class
    result = multiplier._multiply_two_numbers(5,10)
    assert result == 50
    