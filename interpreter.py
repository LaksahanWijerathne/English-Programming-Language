# interpreter.py
class Interpreter:
    def __init__(self, parser):
        self.parser = parser
        self.context = {}

    def run(self, code):
        lexer = self.parser.lexer_class(code)
        commands = self.parser.parse(lexer)
        for command in commands:
            command.execute(self.context)
