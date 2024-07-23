# main.py
import os
import importlib

class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, name, command_class):
        self.commands[name] = command_class

    def get_command(self, name):
        return self.commands.get(name, None)

def load_commands(registry):
    commands_dir = os.path.join(os.path.dirname(__file__), 'commands')
    for filename in os.listdir(commands_dir):
        if filename.endswith('_command.py'):
            module_name = f"commands.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for command_name in dir(module):
                if command_name.endswith('Command'):
                    command_class = getattr(module, command_name)
                    registry.register(command_name.lower().replace('command', ''), command_class)

# Initialize command registry and load commands
registry = CommandRegistry()
load_commands(registry)
