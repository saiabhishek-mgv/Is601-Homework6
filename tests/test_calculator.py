from calculator import Calculator
from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.subtract import SubtractCommand

def test_calculator_initialization():
    calculator = Calculator()
    assert calculator.command_handler is not None

def test_calculator_start(monkeypatch):
    calculator = Calculator()
    
    inputs = iter(['add 1 2', 'subtract 5 3', 'multiply 4 2', 'divide 8 2', 'menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    calculator.start()

class FaultyCommandHandler(CommandHandler):
    def execute_command(self, user_input: str):
        raise Exception("Intentional exception for testing")

def test_calculator_exception_handling(monkeypatch, capsys):
    # Use the faulty command handler that throws an exception
    calculator = Calculator()
    calculator.command_handler = FaultyCommandHandler()
    calculator.command_handler.register_command("add", AddCommand())
    calculator.command_handler.register_command("subtract", SubtractCommand())
    calculator.command_handler.register_command("multiply", MultiplyCommand())
    calculator.command_handler.register_command("divide", DivideCommand())
    calculator.command_handler.register_command("menu", MenuCommand(calculator.command_handler))

    inputs = iter(['add 1 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    calculator.start()
    captured = capsys.readouterr()
    assert "An error occurred: Intentional exception for testing" in captured.out
