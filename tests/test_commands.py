import pytest
from calculator.commands import CommandHandler
from calculator.plugins.add import AddCommand
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.multiply import MultiplyCommand
from calculator.plugins.divide import DivideCommand

def test_add_command():
    handler = CommandHandler()
    add_command = AddCommand()
    handler.register_command("add", add_command)
    handler.execute_command("add 2 3")

def test_subtract_command():
    handler = CommandHandler()
    subtract_command = SubtractCommand()
    handler.register_command("subtract", subtract_command)
    handler.execute_command("subtract 5 3")

def test_subtract_command_missing_arguments():
    subtract_command = SubtractCommand()
    with pytest.raises(ValueError, match="Subtract command requires exactly two arguments."):
        subtract_command.execute("5")

def test_subtract_command_non_numeric():
    subtract_command = SubtractCommand()
    with pytest.raises(ValueError):
        subtract_command.execute("five", "3")

def test_multiply_command():
    handler = CommandHandler()
    multiply_command = MultiplyCommand()
    handler.register_command("multiply", multiply_command)
    handler.execute_command("multiply 4 3")

def test_multiply_command_missing_arguments():
    multiply_command = MultiplyCommand()
    with pytest.raises(ValueError, match="Multiply command requires exactly two arguments."):
        multiply_command.execute("5")

def test_multiply_command_non_numeric():
    multiply_command = MultiplyCommand()
    with pytest.raises(ValueError):
        multiply_command.execute("five", "3")

def test_divide_command():
    handler = CommandHandler()
    divide_command = DivideCommand()
    handler.register_command("divide", divide_command)
    handler.execute_command("divide 10 2")

def test_divide_by_zero_command():
    handler = CommandHandler()
    divide_command = DivideCommand()
    handler.register_command("divide", divide_command)
    handler.execute_command("divide 10 0")

def test_divide_command_missing_arguments():
    divide_command = DivideCommand()
    with pytest.raises(ValueError, match="Divide command requires exactly two arguments."):
        divide_command.execute("5")

def test_divide_command_non_numeric():
    divide_command = DivideCommand()
    with pytest.raises(ValueError):
        divide_command.execute("five", "3")

def test_add_command_missing_arguments():
    add_command = AddCommand()
    with pytest.raises(ValueError, match="Add command requires exactly two arguments."):
        add_command.execute("5")

def test_add_command_non_numeric():
    add_command = AddCommand()
    with pytest.raises(ValueError):
        add_command.execute("five", "3")
