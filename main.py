import sys
from app.calculator import Calculator
from decimal import Decimal, InvalidOperation

from app import App

if __name__ == '__main__':
    app = App()
    app.start()