import inquirer
from data.data import MarkSTMdata
from termcolor import colored

# Define some ASCII art to display at the start of the program
ascii_art = """

███╗░░░███╗░█████╗░██████╗░██╗░░██╗░██████╗████████╗███╗░░░███╗
████╗░████║██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝████╗░████║
██╔████╔██║███████║██████╔╝█████═╝░╚█████╗░░░░██║░░░██╔████╔██║
██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░░╚═══██╗░░░██║░░░██║╚██╔╝██║
██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗██████╔╝░░░██║░░░██║░╚═╝░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝
"""

# Print the ASCII art in red
print(colored(ascii_art, "blue"))

# Use inquirer to prompt the user for input
questions = [
    inquirer.List(
        'model',
        message="Which model would you like to operate with?",
        choices=MarkSTMdata.MODELS,
        ),
    inquirer.Text(
    'ticker',
    message="What stock would you like to auto-trade?",
    )
]

res = inquirer.prompt(questions)

# Print a message to let the user know what they selected, in green
print(colored(f"Trading {res['ticker']} using the {res['model']} model", "green"))