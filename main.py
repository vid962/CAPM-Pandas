import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas as pd

tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM', '^GSPC']
start = dt.datetime(2016, 12, 1)
end = dt.datetime(2022, 10, 1)
data = pdr.get_data_yahoo(tickers, start, end, interval="m")
data = data['Adj Close']
log_returns = np.log(data/data.shift())

cov = log_returns.cov()
var = log_returns['^GSPC'].var()
beta = cov.loc['AAPL', '^GSPC']/var
risk_free_return = 0.0138
market_return = .105
expected_return = risk_free_return + beta*(market_return - risk_free_return)

cov = log_returns.cov()
var = log_returns['^GSPC'].var()
beta = cov.loc['^GSPC']/var
risk_free_return = 0.0138
market_return = .105
expected_return = risk_free_return + beta*(market_return - risk_free_return)

print(expected_return)