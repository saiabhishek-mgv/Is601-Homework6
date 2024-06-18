from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
    
    def execute_command(self, user_input: str):
        parts = user_input.split()
        if not parts:
            print("No input provided.")
            return

        command_name = parts[0]
        args = parts[1:]

        if command_name in self.commands:
            try:
                self.commands[command_name].execute(*args)
            except Exception as e:
                print(f"Error executing command '{command_name}': {e}")
        else:
            print(f"No such command: {command_name}")


        