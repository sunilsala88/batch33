
import pandas as pd
data=pd.read_csv('data.csv')
data.drop(['symbol','trade_count'],axis=1,inplace=True)

data.rename(columns={'timestamp':'Date','open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'},inplace=True)
data['Date']=pd.to_datetime(data['Date'])
print(data.info())
data.set_index('Date',inplace=True)
print(data)

data=data.iloc[:1000]

def ema(
    close: pd.Series,
    length: int = 10,
    presma: bool = True,
    offset: int = 0,
    adjust: bool = False,
    **kwargs
) -> pd.Series:
    """Exponential Moving Average
    
    This Moving Average is more responsive than the Simple Moving
    Average (SMA).
    
    Parameters:
        close (pd.Series): Close price series
        length (int): The period. Default: 10
        presma (bool): Initialize with SMA like TA Lib. Default: True
        offset (int): Post shift. Default: 0
        adjust (bool): Default: False
        
    Other Parameters:
        fillna (value): pd.DataFrame.fillna(value)
        
    Returns:
        pd.Series: EMA values
    """
    # Validate length
    if length <= 0:
        length = 10
    
    # Check if we have enough data
    if len(close) < length:
        return pd.Series([np.nan] * len(close), index=close.index, name=f"EMA_{length}")
    
    # Calculate EMA
    if presma:  # TA Lib implementation - start with SMA
        close_copy = close.copy()
        sma_nth = close.iloc[0:length].mean()
        close_copy.iloc[:length - 1] = np.nan
        close_copy.iloc[length - 1] = sma_nth
        ema_result = close_copy.ewm(span=length, adjust=adjust).mean()
    else:
        ema_result = close.ewm(span=length, adjust=adjust).mean()
    
    # Apply offset
    if offset != 0:
        ema_result = ema_result.shift(offset)
    
    # Fill NaN values if requested
    if "fillna" in kwargs:
        ema_result.fillna(kwargs["fillna"], inplace=True)
    
    # Name and Category
    ema_result.name = f"EMA_{length}"
    
    return ema_result


import yfinance as yf
from backtesting import Backtest,Strategy
import time

import pandas as pd
import numpy as np
from typing import Union, Optional

def supertrend(
    high: pd.Series,
    low: pd.Series,
    close: pd.Series,
    length: int = 7,
    atr_length: Optional[int] = None,
    multiplier: float = 3.0,
    atr_mamode: str = "rma",
    offset: int = 0,
    **kwargs
) -> pd.DataFrame:
    """Supertrend Indicator
    
    This indicator attempts to identify trend direction as well as support and
    resistance levels.
    
    Parameters:
        high (pd.Series): High price series
        low (pd.Series): Low price series
        close (pd.Series): Close price series
        length (int): The period. Default: 7
        atr_length (int): ATR period. Default: length
        multiplier (float): Coefficient for upper and lower band distance. Default: 3.0
        atr_mamode (str): MA type for ATR calculation ('sma', 'ema', 'rma'). Default: 'rma'
        offset (int): Post shift. Default: 0
        
    Returns:
        pd.DataFrame: DataFrame with 4 columns:
            - SUPERT_{length}_{multiplier}: Supertrend line
            - SUPERTd_{length}_{multiplier}: Direction (1 for uptrend, -1 for downtrend)
            - SUPERTl_{length}_{multiplier}: Long (support) line
            - SUPERTs_{length}_{multiplier}: Short (resistance) line
    """
    # Validate and set defaults
    if atr_length is None:
        atr_length = length
    
    # Calculate True Range
    def true_range(high, low, close):
        tr1 = high - low
        tr2 = abs(high - close.shift(1))
        tr3 = abs(low - close.shift(1))
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        return tr
    
    # Calculate ATR based on mode
    def calculate_atr(high, low, close, period, mode='rma'):
        tr = true_range(high, low, close)
        
        if mode == 'sma':
            atr = tr.rolling(window=period).mean()
        elif mode == 'ema':
            atr = tr.ewm(span=period, adjust=False).mean()
        elif mode == 'rma':  # RMA (Wilder's smoothing)
            alpha = 1.0 / period
            atr = tr.ewm(alpha=alpha, adjust=False).mean()
        else:
            # Default to RMA
            alpha = 1.0 / period
            atr = tr.ewm(alpha=alpha, adjust=False).mean()
        
        return atr
    
    # Calculate HL2 (midpoint)
    hl2 = (high + low) / 2
    
    # Calculate ATR
    atr = calculate_atr(high, low, close, atr_length, atr_mamode)
    matr = multiplier * atr
    
    # Calculate basic upper and lower bands
    ub = hl2 + matr
    lb = hl2 - matr
    
    # Initialize arrays
    m = len(close)
    direction = np.ones(m)
    trend = np.full(m, np.nan)
    long = np.full(m, np.nan)
    short = np.full(m, np.nan)
    
    # Calculate Supertrend
    for i in range(1, m):
        # Determine direction
        if close.iloc[i] > ub.iloc[i - 1]:
            direction[i] = 1
        elif close.iloc[i] < lb.iloc[i - 1]:
            direction[i] = -1
        else:
            direction[i] = direction[i - 1]
            
            # Adjust bands based on direction
            if direction[i] > 0 and lb.iloc[i] < lb.iloc[i - 1]:
                lb.iloc[i] = lb.iloc[i - 1]
            if direction[i] < 0 and ub.iloc[i] > ub.iloc[i - 1]:
                ub.iloc[i] = ub.iloc[i - 1]
        
        # Set trend values
        if direction[i] > 0:
            trend[i] = lb.iloc[i]
            long[i] = lb.iloc[i]
        else:
            trend[i] = ub.iloc[i]
            short[i] = ub.iloc[i]
    
    # Set initial NaN values
    direction[:length] = np.nan
    
    # Create output DataFrame
    _props = f"_{length}_{multiplier}"
    data = {
        f"SUPERT{_props}": trend,
        f"SUPERTd{_props}": direction,
        f"SUPERTl{_props}": long,
        f"SUPERTs{_props}": short
    }
    df = pd.DataFrame(data, index=close.index)
    
    df.name = f"SUPERT{_props}"
    df.category = "overlap"
    
    # Apply offset
    if offset != 0:
        df = df.shift(offset)
    
    # Fill NaN values if requested
    if "fillna" in kwargs:
        df.fillna(kwargs["fillna"], inplace=True)
    
    return df


def get_ema(close,length):
    em=ema(close,length)
    return em

def get_trend(high,low,close,length,mul):
    st=supertrend(high,low,close,length,mul)
    return st[f'SUPERTd_{length}_{mul}.0']

def get_super(high,low,close,length,mul):
    st=supertrend(high,low,close,length,mul)
    return st[f'SUPERT_{length}_{mul}.0']


st = supertrend(data['High'], data['Low'], data['Close'], length=10, multiplier=3.0)
print(st)

em= ema(data['Close'],length=10)
print(em)



class Supertrend(Strategy):
    l1=20
    f1=3
    em1=50

    def init(self):
        self.super=self.I(get_super,self.data.df.High,self.data.df.Low,self.data.df.Close,self.l1,self.f1)
        self.trend=self.I(get_trend,self.data.df.High,self.data.df.Low,self.data.df.Close,self.l1,self.f1)
        self.ema=self.I(get_ema,self.data.df.Close,self.em1)

    def next(self):
   
  
        
        if self.trend[-1]==1  and self.ema[-1]<self.data.Close[-1]:
            if self.position.is_short:
                self.position.close()
            if not self.position:
                self.buy()
        if self.trend[-1]==-1  and self.ema[-1]>self.data.Close[-1]:
            if self.position.is_long:
                self.position.close()
            if not self.position:
                self.sell()



bt=Backtest(data,Supertrend,cash=10000,finalize_trades=True)
output=bt.run()
print(output)
bt.plot()
