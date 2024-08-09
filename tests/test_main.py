import pytest
from housing_price_predictor.main import Person


def test_person_info():
    testing_person = Person("Chris", 20, "Intern")


    expected_output = "Hello, my name is Chris. I am 20 years old. My job is a(n) Intern."


    assert testing_person.person_info() == expected_output
