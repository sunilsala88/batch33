import yfinance as yf
from backtesting import Backtest,Strategy
import pandas_ta as ta


def upper(closing,length):
    b=ta.bbands(closing,length)
    return b[f'BBU_{length}_2.0_2.0']

def lower(closing,length):
    b=ta.bbands(closing,length)
    
    return b[f'BBL_{length}_2.0_2.0']

def middle(closing,length):
    b=ta.bbands(closing,length)
   
    return b[f'BBM_{length}_2.0_2.0']



class Bollinger(Strategy):
    l1=10

    def init(self):
        self.lower=self.I(lower,self.data.df.Close,self.l1)
        self.middle=self.I(middle,self.data.df.Close,self.l1)
        self.upper=self.I(upper,self.data.df.Close,self.l1)
    
    def next(self):
        pass





data=yf.download('JPY=X',period='2y',multi_level_index=False)
print(data)
u=upper(data['Close'],20)
print(u)

bt=Backtest(data,Bollinger,cash=1000)
output=bt.run()
bt.plot()