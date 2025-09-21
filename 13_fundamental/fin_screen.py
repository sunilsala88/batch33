

from finvizfinance.screener.overview import Overview

foverview = Overview()
filters_dict = {'Index':'DJIA','P/E':'Over 25','RSI (14)':'Overbought (60)'}
foverview.set_filter(filters_dict=filters_dict)
df = foverview.screener_view()
print(df)
df.to_csv('fin_screen.csv')


import pandas as pd
df=pd.read_html('https://www.screener.in/screens/2/piotroski-scan/')
print(df)