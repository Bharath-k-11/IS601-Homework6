'''This module contains tests for the arithmetic operations and the OperationRecord class'''
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.operation.operations import add, divide

def test_calculation_operations(x, y, operation, expected):
    '''Calculation operations with various cases'''
    calc = Calculation(x, y, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {x} and {y}"

def test_calculation_repr():
    '''Test the string representation (__repr__) of the Calculation class.'''
    calc=Calculation(Decimal('22'), Decimal('15'), add)
    expected_repr="Calculation(22, 15, add)"
    assert repr(calc) == expected_repr, "The __repr__ method is not matching the expected string."

def test_divide_by_zero():
    ''' Division by zero raises a Valueerror'''
    calc=Calculation(Decimal('19'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot be divided by Zero"):
        calc.perform()
#End
