# lexer.py
import re

class SimpleLexer:
    def __init__(self, code):
        self.tokens = re.findall(r'\w+|[^\s\w]', code)
        self.pos = 0

    def next_token(self):
        if self.pos < len(self.tokens):
            self.pos += 1
            return self.tokens[self.pos - 1]
        else:
            return None
