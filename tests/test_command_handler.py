import pytest
from calculator.commands import CommandHandler, Command

class MockCommand(Command):
    def execute(self):
        pass

def test_no_command_provided():
    handler = CommandHandler()
    with pytest.raises(ValueError, match="No input provided."):
        handler.execute_command("")

def test_no_such_command(capfd):
    handler = CommandHandler()
    handler.execute_command("unknown")
    captured = capfd.readouterr()
    assert "No such command: unknown" in captured.out

def test_register_command():
    handler = CommandHandler()
    handler.register_command("mock", MockCommand())
    assert "mock" in handler.commands

def test_execute_command_add():
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command("add", mock_command)
    handler.execute_command("add 2 3")

def test_execute_command_invalid():
    handler = CommandHandler()
    with pytest.raises(ValueError):
        handler.execute_command("")
