import sys
from calculator.commands import Command

class SubtractCommand(Command):
    def execute(self):
        print(f'subtract')

