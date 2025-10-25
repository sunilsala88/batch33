

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
        
        if self.sma1[-1]>self.sma2[-1] and self.sma1[-2]<self.sma2[-2]:
            if self.position.is_short:
                self.position.close()
            self.buy()
        if self.sma1[-1]<self.sma2[-1] and self.sma1[-2]>self.sma2[-2]:
            if self.position.is_long:
                self.position.close()
            self.sell()
data=yf.download('TSLA',period='2y',multi_level_index=False)
print(data)
sma=get_sma(data['Close'],20)
print(sma)

bt=Backtest(data,Smacross,cash=1000,finalize_trades=True)
output=bt.run()
print(output)
bt.plot()
# output['_trades'].to_csv('trades.csv')