
import yfinance as yf

# data=yf.download(tickers='TSLA',period='6d',interval='1m',multi_level_index=False,ignore_tz=True)
# print(data)


data=yf.download(tickers='TSLA',start='2024-01-01',end='2024-12-31',interval='1h',multi_level_index=False)
print(data)


import datetime as dt
s=dt.datetime(2024,1,1)
e=dt.datetime(2024,12,31)
data=yf.download(tickers='TSLA',start=s,end=e,interval='1h',multi_level_index=False)
print(data)



