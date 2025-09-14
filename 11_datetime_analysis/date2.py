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

dt1=dt.datetime.now()
print(dt1.time())
data['time1']=data['date'].dt.time
data['time1']=data['time1'].astype('str')

print(data)
print(data.info())
print(data[data['time1']=='09:15:00']['close'].to_list())
print(data.iloc[0,-1]=='09:15:00')

data['wday']=data['date'].dt.weekday
print(data)

data1=pd.read_csv(r"/Users/algo trading 2025/batch33/10_data_analysis/Unicorn_companies.csv")
print(data1)
data1['Date Joined']=pd.to_datetime(data1['Date Joined'],format='%d-%m-%Y')
data1['year1']=data1['Date Joined'].dt.year
print(data1)
data1=data1[data1['year1']>2021]
print(data1)
print(data1['Company'].to_list())