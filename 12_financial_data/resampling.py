
import yfinance as yf


data=yf.download(tickers='TSLA',period='5d',interval='1m',multi_level_index=False,ignore_tz=True)
print(data)

#resample
d1={'Close':'last','High':'max','Low':'min','Open':'first','Volume':'sum'}
data1=data.resample('5min').agg(d1).dropna()
print(data1.tail(100))