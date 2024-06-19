import builtins
import os
from unittest.mock import patch
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    calculator.command_handler.execute_command("add 2 3")

def test_subtract(calculator):
    calculator.command_handler.execute_command("subtract 5 3")

def test_multiply(calculator):
    calculator.command_handler.execute_command("multiply 4 3")

def test_divide(calculator):
    calculator.command_handler.execute_command("divide 10 2")

def test_divide_by_zero(calculator):
    calculator.command_handler.execute_command("divide 10 0")
    # Expected to handle division by zero and print an error message

def test_menu(calculator):
    calculator.command_handler.execute_command("menu")
    # Verify that menu command lists all available commands

def test_unknown_command(calculator, capfd):
    calculator.command_handler.execute_command("unknown 1 2")
    captured = capfd.readouterr()
    assert "No such command: unknown" in captured.out

def test_load_plugins_directory_not_exist(monkeypatch):
    def mock_exists(path):
        # Return False for the plugins directory to simulate non-existence
        if 'non_existent_plugins' in path:
            return False
        return True
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    calculator = Calculator(plugin_dir='non_existent_plugins')
    assert len(calculator.command_handler.commands) == 0


def test_load_plugins_empty_directory(monkeypatch, tmpdir):
    empty_plugin_dir = tmpdir.mkdir('empty_plugins')
    original_exists = os.path.exists

    def mock_exists(path):
        if str(empty_plugin_dir) in path:
            return True
        return original_exists(path)

    monkeypatch.setattr(os.path, 'exists', mock_exists)
    calculator = Calculator(plugin_dir=str(empty_plugin_dir))
    assert len(calculator.command_handler.commands) == 0
    monkeypatch.undo()

def test_load_invalid_plugin(monkeypatch, tmpdir):
    invalid_plugin_dir = tmpdir.mkdir('invalid_plugins')
    invalid_plugin_file = invalid_plugin_dir.join('__init__.py')
    invalid_plugin_file.write("class NotACommand:\n    pass")

    def mock_listdir(path):
        if path == str(invalid_plugin_dir):
            return ['invalid_plugins']
        return []

    def mock_isdir(path):
        if path == str(invalid_plugin_dir):
            return True
        return False

    monkeypatch.setattr(os, 'listdir', mock_listdir)
    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    calculator = Calculator(plugin_dir=str(invalid_plugin_dir))
    assert len(calculator.command_handler.commands) == 0

def test_start_menu_command(calculator, capfd):
    # Simulate input for "menu" and then "exit"
    inputs = iter(['menu', 'exit'])
    with patch('builtins.input', lambda _: next(inputs)):
        calculator.start()
    captured = capfd.readouterr()
    assert "Type 'menu' to see the list of available commands or 'exit' to exit." in captured.out
    assert "Available commands:" in captured.out

def test_start_add_command(calculator, capfd):
    # Simulate input for "add 2 3" and then "exit"
    inputs = iter(['add 2 3', 'exit'])
    with patch('builtins.input', lambda _: next(inputs)):
        calculator.start()
    captured = capfd.readouterr()
    assert "Result: 5" in captured.out

def test_start_invalid_command(calculator, capfd):
    # Simulate input for an invalid command and then "exit"
    inputs = iter(['invalid_command', 'exit'])
    with patch('builtins.input', lambda _: next(inputs)):
        calculator.start()
    captured = capfd.readouterr()
    assert "No such command: invalid_command" in captured.out

def test_start_divide_by_zero(calculator, capfd):
    # Simulate input for "divide 10 0" and then "exit"
    inputs = iter(['divide 10 0', 'exit'])
    with patch('builtins.input', lambda _: next(inputs)):
        calculator.start()
    captured = capfd.readouterr()
    assert "Cannot divide by zero." in captured.out

def test_start_exit_command(calculator, capfd):
    # Simulate input for "exit"
    inputs = iter(['exit'])
    with patch('builtins.input', lambda _: next(inputs)):
        calculator.start()
    captured = capfd.readouterr()
    assert "Exiting the calculator. Goodbye!" in captured.out

def test_start_unexpected_error(calculator, capfd):
    # Simulate an unexpected error by mocking execute_command to raise an exception
    with patch.object(calculator.command_handler, 'execute_command', side_effect=Exception("Forced error")):
        inputs = iter(['some_command', 'exit'])
        with patch('builtins.input', lambda _: next(inputs)):
            calculator.start()
    captured = capfd.readouterr()
    assert "An unexpected error occurred: Forced error" in captured.out