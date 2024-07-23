# commands/base_command.py
class BaseCommand:
    def execute(self, context):
        raise NotImplementedError("Each command must implement the execute method.")
