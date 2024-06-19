import pytest
from calculator import CommandHandler
from calculator.commands import Command
from calculator.commands.add import AddCommand
from calculator.commands.menu import MenuCommand

class MockCommand(Command):
    def execute(self, *args):
        if "fail" in args:
            raise Exception("Intentional failure")
        print("MockCommand executed")

def test_register_command():
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command("mock", mock_command)
    assert "mock" in handler.commands
    assert handler.commands["mock"] == mock_command

def test_execute_command_add(capfd):
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command("mock", mock_command)
    handler.execute_command("mock 1 2")
    out, _ = capfd.readouterr()
    assert "MockCommand executed" in out

def test_execute_command_no_input_provided(capfd):
    handler = CommandHandler()
    handler.execute_command("")
    out, _ = capfd.readouterr()
    assert "No input provided." in out

def test_execute_command_invalid(capfd):
    handler = CommandHandler()
    handler.execute_command("nonexistent")
    out, _ = capfd.readouterr()
    assert "No such command: nonexistent" in out

def test_execute_command_exception_handling(capfd):
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command("mock", mock_command)
    handler.execute_command("mock fail")
    out, _ = capfd.readouterr()
    assert "Error executing command 'mock'" in out