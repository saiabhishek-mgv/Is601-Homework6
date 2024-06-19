from decimal import Decimal
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
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error in division: {e}")


