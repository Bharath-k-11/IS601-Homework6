'''Tests for the Arithmetic History functionality'''
from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.calculator.calculations import Calculations
from app.operation.operations import add, subtract

@pytest.fixture
def setup_calculations():
    '''Clearing the history and adding sample calculations for tests'''
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('29'), Decimal('13'), add))
    Calculations.add_calculation(Calculation(Decimal('29'), Decimal('25'), subtract))

def test_add_calculation(setup_calculations):
    '''Test adding a calculation to the history'''
    calc=Calculation(Decimal('3'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Adding the calculation to history failed."

def test_get_history(setup_calculations):
    '''Test retrieving the entire calculation history'''
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain expected number of calculations"

def test_clear_history(setup_calculations):
    '''Test clearing the entire calculation history.'''
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History is not cleared"

def test_get_latest(setup_calculations):
    '''Test getting the latest calculation from the history'''
    latest = Calculations.get_latest()
    assert latest.x == Decimal('29') and latest.y == Decimal('25'), "Haven't got the correct latest calculation"

def test_find_by_operation(setup_calculations):
    '''Test finding calculations in the history by operation type'''
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Correct number of calculations with add operation are not found"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Correct number of calculations with subtract operation are not found"

def test_get_latest_with_empty_history():
    '''Test getting the latest calculation when the history is empty'''
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"

#End