import inquirer
from data.data import MarkSTMdata
from fs.cred.RH_CREDS_OBJ import RH_CRED
from termcolor import colored
from fs.getSettings import Settings
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
    ),
    inquirer.List(
    'edit_settings',
    message="Would you like to view/edit your current settings?",
    choices=["Yes", "No"]
    )
]

res = inquirer.prompt(questions)

# Print a message to let the user know what they selected, in green
if str(res['edit_settings']) == "Yes":
    creds = RH_CRED('username', 'password')
    settings = Settings(
        LOG_FILE_DIRECTORY='/var/log/my_app',
        LIMIT_TRADE_USAGE=1000,
        SPEED_OPTIMIZATION=False,
        ALLOW_MULTI_THREAD_TRADING=True,
        ROBBINHOOD_CREDS=creds,
    )    
    settings.LOADING_SETTINGS()

# Do something with the settings...
    print("Log file directory:", settings.LOG_FILE_DIRECTORY)
    print("Trade usage limit:", settings.LIMIT_TRADE_USAGE)
    print("Speed optimization:", settings.OPTIMIZE_SPEED)
    print("Multi-threaded trading:", settings.ALLOW_MULTI_THREAD_TRADING)
    print("Robinhood credentials:", settings.ROBBINHOOD_CREDS)
else:
    print(colored(f"Trading {str(res['ticker']).upper()} using the {res['model']} model", "green"))
