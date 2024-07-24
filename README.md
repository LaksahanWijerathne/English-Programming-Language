<a href="https://www.buymeacoffee.com/LaksahanWijerathna" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

The English Programming Language!

Welcome to the English Programming Language project! This project aims to create a simple, easy-to-understand programming language designed to be as close to natural English as possible. The goal is to make programming accessible to everyone, including children and beginners.

Features
Natural Language Syntax: Commands are written in a way that resembles natural English sentences.
Modular Design: Easily extend the language by adding new command modules.
Interactive CLI: A simple command-line interface to enter and execute commands.
Getting Started
Prerequisites
Make sure you have Python installed on your system. You can download it from python.org.

Installation
Clone the repository:

sh
Copy code
git clone https://github.com/LaksahanWijerathne/English-Programming-Language.git
cd English-programming-language
Install the necessary dependencies (if any):

sh
Copy code
pip install -r requirements.txt
Running the CLI
Start the interactive command-line interface:

sh
Copy code
python cli.py
Example Commands
Set a variable: set x to 10
Show a message: show x
Multiply a variable: multiply x by 5
Adding New Commands
To add a new command:

Create a new file in the commands directory, e.g., new_command.py.
Define your command class in this file, inheriting from BaseCommand.
Update commands/__init__.py to include your new command class.
Project Structure
cli.py: The entry point for the interactive command-line interface.
main.py: Handles command registry and dynamic loading of commands.
commands/: Contains individual command modules.
lexer.py: Tokenizes the input commands.
parser.py: Parses the tokens into executable commands.
interpreter.py: Executes the parsed commands.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the existing style and includes appropriate tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to the contributors and the open-source community for their support and inspiration.
