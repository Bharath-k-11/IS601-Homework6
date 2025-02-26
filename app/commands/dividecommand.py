from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command

class Divide(Command):
    '''This is the divide command class'''
    def execute(self, *args):
        if not args:  # This prompts for input, if arguments are not given
            args = input("Enter two numbers separated by space: ").split()
        if len(args) != 2:  # Makes sure that only two arguments must be given
            print("Only two arguments must be given")
            return

        try:
            x, y = map(Decimal, args) 
            if y==0:
                print("Cannot be divided by zero") # We can't divide by zero which raises a error
                return 
            result = Calculator.divide(x, y)
            print(f"{x} / {y} = {result}")
        except InvalidOperation:
            print(f"One of the entered numbers is invalid. Please enter valid inputs.")
        except ValueError as ve:  
            print(f"{ve}")
        except Exception as e:
            print(f"{e}")
