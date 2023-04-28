from api import __api_init__
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
from pandas.core.frame import DataFrame
def benchmark():
    __api_init__.API.Backtest()
    __api_init__.API.Evaluate()
    __api_init__.API.Metrics()

def getHistoric(stock) -> DataFrame:
    today_date = datetime.today()
    start_date = datetime(1, 1, 1)
    end_date = datetime(today_date.year, today_date.month, today_date.day)
    print(today_date.day)
    data = yf.download(f'{stock}')
    return data
    
ticker = input("What ticker do you want to trade:\t")
print(getHistoric(ticker)['Open'])