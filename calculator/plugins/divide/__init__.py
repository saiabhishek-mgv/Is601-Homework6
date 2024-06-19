from decimal import Decimal, InvalidOperation
from calculator.commands import Command

class DivideCommand(Command):
    def execute(self, *args):
        try:
            if len(args) != 2:
                raise ValueError("Divide command requires exactly two arguments.")
            a, b = Decimal(args[0]), Decimal(args[1])
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
            print(f"Result: {result}")
        except InvalidOperation:
            raise ValueError("Invalid input for Decimal conversion.")

