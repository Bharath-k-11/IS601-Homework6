from app.operation.operations import add, subtract, multiply, divide
from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.x=x
        self.y=y
        self.operation=operation

    @staticmethod
    def create(x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(x, y, operation)
    
    def perform(self) -> Decimal:
        return self.operation(self.x, self.y)
    
    def __repr__(self):
        return f"Calculation({self.x}, {self.y}, {self.operation.__name__})"
