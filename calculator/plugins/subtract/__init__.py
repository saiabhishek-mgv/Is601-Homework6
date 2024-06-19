from decimal import Decimal, InvalidOperation
from calculator.commands import Command

class SubtractCommand(Command):
    def execute(self, *args):
        try:
            if len(args) != 2:
                raise ValueError("Subtract command requires exactly two arguments.")
            a, b = Decimal(args[0]), Decimal(args[1])
            result = a - b
            print(f"Result: {result}")
        except InvalidOperation:
            raise ValueError("Invalid input for Decimal conversion.")
