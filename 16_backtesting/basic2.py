

import yfinance as yf
from backtesting import Backtest,Strategy
import pandas_ta as ta

def get_sma(closing_price,length):
    return ta.sma(closing_price,length)

class Smacross(Strategy):
    s1=20
    s2=50
    def init(self):
        self.sma1=self.I(get_sma,self.data.df.Close,self.s1)
        self.sma2=self.I(get_sma,self.data.df.Close,self.s2)
    def next(self):
        pass

data=yf.download('TSLA',period='2y',multi_level_index=False)
print(data)
sma=get_sma(data['Close'],20)
print(sma)

bt=Backtest(data,Smacross,cash=1000)
output=bt.run()
print(output)
bt.plot()