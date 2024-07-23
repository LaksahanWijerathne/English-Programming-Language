# cli.py
from lexer import SimpleLexer
from parser import SimpleParser
from interpreter import Interpreter
from main import CommandRegistry, load_commands  # Import from main.py

def main():
    registry = CommandRegistry()
    load_commands(registry)

    parser = SimpleParser(SimpleLexer, registry)
    interpreter = Interpreter(parser)

    print("Welcome to the English Programming Language!")
    print("Type your commands below. Type 'exit' to quit.")

    while True:
        try:
            code = input("> ")
            if code.lower() in ['exit', 'quit']:
                break
            interpreter.run(code)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
