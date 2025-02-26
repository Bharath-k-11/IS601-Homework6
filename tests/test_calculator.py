'''Arithmetic Operations Test Suite'''
from faker import Faker
from app.calculator import Calculator

fake=Faker()

def test_addition():
    '''Test that addition function works '''  
    x=fake.random_int(min=0,max=50)
    y=fake.random_int(min=0,max=50)
    expected=x+y
    assert Calculator.add(x,y)==expected

def test_subtraction():
    '''Test that subtraction function works '''   
    x=fake.random_int(min=0,max=50)
    y=fake.random_int(min=0,max=50)
    expected=x-y
    assert Calculator.subtract(x,y)==expected

def test_multiplication():
    '''Test that Multiplication function works'''
    x=fake.random_int(min=0,max=50)
    y=fake.random_int(min=0,max=50)
    expected=x*y
    assert Calculator.multiply(x,y)==expected

def test_division():
    '''Test that Division function works'''
    x=fake.random_int(min=0,max=50)
    y=fake.random_int(min=0,max=50)
    y=y if y!=0 else 1
    expected=x/y
    assert Calculator.divide(x,y)==expected

#End