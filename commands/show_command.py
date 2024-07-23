# commands/show_command.py
from commands.base_command import BaseCommand

class ShowCommand(BaseCommand):
    def __init__(self, message):
        self.message = message

    def execute(self, context):
        print(context.get(self.message, self.message))
