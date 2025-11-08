import yfinance as yf
import pandas as pd
import numpy as np
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
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

# Prepare hourly data
df = hourly_data.copy()
df = df[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

# Remove timezone info if present
if df.index.tz is not None:
    df.index = df.index.tz_localize(None)
if daily_data.index.tz is not None:
    daily_data.index = daily_data.index.tz_localize(None)


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


# Define the Strategy with optimizable parameters
class SupertrendEMAStrategy(Strategy):
    # Strategy parameters that can be optimized
    stop_loss_pct = 0.02  # Stop loss percentage
    ema_period = 20  # EMA period on daily data
    st_period = 10  # Supertrend ATR period
    st_multiplier = 3  # Supertrend multiplier
    
    def init(self):
        # Calculate EMA on daily close with the specified period
        # We need to merge daily EMA to hourly
        daily_close = daily_data['Close'].copy()
        daily_ema = daily_close.ewm(span=self.ema_period, adjust=False).mean()
        
        # Create a date column for merging
        df_temp = pd.DataFrame(index=self.data.index)
        df_temp['Date'] = pd.to_datetime(self.data.index).date
        
        daily_temp = pd.DataFrame({'Date': daily_ema.index.date, 'EMA': daily_ema.values})
        merged = df_temp.merge(daily_temp, on='Date', how='left')
        
        self.ema = self.I(lambda: merged['EMA'].values, name=f'EMA({self.ema_period})', overlay=True)
        
        # Calculate Supertrend with the specified parameters
        st_data = pd.DataFrame({
            'High': self.data.High,
            'Low': self.data.Low,
            'Close': self.data.Close
        })
        supertrend_vals, direction_vals = calculate_supertrend(
            st_data, 
            period=self.st_period, 
            multiplier=self.st_multiplier
        )
        
        self.supertrend = self.I(lambda: supertrend_vals.values, 
                                 name=f'ST({self.st_period},{self.st_multiplier})', 
                                 overlay=True)
        self.supertrend_direction = self.I(lambda: direction_vals.values, 
                                           name='ST_Dir')
    
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


# Drop rows with NaN values
df = df.dropna()

print(f"\nFinal data shape: {df.shape}")
print(f"Date range: {df.index[0]} to {df.index[-1]}")

# Run the backtest
print("\n" + "="*60)
print("Running Initial Backtest with Default Parameters...")
print("="*60)

bt = Backtest(
    df, 
    SupertrendEMAStrategy,
    cash=100000,
    commission=0.002,
    exclusive_orders=True
)

# Run with default parameters
stats = bt.run()

print("\n" + "="*60)
print("DEFAULT PARAMETERS RESULTS")
print("="*60)
print(f"EMA Period:          {stats._strategy.ema_period}")
print(f"Supertrend Period:   {stats._strategy.st_period}")
print(f"Supertrend Multi:    {stats._strategy.st_multiplier}")
print(f"Stop Loss:           {stats._strategy.stop_loss_pct * 100:.2f}%")
print(f"Return:              {stats['Return [%]']:.2f}%")
print(f"Sharpe Ratio:        {stats['Sharpe Ratio']:.2f}")
print(f"Max Drawdown:        {stats['Max. Drawdown [%]']:.2f}%")
print(f"Number of Trades:    {stats['# Trades']}")
print(f"Win Rate:            {stats['Win Rate [%]']:.2f}%")

# Optimize the strategy
print("\n" + "="*60)
print("OPTIMIZING STRATEGY PARAMETERS...")
print("Testing multiple combinations to maximize return...")
print("This may take several minutes...")
print("="*60)

stats_optimized = bt.optimize(
    ema_period=range(10, 51, 5),  # EMA: 10, 15, 20, 25, 30, 35, 40, 45, 50
    st_period=range(7, 21, 3),  # Supertrend period: 7, 10, 13, 16, 19
    st_multiplier=[2, 2.5, 3, 3.5, 4],  # Supertrend multiplier
    stop_loss_pct=[0.01, 0.015, 0.02, 0.025, 0.03, 0.04, 0.05],  # Stop loss %
    maximize='Return [%]',
    constraint=lambda param: param.stop_loss_pct > 0 and param.ema_period > 0
)

print("\n" + "="*60)
print("OPTIMIZATION COMPLETE!")
print("="*60)

print("\n" + "="*60)
print("OPTIMIZED PARAMETERS")
print("="*60)
print(f"EMA Period:          {stats_optimized._strategy.ema_period}")
print(f"Supertrend Period:   {stats_optimized._strategy.st_period}")
print(f"Supertrend Multi:    {stats_optimized._strategy.st_multiplier}")
print(f"Stop Loss:           {stats_optimized._strategy.stop_loss_pct * 100:.2f}%")

print("\n" + "="*60)
print("OPTIMIZED RESULTS")
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
print(f"Calmar Ratio:        {stats_optimized['Calmar Ratio']:.2f}")

print(f"\n{'='*60}")
print("PERFORMANCE COMPARISON")
print(f"{'='*60}")
print(f"Default Return:      {stats['Return [%]']:.2f}%")
print(f"Optimized Return:    {stats_optimized['Return [%]']:.2f}%")
print(f"Improvement:         {stats_optimized['Return [%]'] - stats['Return [%]']:.2f}% points")
print(f"Relative Gain:       {((stats_optimized['Return [%]'] / stats['Return [%]']) - 1) * 100:.2f}%")

print("\n" + "="*60)
print("FULL OPTIMIZED STATISTICS")
print("="*60)
print(stats_optimized)

# Plot the optimized results
print("\nGenerating interactive chart with optimized parameters...")
bt.plot()
