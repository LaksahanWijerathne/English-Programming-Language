# commands/multiply_command.py
from commands.base_command import BaseCommand

class MultiplyCommand(BaseCommand):
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

    def execute(self, context):
        if self.var_name in context:
            context[self.var_name] *= int(self.value)
        else:
            raise ValueError(f"Variable {self.var_name} not found.")
