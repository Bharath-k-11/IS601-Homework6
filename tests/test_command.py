# pylint: disable=missing-class-docstring
'''Test Suite for Command Classes'''
# pylint: disable=missing-class-docstring
'''Test Suite for Command Classes'''
from unittest.mock import patch
import pytest
from app.plugins.addcommand import Add
from app.plugins.subtractcommand import Subtract
from app.plugins.multiplycommand import Multiply
from app.plugins.dividecommand import Divide
from app.plugins.menucommand import Menu

@pytest.fixture
def add_command():
    '''Fixture'''
    return Add()

@pytest.fixture
def subtract_command():
    '''Fixture'''
    return Subtract()

@pytest.fixture
def multiply_command():
    '''Fixture'''
    return Multiply()

@pytest.fixture
def divide_command():
    '''Fixture'''
    return Divide()

@pytest.fixture
def menu_command():
    '''Fixture for Menu Command'''
    class MockCommandHandler:
        '''Mock CommandHandler class'''
        def get_registered_commands(self):
            '''Return a list of registered commands'''
            return ["Add", "Subtract", "Multiply", "Divide", "Menu"]
    command_handler = MockCommandHandler()
    return Menu(command_handler)
# Testing the add command
class TestAddCommand:
    '''Test the Add command.'''
    def test_add(self,add_command, capsys):
        '''Testing the add command'''
        add_command.execute('2', '3')
        captured=capsys.readouterr()
        assert "2 + 3 = 5" in captured.out

    def test_add_one_argument(self,add_command, capsys):
        '''Testing when only one argument is given'''
        add_command.execute('2')
        captured=capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_add_invalid_args(self, add_command,capsys):
        '''Testing for invalid arguments'''
        add_command.execute('x','2')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_add_error(self, add_command, capsys):
        '''Testing for invalid arguments'''
        with patch('app.plugins.addcommand.Calculator.add', side_effect=ValueError("Error")):
            add_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out
# Testing the subtract command
class TestSubtractCommand:
    def test_subtract(self,subtract_command,capsys):
        '''Testing multiply command'''            
        subtract_command.execute('4','2')
        captured=capsys.readouterr()
        assert "4 - 2 = 2" in captured.out

    def test_subtract_one_arg(self,subtract_command,capsys):
        '''Testing one argument'''
        subtract_command.execute('4')
        captured=capsys.readouterr()
        assert "Only two arguments must be given" in captured.out

    def test_subtract_invalid_arg(self,subtract_command,capsys):
        '''Testing invalid argument'''
        subtract_command.execute('x','3')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_subtract_negative_numbers(self, subtract_command, capsys):
        '''Testing subtraction with negative numbers'''
        subtract_command.execute('-5', '3')
        captured = capsys.readouterr()
        assert "-5 - 3 = -8" in captured.out

    def test_subtract_error(self, subtract_command, capsys):
        '''Testing for invalid arguments'''
        with patch('app.plugins.subtractcommand.Calculator.subtract', side_effect=ValueError("Error")):
            subtract_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out


# Testing the Multiply command:
class TestMultiplyCommand:
    def test_multiply(self,multiply_command,capsys):
        '''Testing multiply command'''
        multiply_command.execute('4','2')
        captured=capsys.readouterr()
        assert "4 x 2 = 8" in captured.out

    def test_multiply_one_arg(self,multiply_command,capsys):
        '''Testing one argument'''
        multiply_command.execute('4')
        captured=capsys.readouterr()
        assert "Only two aguments must be given" in captured.out

    def test_multiply_invalid_arg(self,multiply_command,capsys):
        '''Testing invalid argument'''
        multiply_command.execute('x','3')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_multiply_error(self, multiply_command, capsys):
        '''Testing for invalid arguments'''
        with patch('app.plugins.multiplycommand.Calculator.multiply', side_effect=ValueError("Error")):
            multiply_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out

# Testing the Multiply command:

class TestDivideCommand:
    def test_Divide(self,divide_command,capsys):
        '''Testing Divide command'''
        divide_command.execute('4','2')
        captured=capsys.readouterr()
        assert "4 / 2 = 2" in captured.out

    def test_Divide_one_arg(self,divide_command,capsys):
        '''Testing one argument'''
        divide_command.execute('4')
        captured=capsys.readouterr()
        assert "Only two aguments must be given" in captured.out

    def test_Divide_invalid_arg(self,divide_command,capsys):
        '''Testing invalid argument'''
        divide_command.execute('x','3')
        captured=capsys.readouterr()
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_Divide_by_zero(self,divide_command,capsys):
        '''Testing divide by zero'''
        divide_command.execute('9','0')
        captured=capsys.readouterr()
        assert "Cannot be divided by zero" in captured.out

    def test_divide_error(self, divide_command, capsys):
        '''Testing for invalid arguments'''
        with patch('app.plugins.dividecommand.Calculator.divide', side_effect=ValueError("Error")):
            divide_command.execute('4', '2')
            captured = capsys.readouterr()
            assert "Error" in captured.out

# Testing menu command
class TestMenuCommand:
    '''Test the Menu command'''
    def test_menu_command(self, menu_command, capsys):
        '''Test that the Menu command displays the list of available commands.'''
        menu_command.execute()
        captured = capsys.readouterr()
        assert "Commands Available:" in captured.out, "MenuCommand should display the available commands"
        assert "Add" in captured.out
        assert "Subtract" in captured.out
        assert "Multiply" in captured.out
        assert "Divide" in captured.out
        assert "Menu" in captured.out
