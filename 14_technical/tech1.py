
import yfinance as yf
data=yf.download('NVDA',period='10y',multi_level_index=False)
print(data)
data['sma']=data['Close'].rolling(window=10).mean()


import pandas_ta as ta
data['sma2']=ta.sma(data['Close'],length=10)
data['ema']=ta.ema(data['Close'],length=10)
ta.supertrend()

import talib
data['sma3']=talib.SMA(data['Close'],10)
data['ema2']=talib.EMA(data['Close'],10)

#pandasta
#talib
print(data)
import mplfinance as mpf
a=mpf.make_addplot(data['sma'],color='r')
b=mpf.make_addplot(data['ema'],color='black')
mpf.plot(data,type='candle',style='yahoo',addplot=[a,b])


#talib
#doc is poor and install diff

#pandas 
#doc is and install easy