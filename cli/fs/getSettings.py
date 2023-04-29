import json
from cred.RH_CREDS_OBJ import RH_CRED
import platform
import inquirer
import os

class Settings(object):
    def __init__(self, 
                 LOG_FILE_DIRECTORY, 
                 LIMIT_TRADE_USAGE, 
                 SPEED_OPTIMIZATION, 
                 ALLOW_MULTI_THREAD_TRADING, 
                 ROBBINHOOD_CREDS: RH_CRED):
        self.LOG_FILE_DIRECTORY = LOG_FILE_DIRECTORY
        self.LIMIT_TRADE_USAGE = LIMIT_TRADE_USAGE
        self.OPERATING_SYSTEM = platform.system()
        self.OPTIMIZE_SPEED = SPEED_OPTIMIZATION
        self.ALLOW_MULTI_THREAD_TRADING = ALLOW_MULTI_THREAD_TRADING
        self.ROBBINHOOD_CREDS = ROBBINHOOD_CREDS

    def LOADING_SETTINGS(self):
        if self.OPERATING_SYSTEM == 'Windows':
            appdata_dir = os.getenv('APPDATA')
            settings_path = os.path.join(appdata_dir, 'my_app', 'settings.json')
        elif self.OPERATING_SYSTEM == 'Linux':
            home_dir = os.getenv('HOME')
            settings_path = os.path.join(home_dir, '.config', 'my_app', 'settings.json')
        elif self.OPERATING_SYSTEM == 'Darwin': # for macOS
            home_dir = os.getenv('HOME')
            settings_path = os.path.join(home_dir, 'Library', 'Application Support', 'my_app', 'settings.json')
        else:
            raise Exception("Unsupported operating system: {}".format(self.OPERATING_SYSTEM))
        
        questions = [
            inquirer.Text('LOG_FILE_DIRECTORY', message="Enter the log file directory", default=self.LOG_FILE_DIRECTORY),
            inquirer.Text('LIMIT_TRADE_USAGE', message="Enter the trade usage limit", default=self.LIMIT_TRADE_USAGE),
            inquirer.Confirm('SPEED_OPTIMIZATION', message="Enable speed optimization?", default=self.OPTIMIZE_SPEED),
            inquirer.Confirm('ALLOW_MULTI_THREAD_TRADING', message="Enable multi-threaded trading?", default=self.ALLOW_MULTI_THREAD_TRADING),
            inquirer.Text('ROBBINHOOD_CREDS', message="Enter Robinhood credentials", default=self.ROBBINHOOD_CREDS),
        ]
        answers = inquirer.prompt(questions)
        
        self.LOG_FILE_DIRECTORY = answers['LOG_FILE_DIRECTORY']
        self.LIMIT_TRADE_USAGE = answers['LIMIT_TRADE_USAGE']
        self.OPTIMIZE_SPEED = answers['SPEED_OPTIMIZATION']
        self.ALLOW_MULTI_THREAD_TRADING = answers['ALLOW_MULTI_THREAD_TRADING']
        self.ROBBINHOOD_CREDS = answers['ROBBINHOOD_CREDS']
        
        with open(settings_path, 'w') as f:
            settings_dict = {
                'LOG_FILE_DIRECTORY': self.LOG_FILE_DIRECTORY,
                'LIMIT_TRADE_USAGE': self.LIMIT_TRADE_USAGE,
                'OPTIMIZE_SPEED': self.OPTIMIZE_SPEED,
                'ALLOW_MULTI_THREAD_TRADING': self.ALLOW_MULTI_THREAD_TRADING,
                'ROBBINHOOD_CREDS': self.ROBBINHOOD_CREDS,
            }
            json.dump(settings_dict, f)
