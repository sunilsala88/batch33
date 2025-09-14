
import yfinance as yf

data=yf.download(tickers='NVDA',period='6mo')
print(data)