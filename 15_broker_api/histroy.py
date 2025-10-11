

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

import time
while True:
    # no keys required for crypto data
    client = CryptoHistoricalDataClient()

    request_params = CryptoBarsRequest(
                            symbol_or_symbols=["BTC/USD"],
                            timeframe=TimeFrame.Minute,
                            start=datetime(2025, 10, 1),
                            end=datetime(2025, 10, 5)
                    )

    bars = client.get_crypto_bars(request_params)
    # print(bars)
    # convert to dataframe
    print(bars.df)
    time.sleep(60)