import pytest
from housing_price_predictor.dummy import Subtraction

def test_sub_two_nums():
    sub = Subtraction()
    assert sub.sub_two_nums(5,3) == 2
