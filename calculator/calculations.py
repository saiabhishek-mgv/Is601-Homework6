from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrive the entire history of claulation."""
        return cls.history
    
    @classmethod
    def clear_history(cls):
        """Clear the history of calculation."""
        cls.history.clear()
    
    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there is no history."""
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by name of the operation."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
   