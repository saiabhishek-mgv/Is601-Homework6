from decimal import Decimal
import sys
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.commands import Command

class AddCommand(Command):
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return a result."""
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    def execute(self):
            @staticmethod
            def add(a: Decimal, b: Decimal) -> Decimal:
            #    Perform addition by delegating to the _perform_operation method with the add operation
                return AddCommand._perform_operation(a, b, add)
    print(f'Calculator._perform_operation(a, b, add)')

