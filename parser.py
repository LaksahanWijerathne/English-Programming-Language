# parser.py
class SimpleParser:
    def __init__(self, lexer_class, registry):
        self.lexer_class = lexer_class
        self.registry = registry

    def parse(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.next_token()
        commands = []
        while self.current_token is not None:
            command = self.parse_command()
            if command:
                commands.append(command)
        return commands

    def parse_command(self):
        if self.current_token == 'set':
            return self.parse_set()
        elif self.current_token == 'show':
            return self.parse_show()
        elif self.current_token == 'multiply':
            return self.parse_multiply()
        else:
            raise SyntaxError(f"Unknown command: {self.current_token}")

    def parse_set(self):
        self.expect('set')
        var_name = self.current_token
        self.expect(self.current_token)
        self.expect('to')
        value = self.current_token
        self.expect(self.current_token)
        command_class = self.registry.get_command('set')
        return command_class(var_name, value)

    def parse_show(self):
        self.expect('show')
        message = self.current_token
        self.expect(self.current_token)
        command_class = self.registry.get_command('show')
        return command_class(message)

    def parse_multiply(self):
        self.expect('multiply')
        var_name = self.current_token
        self.expect(self.current_token)
        self.expect('by')
        value = self.current_token
        self.expect(self.current_token)
        command_class = self.registry.get_command('multiply')
        return command_class(var_name, value)

    def expect(self, token):
        if self.current_token == token:
            self.current_token = self.lexer.next_token()
        else:
            raise SyntaxError(f"Expected {token}, but found {self.current_token}")
