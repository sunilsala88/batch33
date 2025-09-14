
import yfinance as yf

# data=yf.download(tickers='TSLA',period='6d',interval='1m',multi_level_index=False,ignore_tz=True)
# print(data)


data=yf.download(tickers='TSLA',start='2024-01-01',end='2024-12-31',interval='1h',multi_level_index=False)
print(data)
data.to_csv('stock_data.csv')