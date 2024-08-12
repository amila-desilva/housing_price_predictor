import pytest

from housing_price_predictor.name import PersonName

def test_full_name():
    person = PersonName()
    assert person.full_name("John", "Doe") == "John Doe"