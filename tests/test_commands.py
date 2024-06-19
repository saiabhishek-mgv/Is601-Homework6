import pytest
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand

def test_add_command_invalid_input(capfd):
    add_command = AddCommand()
    add_command.execute('1')
    out, _ = capfd.readouterr()
    assert "Add command requires exactly two arguments" in out

    add_command.execute('a', '2')
    out, _ = capfd.readouterr()
    assert "Error in addition" in out

def test_divide_command_invalid_input(capfd):
    divide_command = DivideCommand()
    divide_command.execute('5')
    out, _ = capfd.readouterr()
    assert "Divide command requires exactly two arguments" in out

    divide_command.execute('5', 'a')
    out, _ = capfd.readouterr()
    assert "Error in division" in out

    divide_command.execute('5', '0')
    out, _ = capfd.readouterr()
    assert "Error: Cannot divide by zero" in out

def test_subtract_command_invalid_input(capfd):
    subtract_command = SubtractCommand()
    subtract_command.execute('1')
    out, _ = capfd.readouterr()
    assert "Subtract command requires exactly two arguments" in out

    subtract_command.execute('5', 'a')
    out, _ = capfd.readouterr()
    assert "Error in subtraction" in out

def test_multiply_command_invalid_input(capfd):
    multiply_command = MultiplyCommand()
    multiply_command.execute('1')
    out, _ = capfd.readouterr()
    assert "Multiply command requires exactly two arguments" in out

    multiply_command.execute('a', '2')
    out, _ = capfd.readouterr()
    assert "Error in multiplication" in out
