# Import necessary modules and classes
from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.subtract import SubtractCommand


# Definition of the calulator class
class Calculator:
    def __init__(self):
        self.command_handler = CommandHandler()
    
    def start(self):
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))


        print("Type 'menu' to see the list of available commands or Type 'exit' to exit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input.lower() == 'exit':
                    break
                self.command_handler.execute_command(user_input)
            except Exception as e:
                print(f"An error occurred: {e}")
