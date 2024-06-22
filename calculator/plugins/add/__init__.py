from decimal import Decimal, InvalidOperation
from calculator.commands import Command
import logging

class AddCommand(Command):
    def execute(self, *args):
        logging.info("Hello")
        if len(args) != 2:
            raise ValueError("Add command requires exactly two arguments.")
        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = a + b
            print(f"Result: {result}")
        except InvalidOperation:
            raise ValueError("Invalid input for Decimal conversion.")

