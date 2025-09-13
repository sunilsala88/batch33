

# import datetime
import datetime as dt

dt1=dt.datetime(2023, 1, 1, 12, 0, 0)
print(dt1)

d1=dt.date(2023, 1, 1)
print(d1)

t1=dt.time(12, 0, 0)
print(t1)

d1=dt.timedelta(days=1,minutes=30)
print(d1)

print(dt1+d1)

n1=dt.datetime.now()
print(n1)

print(n1.day)
start_time=dt.datetime(n1.year,n1.month,n1.day,14,58)
end_time=dt.datetime(n1.year,n1.month,n1.day,15,0)
print(start_time)
print(end_time)

def strategy():
    print('inside strategy')

if start_time<dt.datetime.now()<end_time:
    strategy()

print(n1.weekday())

thursdays=[]
start_day=dt.datetime(2025,9,1)
i=0
while True:
    if i==30:
        break
    # print(start_day)
    start_day=start_day+dt.timedelta(days=1)
    if start_day.weekday()==3:
        thursdays.append(start_day)
    
    i=i+1
print(thursdays)

s1='2023-09-02'
#epoch time
#1971
epoch1=1757756609

#convert epoch to datetime
c1=dt.datetime.fromtimestamp(epoch1)
print(c1)

#convert datetime to epoch
print(n1.timestamp())

#convert str to datetime
s1='2023-09-02'
f1='%Y-%m-%d'
sd1=dt.datetime.strptime(s1,f1)
print(sd1)


s1='2023-Jan-02'
f1='%Y-%b-%d'
sd1=dt.datetime.strptime(s1,f1)
print(sd1)

n1=dt.datetime.now()
#'year--day"
f='%Y--%a'
s3=n1.strftime(f)
print(s3)