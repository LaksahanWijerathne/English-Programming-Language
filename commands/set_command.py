# commands/set_command.py
from commands.base_command import BaseCommand

class SetCommand(BaseCommand):
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

    def execute(self, context):
        context[self.var_name] = int(self.value)
