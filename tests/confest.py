'''Configuration file to define fixtures and other configurations'''
from decimal import Decimal
from faker import Faker
import pytest
from app.operation.operations import add, subtract, multiply, divide

fake = Faker()
'''Initalizing the faker object'''

# pylint: disable=unused-argument
def pytest_addoption(parser):
    '''Adding command-line options for pytest.'''
    parser.addoption("--num_records", action="store",default=5, type=int, help="Number of test records to generate")

@pytest.fixture
def num_records(request):
    '''Adding fixture'''
    return request.config.getoption("--num_records")

def generate_test_data(num_records):
    '''Defining operation mappings for both calculator and calculation tests'''
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        x = Decimal(fake.random_number(digits=2))
        y = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func == divide: # pylint: disable=comparison-with-callable
            y = Decimal('1') if y == Decimal('0') else y
        try:
            if operation_func == divide and y == Decimal('0'): # pylint: disable=comparison-with-callable
                expected = ZeroDivisionError
            else:
                expected = operation_func(x,y)
        except ZeroDivisionError:
            expected = ZeroDivisionError
        yield x, y, operation_name, operation_func, expected

# pylint: disable=unused-argument
def pytest_generate_tests(metafunc):
    '''Defining pytest_generate_tests'''
    if {"x", "y", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [
            (x, y, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for x, y, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("x,y,operation,expected", modified_parameters)

# End