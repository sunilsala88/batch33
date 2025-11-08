import yfinance as yf
import pandas as pd
import numpy as np
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import pandas_ta as ta

# Fetch TSLA hourly data
print("Fetching TSLA data...")
ticker = yf.Ticker("TSLA")

# Get hourly data for backtesting (last 2 years)
hourly_data = ticker.history(period="2y", interval="1h")
print(f"Hourly data shape: {hourly_data.shape}")

# Get daily data for EMA calculation (need more history for EMA)
daily_data = ticker.history(period="2y", interval="1d")
print(f"Daily data shape: {daily_data.shape}")

# Calculate EMA on daily data (let's use 20-period EMA)
daily_data['EMA'] = daily_data['Close'].ewm(span=20, adjust=False).mean()

# Prepare hourly data for backtesting
df = hourly_data.copy()
df = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

# Remove timezone info if present
if df.index.tz is not None:
    df.index = df.index.tz_localize(None)
if daily_data.index.tz is not None:
    daily_data.index = daily_data.index.tz_localize(None)

# Merge daily EMA to hourly data (forward fill for intraday bars)
# Reset index and name it properly
df_temp = df.reset_index()
df_temp.columns = ['Datetime'] + list(df_temp.columns[1:])
daily_temp = daily_data[['EMA']].reset_index()
daily_temp.columns = ['Datetime', 'EMA']

# Convert to date only for merging
df_temp['Date'] = df_temp['Datetime'].dt.date
daily_temp['Date'] = daily_temp['Datetime'].dt.date

# Merge on date
merged = df_temp.merge(daily_temp[['Date', 'EMA']], on='Date', how='left')
df['EMA_Daily'] = merged['EMA'].values

# Calculate Supertrend on hourly data
def calculate_supertrend(df, period=10, multiplier=3):
    """Calculate Supertrend indicator using correct algorithm"""
    high = df['High'].copy()
    low = df['Low'].copy()
    close = df['Close'].copy()
    
    # Calculate ATR
    atr = ta.atr(high, low, close, length=period)
    
    # Calculate basic bands (HL/2)
    hl_avg = (high + low) / 2
    
    # Basic upper and lower bands
    basic_upper_band = hl_avg + (multiplier * atr)
    basic_lower_band = hl_avg - (multiplier * atr)
    
    # Initialize final bands
    final_upper_band = pd.Series(index=df.index, dtype=float)
    final_lower_band = pd.Series(index=df.index, dtype=float)
    supertrend = pd.Series(index=df.index, dtype=float)
    direction = pd.Series(index=df.index, dtype=int)
    
    # Calculate Supertrend
    for i in range(len(df)):
        if i < period:
            final_upper_band.iloc[i] = np.nan
            final_lower_band.iloc[i] = np.nan
            supertrend.iloc[i] = np.nan
            direction.iloc[i] = 1
        else:
            # Calculate final bands
            if i == period:
                final_upper_band.iloc[i] = basic_upper_band.iloc[i]
                final_lower_band.iloc[i] = basic_lower_band.iloc[i]
            else:
                # Final upper band
                if basic_upper_band.iloc[i] < final_upper_band.iloc[i-1] or close.iloc[i-1] > final_upper_band.iloc[i-1]:
                    final_upper_band.iloc[i] = basic_upper_band.iloc[i]
                else:
                    final_upper_band.iloc[i] = final_upper_band.iloc[i-1]
                
                # Final lower band
                if basic_lower_band.iloc[i] > final_lower_band.iloc[i-1] or close.iloc[i-1] < final_lower_band.iloc[i-1]:
                    final_lower_band.iloc[i] = basic_lower_band.iloc[i]
                else:
                    final_lower_band.iloc[i] = final_lower_band.iloc[i-1]
            
            # Determine Supertrend and direction
            if i == period:
                supertrend.iloc[i] = final_upper_band.iloc[i]
                direction.iloc[i] = -1
            else:
                # If previous supertrend was upper band
                if supertrend.iloc[i-1] == final_upper_band.iloc[i-1]:
                    if close.iloc[i] <= final_upper_band.iloc[i]:
                        supertrend.iloc[i] = final_upper_band.iloc[i]
                        direction.iloc[i] = -1
                    else:
                        supertrend.iloc[i] = final_lower_band.iloc[i]
                        direction.iloc[i] = 1
                # If previous supertrend was lower band
                else:
                    if close.iloc[i] >= final_lower_band.iloc[i]:
                        supertrend.iloc[i] = final_lower_band.iloc[i]
                        direction.iloc[i] = 1
                    else:
                        supertrend.iloc[i] = final_upper_band.iloc[i]
                        direction.iloc[i] = -1
    
    return supertrend, direction

# Add Supertrend to dataframe
df['Supertrend'], df['Supertrend_Direction'] = calculate_supertrend(df)

# Drop rows with NaN values
df = df.dropna()

print(f"\nFinal data shape after calculations: {df.shape}")
print(f"Date range: {df.index[0]} to {df.index[-1]}")
print("\nFirst few rows:")
print(df.head())
print("\nLast few rows:")
print(df.tail())

# Analyze signals
print("\n" + "="*60)
print("SIGNAL ANALYSIS")
print("="*60)
price_above_ema = (df['Close'] > df['EMA_Daily']).sum()
supertrend_positive = (df['Supertrend_Direction'] == 1).sum()
both_conditions = ((df['Close'] > df['EMA_Daily']) & (df['Supertrend_Direction'] == 1)).sum()

print(f"Total bars: {len(df)}")
print(f"Bars where Close > EMA: {price_above_ema} ({price_above_ema/len(df)*100:.2f}%)")
print(f"Bars where Supertrend is positive (1): {supertrend_positive} ({supertrend_positive/len(df)*100:.2f}%)")
print(f"Bars where BOTH conditions met: {both_conditions} ({both_conditions/len(df)*100:.2f}%)")
print("="*60)


# Define the Strategy with optimizable parameters
class SupertrendEMAStrategy(Strategy):
    # Strategy parameters that can be optimized
    stop_loss_pct = 0.02  # 2% stop loss
    ema_period = 20  # EMA period
    st_period = 10  # Supertrend ATR period
    st_multiplier = 3  # Supertrend multiplier
    
    def init(self):
        # Recalculate EMA with the parameter
        # For hourly data, we need to use daily EMA already calculated
        self.ema = self.I(lambda: self.data.EMA_Daily, name='EMA (Daily)', overlay=True)
        self.supertrend = self.I(lambda: self.data.Supertrend, name='Supertrend', overlay=True)
        self.supertrend_direction = self.I(lambda: self.data.Supertrend_Direction, name='ST_Direction')
    
    def next(self):
        price = self.data.Close[-1]
        ema_value = self.ema[-1]
        supertrend_dir = self.supertrend_direction[-1]
        
        # Entry condition: Long when price > EMA and Supertrend is positive (1)
        if not self.position:
            if price > ema_value and supertrend_dir == 1:
                # Calculate stop loss price
                sl_price = price * (1 - self.stop_loss_pct)
                self.buy(sl=sl_price)
        
        # Exit condition: Close when price < EMA and Supertrend is negative (-1)
        else:
            if price < ema_value and supertrend_dir == -1:
                self.position.close()


# Run the backtest
print("\n" + "="*60)
print("Running Backtest...")
print("="*60)

bt = Backtest(
    df, 
    SupertrendEMAStrategy,
    cash=100000,
    commission=0.002,  # 0.2% commission
    exclusive_orders=True,
    finalize_trades=True
)

# Run the backtest with default parameters
stats = bt.run()

# Display results
print("\n" + "="*60)
print("BACKTEST RESULTS (Default Parameters)")
print("="*60)
print(stats)

# Display key metrics
print("\n" + "="*60)
print("KEY PERFORMANCE METRICS")
print("="*60)
print(f"Initial Cash:        ${stats['_equity_curve']['Equity'].iloc[0]:,.2f}")
print(f"Final Equity:        ${stats['_equity_curve']['Equity'].iloc[-1]:,.2f}")
print(f"Return:              {stats['Return [%]']:.2f}%")
print(f"Buy & Hold Return:   {stats['Buy & Hold Return [%]']:.2f}%")
print(f"Max Drawdown:        {stats['Max. Drawdown [%]']:.2f}%")
print(f"Number of Trades:    {stats['# Trades']}")
print(f"Win Rate:            {stats['Win Rate [%]']:.2f}%")
print(f"Sharpe Ratio:        {stats['Sharpe Ratio']:.2f}")
print(f"Sortino Ratio:       {stats['Sortino Ratio']:.2f}")
print(f"Profit Factor:       {stats['Profit Factor']:.2f}")

# Optimize the strategy
print("\n" + "="*60)
print("OPTIMIZING STRATEGY PARAMETERS...")
print("This may take a few minutes...")
print("="*60)

# Optimize for maximum return
stats_optimized = bt.optimize(
    stop_loss_pct=[0.01, 0.02, 0.03, 0.05],  # 1%, 2%, 3%, 5% stop loss
    maximize='Return [%]',
    constraint=lambda param: param.stop_loss_pct > 0
)

print("\n" + "="*60)
print("OPTIMIZED BACKTEST RESULTS")
print("="*60)
print(stats_optimized)

print("\n" + "="*60)
print("OPTIMIZED PARAMETERS")
print("="*60)
print(f"Stop Loss %:         {stats_optimized._strategy.stop_loss_pct * 100:.2f}%")

print("\n" + "="*60)
print("OPTIMIZED KEY PERFORMANCE METRICS")
print("="*60)
print(f"Initial Cash:        ${stats_optimized['_equity_curve']['Equity'].iloc[0]:,.2f}")
print(f"Final Equity:        ${stats_optimized['_equity_curve']['Equity'].iloc[-1]:,.2f}")
print(f"Return:              {stats_optimized['Return [%]']:.2f}%")
print(f"Buy & Hold Return:   {stats_optimized['Buy & Hold Return [%]']:.2f}%")
print(f"Max Drawdown:        {stats_optimized['Max. Drawdown [%]']:.2f}%")
print(f"Number of Trades:    {stats_optimized['# Trades']}")
print(f"Win Rate:            {stats_optimized['Win Rate [%]']:.2f}%")
print(f"Sharpe Ratio:        {stats_optimized['Sharpe Ratio']:.2f}")
print(f"Sortino Ratio:       {stats_optimized['Sortino Ratio']:.2f}")
print(f"Profit Factor:       {stats_optimized['Profit Factor']:.2f}")

print(f"\n{'='*60}")
print("PERFORMANCE COMPARISON")
print(f"{'='*60}")
print(f"Default Return:      {stats['Return [%]']:.2f}%")
print(f"Optimized Return:    {stats_optimized['Return [%]']:.2f}%")
print(f"Improvement:         {stats_optimized['Return [%]'] - stats['Return [%]']:.2f}%")

# Plot the optimized results
print("\nGenerating interactive chart with optimized parameters...")
bt.plot()
