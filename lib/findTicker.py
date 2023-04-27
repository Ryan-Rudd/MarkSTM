import pandas as pd
from yahoo_fin import stock_info as si 

data_frame_nasdaq = pd.DataFrame(si.tickers_nasdaq())
data_frame_dow = pd.DataFrame(si.tickers_dow())
data_frame_ftse100 = pd.DataFrame(si.tickers_ftse100())
data_frame_ftse250 = pd.DataFrame(si.tickers_ftse250())
data_frame_ibovespa = pd.DataFrame(si.tickers_ibovespa())
data_frame_nifty50 = pd.DataFrame(si.tickers_nifty50())
data_frame_sp500 = pd.DataFrame(si.tickers_sp500())
data_frame_other = pd.DataFrame(si.tickers_other())

symbol_set_nasdaq = set(symbol for symbol in data_frame_nasdaq[0].values.tolist()) 
symbol_set_dow = set(symbol for symbol in data_frame_dow[0].values.tolist()) 
symbol_set_ftse100 = set(symbol for symbol in data_frame_ftse100[0].values.tolist()) 
symbol_set_ftse250 = set(symbol for symbol in data_frame_ftse250[0].values.tolist()) 
symbol_set_ibovespa = set(symbol for symbol in data_frame_ibovespa[0].values.tolist()) 
symbol_set_nifty50 = set(symbol for symbol in data_frame_nifty50[0].values.tolist()) 
symbol_set_sp500 = set(symbol for symbol in data_frame_sp500[0].values.tolist()) 
symbol_set_other = set(symbol for symbol in data_frame_other[0].values.tolist()) 

TICKERS = set.union(
    symbol_set_dow,
    symbol_set_nasdaq,
    symbol_set_ftse100, 
    symbol_set_ftse250, 
    symbol_set_ibovespa, 
    symbol_set_nifty50, 
    symbol_set_sp500, 
    symbol_set_other)
