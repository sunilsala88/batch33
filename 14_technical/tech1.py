
import yfinance as yf
data=yf.download('TSLA',period='10y',multi_level_index=False)
print(data)
data['sma']=data['Close'].rolling(window=10).mean()

print(data)