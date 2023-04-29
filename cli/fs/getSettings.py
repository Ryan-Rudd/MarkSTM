from security.RH_CREDS_OBJ import RH_CRED
class Settings(object):
    def __init__(self, 
                 LOG_FILE_DIRECTORY, 
                 LIMIT_TRADE_USAGE, 
                 OPERATING_SYSTEM, 
                 SPEED_OPTIMIZATION, 
                 ALLOW_MULTI_THREAD_TRADING, ROBBINHOOD_CREDS: RH_CRED):
        self.LOG_FILE_DIRECTORY = LOG_FILE_DIRECTORY
        self.LIMIT_TRADE_USAGE = LIMIT_TRADE_USAGE
        self.OPERATING_SYSTEM = OPERATING_SYSTEM
        self.OPTIMIZE_SPEED = SPEED_OPTIMIZATION
        self.ALLOW_MULTI_THREAD_TRADING = ALLOW_MULTI_THREAD_TRADING
        self.ROBBINHOOD_CREDS = ROBBINHOOD_CREDS