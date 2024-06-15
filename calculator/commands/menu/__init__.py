import sys
from calculator.commands import Command

class MenuCommand(Command):
    def execute(self):
        print(f'menu')

