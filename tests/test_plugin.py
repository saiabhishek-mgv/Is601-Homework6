import os
from calculator import Calculator

def test_load_plugins():
    calculator = Calculator(plugin_dir='plugins')
    # Ensure the expected commands are registered
    assert 'add' in calculator.command_handler.commands
    assert 'subtract' in calculator.command_handler.commands
    assert 'multiply' in calculator.command_handler.commands
    assert 'divide' in calculator.command_handler.commands

def test_no_duplicate_commands():
    calculator = Calculator(plugin_dir='plugins')
    commands = calculator.command_handler.commands
    assert len(commands) == len(set(commands.keys()))
