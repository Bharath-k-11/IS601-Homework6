'''Testing operations'''
from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.operation.operations import add, subtract, multiply, divide

def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('29'), Decimal('13'), add)
    assert calculation.perform() == Decimal('42'), "Addition operation failed"

def test_operation_subtract():
    '''Testing the subtraction operation'''
    calculation = Calculation(Decimal('29'), Decimal('25'), subtract)
    assert calculation.perform() == Decimal('4'), "Subtraction operation failed"

def test_operation_multiply():
    '''Testing the multiplication operation'''
    calculation = Calculation(Decimal('3'), Decimal('4'), multiply)
    assert calculation.perform() == Decimal('12'), "Multiplication operation failed"

def test_operation_divide():
    '''Testing the division operation'''
    calculation = Calculation(Decimal('39'), Decimal('3'), divide)
    result = calculation.perform()
    assert result == Decimal('13'), f"Division operation failed: expected Decimal('12'), got {result}"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot be divided by Zero"):
        calculation = Calculation(Decimal('19'), Decimal('0'), divide)
        calculation.perform()

# End
