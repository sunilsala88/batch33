
import yfinance as yf


data=yf.download(tickers='TSLA',start='2024-01-01',end='2024-12-31',interval='1h',multi_level_index=False)
print(data)