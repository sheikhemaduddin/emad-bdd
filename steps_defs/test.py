import pytest
from pytest_bdd import scenarios, given, parsers

scenarios("../features/")


@given('test step')
def test_func():
    print("Step Executed")


#To pass an argument
@given(parsers.parse('test step 2 "{name}"'))
def test_func2(name):
    print(f'Step Executed "{name}"')



