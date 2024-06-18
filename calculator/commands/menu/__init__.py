from calculator.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        print("Available commands:")
        for command_name in self.command_handler.commands:
            if command_name != "menu":  # Exclude the 'menu' command itself
                print(f"- {command_name}")


