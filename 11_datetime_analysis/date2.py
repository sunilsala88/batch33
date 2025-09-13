import pandas as pd
import datetime as dt

data=pd.read_csv(r"/Users/algo trading 2025/batch33/10_data_analysis/SBIN.csv")
print(data)
print(data.info())

# data['date']=pd.to_datetime(data['date'])
# print(data.info())

l1=[]
for i in data['date']:
    l1.append(dt.datetime.strptime(i,'%Y-%m-%d %H:%M:%S'))
data['date']=l1
print(data.info())
